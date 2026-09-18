"""Validate tracked mod snapshots without touching installed game files."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]

def game_files(folder):
    excluded = {'README.md', 'metadata.yaml', 'references', 'docs', '.git', 'CHANGELOG.md'}
    return {p.relative_to(folder).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in folder.rglob('*') if p.is_file()
            and p.relative_to(folder).parts[0] not in excluded
            and p.suffix != '.md'}

def localization(folder):
    result = {}
    for p in sorted(folder.rglob('*.yml')):
        for key, value in re.findall(r'^\s*([\w.]+):\d*\s+"(.*)"',
                                    p.read_text(encoding='utf-8-sig'), re.M):
            assert key not in result, (p, key, 'duplicate')
            result[key] = value
    return result

def main():
    count = 0
    for kind in ('workshop', 'derived'):
        for folder in sorted((ROOT / 'mods' / kind).iterdir()):
            if not folder.is_dir():
                continue
            # Existing metadata uses the JSON subset of YAML 1.2.
            meta = json.loads((folder / 'metadata.yaml').read_text(encoding='utf-8'))
            assert meta['kind'] == kind and meta['mod_id'] == folder.name
            assert (folder / 'README.md').is_file()
            for name in ('description', 'comments', 'updates'):
                assert (folder / 'references' / (name + '.md')).is_file()
            descriptor = (folder / 'descriptor.mod').read_text(encoding='utf-8-sig')
            assert re.search(r'^name="([^"]+)"', descriptor, re.M)[1] == meta['name']
            assert re.search(r'^version="([^"]+)"', descriptor, re.M)[1] == meta['version']
            assert 'replace_path' not in descriptor
            dep = re.search(r'dependencies\s*=\s*\{([^}]+)', descriptor)
            assert (re.findall(r'"([^"]+)"', dep[1]) if dep else []) == meta['dependencies']
            files = game_files(folder)
            manifest = json.loads((folder / 'references/source-files.json').read_text())
            assert files == manifest['files'], (folder, 'file fingerprint mismatch')
            revision = 'sha256:' + hashlib.sha256(json.dumps(files, sort_keys=True).encode()).hexdigest()
            assert revision == meta['source_revision'] == manifest['source_revision']
            if kind == 'derived':
                for upstream in [meta['upstream'], *meta.get('additional_upstreams', [])]:
                    path = (folder / upstream['repository_path']).resolve()
                    assert path.is_relative_to(ROOT / 'mods/workshop')
                    source_meta = json.loads((path / 'metadata.yaml').read_text(encoding='utf-8'))
                    assert upstream['source_revision'] == source_meta['source_revision']
                    assert upstream['version'] == source_meta['version']
                for p in (folder / 'localization').rglob('*.yml'):
                    assert p.read_bytes().startswith(b'\xef\xbb\xbf'), p
                    assert p.read_text(encoding='utf-8-sig').splitlines()[0] == 'l_simp_chinese:'
            count += 1
            print(f'OK {kind}/{folder.name}: {len(files)} game files')
    for original, patch, expected in [
        ('automated-courtier-management', 'automated-courtier-management-cn', 87),
        ('vassal-manager-reboot', 'vassal-manager-reboot-cn', 215),
    ]:
        english = localization(ROOT / 'mods/workshop' / original / 'localization/english')
        chinese = localization(ROOT / 'mods/derived' / patch / 'localization')
        assert len(english) == expected and not english.keys() - chinese.keys()
        # Vassal strings have no conditional display text inside their expressions.
        if expected == 215:
            for key, value in english.items():
                for pattern in (r'\[[^\]]*\]', r'#[\w!]+', r'\\n'):
                    assert re.findall(pattern, value) == re.findall(pattern, chinese[key]), key
        print(f'OK {patch}: {expected} upstream keys covered')
    print(f'Validated {count} mods. Runtime behavior has not been tested.')

if __name__ == '__main__':
    main()
