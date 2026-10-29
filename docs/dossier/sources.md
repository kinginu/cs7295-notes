# Sources for the CS 7295 / CS 8803 O21 dossier

Fetched 2026-10-29. Raw copies are in `raw/` (HTML, PDF and extracted `.txt`). Nothing in `raw/` was executed.
Status: **ok** = full text fetched and read; **partial** = only some of the content was available; **failed** = not available (reason given).

## 1. Primary source: lowyx notes (student notes published with the instructor's permission)

Permission and licence, quoted verbatim from https://lowyx.com/posts/gt-gpu-notes/ (header paragraph):

> "Content of these notes are from Georgia Tech OMSCS 7295 (Formally 8803): GPU Hardware and Software by Prof. Hyesoon Kim. They kindly allowed this to be shared publicly, please use them responsibly!"

Footer on that page and on every per-module page:

> "This post is licensed under CC BY 4.0 by the author."

(The CC BY 4.0 licence is the author's (yxlow's) licence for the post. The underlying lecture content belongs to the course. Treat the notes as a structural and factual source, paraphrase rather than copy, and attribute.)

| URL | Status | Covers |
|---|---|---|
| https://lowyx.com/posts/gt-gpu-notes/ | ok | All 12 modules, 42 lessons, "223 min read", posted 2024-04-09, updated 2026-01-19. Objectives, required/optional readings, every lesson's text (transcript-like), slide image names. Read in full (4216 lines extracted). |
| https://lowyx.com/posts/gt-gpu-M1/ ... /gt-gpu-M12/ | ok (12 pages) | Per-module pages, posted 2024-01-06 to 2024-04-06. A line-by-line diff shows each per-module page is a strict subset of the all-modules page (no extra content). They lack the "Module N: title" headings, which only the all-modules page has. |
| https://lowyx.com/posts/gt-gpu/ | ok | Course review by the same student (Spring 2024): a module table with lesson titles, grading in Spring 2024, assignment descriptions. Used only for module/lesson titles and the exclusion boundary. Its Module 5 row lists no lessons, and its Module 2 row merges the two OpenMP-vs-MPI parts. |
| https://lowyx.com/ , /archives/ , /page2..4 | ok | Site index, used to find the posts. |

Anomalies inside the lowyx notes (record them, do not copy them):
- The objectives of Module 2 are copied from Module 1 ("Describe the basic backgrounds of GPU..."), and the objectives of Module 5 are copied from Module 4.
- The objective of Module 7 ("Describe the performance issues related to divergent branches...") is copied from Module 6.
- The objectives of Modules 10 and 11 read "Be able to explain comparisons with other GPU programming", and the only reading listed is "OpenCL overview". This looks like a placeholder.
- The Module 12 required reading `https://resources.nvidia.com/en-us-tensor-core` now redirects to the nvidia.com home page (see section 5).
- Some titles are misspelled: "History Trend of GPU Architechtures" (eizyc has the same spelling), "Loop Parallelism PAttern", "Strength Redunction", "Kernel Lanuch". syllabus-draft.json uses corrected spellings.
- eizyc spells the M10L4 title "Instruction to Data Flow Analysis" and calls M5L1 "Overview". lowyx has "Introduction to Data Flow Analysis" and "Advanced GPU Programming". The lowyx forms are used.

## 2. Official syllabi and course pages

| URL | Status | Covers |
|---|---|---|
| https://omscs.gatech.edu/cs-7295-gpu-hardware-and-software | ok | Course page: Hyesoon Kim (Creator, Instructor), Scott Madeira (Head TA). Overview text. Links the "Summer 2026", "Spring 2026" and "Fall 2025" syllabi. Suggested background (CS 6200 for projects 3–5, CS 6290 for 3–4, CSE 6220 for 1–2, CS 6340 for 5). |
| https://omscs.gatech.edu/cs-8803-o21-gpu-hardware-and-software | ok | Serves the same page as CS 7295. |
| https://omscs.gatech.edu/sites/default/files/documents/Syllabi/CS%207295%202026-2.pdf | ok | **Summer 2026** syllabus. The "2026-2" file is Summer, not Fall: the course page labels it "Summer 2026 syllabus", and the PDF heading says Summer 2026. P1 5 %, P2 20 %, P3 20 %, P4 15 %, P5 20 %, quizzes 10 %, final 10 %, Ed up to 3 %. |
| https://omscs.gatech.edu/sites/default/files/documents/Syllabi/CS%207295%202026-1.pdf | ok | Spring 2026 (CS 7295). The old 5-project structure with two simulator projects: P3 15 %, P4 15 % "Add execution units in a trace-driven GPU simulator", homework 15 %. |
| https://omscs.gatech.edu/sites/default/files/documents/Syllabi/CS%208803%20O21%202025-3.pdf | ok | Fall 2025 (CS 8803). Same structure as Spring 2026. |
| …/CS%208803%20O21%202025-2.pdf, …/2025-1.pdf, …/2024-3.pdf | ok | Summer 2025, Spring 2025, Fall 2024. Same 5-project structure (P3 15 %, P4 15 %). |
| https://omscs.gatech.edu/sites/default/files/documents/2024/Syllabi-CS%208803%20O21%202024-2.pdf | ok | Summer 2024. P3 20 %, P4 20 %, P5 20 %, quizzes 15 %, final exam (optional) 10 %, Ed up to 5 %. |
| …/CS%208803%20O21%202024-1.pdf, …/2024-2.pdf (non-"2024/" path), …/2026-1.pdf (8803), CS%207295%202025-3.pdf, CS%207295%202026-3.pdf | failed (404) | Not published under those names. |
| https://syllabus.gatech.edu/syllabi/7295/o01 → https://syllabus.gatech.edu/sites/default/files/2026-08/cs7295-gpu-fall2026.pdf | ok | **Fall 2026** syllabus (CS 7295 O01, CRN 94504). The PDF's table still says "Grading breakdown (Summer offering)". P1 5 %, P2 20 %, P3 20 %, P4 20 %, P5 15 %, quizzes 10 %, final 10 %, Ed up to 3 %. Quizzes 1, 6, 7, 8 allow two attempts. "Modules 1–3 are published at the beginning of the semester. Project 1 is released on Monday of week 1. Project 2 is released at the beginning of week 2. Additional modules, projects, and due dates follow the schedule posted on Canvas." Also covers AI-use policy and Gradescope. |
| https://syllabus.gatech.edu/sites/default/files/2026-04/cs7295-gpu-fall2026.pdf | ok | Earlier (April) draft of the Fall 2026 syllabus, 5 pages. |
| https://syllabus.gatech.edu/syllabi/7295/o01-0 → …/2026-05/cs7295-gpu-summer2026_final.pdf | ok | Summer 2026 final (8 pages). Differs from Fall 2026 only in P4 15 % / P5 20 %. |
| https://syllabus.gatech.edu/syllabi/7295/o01-1 → …/2026-10/cs7295-gpu-spring2027.pdf | ok | **Spring 2027** syllabus (CRN 33707, updated 2026-10-26). Identical to Fall 2026 apart from the term. |
| https://syllabus.gatech.edu/syllabi/8803/o21 | failed (403) | Access denied. |

None of the syllabi has a module list or a week-by-week schedule: they defer to Canvas. The module list comes only from lowyx, the eizyc README and the lowyx review page.

## 3. Lesson-title cross-check

| URL | Status | Covers |
|---|---|---|
| https://github.com/eizyc/CS7295-GPU (README.md via `gh api`) | ok | Single README, 3203 lines, no licence. Headings M1L1…M12L3 (42 lessons) agree with lowyx. **Used only for titles and ordering. No text taken.** |
| https://www.omscentral.com/courses/gpu-hardware-and-software/reviews | partial (WebFetch summary) | No module list. Project names as students describe them: P1 CUDA matrix multiply intro; P2 bitonic sort in CUDA; P3/P4 GPU hardware simulation, merged into one P3 by Spring 2026; P4 attention layers / FlashAttention (new in Spring 2026); P5 dataflow analysis (reaching definitions and liveness, Fall 2025). Used only to fix the exclusion boundary. |
| https://github.com/sofiework/flashattn (README) | partial (read for scope only) | A student repo that copies the Project 4 handout ("CS 7295 GPU Project 4: Implementing a self-attention kernel in CUDA ... specifically targeting the FlashAttention algorithm"). **It is a project handout: do not use it as a source for any book text.** Read only to identify the P4 topic. |

## 4. Textbooks and NVIDIA documentation

| URL | Status | Covers |
|---|---|---|
| doi.org BibTeX + api.crossref.org for 10.1007/978-3-031-01737-7 (Kim et al. 2012) | ok (metadata, chapter titles) | Chapter titles via Crossref chapter DOIs `_1`…`_4`. Original Morgan & Claypool DOI 10.2200/S00451ED1V01Y201209CAC020 redirects to the Springer DOI. Section-level TOC not obtained. |
| doi.org + Crossref for 10.1007/978-3-031-01759-9 (Aamodt, Fung, Rogers 2018) | ok (metadata, chapter titles) | Chapters 1–5 via Crossref, confirmed by https://www.sigarch.org/other-announcements/book-release-general-purpose-graphics-processor-architectures/ (ok) and https://engineering.purdue.edu/tgrogers/publication/aamodt-book-2018 (ok). |
| https://link.springer.com/book/10.1007/978-3-031-01759-9 , …/978-3-031-01737-7 | failed | Bot "Client Challenge" / cookie redirect. Section-level TOCs of both Synthesis Lectures were therefore **not verified**. |
| https://educate.elsevier.com/book/details/9780323912310 (WebFetch) | ok | PMPP 4th ed. chapter list (23 chapters + Appendix A), publication date 2022-08-04. |
| https://www.oreilly.com/library/view/programming-massively-parallel/9780323984638/ , lavoisier.fr | failed | Empty page / HTTP 403. |
| https://openlibrary.org/api/books (ISBN 9780321630582, 0321228111, 9780323912310) | ok | Patterns for Parallel Programming metadata. Its chapter titles come from search-result listings (WebSearch summary), not a publisher page: ch. 2 background and jargon of parallel computing, ch. 3 Finding Concurrency design space, App. A OpenMP, App. B MPI, App. C Java. Partial. |
| https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html | ok | Now redirects to the restructured **CUDA Programming Guide v13.4.2** (Parts 1–5). The course's "section 1-2, 4" and "section 3" numbering refers to the older guide. |
| https://docs.nvidia.com/cuda/archive/12.4.0/cuda-c-programming-guide/index.html | ok | Legacy guide: 1 Introduction, 2 Programming Model, 3 Programming Interface, 4 Hardware Implementation (4.1 SIMT Architecture, 4.2 Hardware Multithreading), 5 Performance Guidelines. Table 21 "Technical Specifications per Compute Capability", Compute Capability 5.x/7.x/8.x/9.0 shared-memory and global-memory sections. Read in the relevant parts. |
| https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/index.html | ok | Full heading list. §9 Performance Metrics, §10 Memory Optimizations, §11 Execution Configuration Optimizations. Read occupancy, coalescing, bank and bandwidth passages. |
| https://docs.nvidia.com/cuda/parallel-thread-execution/index.html | ok | PTX ISA 9.4: instruction format, guard predicates, setp, mma shapes. |
| https://images.nvidia.com/aem-dam/en-zz/Solutions/data-center/nvidia-ampere-architecture-whitepaper.pdf | ok | A100 whitepaper: tensor core rates, P100/V100/A100 comparison table, 2:4 sparsity, BF16/TF32, MIG, async copy. |
| https://resources.nvidia.com/en-us-tensor-core/gtc22-whitepaper-hopper | failed | Landing page gated or redirected, no PDF. |
| https://www.ece.lsu.edu/koppel/gp/refs/gtc22-whitepaper-hopper.pdf | ok (mirror) | H100 whitepaper V1.02: A100/H100 table (H100 figures marked preliminary), FP8 E4M3/E5M2, TMA, thread block clusters, DSMEM, 256 KB L1+shared. |
| https://www.pny.com/…/nvidia-h100-datasheet.pdf | ok | H100 **PCIe/NVL** datasheet only (FP16 1,513 TF sparse, 2 TB/s). The shipped H100 SXM5 figures (bandwidth and dense TFLOPS) were **not** verified from a fetched source. |
| https://docs.nvidia.com/deeplearning/performance/dl-performance-matrix-multiplication/index.html | ok | GEMM arithmetic intensity, V100 FLOPS:B = 138.9, tile and wave quantisation, Tensor Core dimension multiples. |
| https://developer.nvidia.com/gpugems/gpugems2/part-vi-simulation-and-numerical-algorithms/chapter-46-improved-gpu-sorting | ok | Kipfer & Westermann, odd-even transition sort, odd-even merge sort, bitonic merge sort. Project 2 preparation. |
| https://developer.nvidia.com/blog/using-shared-memory-cuda-cc/ | ok | Harris 2013: shared memory, `__syncthreads`, bank conflicts. |
| https://hpc.llnl.gov/documentation/tutorials/introduction-parallel-computing-tutorial | ok | Barney & Frederick, version dated June 16, 2026. M2 required reading. |
| https://developer.nvidia.com/blog/gpu-pro-tip-cuda-7-streams-simplify-concurrency/ | ok | M5 optional. Fetched, not mined. |
| https://developer.nvidia.com/blog/how-optimize-data-transfers-cuda-cc/ | ok | M5 optional. Fetched, not mined. |
| https://developer.nvidia.com/blog/using-nsight-compute-to-inspect-your-kernels/ | ok | M5 optional. Fetched, not mined. |
| https://developer.download.nvidia.com/GTC/PDF/1083_Wang.pdf | ok | M5 optional (GTC talk). Fetched, not mined. |
| https://docs.nvidia.com/nsight-systems/UserGuide/index.html , https://developer.nvidia.com/nsight-compute-videos | ok | M5 optional. Fetched, not mined. |
| https://youtu.be/Iuy_RAvguBM | not fetched | Video (M5 optional). |
| https://www.nvidia.com/en-us/data-center/nvlink/ | ok | NVLink generation table: 4th gen (Hopper) 900 GB/s and 18 links, 5th gen (Blackwell) 1,800 GB/s and 18 links, 6th gen (Vera Rubin) 3,000 GB/s and 36 links. |
| https://developer.nvidia.com/blog/upgrading-multi-gpu-interconnectivity-with-the-third-generation-nvidia-nvswitch | failed (redirect) | Now redirects to an unrelated GB200 NVL72 blog post. Original NVSwitch article unavailable. |
| https://docs.nvidia.com/cuda/gpudirect-rdma/index.html | ok | GPUDirect RDMA overview (v13.4). |
| https://docs.nvidia.com/deploy/pdf/CUDA_Multi_Process_Service_Overview.pdf | ok | MPS overview, Volta MPS, execution resource provisioning. |
| https://www.khronos.org/opencl/ | ok | The "OpenCL overview" named in M10/M11 (best guess at the intended page). |

## 5. Papers

| Paper (bib key) | Metadata source | Full text | Status |
|---|---|---|---|
| fung2007dwf | doi.org BibTeX | https://people.ece.ubc.ca/aamodt/papers/wwlfung.micro2007.pdf | ok |
| jeon2015rfv | doi.org BibTeX | none found (IEEE/ACM paywalled; Illinois experts page and scite summaries via WebSearch only) | partial (abstract-level only) |
| gebhart2012unifying (MICRO 2012, the "Unifying" paper) | doi.org | https://www.cs.utexas.edu/users/skeckler/pubs/micro12.pdf | ok |
| gebhart2011energy (ISCA 2011, register file cache + two-level scheduler) | doi.org | https://www.cs.utexas.edu/~skeckler/pubs/RF_ISCA_11.pdf | ok |
| gebhart2011compile (MICRO 2011, compile-time managed multi-level RF) | doi.org | not fetched | metadata only |
| power2014x86 | doi.org | https://research.cs.wisc.edu/multifacet/papers/hpca14_gpummu_appendix.pdf (the file named "appendix" is the full paper) | ok |
| narasiman2011twolevel | doi.org | https://users.ece.cmu.edu/~omutlu/pub/large-gpu-warps_micro11.pdf | ok |
| rogers2012ccws | doi.org | https://people.ece.ubc.ca/aamodt/papers/tgrogers.micro2012.pdf | ok |
| liu2023photon | doi.org | https://www.comp.nus.edu.sg/~tcarlson/pdfs/liu2023pafssmfgw.pdf | ok |
| williams2009roofline | doi.org | Tech-report version https://www2.eecs.berkeley.edu/Pubs/TechRpts/2008/EECS-2008-134.pdf (the CACM PDF link failed) | ok (TR version) |
| hong2009analytical | doi.org | https://www.cc.gatech.edu/~hyesoon/hong_isca09.pdf | ok |
| huang2014gpumech | doi.org | https://hsienhsinlee.github.io/MARS/pub/micro14.pdf (the gatech URL failed) | ok |
| arunkumar2017mcmgpu | doi.org | https://research.nvidia.com/sites/default/files/publications/ISCA_2017_MCMGPU.pdf | ok |
| karkhanis2004firstorder, ganguly2019interplay, jog2013owl, jog2013orchestrated, ausavarungnirun2017mosaic, li2021tlb, kim2020batch, ye2024dlsched | doi.org | not fetched (optional readings) | metadata only |
| yu2022multitenant | arXiv BibTeX + abstract page | not mined | metadata only |
| dao2022flashattention, dao2023flashattention2 | arXiv BibTeX, Crossref (NeurIPS DOI) | arXiv PDFs | ok |

## 6. Searches for instructor slides or other syllabus text

- WebSearch "Hyesoon Kim CS 8803 GPU hardware software lecture slides pdf hparch gatech" and a site:gatech.edu variant found no public lecture slides. Slides are distributed on Canvas only. https://hyesoon.github.io, https://sites.gatech.edu/hparch and the 2012 CS4803PGC page (https://sites.cc.gatech.edu/fac/hyesoon/spr12/index.html) were seen in results but not mined: they belong to other courses or are lab pages.
- No public week-by-week schedule exists. The Fall 2026 syllabus states that only Modules 1–3 open at the start and the rest follow the Canvas schedule.

## 7. Follow-up pass (2026-10-29, second round)

**Lowyx slide images.** All 229 images referenced by the all-modules page were downloaded from `https://lowyx.com/assets/posts/gatech/gpu/<file>` into `raw/lowyx_img/` (ok, 0 failures; `list.txt` gives the page order). Every image was viewed and described for redrawing; the descriptions are folded into outline.md.
- The M9–M12 description file is kept as `raw/lowyx_img/figdesc_M09-M12.md`.
- One file, `m7l2_cudahost.png`, is a screenshot of a Canvas page carrying a Module 8 erratum, not a slide.
- These images are course slides: use them only as a reference for redrawing.

**Book contents**

| URL | Status | Covers |
|---|---|---|
| https://jeewhanchoi.github.io/publication/pdf/perf_analysis_book.pdf | ok | Full PDF of Kim et al. 2012, hosted on co-author Jee Choi's page. Full section-level TOC verified. Ch. 1 §1.2–1.4 read (GPU pipeline, scoreboarding, register banks and operand collectors, SIMT stack, memory systems). Saved as `raw/books/kim2012_perf_analysis_book.pdf`. |
| https://books.google.com/books/about/General_Purpose_Graphics_Processor_Archi.html?id=gYZyEAAAQBAJ | partial | Chapter titles and start pages of Aamodt et al. 2018 (1, 9, 21, 67, 85; bibliography 103; biographies 120). The TOC page image is served only as a 128 px thumbnail (unreadable). Google Books "search inside" returned a bot challenge, so it was left. |
| https://www.googleapis.com/books/v1/volumes | failed | Daily quota exhausted (HTTP 429). |
| https://searchworks.stanford.edu/view/12689676 , https://catalog.princeton.edu/catalog/10820415 , https://search.worldcat.org/oclc/1037800609 | failed | Bot challenge / "Verifying connection" / HTTP 403. Left as instructed. |
| WebSearch snippets of the WorldCat contents note (Aamodt) | partial | A18 section headings: ch1 1.1–1.4; ch3 3.1 One-Loop Approximation (3.1.1–3.1.3), 3.2 Two-Loop, 3.3 Three-Loop (operand collector, instruction replay), 3.4 Research Directions on Branch Divergence; ch4 first-level memory structures, on-chip interconnection network, memory partition unit, research directions. **Unverified** (search index only). |
| https://people.ece.ubc.ca/aamodt/ (and /publications/, book blog posts), https://engineering.purdue.edu/tgrogers/publication/aamodt-book-2018 | ok | No TOC or PDF; book announcements only. The old Morgan & Claypool catalogue page is dead, and the archive.org availability API rate-limited (429). |

**Papers added in this pass**

| Paper | URL | Status |
|---|---|---|
| gebhart2011compile | https://www.cs.utexas.edu/users/skeckler/pubs/micro11.pdf | ok (abstract and intro read) |
| jog2013owl | https://people.inf.ethz.ch/omutlu/pub/owl_asplos13.pdf | ok (abstract and intro) |
| jog2013orchestrated | https://people.inf.ethz.ch/omutlu/pub/orchestrated-gpgpu-scheduling-prefetching_isca13.pdf | ok (abstract) |
| ausavarungnirun2017mosaic | https://people.inf.ethz.ch/omutlu/pub/mosaic-application-transparent-multiple-page-sizes-for-GPUs_micro17.pdf | ok (abstract and intro) |
| ganguly2019interplay | https://par.nsf.gov/servlets/purl/10157887 (NSF PAR) | ok (abstract and the TBNp mechanism section) |
| li2021tlb | https://par.nsf.gov/servlets/purl/10316334 (NSF PAR) | ok (abstract and intro) |
| kim2020batch | https://ramyadhadidi.github.io/files/kim-asplos20.pdf (co-author page) | ok (abstract and measurement sections) |
| ye2024dlsched | https://arxiv.org/pdf/2205.11913 (arXiv v3, 2022 preprint of the CSUR paper) | ok (abstract) |
| karkhanis2004firstorder | typeset.io mirror | **failed**: HTML challenge. No author-hosted copy found (the UW archive lists its download as unavailable). Numbers come only from a search summary and are flagged. |
| jeon2015rfv | Hyeran Jeon / Murali Annavaram homepages (sites.usc.edu/scip/publications is JS-rendered with no PDF link; hyeranjeon.github.io and faculty.ucmerced.edu returned 404) | **failed**. Unpaywall lists the ACM DL PDF as open access, but automated fetching of dl.acm.org was refused by the session's permission classifier (bot-check), so it was left. Still a gap. |
| cambier2020s2fp8 (S2FP8, named on an M12 slide) | arXiv 2001.05674 BibTeX | ok (metadata) |

**Verification sources re-read for exact quotes in this pass:** CPG 12.4 (§3.1.1.2 JIT, §4.2, §5.4.2, CC sections); BPG (§9.2, §10.2.1, §10.2.3, §11.1); PTX ISA (`setp`, mma shape table); MPS overview (error containment, 60 clients per device); AWP (Volta and A100 tensor-core rates, BF16/TF32, 2:4 sparsity); HWP (FP8, TMA); rogers2012ccws (LRR/GTO definitions); hong2009analytical (equations 5–24); arunkumar2017mcmgpu (optimisation list, 256-SM configuration).

**Process note.** To query Unpaywall for an open-access location of Jeon 2015, the API's required `email` parameter was filled with the user's address. This was done once, on api.unpaywall.org only.
