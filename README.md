# cs7295-notes

Bilingual (English / 日本語) lecture notes for **CS 7295 GPU Hardware and Software**
(Georgia Tech OMSCS, Spring 2027), written as a textbook-style summary of
what the lectures cover.  Built with
[latex-lecture-notes-template](https://github.com/kinginu/latex-lecture-notes-template).

- **Read the latest PDFs in the browser** (rebuilt by CI on every push):
  <https://kinginu.github.io/cs7295-notes/> —
  [English](https://kinginu.github.io/cs7295-notes/notes-en.pdf) ·
  [日本語](https://kinginu.github.io/cs7295-notes/notes-ja.pdf)
- Local build: `make docker-all` → `en/build/main.pdf`, `ja/build/main.pdf`.
- Print editions: compact two-sided books scaled from the A4 layout
  (class option `print=`, no chapter changes): `make docker-print-a5`
  (also `b6`, `shinsho` = 新書判, `b5`) → `dist/notes-<lang>-<size>.pdf`.
  CI builds the A4 and A5 editions (repository variable `PRINT_VARIANTS`),
  each also as a grayscale PDF, and lists them on the Pages index.
  The English edition prints no margin glosses (`gloss=false`); the Japanese
  edition adds an English index built from the glosses (`index=dual`).
- `en/` English edition, `ja/` Japanese edition — same chapter files under
  `lessons/`, one chapter per lesson; `figures/` and `references.bib` shared.

## Status

Chapters appear here as soon as both editions are finished and pushed.

| Lesson | Title | en | ja |
|---|---|---|---|

## Writing conventions

See [`docs/style-guide.md`](docs/style-guide.md), the book profile
[`docs/book.md`](docs/book.md) and the production process
[`docs/workflow.md`](docs/workflow.md).  In short:

- Textbook register: no lecture anecdotes or metaphors; scope limited to
  what the lectures cover.  Pointers to textbooks and papers go in the
  margin via `\source{}`.
- Every new term is introduced with `\term[reading]{word}[gloss]` so it
  lands in the index; [`glossary.tsv`](glossary.tsv) fixes the English
  index key, the Japanese term, its reading and the chapter that owns it.
- Numbers in worked examples are our own; **no lab, project, quiz or exam
  content is reproduced** (Georgia Tech honor code).
- `tools/chapter-lint.py <slug>` checks both editions of a chapter without
  TeX; CI builds the PDFs.

## License

`format/` and the build files come from the template (MIT), except
`format/lnmarginfix.sty`, a modified copy of `marginfix` under the LPPL
1.3c.  The notes
themselves (`en/`, `ja/`, `figures/`) are © kinginu and released under
[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
