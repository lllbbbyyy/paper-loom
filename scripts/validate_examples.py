#!/usr/bin/env python3
"""Check example coverage, exact wording, hierarchy, adjacency, and local links.

This checks document consistency, not research validity or prose quality.
Uses only the Python standard library. Run from any working directory.
"""
import argparse
import json
import re
from pathlib import Path


def field(text, label):
    prefix = '- ' + label + ': '
    matches = [line[len(prefix):] for line in text.splitlines() if line.startswith(prefix)]
    if len(matches) != 1:
        raise ValueError(f'Expected one field: {label}')
    return matches[0]


def validate(root):
    base = root / 'skills/paper-loom/examples'
    index = json.loads((base / 'index.json').read_text())
    report = {}
    for language, spec in index['languages'].items():
        folder = base / language
        zh = language == 'zh-CN'
        manuscript = (base / spec['manuscript']).read_text()
        actual_paragraphs = [p.strip() for p in manuscript.strip().split('\n\n') if not p.startswith('#')]
        expected_paragraphs, seen, all_sentences = [], set(), []
        for section in spec['sections']:
            sec_path = folder / 'narrative/sections' / (section['id'] + '.md')
            sec_text = sec_path.read_text()
            if '## ' + section['title'] not in manuscript:
                raise ValueError(f'Missing manuscript heading: {section["id"]}')
            ordered_paragraphs = re.findall(r'^\d+\. \[(P-[^\]]+)\]', sec_text, re.M)
            if ordered_paragraphs != [p['id'] for p in section['paragraphs']]:
                raise ValueError(f'Paragraph order differs: {section["id"]}')
            for paragraph in section['paragraphs']:
                para_path = folder / 'narrative/paragraphs' / (paragraph['id'] + '.md')
                para_text = para_path.read_text()
                if f'[{section["id"]}](../sections/{section["id"]}.md)' not in para_text:
                    raise ValueError(f'Wrong section parent: {paragraph["id"]}')
                ordered_sentences = re.findall(r'^\d+\. \[(S-[^\]]+)\]', para_text, re.M)
                if ordered_sentences != paragraph['sentences']:
                    raise ValueError(f'Sentence order differs: {paragraph["id"]}')
                sentence_texts = []
                for sid in paragraph['sentences']:
                    if sid in seen:
                        raise ValueError(f'Duplicate sentence ID: {sid}')
                    seen.add(sid)
                    card = (folder / 'narrative/sentences' / (sid + '.md')).read_text()
                    if f'[{paragraph["id"]}](../paragraphs/{paragraph["id"]}.md)' not in card:
                        raise ValueError(f'Wrong paragraph parent: {sid}')
                    sentence_texts.append(field(card, '当前原句' if zh else 'Exact current sentence'))
                    all_sentences.append((sid, section['id'], card))
                prose = ('' if zh else ' ').join(sentence_texts)
                if field(para_text, '内容' if zh else 'Content') != prose:
                    raise ValueError(f'Paragraph and sentence cards differ: {paragraph["id"]}')
                expected_paragraphs.append(prose)
        if actual_paragraphs != expected_paragraphs:
            raise ValueError(f'Manuscript wording or coverage differs: {language}')
        expected_sections = [section['id'] for section in spec['sections']]
        expected_paragraph_ids = [p['id'] for section in spec['sections'] for p in section['paragraphs']]
        for directory, ids in [('sections', expected_sections), ('paragraphs', expected_paragraph_ids)]:
            actual = {p.stem for p in (folder / 'narrative' / directory).glob('*.md')}
            if len(ids) != len(set(ids)) or actual != set(ids):
                raise ValueError(f'Duplicate, orphan, or missing {directory}: {language}')
        actual_ids = {p.stem for p in (folder / 'narrative/sentences').glob('*.md')}
        if actual_ids != seen:
            raise ValueError(f'Orphan or missing sentence cards: {language}')
        for i, (sid, sec, card) in enumerate(all_sentences):
            previous = all_sentences[i-1] if i else None
            following = all_sentences[i+1] if i+1 < len(all_sentences) else None
            if previous and previous[1] == 'SEC-ABSTRACT' and sec != 'SEC-ABSTRACT':
                previous = None
            if following and sec == 'SEC-ABSTRACT' and following[1] != 'SEC-ABSTRACT':
                following = None
            for label, neighbor, endpoint in [
                ('前句及进入关系' if zh else 'Previous and incoming relation', previous, 'START'),
                ('后句及离开关系' if zh else 'Next and outgoing relation', following, 'END'),
            ]:
                value = field(card, label)
                expected = f'[{neighbor[0]}]({neighbor[0]}.md)' if neighbor else endpoint
                if not value.startswith(expected):
                    raise ValueError(f'Incorrect adjacency: {sid}, {label}')
        report[language] = dict(sections=len(spec['sections']), paragraphs=len(expected_paragraphs), sentences=len(seen))
    # Relative links must resolve in the repository. Template fill-in slots are plain text.
    for path in root.rglob('*.md'):
        if '.git' in path.parts or ('assets' in path.parts and 'templates' in path.parts):
            continue
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', path.read_text()):
            target = target.strip('<>')
            if re.match(r'^[A-Za-z][A-Za-z0-9+.-]*:', target) or target.startswith('#'):
                continue
            location = target.split('#', 1)[0]
            if location and not (path.parent / location).exists():
                raise ValueError(f'Broken local link in {path.relative_to(root)}: {target}')
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    print(json.dumps({'status': 'passed', 'examples': validate(args.root.resolve())}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
