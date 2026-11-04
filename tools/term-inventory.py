#!/usr/bin/env python3
"""Inventory of \\term, \\index and glossary rows (both editions), one TSV line each.
kind  lang  lesson  sort  word  gloss  line"""
import csv, glob, os, re, sys
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def arg(s, i, o, c):
    if i >= len(s) or s[i] != o: return None, i
    d = 0
    for j in range(i, len(s)):
        if s[j] == o: d += 1
        elif s[j] == c:
            d -= 1
            if d == 0: return s[i+1:j], j+1
    return None, i
out = csv.writer(sys.stdout, delimiter='\t', lineterminator='\n')
for lang in ('en', 'ja'):
    for f in sorted(glob.glob(f'{root}/{lang}/lessons/[0-9][0-9]-*.tex')):
        les = os.path.basename(f)[:2]
        s = open(f, encoding='utf-8').read()
        for m in re.finditer(r'\\(term\*?|index)(?![a-zA-Z])', s):
            i = m.end(); kind = m.group(1)
            sort = gloss = ''
            if kind != 'index':
                a, i2 = arg(s, i, '[', ']')
                if a is not None: sort, i = a, i2
            w, i = arg(s, i, '{', '}')
            if w is None: continue
            if kind != 'index':
                g, i2 = arg(s, i, '[', ']')
                if g is not None: gloss = g
            ln = s.count('\n', 0, m.start()) + 1
            out.writerow([kind, lang, les, sort, ' '.join(w.split()), ' '.join(gloss.split()), ln])
for r in csv.DictReader(open(f'{root}/glossary.tsv', encoding='utf-8'), delimiter='\t'):
    out.writerow(['gloss', 'tsv', r['lesson'], r['reading'], r['en'], r['ja'], r['note']])
