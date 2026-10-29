# Book profile

Everything that is specific to **this** book.  The generic rules are in
[`style-guide.md`](style-guide.md); writers and reviewers read both.  Fill
in every field when you create a book from the template, and keep it
current.

## Identity

- **Title**: GPU Hardware and Software: Lecture Notes for CS 7295
  (Georgia Tech OMSCS, Spring 2027); JA: GPUのハードウェアとソフトウェア
  講義ノート (CS 7295)
- **Kind**: course notes (bilingual EN/JA), one chapter per course module
  (12 chapters, M1–M12 in the order of the course's module list)
- **Field**: computer architecture / parallel programming: GPU
  microarchitecture, CUDA programming and optimisation, GPU performance
  modelling and simulation, compiler analysis for GPUs, ML acceleration
- **Course**: Georgia Tech OMSCS CS 7295 GPU Hardware and Software
  (formerly CS 8803 O21); created and taught by Hyesoon Kim (Head TA Scott
  Madeira).  Catalog description: "The course explores GPU software and
  hardware, covering GPU programming, optimizations, GPU architecture,
  compiler techniques, and performance analysis."
- **Prerequisites the lectures assume**: C/C++ (Python only for one
  project); no prior CUDA; undergraduate computer organisation (ISA, a
  basic 5-stage pipeline).
- **Chapter label**: Lesson  <!-- class default ("lesson") -->
- **Sections**: one per unit in `docs/syllabus.json` (unit = one of the
  course's own lessons inside the module; 42 in total, 1–5 per chapter).
  M5 has a single unit ("Advanced GPU Programming"); writers structure it
  with subsections from the dossier outline.

## Source material

What each chapter summarizes, in the order the chapters follow.

- **Primary source**: the lecture content as transcribed in lowyx's notes
  "CS8803 OMSCS - GPU hardware and software notes"
  (<https://lowyx.com/posts/gt-gpu-notes/>, updated 2026-01-19), published
  with the instructor's permission ("They kindly allowed this to be shared
  publicly, please use them responsibly!") under CC BY 4.0 by their author.
  The CC BY licence is the note author's; the lecture content belongs to
  the course.  Paraphrase, do not paste transcript passages, and attribute.
- **Version pinned**: not applicable (recorded lectures; notes fetched
  2026-10-29).  NVIDIA documents are pinned in their bib entries (CUDA C++
  Programming Guide 12.4, PTX ISA 9.4).
- **Unit list**: `docs/syllabus.json` (one entry per chapter; `units` lists
  the course lessons of the module in order, spelling normalised as in the
  dossier's `sources.md`).
- **Reference in `\source` and `\lessoninfo`**: `M<module>, <short topic>`,
  the module number and a 2–4 word topic matching the outline headings,
  e.g. `\source{M4, bank conflicts}`, `\source{M3, occupancy}`,
  `\source{M6, SIMT stack}`, `\source{M7, GTO vs round-robin}`,
  `\source{M8, Roofline}`, `\source{M10, reaching definitions}`,
  `\source{M12, floating-point formats}`.  Where a statement comes from a
  paper or document rather than the lecture, cite it with `\cite{key}`
  instead of, or in addition to, `\source{}`.
- **Dossier**: writers and reviewers read
  [`docs/dossier/outline.md`](dossier/outline.md) (per-unit content
  outline with objectives, worked examples, key terms, backing sections,
  margin numbers, redraw descriptions of every slide figure, [SIMPLIFIED]
  marks and the slide errata of Appendix C) and
  [`docs/dossier/sources.md`](dossier/sources.md) (what was fetched, the
  licences, and which paper or document backs which claim).
- **Figures**: every figure is redrawn from the outline's descriptions,
  with the slide errors of outline Appendix C corrected; **never include a
  slide image** (the lowyx images are the course's slides).  The bfloat16
  comparison figure on the M12 floating-point slide is Wikipedia's
  (CC BY-SA 4.0): redraw it too.
- **Lecture vs. paper**: where the outline marks **[SIMPLIFIED]** (the
  lecture is looser than, or contradicts, the paper or document behind
  it), the body keeps the lecture's statement and a `\caution` gives the
  paper's, with `\cite`.
- **Unverified items**: anything the outline marks "verify" (e.g. the
  A18 section headings, the exact CPG §2.2 sentence, the
  karkhanis2004firstorder accuracy figures, the Photon slide speed-ups,
  FP8 E4M3's 448 maximum) must be checked against the document before it
  is printed, or stated with its uncertainty ("reported as …"); never
  assert it as fact.
- **Lecture vs. reality** (state the lecture's figure, then a `\caution`
  with the correct one):
  - M8.4: 10^9 instructions at 1 KIPS take 10^6 s (about 11.6 days), not
    the lecture's 28 hours (that needs about 10 KIPS);
  - M7.2: GPU page-fault handling takes tens of **microseconds** (20–50 µs
    in prior work; batches 223–553 µs, `kim2020batch`), not the
    transcript's "tens of milliseconds";
  - M8.3: the Roofline byte counts ("2 bytes per 1 FLOP") assume 1-byte
    elements; with FP32 a dot product loads 8 B per 2 FLOPs (0.25 FLOP/B),
    and the 1 TFLOP/s design example needs 8 TB/s, not 2.
- **Not sources**: github.com/eizyc/CS7295-GPU (titles and ordering only),
  the lowyx course-review post, OMSCentral reviews and student project
  repositories.  They only define the exclusion boundary and are never the
  source of book text.
- **Textbook / reference** (cite with the section, e.g. "K12 §1.4.2"):
  - Kim et al., *Performance Analysis and Tuning for General Purpose
    Graphics Processing Units (GPGPU)* (`kim2012gpgpu`; "K12"), the
    course's own text: ch. 1 assigned in M1 (§1.4 also backs M4/M6),
    ch. 2–4 for M5 and M8.  Full section TOC verified.
  - Aamodt, Fung & Rogers, *General-Purpose Graphics Processor
    Architectures* (`aamodt2018gpu`; "A18"): ch. 3 assigned in M4–M6;
    ch. 1, 2, 4, 5 as background.  Section headings are unverified: cite
    by chapter unless checked.
  - Hwu, Kirk & El Hajj, *Programming Massively Parallel Processors*, 4th
    ed. (`hwu2022pmpp`; "PMPP"): not assigned, a supplementary text for
    CUDA pedagogy (ch. 2–8, 10, 14, 16, 20, 22, App. A).
  - NVIDIA, *CUDA C++ Programming Guide*, Release 12.4
    (`nvidia2024cudaguide`; "CPG"): §1–2 and §4 assigned in M1, §3 in M3.
    Section numbers are the legacy 12.x numbering; CUDA 13 reorganised
    the guide, so cite the section **title** together with the number.
  - NVIDIA, *CUDA C++ Best Practices Guide* (`nvidia2026cudabestpractices`;
    "BPG"): §9 Performance Metrics, §10 Memory Optimizations, §11
    Execution Configuration Optimizations (M5).
  - NVIDIA PTX ISA 9.4 (`nvidia2026ptx`), Ampere and Hopper whitepapers
    (`nvidia2020ampere`, `nvidia2022hopper`; H100 numbers are the V1.02
    preliminary ones, say so), GEMM performance guide
    (`nvidia2026gemmguide`).
  - Mattson, Sanders & Massingill, *Patterns for Parallel Programming*
    (`mattson2004patterns`; "PPP"): ch. 2–5, App. A–B (M1, M2, optional).
  - Barney & Frederick, *Introduction to Parallel Computing Tutorial*
    (`barney2026parallel`): M2.
  - Eeckhout, *Computer Architecture Performance Evaluation Methods*
    (`eeckhout2010perfeval`): M8 (optional).
  - Assigned readings: `kipfer2005gpusort` (GPU Gems 2 ch. 46, sorting
    networks), `harris2013sharedmem` (shared memory and bank conflicts,
    M5).
- **Papers the source discusses** (all in `references.bib`):
  M6 `fung2007dwf`, `jeon2015rfv`, `gebhart2012unifying`,
  `gebhart2011energy`, `gebhart2011compile`;
  M7 `power2014x86`, `narasiman2011twolevel`, `rogers2012ccws`,
  `jog2013owl`, `jog2013orchestrated`, `ganguly2019interplay`,
  `ausavarungnirun2017mosaic`, `li2021tlb`, `kim2020batch`;
  M8 `liu2023photon`, `williams2009roofline`, `hong2009analytical`,
  `huang2014gpumech`, `karkhanis2004firstorder`;
  M9 `arunkumar2017mcmgpu`, `yu2022multitenant`, `ye2024dlsched`;
  M12 `dao2022flashattention`, `dao2023flashattention2`,
  `cambier2020s2fp8`.  The outline says per unit what each lesson takes
  from them.  IEEE 754-2019 has no bib entry yet: add one before citing it.

## Code

- **Language in listings**: `language=C++` for CUDA C++ (M3–M5, M7, M9,
  M12: short kernels with `threadIdx`/`blockIdx`/`blockDim`, `__shared__`
  and `__syncthreads()`, host code with `cudaMalloc`, `cudaMemcpy`,
  `<<<grid, block>>>`, streams and `cudaMemcpyAsync`, `cudaSetDevice`,
  `cudaMallocManaged`) and for C++ with OpenMP (M2: full small programs
  with `parallel for reduction`, `critical`, `atomic`, `sections`,
  `ordered`, `single`); PTX fragments (M4, M10, M11) and LLVM IR (M10,
  M11: `add i32`, `phi`) via a `language=` defined in the chapter;
  pseudocode and math for CPI, interval and Roofline models, data-flow
  equations and iterative algorithms (M8, M10, M11).
- **Conventions**: examples are original, compile-checkable CUDA C++ in
  the spirit of the lecture's, sized to the concept.  MPI appears in the
  lectures only as call names in diagrams; a minimal C example may be
  added.  SASS appears only as the mnemonic `HMMA.1688.F16` (M12), no
  listings.  The M8 simulator screenshots (MacSim) are project code: never
  reproduce them, use generic pseudocode.  No Python: the lectures show
  none, and Python implementations of the M10/M11 analyses are excluded.

## Excluded

Never include (the reviewers treat any of it as a major issue):

- quiz, exam, homework and project questions, numbers and answers of the
  course (honor code); never reproduce or paraphrase quiz or final-exam
  questions as exercises;
- the five projects: handouts, starter code, test cases, grading
  thresholds, solutions, tuned parameters and "how to get full marks"
  advice.  The underlying papers and lecture concepts stay in scope.
  1. *Project 1: CUDA Programming* (basic CUDA, in practice a tiled
     matrix multiplication): tiled matmul may be taught generically, with
     our own sizes and code, no cluster job scripts, no speed-up targets,
     and not shaped as the project's interface.
  2. *Project 2: CUDA Programming II* (performance optimisation, in
     practice a bitonic sort with Nsight report): sorting networks and
     bitonic sequences conceptually (`kipfer2005gpusort`); no optimised
     CUDA sort kernel, no tuning recipe, no numbers tied to the project.
  3. *Project 3: GPU Simulator* (warp-scheduler policies and tensor-core
     timing in a trace-driven simulator; earlier also execution units):
     RR, GTO, two-level and CCWS policies, tensor-core latency/throughput
     and simulator architecture in general are in scope (M7, M8, M12); no
     code against MacSim or the course simulator, no trace formats, no
     project parameters or expected cycle counts.
  4. *Project 4: CUDA Programming for ML* (in practice a self-attention /
     FlashAttention kernel): attention, IO-aware tiling and online softmax
     at the level of `dao2022flashattention` and
     `dao2023flashattention2`; no CUDA attention kernel and no
     step-by-step implementation plan.
  5. *Project 5: GPU Code Analysis* (a code-analysis pass in a
     Python-based framework: divergence detection, or reaching
     definitions and liveness): M10 and M11 teach data-flow equations,
     worked examples on the book's **own** CFGs and divergence-analysis
     concepts, and those stay in scope; no Python or pseudo-Python
     implementation of reaching definitions, liveness or divergence
     detection, and the lecture's exact example CFGs are not reused as
     solved exercises.
- the lowyx slide images (redraw instead, see Figures), long transcript
  passages, and student retrospectives (lowyx review post, OMSCentral) as
  a source of any book text.

## Real-world numbers

Typical kinds of numbers worth adding in margin notes (style guide §3.1),
and where they come from.  outline.md Appendix B is the index of numbers
with their sources; use it.

- CUDA limits per compute capability (warp size 32, 1024 threads per
  block, 64/48/32 warps per SM, 65,536 registers per SM, 255 registers per
  thread, shared memory per SM 96–228 KB, 32 banks) — CPG Table 21, HWP
  Table 4, BPG §10.2;
- data-centre GPU generations P100/V100/A100/H100 (SMs, FP32 and tensor
  cores per SM, tensor TFLOPS, HBM bandwidth 720 GB/s to 3 TB/s, L2,
  transistors, TDP) — AWP Table 4, HWP Table 3 (H100 preliminary);
- memory-system figures (32-byte sectors, 32/64/128-byte transactions,
  shared memory ~100× lower latency than uncached global) — BPG, CPG
  §5.3.2, `harris2013sharedmem`; Tesla/Fermi latencies from K12 Table 1.4;
- interconnect (NVLink generations, NVLink 4 = 7× PCIe Gen 5, MIG up to 7
  instances, MPS client limits) — nvidia.com, HWP, MPS overview;
- virtual memory (UVM fault latency 20–50 µs, batches 223–553 µs; TLB
  reach of 2 MB pages; GPU MMU results) — `kim2020batch`,
  `ganguly2019interplay`, `power2014x86`;
- research results the lectures present (read-once register values up to
  70 %, CCWS −25 % L1D misses, Photon 7.05 days to 1.7 h) —
  `gebhart2011energy`, `rogers2012ccws`, `liu2023photon`;
- Roofline ridge points (V100 138.9 FLOP/B) — `nvidia2026gemmguide`.

## Reference chapters

Chapters whose style, density and macro use are approved and should be
imitated by new chapters (both editions):

- none yet: the first finished chapters of this book will be listed here.
  Until then, the reference chapters of the sister books
  (cs6290-notes, cs6200-notes, cs6340-notes) show the expected density
  and macro use; cs6290-notes is the closest in field (computer
  architecture).

Back matter:

- Glossary from `glossary.tsv` (one row per term, owned by the lesson that
  first introduces it).
- Bibliography from `references.bib`.
- Suggested appendices (writer's choice, each built from fetched
  sources): A. CUDA quick reference (CPG 12.4 §7; BPG); B. compute
  capability table for CC 7.0–9.0 (CPG Table 21; HWP Table 4); C. NVIDIA
  data-centre GPU comparison P100–H100 (AWP Table 4, HWP Table 3; H100
  preliminary); D. PTX cheat sheet (PTX ISA); E. floating-point formats
  FP64 to INT4 (AWP, HWP; IEEE 754 needs a bib entry); F. data-flow
  analysis summary table (reaching definitions vs liveness, M11.1);
  G. performance-model formulas (occupancy, Amdahl, bandwidth, Roofline,
  CPI stack, MWP/CWP, GEMM arithmetic intensity); H. reading guide, one
  paragraph per assigned paper (outline.md has the one-line summaries).
