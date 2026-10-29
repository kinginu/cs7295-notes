# Outline: GPU Hardware and Software (CS 7295 / CS 8803 O21)

Structure: 12 modules (M1–M12) and 42 lessons, following lowyx (all-modules page) and checked against the eizyc README headings.
Version 2 (2026-10-29). Every unit was re-expanded from a full re-read of the lowyx module text and all 229 lowyx slide images (one is a Canvas erratum page, not a slide), which were viewed and described. Each unit gives:
- the lesson objectives (verbatim);
- what it teaches, with definitions, formulas and worked examples with their numbers;
- key terms;
- the paper or book sections behind it;
- margin numbers with their sources;
- redraw-ready descriptions of the lowyx figures, given as "Figure `file`" or listed under "Figures (lowyx; redraw)".
**[SIMPLIFIED]** marks a place where the lecture is looser than, or contradicts, the paper or document behind it, and gives the precise statement. Slide errors found while describing figures are listed where they occur.

Source abbreviations
- **L** = lowyx all-modules notes (lecture transcript). Cite as `\source{M4, bank conflicts}`. Figure files are under `raw/lowyx_img/` (course slides: describe and redraw, never reproduce).
- **CPG** = CUDA C++ Programming Guide 12.4 (legacy numbering). **BPG** = CUDA C++ Best Practices Guide (2026). **PTX** = PTX ISA 9.4.
- **K12** = kim2012gpgpu. Its full section TOC was verified from the authors' PDF at jeewhanchoi.github.io (see sources.md).
- **A18** = aamodt2018gpu. Chapter page ranges come from Google Books (ch1 p. 1, ch2 p. 9, ch3 p. 21, ch4 p. 67, ch5 p. 85, bibliography p. 103). Section headings are taken from a WorldCat-derived search snippet only and are **unverified**.
- **PMPP** = hwu2022pmpp. **PPP** = mattson2004patterns.
- **AWP** = nvidia2020ampere. **HWP** = nvidia2022hopper (H100 figures preliminary, V1.02). **GEMM** = nvidia2026gemmguide.

K12 table of contents (verified): 1 GPU Design, Programming, and Trends (1.1 A Brief History of GPU; 1.2 A Brief Overview of a GPU System, 1.2.1 An Overview of GPU Architecture; 1.3 A GPGPU Programming Model: CUDA, 1.3.1 Kernels, 1.3.2 Thread Hierarchy in CUDA, 1.3.3 Memory Hierarchy, 1.3.4 SIMT Execution, 1.3.5 CUDA language extensions, 1.3.6 Vector Addition Example, 1.3.7 PTX, 1.3.8 Consistency Model and Special Memory Operations, 1.3.9 IEEE floating-point support, 1.3.10 Execution Model of OpenCL; 1.4 GPU Architecture, 1.4.1 GPU Pipeline, 1.4.2 Handling Branch Instructions, 1.4.3 GPU Memory Systems; 1.5 Other GPU Architectures, 1.5.1 Fermi, 1.5.2 AMD, 1.5.3 Many Integrated Core, 1.5.4 Combining CPUs and GPUs on the same Die) · 2 Performance Principles (2.1 Theory: Algorithm design models overview; 2.2 Characterizing parallelism: the Work-Depth Model; 2.3 Characterizing I/O behavior: the External Memory Model; 2.4 Combined analyses of parallelism and I/O-efficiency; 2.5 Abstract and concrete measures; 2.6 Summary) · 3 From Principles to Practice: Analysis and Tuning (3.1 The computational problem: Particle interactions; 3.2 An optimal approximation: the fast multipole method; 3.3 Designing a parallel and I/O-efficient algorithm; 3.4 A baseline implementation; 3.5 Setting an optimization goal, 3.5.1–3.5.3) · 4 Using Detailed Performance Analysis to Guide Optimization (4.1 Instruction-level Analysis and Tuning: 4.1.1 Execution Time Modeling, 4.1.2 Applying the Model to FMM, 4.1.3 Performance Optimization Guide; 4.2 Other Performance Modeling Techniques and Tools: 4.2.1 Limited Performance Visibility, 4.2.2 Work Flow Graphs, 4.2.3 Stochastic Memory Hierarchy Model, 4.2.4 Roofline Model, 4.2.5 Profiling and Performance Analysis of CUDA Workloads Using Ocelot, 4.2.6 Other GPGPU Performance Modeling Techniques, 4.2.7 Performance Analysis Tools for OpenCL).

A18 section headings (unverified, from a search snippet of the WorldCat contents note): ch1 1.1 the landscape of computation accelerators, 1.2 GPU hardware basics, 1.3 a brief history of GPUs, 1.4 book outline · ch3 3.1 One-Loop Approximation (3.1.1 SIMT Execution Masking, 3.1.2 SIMT Deadlock and Stackless SIMT Architectures, 3.1.3 Warp Scheduling), 3.2 Two-Loop Approximation, 3.3 Three-Loop Approximation (operand collector; instruction replay: handling structural hazards), 3.4 Research Directions on Branch Divergence, … · ch4 4.1 First-Level Memory Structures (scratchpad memory and L1 data cache; L1 texture cache; unified texture and data cache), 4.2 On-Chip Interconnection Network, 4.3 Memory Partition Unit, research directions for GPU memory systems.

Textbook map

| Module | K12 | A18 | PMPP 4e | CPG 12.4 / BPG / other |
|---|---|---|---|---|
| M1 | ch1 (§1.1, 1.2, 1.4.1) | ch1 | ch1, ch4 | CPG §1, §2, §4 |
| M2 | — | — | ch20 | PPP ch2–5, App. A–B; LLNL tutorial |
| M3 | §1.3 | ch2 | ch2–5, ch7–8 | CPG §2, §3, §4.2; BPG §11 |
| M4 | §1.4.1, §1.4.3 | ch3 (§3.1–3.3), ch4 | ch4–6 | CPG §4, §5.3, CC 5.x–9.0; BPG §10.2 |
| M5 | ch3, §4.1 | ch3 | ch6, ch10, ch22 | BPG §9–13; CPG §5, §7.19–7.29 |
| M6 | §1.4.1 (RF), §1.4.2 | ch3 (§3.1.1–3.1.2, §3.4), ch4 §4.1 | ch10 | CPG §4.1; CPG CC 7.x–9.0 shared memory |
| M7 | §1.4.1 (fetch policies) | ch3 §3.1.3, ch4 | — | CPG Unified Memory; BPG §10.1 |
| M8 | ch2, §4.1.1, §4.2.4 | ch5 | — | eeckhout2010perfeval |
| M9 | §1.5.4 | ch5 | ch20 | MPS overview; GPUDirect RDMA; HWP |
| M10 | §1.3.7 | — | — | PTX ISA; CPG §3.1; NVCC docs |
| M11 | — | — | ch10 | CPG §5.4.2, §7.39 |
| M12 | §1.3.9 | — | ch14, ch16, App. A | CPG §7.24–7.29; AWP; HWP; GEMM |

---

## M1 Introduction of GPU

Module objectives (L, verbatim): "Describe the basic backgrounds of GPU"; "Explain the basic concept of data parallel architectures".
Readings (L, verbatim):
- Required: "CUDA Programming guide, section 1-2, section 4" (legacy 12.x: §1 Introduction, §2 Programming Model, §4 Hardware Implementation); "Performance analysis and tuning for general purpose graphics processing units (GPGPU) (Chapter 1)" (K12 ch1 "GPU Design, Programming, and Trends", pp. 1–24).
- Optional: "Patterns for Parallel Programming, Chapter 2" (PPP).
Book sections behind the module: K12 §1.1 A Brief History of GPU, §1.2 A Brief Overview of a GPU System (§1.2.1 An Overview of GPU Architecture), §1.3 A GPGPU Programming Model: CUDA (§1.3.1–1.3.10), §1.4 GPU Architecture (§1.4.1 GPU Pipeline), §1.5 Other GPU Architectures. A18 ch1. CPG §1.1–1.3, §2.1–2.6, §4.1–4.2. PMPP ch1.

### M1.1 Instructor and Course Introduction
What it teaches
- Course learning objectives (L, verbatim list): "Describe how GPU architecture works and be able to optimize GPU programs"; "Conduct GPU architecture or compiler research"; "Explain the latest advancements in hardware accelerators"; "Build a foundation for understanding the CUDA features (the course does not teach the latest CUDA features)".
- Prerequisites (L): "Basic 5-stage CPU pipeline"; "C++/Python Programming skill set"; "Prior GPU programming experience is not necessary."
- Why GPUs matter: born for 3D graphics, now general parallel processors; today associated with ML accelerators and HPC.
- CPU vs GPU, the frame for the whole book. The lecture table (reproduce as a table; content verbatim):

| | CPU | GPU |
|---|---|---|
| Target applications | Latency sensitive applications | Throughput sensitive applications |
| Support precise exceptions? | Yes | No |
| Host-accelerator | Host | Accelerator |
| ISA | Public or open | Open/Closed |
| Programming model | SISD/SIMD | SPMD |

- Why "host/accelerator": GPUs rely on the CPU for OS and I/O work, so the CPU is the host and the GPU the accelerator.
- ISA point: CPUs keep a stable public ISA for software compatibility. GPUs run in accelerator mode, so a driver translates code to each hardware generation's ISA. PTX was introduced as a public, *virtual* ISA (developed fully in M10).
- SISD, SIMD and SPMD are defined. The lecture's analogies: SIMD is chefs doing the same chopping motion on different vegetables (strength: regular data-parallel work; weakness: branching under lockstep). SPMD is artists each working on a section of the same painting with their own data (more flexible with branches; overhead of thread management and communication).
Key terms: throughput, latency, precise exception, host, accelerator, ISA, virtual ISA, PTX, SISD, SIMD, SPMD.
Sources: L M1L1; K12 §1.2 ("A GPU is an accelerator (or a co-processor) that is connected to a host processor"); CPG §1.1 "The Benefits of Using GPUs".
Numbers: K12 §1.2 (2012): PCIe "provides 4 Gbit/s (Gen 2) or 8 Gbit/s (Gen 3)". The book means per lane; flag it if quoted. It adds that the link "often becomes one of the biggest bottlenecks".
Figures: none on lowyx for this lesson (table only).

### M1.2 Modern Processor Paradigms
Objective (L): "Describe CPU design and techniques to improve the performance on CPUs".
What it teaches
- The 5-stage CPU frame as used in the course: front-end (fetch from the I-cache), decode (x86 cracks one instruction into several micro-ops), rename, schedule, execute (compute or memory access), write-back. Register files are read after decode. An in-order scheduler issues in program order; an out-of-order one issues any ready instruction.
- Single-issue vs superscalar: a superscalar fetches, decodes and executes more than one instruction per cycle, so IPC > 1.
- Increasing parallelism (1): ILP. With two execution units, (a) two independent instructions issue together, while (b) a dependent pair serialises (instruction 2 waits for instruction 1). OoO execution finds more independent instructions, which has been a main focus of CPU design.
- Increasing CPU performance: deeper pipelines for frequency (which need better branch prediction) and larger caches (fewer misses).
- Increasing parallelism (2): multithreading, i.e. switch to another thread's ready instruction. It is "one of the key ingredients of high performance GPUs" and cheap in hardware.
- Multiprocessors: replicate whole cores. Used in both CPUs and GPUs.
Key terms: front-end, micro-op, rename, in-order/out-of-order scheduling, superscalar, IPC, ILP, dependence, branch prediction, multithreading, multiprocessor.
Sources: L M1L2; any HPCA text (cs6290 companion book).
- Figure `m1l2_cpupipeline` (lowyx, redraw): Pipeline strip Front-end | Decode | Schedule | Execution | Write-back (orange latch bars; "Memory" above Front-end and below Execution). Left: "5-stage pipeline" with 4 green rows F D S E W staggered one cycle. Right: "Superscalar" with 8 rows in 4 aligned pairs (2 instructions per cycle).
- Figure `m1l2_ilp` (lowyx, redraw): Text only. case (a): `#1: R1 = R2 + R3`, `#2: R4 = R6 + R5` (independent). case (b): `#1: R1 = R2 + R3`, `#2: R4 = R1 + R5` (#2 reads R1, so dependent).
- Figure `m1l2_multi_thread` (lowyx, redraw): Same pipeline strip with three charts: "5-stage pipeline" (4 staggered rows), "Superscalar" (4 aligned pairs), "Multi-threading" (4 pairs, each pair a different colour = a different thread: green, white/orange outline, yellow, lavender).
- Figure `m1l2_cpu_gpu` (lowyx, redraw): "CPU": 4 large "Core" boxes over one wide "Cache". "GPU": a 4×4 grid of small "Core" boxes with a thin "Cache" bar between rows 2 and 3.

### M1.3 How to Write Parallel Programs
Objectives (L): "Describe different parallel programming paradigms"; "Recognize Flynn's classical taxonomy"; "Explore a CUDA program example".
What it teaches
- **Amdahl's law** (lecture form): speedup = 1 / (P/N + S), where P is the parallel fraction, S the serial fraction (P + S = 1) and N the number of processors. With little serial work the speedup scales almost linearly with N. A serial fraction "even 10%" caps scalability: the limit is 1/S = 10× however large N grows.
- Worked numbers for the book (derived from the formula, not on the slide): S = 0.1, N = 8 gives 1/(0.9/8 + 0.1) = 4.7×; N = 1024 gives 9.9×.
- Writing parallel programs, with the running example "array addition and find min/max":
  - **Task decomposition**: one core sums while the other finds min/max, and the whole array A is sent to both cores.
  - **Data decomposition**: split the array across the two cores, and each core does both operations on its half; a **reduction** (for the sum and for min/max) combines the partial results.
- **Flynn's taxonomy**: SISD, SIMD/SIMT, MISD, MIMD. "CPUs can be SISD, SIMD, and MIMD"; "GPUs are typically SIMT". CPUs do SIMD with vector units; GPUs do SIMT with many ALUs.
- **SPMD**: all threads run the same program on different data. Data decomposition is SPMD's typical pattern. "SPMD is typical GPU programming pattern and the hardware's execution model is SIMT."
- First CUDA-flavoured kernel, pseudocode `vector_sum() { index; // differentiate by thread ids  sum += A[index]; }`. All threads run the same `vector_sum()`.
- Note for writers: the lecture's `sum += A[index]` from many threads is a data race. Use it to motivate reductions (M2.2) rather than present it as correct code.
Key terms: Amdahl's law, parallel/serial fraction, speedup, task decomposition, data decomposition, reduction, Flynn's taxonomy, SISD/SIMD/SIMT/MISD/MIMD, SPMD.
Sources: L M1L3; BPG §4.1.3.1 (S = 1/((1−P)+P/N)) and §4.1.3.2 Gustafson's law S = N + (1−P)(1−N); PPP ch2; LLNL tutorial "Amdahl's Law" section.
- Figure `m1l3_amdahllaw` (lowyx, redraw): Line chart, y "speedup" 0–18, x "Serial fraction" from 1 down to 0.05 in steps of 0.05. Curves for N = 2, 4, 8, 16, 100. All stay below ~3 until S ≈ 0.3, then spread. At S = 0.05: ≈1.9, 3.5, 6, 9.1, 16.8 (= 1/(0.05 + 0.95/N)). N = 100 is ≈9.2 at S = 0.1.
- Figure `m1l3_taskdecompose` (lowyx, redraw): Row A[0]…A[9]. Arrows from the whole array to "Core #1" → "Total sum" and "Core #2" → "Total min/max".
- Figure `m1l3_datadecompose` (lowyx, redraw): A[0]–A[4] → Core #1 → "Partial sum-1"; A[5]–A[9] → Core #2 → "Partial sum-2"; "Total sum" centred below (no arrows drawn into it).
- Figure `m1l3_flynn` (lowyx, redraw): 2×2 grid: SISD "Single Instruction, Single Data"; SIMD/SIMT "Single Instruction, Multiple Data/Thread"; MISD "Multiple Instruction, Single Data"; MIMD "Multiple Instruction, Multiple Data".

### M1.4 Introduction to GPU Architecture
Objectives (L): "Gain a high-level understanding of GPU architecture"; "Describe key terms including 'streaming multiprocessors' and 'warp' and 'wave-front'".
What it teaches
- A GPU is many cores, each able to run many threads. NVIDIA calls the core a **streaming multiprocessor (SM)** ("SIMT multiprocessor"). An SM contains an instruction cache, decoder, shared memory and many **stream processors (SP)**, which are ALUs or SIMT lanes and are marketed as "cores". The course rule is **"core ≠ stream processor"**: a SIMT lane is never called a core. Keep this convention in the book (JA: SM = コア, lane = レーン).
- GPU pipeline overview: fetch (each work item fetched; multiple PC/register sets support multithreading) → schedulers (round-robin, or "greedy" schedulers that consider cache misses or branch outcomes) → decode → register read → scheduler/scoreboard selects ready warps → execute → write-back. This is detailed in M4.3.
- **Warp / wavefront**: a group of threads that forms the unit of execution. One instruction is fetched per warp and executed by all its threads. "Warp size ... has remained constant at 32 for an extended period but this can be changed in future." The course uses warp and wavefront interchangeably.
- Worked example: the programmer launches 12 threads; with warp size 4 they form 3 warps. When a warp's source operands are ready the whole warp executes, then the next ready warp, and so on.
Key terms: streaming multiprocessor (SM), SIMT multiprocessor, stream processor (SP), SIMT lane, warp, wavefront, warp size, scheduler, scoreboard.
Sources: L M1L4; K12 §1.2.1 ("NVIDIA calls an SM and AMD calls a Compute Unit (CU). Each SM has a number of single-instruction multiple data (SIMD) units, also called stream processors (SPs)"); A18 ch1; CPG §4.1.
Numbers: warp size 32 for CC 5.0–9.0 (CPG Table 21). CPG §4.1: "The term warp originates from weaving, the first parallel thread technology." K12 §1.4.1: G80 had 8 lanes per SM, so a 32-thread warp took four cycles. G80 had a 16 KB software-managed cache (shared memory) and a 32 KB register file per SM (K12 §1.2.1; §1.4.1 says 64 KB RF for G80 and 128 KB per SM for Fermi, so the two passages disagree; cite with care).
- Figure `m1l4_gpuarch` (lowyx, redraw): 4×4 "Core" grid with a "Cache" bar, captioned "GPU". One core zoomed: stack of "PC" cards, "I-Cache", "Decoder", "Shared Memory", 4 vertical "Stream Processor" bars (• • • before the 4th), "Caches".
- Figure `m1l4_gpupipeline` (lowyx, redraw): Block diagram: "Scheduler" ↔ "Active bit mask vectors/score boarding"; I-cache ↔ "Fetch unit" → "Decoder" → "Register" → "Scheduler (Score boarding)" → lanes "Lane 0, Lane 1, …, Lane N-1" → "Memory access unit" (↔ "Memory") → second lane row → "Writeback", with a feedback arrow from Writeback to Register.
- Figure `m1l4_gpuwarp` (lowyx, redraw): "Warp Execution" (frame 1): program page Inst 1–3 with Inst 1 circled; 12 "T" squares in 3 coloured groups of 4, each bracketed "One warp"; "SIMT Execution Unit" with 4 "SP" slots, empty.
- Figure `m1l4_gpuwarp2` (lowyx, redraw): Frame 2: the first (grey) warp's 4 T's sit on the 4 SP slots executing Inst 1; the cyan and yellow warps wait.

### M1.5 History Trend of GPU Architectures
Objectives (L): "Describe the evolution history of GPUs"; "Describe the evolution of traditional 3D graphics pipelines".
What it teaches
- Four stages (L, verbatim bullets): "Traditional pipelined GPUs: separate Vortex [sic: vertex] processing and pixel processing units"; "Programmable GPUs: introduction of programmable units for vertex/pixel shader"; "Vertex/pixel shader progression to CUDA programmable cores (GPGPU)"; "Modern GPUs: addition of ML accelerator components (e.g., tensor cores), programmable features."
- Traditional 3D pipeline: 3D primitives in → geometry processing → 2D primitives → rasterised into pixels. Fixed-function shaders became programmable, then unified shaders (a hallmark of Tesla), which opened GPGPU. The term "GPGPU" is no longer needed now that GPUs are routinely used for non-graphics work.
- Evolution list (L): cache hierarchies (L1, L2); FP32 → FP64 for HPC; atomics and fast integer operations; HBM; smaller formats (FP16) for ML; tensor cores; "transformer cores" (Transformer Engine).
- NVIDIA H100 ("2023's latest"): FP32, FP64, FP16, INT8 and FP8; tensor cores; Transformer Engine; larger register files; Tensor Memory Accelerator; more SMs and FP units; NVLink Switch System.
Key terms: graphics pipeline, vertex/pixel processing, shader, unified shader, GPGPU, HBM, tensor core, Transformer Engine, TMA, NVLink Switch.
Sources: L M1L5; K12 §1.1 (fixed pipelines → programmable cores; shader-language GPGPU via DirectX/OpenGL/Cg; Brook+/Sh stream extensions; "the inflection point ... G80 family ... CUDA"); A18 ch1 (brief history); HWP (H100 feature list).
Numbers (AWP Table 4, HWP Table 3):

| | P100 | V100 | A100 | H100 SXM5 (prelim.) |
|---|---|---|---|---|
| SMs | 56 | 80 | 108 | 132 |
| FP32 cores/SM | 64 | 64 | 64 | 128 |
| Tensor cores/SM | — | 8 | 4 | 4 |
| Register file/SM | 256 KB | 256 KB | 256 KB | 256 KB |
| L2 | 4 MB | 6 MB | 40 MB | 50 MB |
| HBM bandwidth | 720 GB/s | 900 GB/s | 1555 GB/s | 3000 GB/s |
| Transistors | 15.3 B | 21.1 B | 54.2 B | 80 B |
| Process | 16 nm | 12 nm | 7 nm | 4N |

- Figure `m1l5_trad3dpipeline` (lowyx, redraw): Left-to-right flow: "3D primitives" → "Geometry Stage" (caption "Vertex shader") → "2D primitives" → "Rasterization Stage" (caption "Fragment (pixel) shader") → "pixels".

---

## M2 Parallel Programming

Module objectives (L): verbatim copies of M1's objectives ("Describe the basic backgrounds of GPU"; "Explain the basic concept of data parallel architectures"). This is a copy error in the notes; the real aim, from the lesson objectives, is shared- vs distributed-memory programming with OpenMP and MPI as a bridge to CUDA.
Readings (L, verbatim):
- Required: "Introduction to Parallel Computing tutorial" (LLNL, barney2026parallel).
- Optional: "Parallel programming patterns, Chapter 3, Appendix A, Appendix B" (PPP ch3 Finding Concurrency design space; App. A OpenMP; App. B MPI).
Code the lessons show: small C++ programs with OpenMP pragmas (full listings), and MPI only as call names in diagrams.

### M2.1 Parallel Programming Patterns
Objective (L): "Provide an overview of different parallel programming paradigms".
What it teaches
- Creating a parallel application: the original program's tasks are divided, the data structures adapted, and the work distributed to processors (figure).
- Four steps (L): (1) discover concurrency, (2) structure the algorithm to exploit it, (3) implementation (choose language and tools), (4) execution and optimisation (tune on the parallel system).
- Five patterns:
  - **Master/Worker**: a master process or thread manages a pool of workers and a task queue; workers dequeue and run tasks concurrently. Good when work splits into independent pieces.
  - **Loop Parallelism**: independent iterations, e.g. `for (i = 0; i < 16; i++) c[i] = A[i]+B[i];`. Unlike master/worker, the tasks are usually identical.
  - **SPMD**: every processing element runs the same program on its own data. "A popular choice, especially in GPU programming."
  - **Fork/Join**: a parent forks child tasks, then joins (waits) before continuing; it mixes serial and parallel phases from a single entry point.
  - **Pipeline**: stages over a data stream, like a CPU pipeline. Examples: signal processing, graphics pipelines, compression workflows (decompress → work → compress).
Key terms: concurrency, design pattern, master/worker, task queue, loop parallelism, SPMD, fork/join, pipeline.
**[SIMPLIFIED]** In PPP these patterns sit in different design spaces: Finding Concurrency (ch3: task and data decomposition), Algorithm Structure (ch4: e.g. Pipeline) and Supporting Structures (ch5: SPMD, Master/Worker, Loop Parallelism, Fork/Join). The lecture flattens them into one list of five.
Sources: L M2L1; PPP ch3–5.
- Figure `m2l1_parallelapp` (lowyx, redraw): "Original Program" (one big yellow block + orange + green bars) → "Divide the work / Adjust the data structure" (6 yellow strips, 2 orange, 1 green) → "Distribute the work" (6 "Processors" boxes).
- Figure `m2l1_master_worker_pattern` (lowyx, redraw): Box "Master: Initiate computation, Set up problem, Create bag of tasks, Lunch [sic: Launch] workers, Wait, Collect results, Terminate computation". To its right, a "bag" of coloured task rectangles (one labelled "task"). Arrows: Initiate → task; a task → Wait.
- Figure `m2l1_forkjoin_pattern` (lowyx, redraw): "Parallel region": one line enters a yellow box, forks into 4 paths and rejoins to one line on the right.
- Figure `m2l1_pipeline_pattern` (lowyx, redraw): 4 "Work" boxes → 4 rows of 5 coloured stage squares (red, green, purple, yellow, grey), each row shifted one step right (staircase).

### M2.2 OpenMP vs. MPI (Part 1)
Objectives (L): "Explain the fundamental concepts of shared memory programming"; "Describe key concepts essential for shared memory programming"; "Explore the primary components of OpenMP programming".
What it teaches
- **Shared-memory programming**: all processors access one memory. P1 writes a value and P2 sees it by reading it.
- **Distributed-memory programming**: each processor has its own memory, so remote data travels in messages. Figure example: the same address in three memories; P2 requests data from P1 (value 0) and P3 (value 200), adds them, and writes back.
- **OpenMP** = "a collection of compiler directives, library routines, and environment variables to write parallel programs", an open standard for shared-memory systems.
- Key tasks of parallel programming: parallelisation, specifying the thread count, scheduling, data sharing, synchronisation.
- **Thread**: "an entity that runs on a sequence of instructions", with its own registers and stack. A thread is a software concept and is not a core: one core may run several threads. Its meaning differs on CPUs and GPUs.
- Data decomposition revisited: a 10-element array is split in half across two cores (one thread per core assumed).
- Serial vector sum (listing: `int main(){ const int size = 10; ... for (int i = 0; i < size; ++i) sum += data[i]; ... }`).
- Manual parallelisation: (1) create two threads, (2) give each half the array, (3) merge the two partial sums. The merge is a **reduction**.
- Reduction in shared memory: each thread computes a partial sum, then updates the total in memory one at a time. Without protection the total ends up 100 or 200 instead of 300 (the race). Updating a shared variable is a **critical section**, protected by a **mutex** (lock to acquire, unlock to release).
- Low-level route: pthreads, with manual create/join/mutex.
- OpenMP route: `#pragma omp parallel for reduction(+:sum)` over the loop (listing with `size = 1000`). "Parallel for" invokes the loop-parallelism pattern and creates the threads.
- Directive anatomy: `#pragma omp directive [ clause [ clause ] ... ]`. The compiler replaces directives with runtime-library calls that create and join threads. It works for C/C++/Fortran. `reduction(+:sum)` is a clause.
Key terms: shared memory (CPU sense), distributed memory, message, OpenMP, compiler directive, clause, runtime library, thread, stack, partial sum, reduction, race, critical section, mutex, lock/unlock, pthreads.
Sources: L M2L2; PPP App. A; LLNL tutorial (shared vs distributed memory models).
- Figure `m2l2_shared_mem` (lowyx, redraw): Processor 1 ("mem[0x100] = 10"), Processor 2 ("mem[0x100] = ?"), Processor 3, all arrowed to one "Memory" holding "mem[0x100] =10".
- Figure `m2l2_shared_mem_distributed` (lowyx, redraw): Processors 1–3 each with their own Memory: Mem[0x100] = 0 (orange), = 100 (blue), = 200 (red). P2 has arrows to all three with message envelopes on the remote ones. Above P2: "0 + 100 + 200 = 300".
- Figure `m2l2_data_decomposition` (lowyx, redraw): A[0]…A[9] above Core #1 and Core #2, with a thread squiggle drawn on each core.
- Figure `m2l2_data_decomposition2` (lowyx, redraw): A[0]–A[4] → Core #1, A[5]–A[9] → Core #2.
- Figure `m2l2_manual_parallel` (lowyx, redraw): Each half → a thread (wavy line) → "Partial sum-1" / "Partial sum-2"; "Total sum" below.
- Figure `m2l2_shared_memory_sum` (lowyx, redraw): Two thread boxes: "Partial-sum1 = 100, 100 + ___ = 100" and "Partial-sum2 = 200, 200 + ___ = 300", both arrowed to Memory "Mem[sum] = 0". The blanks are the value each thread reads from memory (0, then 100).

### M2.3 OpenMP vs. MPI (Part 2)
Objectives (L): "Extend your understanding of the concept of scheduling in OpenMP"; "Describe key components of OpenMP and MPI programming".
What it teaches
- **How many threads?** Set it with the environment variable `OMP_NUM_THREADS` or with `omp_set_num_threads()`. The default equals the hardware parallelism (number of cores).
- **Scheduling problem**: 1 M elements, 5 threads, 2 cores. One core runs 3 threads and the other 2, so equal chunks progress unevenly.
- Options (L):
  1. *static*: 200 K elements to each thread.
  2. *dynamic, chunk 1*: one element per request; the thread asks for more when done.
  3. *dynamic, chunk 1000*: amortises the cost of asking.
  4. *guided*: chunk size shrinks over time (start at 1000, later 100).
  Dynamic scheduling adapts to run-time effects (e.g. a thread on a slower machine).
- **Data sharing**: private (partial sums) vs shared (total). The programmer must specify the policy.
- **Synchronisation** (correctness):
  - `#pragma omp barrier`: all threads reach the point before any continues ("Green work won't be started until all blue work is over").
  - `#pragma omp critical [(name)]`: one thread at a time (example: `parallel num_threads(4)` around a critical block; only one thread in the red region).
  - `#pragma omp atomic`: e.g. `counter++`, whose load, add and store happen all or nothing; implemented with a mutex or hardware support.
- **Work outside loops**: `#pragma omp parallel sections` with `#pragma omp section` blocks (work-1 and work-2 in parallel). Combined constructs:
  - `ordered`: a `for ordered` loop prints "Hello thread %d is doing iteration %d" in ascending order.
  - `single`: exactly one (unspecified) thread runs the block, e.g. for initialisation.
Key terms: OMP_NUM_THREADS, omp_set_num_threads, static/dynamic/guided schedule, chunk size, load imbalance, private/shared variable, barrier, critical, atomic, sections, ordered, single.
Sources: L M2L3; PPP App. A.
Note for writers: the lecture's listing `#pragma omp atomic counter++;` puts the statement on the pragma line. In real code `counter++;` goes on the next line.
- Figure `m2l3_barrier` (lowyx, redraw): Blue box of ~5 thread lines, a yellow "Barrier" bar, a green box of thread lines (no thread enters green until all finish blue).
- Figure `m2l3_critical` (lowyx, redraw): Legend: red = "Critical section". Rows Th 1–Th 4 are long blue bars, each with one red segment, staggered back-to-back so no two overlap.
- Figure `m2l3_ordered` (lowyx, redraw): Two console panels. "#pragma omp": Hello thread 1/2/4/3/5 is doing iteration 1/2/4/3/5 (4 before 3). "#pragma omp ordered": iterations 1, 2, 3, 4, 5 in order.

### M2.4 Programming with MPI
Objectives (L): "Describe fundamental concepts of distributed memory parallel programming"; "Gain understanding of MPI (Message Passing Interface) programming".
What it teaches
- Why OpenMP and MPI before CUDA: "CUDA programming combines elements of shared memory and distributed memory programming. Some memory regions are shared among all cores, while others remain invisible and need explicit communications."
- MPI point-to-point: process 0 sends an integer with `MPI_Send()` and process 1 receives it with `MPI_Recv()`. Collective: `MPI_Bcast()` sends from one process to all others.
- **Stencil** (common in HPC): each output C is the average of its 4 neighbours (N, S, E, W), applied to every element.
- Distributed stencil on 4 processes: each process can access only its own region, so an element C on a region edge needs values owned by neighbours ("orange and green area").
- Fix: communicate the **boundary** (grey cells) by messages before computing. This is the halo exchange that M3.4 mirrors on the GPU with shared memory.
Key terms: MPI, process, rank, MPI_Send/MPI_Recv, broadcast, collective, stencil, neighbourhood, boundary (halo) exchange.
Sources: L M2L4; PPP App. B; LLNL tutorial; PMPP ch20 (MPI + CUDA).
- Figure `m2l4_mpi_programming` (lowyx, redraw): "Process 0" ⇄ "Process 1" with a message envelope (send right, receive left).
- Figure `m2l4_broadcasting` (lowyx, redraw): Process 0 sends envelopes to Process 1, 2 and 3.
- Figure `m2l4_stencil` (lowyx, redraw): A 10 × 8 grid; centre "C" (row 5, col 5) with neighbours 1 (above), 2 (left), 3 (right), 4 (below).
- Figure `m2l4_stencil2` (lowyx, redraw): The same grid in 4 quadrants (orange top-left cols 1–5 rows 1–4; yellow top-right; blue bottom-left; green bottom-right). C, 2 and 4 are in blue; 1 is in orange; 3 is in green.
- Figure `m2l4_stencil3` (lowyx, redraw): Only the blue quadrant (cols 1–5, rows 5–8) plus a grey one-cell halo: row 4 cols 1–5 and col 6 rows 5–8 (corner (4,6) not included). 1 and 3 are grey halo cells.

---

## M3 GPU Programming Introduction

Module objectives (L, verbatim): "Describe GPU programming basic"; "Be able to program using CUDA".
Readings (L): "CUDA Programming guide, Section 3" (legacy §3 Programming Interface: §3.1 Compilation with NVCC, §3.2 CUDA Runtime, ...). In practice §2 Programming Model is also needed.
Book sections: K12 §1.3 A GPGPU Programming Model: CUDA (§1.3.1 Kernels, §1.3.2 Thread Hierarchy in CUDA, §1.3.3 Memory Hierarchy, §1.3.4 SIMT Execution, §1.3.5 CUDA language extensions, §1.3.6 Vector Addition Example). A18 ch2 Programming Model. PMPP ch2–5, 7–8. CPG §2.1–2.4, §3.2; BPG §11.

### M3.1 Introduction of CUDA Programming
Objectives (L): "Write kernel code for Vector Addition"; "Explain basic CUDA programming terminologies"; "Explain Vector addition CUDA code example".
What it teaches
- **Vector addition**. Kernel: `__global__ void vectorAdd(const float *A, const float *B, float *C, int numElements) { int i = blockDim.x * blockIdx.x + threadIdx.x; if (i < numElements) C[i] = A[i] + B[i] + 0.0f; }` (the lecture listing has typos: `__global` and a missing `;`). Host: `cudaMalloc((void **)&d_A, size)`, `cudaMemcpy(d_A, h_A, size, cudaMemcpyHostToDevice)`, `vectorAdd<<<blocksPerGrid, threadsPerBlock>>>(d_A, d_B, d_C, numElements)`, `cudaMemcpy(h_C, d_C, size, cudaMemcpyDeviceToHost)`. The host sets up data and memory and launches with triple angle brackets, passing grid and block sizes plus the kernel arguments.
- **SPMD**: four threads each print "hello, I'm an OMSCS student" in no particular order. To work on different data, each thread needs an identifier.
- **`threadIdx.x`**: a built-in x-coordinate of the thread. Simplified add: `int idx = threadIdx.x; c[idx] = a[idx] + b[idx];`.
- **Execution hierarchy**: threads → blocks → grid. A warp is a microarchitecture concept, hidden in early CUDA and exposed later. A CUDA block is "a group of threads that are executed concurrently". Because blocks have different memory scopes, data is divided among blocks. Simplification: one block per SM. No guaranteed order among blocks.
- **Indexing**: `threadIdx.{x,y,z}`, `blockIdx.{x,y}`. 16 elements over 4 blocks of 4 threads: `idx = blockIdx.x * blockDim.x + threadIdx.x` (e.g. block 2, thread 1 gives idx = 9). 2D/3D indices match images and volumes.
- **Shared memory**: a software-managed scratchpad on chip, declared `__shared__`, faster than off-chip global memory, visible only within one block. Example: `__shared__ int sharedMemory[N]; sharedMemory[idx] = a[idx] + b[idx]; __syncthreads(); c[idx] = sharedMemory[idx];`.
- **Execution order**: threads in any order (prints 4,3,2,1 / 1,3,4,2 / 1,2,3,4); blocks in any order (ascending, descending, three at once).
- **Synchronisation**: `__syncthreads()` is a barrier across the threads of one block. Inter-block synchronisation needs separate kernel launches.
- **BSP usage pattern**: load global → shared; `__syncthreads()`; compute; `__syncthreads()`; store shared → global. The course calls this "BSP, Bulk Synchronous Parallel".
- **Kernel launch**: total threads = gridDim × blockDim. Example host: `sortKernel<<<1,1>>>(d_data, dataSize); addKernel<<<gridDim,blockDim>>>(...); storeKernel<<<1,1>>>(d_result, dataSize);`. Different kernels with different configurations, with single-thread kernels for serial steps.
- **Memory spaces** summary: local (per thread), shared (per block), global (all blocks of a kernel), constant (small, read-only, e.g. the value of π; the transcript writes "fhi") and texture (read-only, 2D-structured), the last two inherited from graphics and little used. Information sharing is limited by the hierarchy: shared-memory data stays in one SM. Thread block clusters (Hopper) are mentioned as the newer way to share shared memory.
Key terms: kernel, `__global__`, host code, device code, launch configuration, grid, block (CTA), thread, `threadIdx`, `blockIdx`, `blockDim`, `gridDim`, global index, SPMD, `__shared__`, `__syncthreads()`, barrier, BSP, local/shared/global/constant/texture memory, thread block cluster.
**[SIMPLIFIED]** (a) One block per SM is a simplification; several blocks are resident per SM (M3.2). (b) CPG §2.2: blocks "are required to execute independently: It must be possible to execute them in any order, in parallel or in series." The lecture says the same informally (verify the exact sentence in CPG §2.2 before quoting).
Numbers (CPG Table 21): max 1024 threads/block; block x,y ≤ 1024, z ≤ 64; grid x ≤ 2^31−1, y,z ≤ 65535; constant memory 64 KB with an 8 KB per-SM constant cache (4 KB on some CCs); local memory up to 512 KB per thread. K12 Table 1.4 (Tesla/Fermi era) latencies: local and global "100s cycles", shared "4 – 32 cycles", constant/texture "100s cycles or 4 cycles (cache hit)".
Sources: L M3L1; CPG §2.1 Kernels, §2.2 Thread Hierarchy, §2.3 Memory Hierarchy, §2.4 Heterogeneous Programming; K12 §1.3; PMPP ch2–3; A18 ch2.
- Figure `m3l1_spmd` (lowyx, redraw): Box "program: print_kernel() { prinf("Hello I'm an OMSCS student\n"); }" [sic prinf] → 4 thread squiggles → 4 staircase banners "Hello I'm an OMSCS student". Caption "Executed by 4 threads?".
- Figure `m3l1_threadidx` (lowyx, redraw): Same with `printf("Hello I'm %dth an OMSCS student", threadIdx.x)`. Banners read "Hello I'm 1th / 2th / 3th / 4th OMSCS student".
- Figure `m3l1_threadidx_vectoradd` (lowyx, redraw): Blue row 0–15 "+" green row 0–15. Below, 16 units each pairing one blue and one green cell with "+" and one thread line.
- Figure `m3l1_data_index` (lowyx, redraw): "N=16, blockDim=4 → 4 blocks". Four groups with captions: Block k: blockIdx.x = k, blockDim.x = 4, threadIdx.x = 0,1,2,3, Idx = 4k…4k+3 (0–3, 4–7, 8–11, 12–15).
- Figure `m3l1_sharedmemory` (lowyx, redraw): 4×4 grid of "SM", each with a small green square (its shared memory) at the lower right; a wide "Global memory" box below.
- Figure `m3l1_execution_order_threads` (lowyx, redraw): The same kernel (`threaddx.x` [sic]) → three output sets with ordinals 1,2,3,4 / 4,3,2,1 / 1,3,4,2.
- Figure `m3l1_execution_order_blocks` (lowyx, redraw): Grid of 6 blocks Block (0,0)…(2,1) → "Case 1" sequential in order; "Case 2" sequential in the order (2,1),(1,1),(1,0),(0,0),(2,0),(0,1); "Case 3" two rows of three blocks overlapping (concurrent).
- Figure `m3l1_usage_with_thread_sync` (lowyx, redraw): A tall block of ~10 thread lines in three phases separated by two "Thread synch" bars.
- Figure `m3l1_kernel_launch` (lowyx, redraw): Bullets: launch with `<<< >>>`; `kernelName<<<numBlocks, threadsPerBlock>>>(arguments);`; "Total number of threads in a kernel = numBlocks x threadsPerBlock"; "Grid consists of multiple blocks, block consists of multiple threads"; "Multiple different tasks → multiple kernels". Code: `sortKernel<<<1,1>>>` (label "1 CUDA block & 1 CUDA thread"), `addKernel<<<gridDim,blockDim>>>` ("gridDim x blockDim"), `storeKernel<<<1,1>>>`.
- Figure `m3l1_memory_space` (lowyx, redraw): Table (Scope / Note): Shared Memory — Within one CUDA block; Global Memory — All blocks in a Kernel; Local Memory — Within a CUDA thread; Constant Memory — All blocks in a Kernel, Read only (3D-graphics); Texture Memory — All blocks in a Kernel, Read only (3D graphics). Footnote: constant memory stores constants for graphics; texture memory stores texture images (2D data).

### M3.2 Occupancy
Objectives (L): "Explain the concept of occupancy"; "Determine how many CUDA blocks can run on one Streaming Multiprocessor".
What it teaches
- Several blocks share an SM. How many is decided by three resources (lecture): **registers, shared memory, number of threads**. The exact limits vary by generation.
- **Worked example (lecture numbers).** Hardware per SM: 256 threads, 64 × 1024 registers, 32 KB shared memory. Kernel: 32 threads per block, 64 registers per thread, 2 KB shared memory per block.
  - Thread limit: 256 / 32 = **8** blocks.
  - Register limit: (64 × 1024) / (64 × 32) = **32** blocks (the transcript garbles this as "641,024/6432").
  - Shared-memory limit: 32 KB / 2 KB = **16** blocks.
  - Answer = min(8, 32, 16) = **8 blocks per SM** (thread-limited).
- Who sets what: the host sets threads per block at launch (`kernelName<<<numBlocks, threadsPerBlock>>>(args)`). The **compiler** sets registers per thread (unlike a CPU, where the ISA fixes, e.g., 32 architectural registers). Shared memory per block comes from the declarations: `__shared__ int sharedMemory[1000];` is 4 × 1000 = 4000 bytes.
- Why occupancy matters: more parallelism and better utilisation usually mean more performance (exceptions come in M7.3).
  - Comparison: case A has 4 SMs × 1 block × 6 threads = 24 threads; case B has 4 SMs × 2 blocks × 4 threads = 32 threads, so B keeps more threads busy despite smaller blocks.
- Exact definition (BPG §11.1, verbatim): "Occupancy is the ratio of the number of active warps per multiprocessor to the maximum number of possible active warps." Also: "Higher occupancy does not always equate to higher performance-there is a point above which additional occupancy does not improve performance. However, low occupancy always interferes with the ability to hide memory latency, resulting in performance degradation."
- Full formula for the book (BPG §11 and CPG §4.2, real-hardware form): blocks/SM = min(⌊MaxThreads/SM ÷ T⌋, MaxBlocks/SM, ⌊Regs/SM ÷ (R × T)⌋, ⌊Smem/SM ÷ S⌋), with T = threads per block, R = registers per thread, S = shared memory per block. Warps per block = ceil(T / 32) (CPG §4.2). Occupancy = blocks/SM × warps/block ÷ MaxWarps/SM.
- Book worked example on real numbers (A100, CC 8.0): T = 256 (8 warps), R = 64, S = 48 KB. Threads: 2048/256 = 8. Registers: 65,536/(64 × 256) = 4. Smem: 164/48 = 3. Blocks: 32. So min = 3 blocks = 24 warps, occupancy 24/64 = 37.5 %. Allocation granularity (registers allocated per warp in units, smem allocation units, 1 KB reserved per block on CC ≥ 8.0) is ignored here; check the CUDA Occupancy Calculator rules before printing.
Key terms: occupancy, resident block, active warp, max warps per SM, resource limit, register pressure, shared memory per block, theoretical vs achieved occupancy, latency hiding.
**[SIMPLIFIED]** (a) The lecture's "64 kilobyte of register files" means 64 K registers; real SMs have 65,536 × 32-bit = 256 KB (AWP/HWP). (b) The lecture omits the max-blocks-per-SM limit and allocation granularities. (c) "Higher occupancy, more performance" is qualified by BPG and by M7.3's CCWS.
Numbers (CPG Table 21; HWP Table 4):

| CC | Max threads/SM | Max warps/SM | Max blocks/SM | Regs/SM | Max regs/thread | Max smem/SM | Max smem/block |
|---|---|---|---|---|---|---|---|
| 7.0 (V100) | 2048 | 64 | 32 | 64 K | 255 | 96 KB | 96 KB |
| 7.5 (Turing) | 1024 | 32 | 16 | 64 K | 255 | 64 KB | 64 KB |
| 8.0 (A100) | 2048 | 64 | 32 | 64 K | 255 | 164 KB | 163 KB |
| 8.6 | 1536 | 48 | 16 | 64 K | 255 | 100 KB | 99 KB |
| 9.0 (H100) | 2048 | 64 | 32 | 64 K | 255 | 228 KB | 227 KB |

(Values follow the CPG 12.4 Table 21 layout; re-read the table cell by cell before printing, because the extracted HTML lost colspans.)
Sources: L M3L2; BPG §11.1 Occupancy, §11.1.1 Calculating Occupancy, §11.3 Thread and Block Heuristics, §11.4 Effects of Shared Memory; CPG §4.2; PMPP ch4.
- Figure `m3l2_howmanycuda` (lowyx, redraw): "Grid 0" with 6 blocks → a 4×4 SM grid; red "3 to 1? / 2 to 1?" (how many blocks per SM?).
- Figure `m3l2_occupancy` (lowyx, redraw): Case (a): 4 SMs, each with one block of 6 threads ("Each SM runs one CUDA block (6 threads per block)"). Case (b): 4 SMs, each with two blocks of 4 threads ("Each SM runs two CUDA block (4 threads per block)").

### M3.3 Host Code
Objectives (L): "Write the host code for vector addition operation"; "Explain the management of global memory".
What it teaches
- Shared memory is visible within a block and global memory to all blocks. Global memory lives in device memory, behind an I/O interface the CPU cannot address directly, so explicit host APIs manage it.
- `cudaMalloc(&d_A, size)` allocates device memory. `cudaMemcpy(dst, src, size, cudaMemcpyHostToDevice | cudaMemcpyDeviceToHost)` transfers. Unified memory, which removes the explicit copies, is previewed for M7.
- Full vector-add program: the kernel (left, executed by GPU threads) and the host code (right, executed by the CPU).
Key terms: host, device, device memory, global memory, `cudaMalloc`, `cudaMemcpy`, copy direction, `cudaFree`, error code (`err = ...`), unified memory.
Sources: L M3L3; CPG §3.2 CUDA Runtime (§3.2.2 Device Memory); K12 §1.3.6 Vector Addition Example.
- Figure `m3l3_managing_global_mem` (lowyx, redraw): "Host (CPU)" box (CPU + Memory) ⇄ "I/O interface" ⇄ "Device (GPU)" box (8 SMs + "Global Memory").
- Figure `m3l3_hostcode` (lowyx, redraw): Host listing (int main … cudaMalloc, cudaMemcpy H2D, launch, cudaMemcpy D2H) with the three memory-management lines boxed.
- Figure `m3l3_vectadd` (lowyx, redraw): Side by side, "Kernel code" (vectorAdd with index and bounds check) and "Host code" (the listing above).

### M3.4 Stencil Operation with CUDA
Objective (L): "Be able to write a stencil code with CUDA shared memory and synchronization".
What it teaches
- Recap: C is the average of its 4 neighbours (E, W, N, S). Each block owns a coloured zone (data decomposition) and each thread computes one element, fully parallel. Each input element is used at least 4 times, so it is a good candidate for caching. Because the reuse pattern is known, use shared memory.
- Three stages per thread: load global → shared; compute the stencil; write back to global. Put `__syncthreads()` between load and compute.
- **Boundaries**: shared memory is per block, but computing a zone-edge element needs neighbours in other zones (e.g. element 1 in the red zone, 3 in the green zone). Each block therefore also loads the boundary (halo) elements into its shared memory. This is like MPI boundary communication, but safe here because the input is read-only.
- Code shown (convolution style, to reduce if-else): `__shared__ float sharedInput[sharedDim][sharedDim]; int sharedX = threadIdx.x + filterSize / 2; int sharedY = threadIdx.y + filterSize / 2;`. The load is `if (x >= 0 && x < width && y >= 0 && y < height) sharedInput[sharedY][sharedX] = input[y * width + x]; else sharedInput[sharedY][sharedX] = 0.0f;`. The compute is `for i,j < filterSize: result += sharedInput[threadIdx.y + i][threadIdx.x + j] * filter[i][j];`.
- More threads than outputs are launched: edge threads only load halo values, and only inner threads compute. Out-of-image positions are zero-filled.
Key terms: stencil, tile, halo/ghost cells, boundary condition, zero padding, convolution filter, data reuse, shared-memory tiling.
Note for writers: the halo-loading scheme (block size = tile + halo; inner threads compute) is one of two standard designs. PMPP ch7–8 also shows the "tile = block, halo loaded by extra passes" variant. Pick one and keep the code original.
Sources: L M3L4; PMPP ch7 (convolution, constant memory) and ch8 (stencil); BPG §10.2.3.
- Figure `m3l4_stencil` (lowyx, redraw): The 10 × 8 four-colour quadrant grid with C and neighbours 1–4 (as m2l4_stencil2), now one quadrant per CUDA block.
- Figure `m3l4_stencil_boundaries` (lowyx, redraw): The same grid with thick navy lines: an outer frame plus lines just outside cols 5–6 and rows 4–5. This marks the shared-memory tile including its halo, which straddles the quadrant edges where C and 1–4 lie.

---

## M4 GPU Architecture

Module objectives (L, verbatim): "Describe GPU microarchitecture"; "Be able to explain the basic GPU architecture terminologies".
Readings (L): "General-Purpose Graphics Processor Architectures ... Chapter 3" (A18 ch3 "The SIMT Core: Instruction and Register Data Flow", pp. 21–66).
A18 ch3 section headings, from a WorldCat-derived search snippet (WorldCat itself is blocked; verify before citing numbers): 3.1 One-Loop Approximation (3.1.1 SIMT Execution Masking, 3.1.2 SIMT Deadlock and Stackless SIMT Architectures, 3.1.3 Warp Scheduling); 3.2 Two-Loop Approximation; 3.3 Three-Loop Approximation (operand collector; instruction replay: handling structural hazards); 3.4 Research Directions on Branch Divergence.
Also behind this module: K12 §1.4.1 GPU Pipeline (fetch/decode, scheduler and scoreboarding, register read/write with multiple banks and operand buffer/collectors, execution stage, back-to-back operation, special function units) and §1.4.3 GPU Memory Systems; CPG §4.1–4.2; BPG §10.2.

### M4.1 Multi-threaded Architecture
Objectives (L): "Explain the difference between multithreading and context switch"; "Describe resource requirements for GPU multithreading".
What it teaches
- Recap: a GPU has many cores (SMs). Each runs warps/wavefronts by multithreading and has shared memory and hardware caches.
- **Three timing charts on one 4-instruction program.** The code is `I1: R1 = LD [0x400]; I2: R2 = R5 + R6; I3: R3 = R2 + R6; I4: R5 = R1 + R6` on a 5-stage pipeline (Front-end, Decode/Rename, Schedule, Execution, Write-back).
  - *In-order*: I1 misses in the cache, so I2–I4 all stall behind it although only I4 depends on R1.
  - *Out-of-order*: I2 and I3 complete during the miss, and only I4 waits.
  - *Multithreading*: four threads each issue a load, so four misses overlap. Instructions from different threads are always independent, and four memory requests are generated concurrently.
- Benefits: hides stalls from cache misses, branches and long-latency ALU ops. GPUs use multithreading where CPUs use OoO, caches and ILP. "Longer memory latency requires a greater number of threads to hide latency."
- **Front-end extension**: one PC per warp (4 warps = 4 PC registers) and a register set per thread. A GPU "context switch" just changes which PC and register set the pipeline uses.
- **CPU context switch**: the pipeline, PC and registers belong to one thread. Switching T2 → T3 stores T2's state to memory and loads T3's, which is a large overhead.
- **Resource requirements**: the front-end needs one PC per warp ("Later GPUs have other advanced features", e.g. ITS, but assume one PC per warp). Register file = K × number of threads, where K (registers per thread) varies by application. Y (threads per SM) relates to the number of PCs: 5 PCs × 32 = 160 threads. Z (registers) relates to K. The transcript's "Each SM (shared memory)" is a slip for streaming multiprocessor.
- **Revisited occupancy example**: 256 threads / 32 per warp = **8 PCs**. A program of 10 instructions needs 10 × 8 = **80 warp-instruction fetches** per SM.
Key terms: multithreading, fine-grained multithreading, latency hiding, stall, in-order, out-of-order, context switch, PC per warp, per-thread register file, memory-level parallelism.
Sources: L M4L1; CPG §4.2, verbatim: "The execution context (program counters, registers, and so on) for each warp processed by a multiprocessor is maintained on-chip during the entire lifetime of the warp. Therefore, switching from one execution context to another has no cost"; K12 §1.2.1 (CPU vs GPU context switching; "two hyperthreads vs. hundreds of GPU threads"); A18 ch3.
Figures (lowyx; redraw)
- `m4l1_gpu_architecture`: left, a 4×4 grid of "SM" boxes with a full-width purple "Cache" bar between rows 2 and 3, captioned "GPU". One SM is zoomed into a box listing top to bottom: a stack of 3 "PC" boxes, "I-Cache", "Decoder", "Shared Memory", 4 vertical "Stream Processor" boxes (the 4th after "• • •"), "Caches".
- `m4l1_multithreading`: the code above; pipeline Front-end (Memory above) | Decode Rename | Schedule | Execution (Memory below) | Write-back. Left chart "Ideal case": I1–I4 each F D S E W, staggered by one cycle, time running downwards. Right chart "Cache miss (in order processor)": I1 F D S E[M] + long grey "stall" bar + W; I2, I3, I4 show grey stall bars ending in the same column before their remaining stages.
- `m4l1_multithreading_2`: same, right chart "out of [order] processor": I2 and I3 run F D S E W with no stall, and only I4 waits (arrow from the end of I1's stall to I4).
- `m4l1_multithreading_3`: four rows T1–T4 (green, orange, light blue, magenta), each F D S E[M] + stall + W, each starting one cycle later, so the stalls overlap. Caption "Multi threading".
- `m4l1_fe_extension`: SM diagram with the PC stack linked to a table W-#1 0x8000, W-#2 0x8004, W-#3 0x9000, W-#4 0x8010. Bullets: "Multiple PC registers for Warps (one PC for each warp)"; "One static instruction for one warp (SPMD programming model)"; "Individual registers for each thread – Minimizes context switch overhead – Significant resource". Register table with columns W-1(T1..T3) … W-4(T1..T3) and rows R1–R4.
- `m4l1_cpu_context`, `m4l1_cpu_context_1`, `m4l1_cpu_context_2` (3-frame animation): CPU core (PC, I-Cache, Decoder, Scheduler, 4 ALUs, Caches), a register table (PC, R1–R4) and a memory column holding T1 (yellow), T2 (green), T3 (blue), T4 (grey). Frame 1: core and registers green (T2 loaded). Frame 2: cleared, and the T3 block moves from memory into the registers. Frame 3: core and registers blue (T3 loaded).

### M4.2 Bank Conflicts
Objectives (L): "Explain SIMT behavior of register file accesses and shared memory accesses"; "Describe techniques to enhance bandwidth in register and shared memory accesses".
What it teaches
- Register bandwidth need: per instruction 2 reads + 1 write. With execution width 8 that is 8 × 3 = **24 values** at once.
- **Port vs bank.** A port is a hardware access interface, and wires cost area. A *no-bank* file for width 4 needs **8 read + 4 write ports on every register entry**. A *4-bank* file gives each bank 2 read + 1 write ports. Banks can be accessed simultaneously, so fewer ports are needed.
- **Bank conflict** (4-bank toy):
  - Scenario 1, read R1 of T1–T4: each thread's registers are in a different bank, so all 4 are read in one cycle, as with the no-bank version.
  - Scenario 2, read R1–R4 of T1: all are in one bank with 2 read ports, so it takes 2 cycles.
- **Variable registers per thread** creates conflicts even for "same register, different threads":
  - Case 1 (4 registers per thread, one thread per bank): `R3 = R1 + R2` reads conflict-free.
  - Case 2 (2 registers per thread, two threads share a bank): T1 and T2 in one bank, T3 and T4 in another, so reading R1 and R2 of all threads conflicts.
  - Because a warp reads the same register for every thread, the thread-to-bank layout matters.
- **Solution 1: compile-time optimisation.** Register IDs are static, so the compiler can lay out and order instructions to avoid conflicts, though not all of them.
  - Side bar, static vs dynamic: "static often means before running code ... not dependent on input"; dynamic depends on input. `LOOP: ADD R1 R1 #1; BREQ R1, 10, LOOP` has 2 static instructions and 2 × 10 = **20 dynamic instructions**. Static analysis = compile-time analysis.
- **Real pipeline**: register read may take several cycles (bank conflict, or a single read port), so values go into a **buffer / operand collector**, and a **scoreboard** then selects instructions. Pipeline: Front-end | Decode/RF read | Buffer and operand collector | Schedule | Execution | Write-back.
- **Scoreboarding** on GPUs: a CPU uses it for OoO dynamic scheduling. A GPU uses it to check that all source operands of a warp are ready, then chooses among ready warps (oldest-first or other policies).
- Scoreboard example (animation): per lane, a table of warps with Src1 (value v, ready r) and Src2 (v, r). Values arrive over cycles in the order w1.Src1, w2.Src2, w3.Src1, w1.Src2. When w1 has both, it is selected and its operands go to the 4 ALUs together.
- **Shared-memory bank conflicts**: shared memory is banked for bandwidth. With 4 banks (addresses 0,4,8,12 in bank 1; 1,5,9,13 in bank 2; …), `sharedInput[threadIdx.x * 4]` puts T1 → 4, T2 → 8, T3 → 12, all in the same bank, so every thread conflicts. The fix is restructuring software (later lectures).
- **Exact NVIDIA rules for the book** (BPG §10.2.3.1 and CPG CC 5.x, verbatim):
  - "To achieve high memory bandwidth for concurrent accesses, shared memory is divided into equally sized memory modules (banks) that can be accessed simultaneously. Therefore, any memory load or store of n addresses that spans n distinct memory banks can be serviced simultaneously, yielding an effective bandwidth that is n times as high as the bandwidth of a single bank."
  - "However, if multiple addresses of a memory request map to the same memory bank, the accesses are serialized. The hardware splits a memory request that has bank conflicts into as many separate conflict-free requests as necessary, decreasing the effective bandwidth by a factor equal to the number of separate memory requests. The one exception here is when multiple threads in a warp address the same shared memory location, resulting in a broadcast."
  - "On devices of compute capability 5.x or newer, each bank has a bandwidth of 32 bits every clock cycle, and successive 32-bit words are assigned to successive banks. The warp size is 32 threads and the number of banks is also 32, so bank conflicts can occur between any threads in the warp."
  - CPG CC 5.x: "A shared memory request for a warp does not generate a bank conflict between two threads that access any address within the same 32-bit word ... for read accesses, the word is broadcast to the requesting threads and for write accesses, each address is written by only one of the threads (which thread performs the write is undefined)."
  - Derived rule (state as derived): bank(addr) = (addr / 4) mod 32. For 32-bit elements at word stride s, the conflict degree is gcd(s, 32): s odd gives conflict-free, s = 2 gives 2-way, s = 4 gives 4-way, s = 32 gives 32-way.
  - Padding fix (BPG §10.2.3.3): with a w × w tile and w = 32, column access has stride w (every thread hits one bank). Padding to `[w][w+1]` gives stride w + 1 = 33, "which, due to modulo arithmetic used to compute bank indices, is equivalent to a unit stride."
Key terms: register file bandwidth, read/write port, bank, banked register file, register bank conflict, shared-memory bank conflict, broadcast, multicast, static vs dynamic, compile-time register allocation, operand collector, operand buffer, scoreboard, ready bit, oldest-first.
**[SIMPLIFIED]** The 4-bank toy turns `threadIdx.x*4` into a full conflict. With 32 banks it is 4-way (8 banks used). K12 §1.4.1 gives the bandwidth arithmetic: "If a GPU has 1 Tflop/s peak performance and each FP operation needs at least two register reads and one register write, 2 T*32 B/s=64 TB/s register read bandwidth is required". It also cites Gebhart's design where "four SIMT lanes form a cluster. Each entry in the streaming multiprocessor's main register file is 128 bits wide". Operand collectors also act as result queues.
Numbers: 32 banks × 4 B (CC ≥ 5.0); registers 64 K/SM; Harris blog: shared memory "latency is roughly 100x lower than uncached global memory latency"; K12 Table 1.4: shared 4–32 cycles vs global 100s of cycles (Tesla/Fermi era).
Sources: L M4L2; BPG §10.2.3; CPG CC 5.x Shared Memory; K12 §1.4.1 "Register read/write"; A18 ch3 §3.3 (operand collector; number unverified); harris2013sharedmem.
Figures (lowyx; redraw)
- `m4l2_warp`: two blocks (yellow, green) of threads; an "SM"; two rows of 16 "T" boxes grouped by braces into warps of 8; a row of 8 "SP" boxes; a register table Th1–Th8 × R1–R4.
- `m4l2_port_vs_bank`: rows T1-R1…T1-R4, T2-R1…T2-R4, crossed by 8 blue "R" and 4 orange "W" lines. Text "8 read ports and 4 write ports per each register element / No bank version".
- `m4l2_port_vs_bank_1`: a 4 × 4 grid, column k = Tk-R1…R4, each column crossed by its own "R R W". Text "2 read ports and 1 write port per each register element / 4 bank version".
- `m4l2_bank_conflict`, `m4l2_bank_conflict2`, `m4l2_bank_conflict3` (3 frames): the unbanked and 4-bank files side by side with "BUS" arrows. Text "Bank Conflict!! Can't read 8 values from any locations!! Only two values from each bank!" Frame 2 highlights R1 of Th1–Th4: on the left each on a different read line, on the right one row across 4 banks. Frame 3 highlights Th1-R1 and Th1-R2 in one bank.
- `m4l2_variable`: Case 1 has 4 coloured columns Th1..Th4, each R1–R4 (colour = bank). Case 2 packs two threads per column (Th1+Th2, Th3+Th4, …), each with R1–R2. The slide's third column is mislabelled (Th5, R1, R1, R2, …, no Th6). Caption "Different colors different banks".
- `m4l2_solution`: pipeline Front-end | Decode RF read | Buffer and operand collector | Schedule | Execution | Write-back.
- `m4l2_scoreboarding`, `m4l2_scoreboarding2`, `m4l2_scoreboard3`, `m4l2_scoreboard4`, `m4l2_scoreboard5`, `m4l2_scoreboard_ready`, `m4l2_scoreboard_ready_execution` (7 frames): 4 lane tables (w1–w5 × Src1 v r | Src2 v r), each feeding a trapezoid ALU. Successive frames mark w1.Src1 value (blue V) then ready (check); w2.Src2; w3.Src1; w1.Src2. w1 is then boxed in yellow as ready ("Scoreboarding"), and finally the ALUs hold w1's two operands.
- `m4l2_shared_mem`: 4 bank columns; Bank 1 = 0, 4, 8, 12; Bank 2 = 1, 5, 9, 13; Bank 3 = 2, 6, 10, 14; Bank 4 = 3, 7, 11, 15.

### M4.3 GPU Architecture Pipeline
Objectives (L): "Describe GPU pipeline behavior [w]ith multithreading and register file access"; "Explain how mask bits are used."
What it teaches. A complete worked example; reproduce it with redrawn tables.
- Pipeline: Front-end (I-cache) | Decode | RF | schedule | Execution (Memory, Shared Memory) | Write-back.
- Setup: 2 blocks × 8 threads, warp size 4, so 4 warps.

  | Warp | PC |
  |---|---|
  | #1 (b:1, T1–T4) | 0x8000 |
  | #2 (b:1, T5–T8) | 0x8004 |
  | #3 (b:2, T1–T4) | 0x8000 |
  | #4 (b:2, T5–T8) | 0x800A |

- Block 1 registers (Th1..Th4): R1 = 11 12 13 14; R2 = 2 2 2 2; R3 = 3 4 13 15; R4 = 23 24 32 33.
- I-cache: 0x8000 `add r1, r1, 1`; 0x8004 `sub r2, r2, 1` (slide typo "r,2,1"); 0x8008 `mov r1, tid.x`; 0x800A `mov r2, ctaid.x`; 0x8010 `ld.shared r1 [A]`.
- Special registers: `tid.x` is the thread ID within a block; `ctaid.x` is the block ID within a grid.
- Step 1 (warp 1): fetch one instruction for the whole warp (`add r1, r1, 1`). Decode broadcasts the immediate 1 into every lane's Src2 (ready). RF read fills Src1 with 11, 12, 13, 14, so all operands are ready. The scoreboard selects W1, execute, and write-back: R1 becomes 12, 13, 14, 15.
- Step 2 (warp 2 = block 1, T5–T8): `sub r2, r2, 1`. The immediate 1 is broadcast; R2 of T5–T8 = 2, 2, 2, 2 is read; 2 − 1 gives write-back R2 = 1, 1, 1, 1. "The hardware performs the same work for all thread in a warp". On the slide one lane is omitted for space.
- Step 3 (warp 4 = block 2, T5–T8 at 0x800A): `mov r2, ctaid.x`. The block ID is 2, so R2 = 2 for all four threads of block 2.
- Step 4 (variant: warp 4 at 0x8008): `mov r1, tid.x`. Thread IDs 5, 6, 7, 8 are written to R1.
- **Mask bits**: "What if we do not need to execute all 4 threads?" One ALU path is a **lane**. Per-warp active masks are w1 1111, w2 1110, w3 0111, w4 1111, w5 1111. With 1110 only the first three lanes compute; the inactive lane does no work and is not written back.
Key terms: warp PC table, instruction fetch per warp, immediate broadcast, operand buffer, scoreboard selection, special registers `%tid` and `%ctaid`, lane, active mask, mask bits, write-back.
Sources: L M4L3; K12 §1.4.1 (fetch/decode with round-robin or greedy-fetch; "The GPU processor has an in-order scheduler ... the scheduler can select any warps that are ready ... a program might look like an out-of-order execution"; scoreboarding checks RAW/WAW); PTX ISA special registers %tid, %ntid, %ctaid; A18 ch3.
Numbers: K12 §1.4.1: G80 has 8 lanes, so a warp takes 4 cycles; 2–4 SFUs per SM; no data forwarding because a result is 32 × 32 B = 1 KB wide; back-to-back dependent instructions rely on TLP to hide latency (Volkov GTC'10).
Figures (lowyx; redraw)
- `m4l3_gpu_pipeline`: the stage strip above.
- `m4l3_pc_values`, `m4l3_register_values`, `m4l3_i_cache`: the three tables above (verbatim values).
- `m4l3_scoreboard` (empty 4-lane tables W1–W4 × Src1/Src2) → `m4l3_scoreboard1` (decode shows `add r1, r1, 1`, arrows to 4 lanes, W1.Src2 = 1 ✓) → `m4l3_scoreboard2` (W1.Src1 = 11, 12, 13, 14 ✓, row boxed magenta) → `m4l3_scoreboard3` (register R1 now green 12, 13, 14, 15).
- `m4l3_scoreboard4`, `m4l3_scoreboard5`, `m4l3_scoreboard6`: "One lane is not shown"; an 8-thread register table (R1 = 12–15 for Th1–4 and 16–19 for Th5–8; R2 = 2 2 2 2 for Th5–8; R3 = 3 4 13 15 23 32 37 23; R4 = 23 24 32 33 11 7 8 5); W2 gets Src2 = 1 then Src1 = 2; R2 of Th5–8 becomes 1. The slide shows R2 of Th1–4 as 3, inconsistent with the earlier 2, so correct it when redrawing. Blue footnote text defines tid.x and ctaid.x.
- `m4l3_scoreboard7`: "Block 2 register file"; W4.Src1 = 2; R2 of Th5–8 = 2.
- `m4l3_scoreboard8`: the warp #4 PC is changed to **0x8008** (red); W4.Src1 = 5–8; R1 of Th5–8 = 5, 6, 7, 8.
- `m4l3_scoreboard9` "Mask Bits": the mask table above; 4 lane tables labelled thread 1–4 (one boxed "Lane"); w2's 4th lane is left unready. The slide marks w3 lane 1 ready despite mask 0111, so fix this when redrawing.

### M4.4 Global Memory Coalescing
Objectives (L): "Explore global memory accesses"; "Explain Memory address coalescing"; "Describe how one warp can generate multiple memory requests".
What it teaches
- One memory instruction can generate up to 32 requests (warp size 32). **Worked bandwidth number**: 32 SMs × 1 warp × 32 requests = 1024 requests per cycle. At 64 B each that is 64 KB per cycle, so at 1 GHz it needs **64 TB/s**.
- **SRAM vs DRAM vs HBM**: SRAM is a 6-transistor cell used in caches. DRAM is a one-transistor cell (1T1C) giving high capacity, but all communication goes through pins, which limits it. HBM stacks DRAM (density) and connects it to the GPU through a silicon interposer inside the same package, avoiding off-package links and giving very high bandwidth.
- **Coalescing**: GPU caches are small, so bandwidth saturates easily.
  - First load `ld.global.u32 %r3, [%r1]` with R1 = 0, 4, 8, 12, 16, 20, 24, 28 (consecutive 4-byte words) combines into **one** request "Mem[0-63]": *coalesced*.
  - Second load with R2 = 0, 128, 256, … (128 B apart) needs one 64-byte request per thread (8 requests): *uncoalesced*.
- "Coalesced memory combines multiple memory requests into a single or more efficient memory request ... one of the key software optimization techniques." Uncoalesced accesses degrade performance significantly.
- **Exact rules for the book**:
  - BPG §10.2.1, verbatim: "For devices of compute capability 6.0 or higher, the requirements can be summarized quite easily: the concurrent accesses of the threads of a warp will coalesce into a number of transactions equal to the number of 32-byte transactions necessary to service all of the threads of the warp."
  - CPG §5.3.2: "Global memory resides in device memory and device memory is accessed via 32-, 64-, or 128-byte memory transactions. These memory transactions must be naturally aligned". Also "if a 32-byte memory transaction is generated for each thread's 4-byte access, throughput is divided by 8."
- **Book worked examples** (derived from the rule): 32 threads × 4 B consecutive and 128-B aligned = 4 sectors (1 line). Same but offset by 4 B = 5 sectors. Stride 2 words = 8 sectors (50 % efficiency). Stride ≥ 8 words (32 B) = 32 sectors (12.5 % efficiency for 4-B loads). See BPG §10.2.1.1–10.2.1.4 (simple, sequential-misaligned, effects of misalignment, strided).
Key terms: global memory, memory request, memory transaction, coalesced/uncoalesced access, sector (32 B), cache line (128 B), alignment, stride, memory bandwidth, SRAM, DRAM, HBM, 3D-stacked DRAM, silicon interposer, memory channel.
**[SIMPLIFIED]** (a) The lecture's request size is 64 B ("DRAM memory requests size is 64 ~ 128B"). Since CC 6.0, transactions are counted in 32-B sectors (BPG). (b) The slide's R1 addresses read 0 4 8 12 16 18 20 24 (typo; should be consecutive words), so correct it in the redraw. (c) In the uncoalesced slide, R2 jumps 256 → 512 (not uniformly 128); keep it as "scattered" or fix it to a uniform 128-B stride. (d) K12 §1.4.3: early GPUs (before compute capability 1.2) had strict coalescing rules, and coalesced accesses produced "one to four memory transactions".
Numbers: HBM bandwidth P100 720 GB/s, V100 900 GB/s (BPG derives 898 GB/s = 0.877 GHz × 2 × 4096 bit / 8), A100 40 GB 1555 GB/s, H100 SXM5 3000 GB/s (HWP V1.02, preliminary). Memory interfaces are 4096-bit HBM2 (P100, V100) and 5120-bit HBM2/HBM3 (A100, H100). K12 §1.4.3: older GPUs used GDDR with an FR-FCFS DRAM scheduler.
Sources: L M4L4; BPG §9.2.1, §10.2.1; CPG §5.3.2; K12 §1.4.3; A18 ch4; PMPP ch6.
Figures (lowyx; redraw)
- `m4l4_dram`: the 16-SM grid with Cache, an orange "Channel", and a green "DRAM" box.
- `m4l4_sram`: three panels. "DRAM": a 1-bit DRAM cell (bit line, word line, 1 transistor + capacitor), a DRAM chip array, a DRAM chip package with 4 chips. "GPU with HBM": a package containing a silicon interposer holding the GPU and a "3D-stack DRAM" stack, linked by a double arrow. "SRAM": a 1-bit SRAM cell (cross-coupled inverters + 2 access transistors, word line, bit lines) and a 4×4 SRAM array.
- `m4l4_coalesce`: code `ld.global.u32 %r3, [%r1];` / `ld.global.u32 %r3, [%r2];`. Register table Th1–Th8: R1 = 0 4 8 12 16 18 20 24 (sic), R2 = 0 128 256 512 768 1024 1152 1280. Arrow from R1 to one box "Mem [0-63]". Bullets: "DRAM memory requests size is 64 ~ 128B"; "All memory requests from the first load can be combined into one memory request ... called coalesced".
- `m4l4_coalesce2`: R2 highlighted, 8 boxes "Mem [0+64]", "Mem [128+64]" … "Mem [1280+64]"; "Second load cannot be easily combined → uncoalesced".

---

## M5 Advanced GPU Programming

Module objectives (L): verbatim copies of M4's ("Describe GPU microarchitecture"; "Be able to explain the basic GPU architecture terminologies"), a copy error. The lesson objectives are the real ones.
Readings (L, verbatim):
- Required: "General-Purpose Graphics Processor Architectures ... Chapter 3"; "CUDA best practices (sections 9, 10, 11)"; "Shared memory" (NVIDIA blog, harris2013sharedmem); "For Project #2 preparation" GPU Gems 2 ch. 46 "Improved GPU Sorting" (kipfer2005gpusort).
- Optional: "Nvisight" (YouTube video); "NSight doc" (Nsight Systems User Guide); "NVIDIA presentation" (GTC 1083_Wang.pdf); "CUDA stream" (CUDA 7 streams blog); "Data transfer" (How to Optimize Data Transfers blog); "NSight Compute Video Series"; "NSight Blog" (Using Nsight Compute to Inspect your Kernels).
Book sections: BPG §9 Performance Metrics (§9.1 Timing, §9.2 Bandwidth: §9.2.1 Theoretical, §9.2.2 Effective, §9.2.3 Throughput Reported by Visual Profiler); §10 Memory Optimizations (§10.1 Data Transfer Between Host and Device: §10.1.1 Pinned Memory, §10.1.2 Asynchronous and Overlapping Transfers with Computation, §10.1.3 Zero Copy, §10.1.4 Unified Virtual Addressing; §10.2 Device Memory Spaces: §10.2.1 Coalesced Access, §10.2.2 L2 Cache, §10.2.3 Shared Memory, §10.2.4 Local, §10.2.5 Texture, §10.2.6 Constant, §10.2.7 Registers; §10.3 Allocation; §10.4 NUMA); §11 Execution Configuration Optimizations (§11.1 Occupancy, §11.2 Hiding Register Dependencies, §11.3 Thread and Block Heuristics, §11.4 Effects of Shared Memory, §11.5 Concurrent Kernel Execution, §11.6 Multiple contexts). Also BPG §12 Instruction Optimization and §13 Control Flow (not assigned but cited by the lecture's "reduce computation" list). K12 ch3 (FMM case study: baseline, optimisation goal, candidate optimisations, exploring the optimisation space) and ch4 (§4.1 Instruction-level Analysis and Tuning). PMPP ch6 (performance considerations, optimisation checklist), ch22.

### M5.1 Advanced GPU Programming (the module's only lesson; eizyc: "Overview")
Objectives (L): "Describe GPU optimization techniques"; "Prepare for advanced technique materials".
What it teaches
- **What suits GPUs**: massive data parallelism; host–device communication that is a small share of the cost; coalesced global accesses.
- **Profiling**: find the hotspots. The metrics named are throughput, number of divergent branches, coalesced vs uncoalesced memory accesses ("divergent memory"), occupancy and bandwidth utilisation. Use the vendor profilers (Nsight Systems for the timeline, Nsight Compute for kernels), and profile the CPU code first to choose what to port.
- **Execution time = data transfer + memory access + compute**, so attack all three, and prefer the provided libraries.
- **Data-transfer optimisations** (one CPU ⇄ I/O interface ⇄ GPU figure, then timelines):
  1. Fast transfer: pinned (page-locked) memory shrinks the copy boxes.
  2. Overlap compute and transfer with `cudaMemcpyAsync`.
  3. Pipeline transfer and compute ("concurrent copy and execute") with streams: split the data and kernel into chunks so copy k+1 overlaps kernel k.
  4. Direct host access:
     - **Zero copy** reads CPU data directly in an integrated CPU–GPU memory.
     - **UVA**: the driver and runtime hide the physically separate spaces. "Ideally no data copy cost but the implementation still requires data copy and the overhead exists."
  Not every method fits every system; try them.
- **Memory-access optimisations**: use the caches; coalesce and align global accesses; reduce the number of transactions; compare achieved bandwidth with peak; avoid shared-memory bank conflicts.
- **Reduce computation**:
  - Cheaper instructions (shift instead of multiply/divide by 2^k).
  - Lower precision (32-, 16- or 8-bit) where allowed.
  - Hardware special functions (e.g. `rsqrtf()`), which math libraries use automatically.
  - Fewer branches (predication).
  - Avoid atomics: much cheaper than before, but still best avoided.
  - Use tensor cores; libraries do so when possible.
- **Newer CUDA features**:
  - Warp-level operations (shuffle, vote, ballot). Thread-to-thread communication is otherwise costly: registers are private, so data must round-trip through shared memory, with possible bank conflicts. Figure: TH-1..TH-8 swap R1 pairwise (1↔2, 3↔4, …), i.e. an XOR-1 shuffle.
  - Cooperative groups (other warp formations).
  - Volta's Independent Thread Scheduling, which makes GPUs depart from strict SIMT.
  - Shared memory shared by multiple blocks (clusters / distributed shared memory) when they run on the same SM or cluster.
  - Unified L1 / shared / texture storage.
  - Hardware split arrive/wait barriers.
- **Libraries**: cuBLAS (linear algebra), cuSPARSE, cuTENSOR, Thrust (parallel algorithms), NCCL and NVSHMEM (multi-GPU communication), cuDNN (DL).
- **Other platforms**: OpenCL, oneAPI/SYCL, OpenACC, HIP, Kokkos, Python, Julia.
- Summary (L): reduce computation, reduce host–device transfer overhead, keep global and shared accesses efficient.
Formulas and exact definitions for the book
- BPG §9.2.1, theoretical bandwidth: "the NVIDIA Tesla V100 uses HBM2 (double data rate) RAM with a memory clock rate of 877 MHz and a 4096-bit-wide memory interface ... the peak theoretical memory bandwidth of the NVIDIA Tesla V100 is 898 GB/s", i.e. 0.877 × 10^9 × (4096/8) × 2 / 10^9.
- BPG §9.2.2: Effective bandwidth = ((B_r + B_w) / 10^9) / time.
- BPG §11.1 occupancy definition (quoted in M3.2). BPG §11.2: hiding register dependencies needs enough active threads per SM.
- BPG §10.1.1: pinned memory gives the highest host–device bandwidth, but over-allocating it degrades system performance (check the exact wording before quoting).
- BPG §13.1 / CPG §5.4.2, verbatim: "To obtain best performance in cases where the control flow depends on the thread ID, the controlling condition should be written so as to minimize the number of divergent warps ... A trivial example is when the controlling condition only depends on (`threadIdx / warpSize`) ... no warp diverges".
Key terms: profiling, hotspot, Nsight Systems, Nsight Compute, pinned (page-locked) memory, `cudaMemcpyAsync`, stream, concurrent copy and execute, zero copy, UVA, theoretical/effective bandwidth, alignment, strength reduction (at the instruction level), low precision, intrinsic (`rsqrtf`), predication, atomic, tensor core, warp shuffle/vote/ballot, cooperative groups, independent thread scheduling, thread block cluster / distributed shared memory, split arrive/wait barrier, cuBLAS, cuSPARSE, cuTENSOR, Thrust, NCCL, NVSHMEM, cuDNN, OpenCL, SYCL, HIP, Kokkos.
**[SIMPLIFIED]**
- (a) ITS: CPG §4.1, verbatim: "Starting with the NVIDIA Volta architecture, Independent Thread Scheduling allows full concurrency between threads, regardless of warp. With Independent Thread Scheduling, the GPU maintains execution state per thread, including a program counter and call stack ... threads can now diverge and reconverge at sub-warp granularity." The warp size is still 32. The lecture's "smaller warp-level operations instead of fixed warp sizes" is loose.
- (b) "Shared memory shared by multiple blocks" means Hopper thread block clusters with distributed shared memory (HWP "Thread Block Clusters", "Distributed Shared Memory"; up to 16 blocks per cluster, non-portable).
- (c) Split arrive/wait barriers are `cuda::barrier` / the asynchronous barrier (CPG §7.26), with hardware acceleration from Ampere.
**Exclusion note (Project 2):** GPU Gems 2 ch46 (Kipfer & Westermann: odd-even transition sort, odd-even merge sort, bitonic merge sort on the GPU) is "Project #2 preparation". The book may explain sorting networks and the bitonic merge network conceptually (comparators, O(n log² n) comparisons, log n (log n + 1)/2 stages). It must contain no optimised CUDA sort, no speed-up targets and no tuning walk-through. The lecture's optimisation checklist itself is fine as general guidance.
Numbers: PCIe: K12 §1.2 (2012) Gen 2 "4 Gbit/s" and Gen 3 "8 Gbit/s" (per lane). NVLink 4 is "7x the bandwidth of PCIe Gen 5" (HWP). Libraries and platforms: as listed.
Sources: L M5L1; BPG §9–13; CPG §5 Performance Guidelines, §7.19–7.22 warp vote/match/reduce/shuffle, §7.26–7.29 asynchronous barrier and copies; K12 ch3–4; PMPP ch6, ch20, ch22; harris2013sharedmem; GPU Gems 2 ch46 (concept level only).
Figures (lowyx; redraw)
- `m5l1_dataopt0`: "CPU" ⇄ "I/O interface" ⇄ "GPU"; timeline [Data copy][Kernel][Data copy].
- `m5l1_dataopt1`: "1. Utilize fast transfer methods – E.g.) Pinned (page-locked) memory"; timeline [C][Kernel][C] with shorter copies.
- `m5l1_dataopt2`: "2. Overlap Computation and Data Transfers – E.g.) cudaMemcpyAsync"; two rows, a long C on top and a Kernel + C row starting under it (overlap).
- `m5l1_dataopt3`: "3. Pipeline Transfer and Computation (Concurrent Copy and Execute) – E.g.) Use stream"; top row C C _ C, bottom row K K staggered into the gaps.
- `m5l1_dataopt4`: text: "4. Direct host memory access – Zero copy: access CPU data directly in the CPU and GPU integrated memory – Unified virtual addressing (UVA): Driver/runtime system hides the physically separated memory spaces and provides an interface as if CPU and GPU can access any memory; Ideally no data copy cost but the implementation still requires data copy and the overhead exists".
- `m5l1_cudafeat`: two rows TH-1 R1 … TH-8 R1 with crossing arrows swapping neighbours (1↔2, 3↔4, 5↔6, 7↔8); colours swap with the values.

---

## M6 GPU Architecture Optimizations - I

Module objectives (L, verbatim): "Describe the performance issues related to divergent branches and the basic mechanisms for handling them."; "Describe the opportunities for GPU register optimization."; "Explain the differences between shared memory and register files."; "Develop the ability to read GPU architecture papers".
Readings (L):
- Required: A18 ch3 ("Chaper 3" [sic]); fung2007dwf (MICRO 2007, pp. 407–420); jeon2015rfv (MICRO 2015, pp. 420–432); gebhart2012unifying (MICRO 2012, pp. 96–106).
- Optional: narasiman2011twolevel (MICRO 2011, pp. 308–317); gebhart2011energy (ISCA 2011, pp. 235–246); gebhart2011compile (MICRO 2011, pp. 465–476).
- Which "Gebhart" is which: the required one is the MICRO 2012 unified local memory paper. "Hierarchical register file" refers to ISCA 2011 (hardware register file cache + two-level scheduler) and MICRO 2011 (compiler-managed ORF/LRF hierarchy).
Book sections: A18 ch3 §3.1.1 SIMT Execution Masking, §3.1.2 SIMT Deadlock and Stackless SIMT Architectures, §3.4 Research Directions on Branch Divergence (heading list from a search snippet; verify); K12 §1.4.2 Handling Branch Instructions (SIMT stack with three fields; DWF, dynamic warp subdivision, large warps, compaction; software remapping), §1.4.1 "Register File Cache"; CPG §4.1 SIMT Architecture; PMPP ch10 (reduction and minimising divergence).

### M6.1 Handling Divergent Branch
Objectives (L): "Explain the definition of divergent warps"; "Apply hardware techniques to handle divergent warps".
What it teaches
- **Divergent branch**: threads of one warp follow different paths (e.g. `if (threadIdx.x < 2) Work-1 else Work-2`). The warp is a **divergent warp**. An **active mask** per basic block records participating lanes: BB1 1111 (If), BB2 1100 (Work-1), BB3 0011 (Work-2), BB4 1111. The paths split after BB1 and meet at BB4, the **reconvergence point**, called the **immediate post-dominator** in compiler terms.
- **If-conversion / predicated execution**: the branch becomes "Set predicate; (p) Work-1; (!p) Work-2". Common in vector processors and used even on CPUs for short bodies. Downside: the instructions of both paths are fetched even when not executed, so use it carefully for large bodies.
- **GPU execution flow** (the lecture builds the SIMT stack in six steps):
  1. After fetching BB1, the next PCs within the warp differ, so the branch is divergent. One PC + one mask cannot say where to go: "?".
  2. Following only the taken path (BB1 → BB2 → BB4) silently skips BB3.
  3. Add an **alternate PC** slot holding BB3 (mask 0011), so BB3 can run later. Execution order BB1, BB2, BB3, BB4.
  4. **Nested branch**: BB2 itself branches (BB4 Work-3 mask 1000, BB5 Work-4 mask 0100, reconverging at BB6). A single slot is overwritten with BB5, losing BB3 ("Overwrite BB #3's information?").
  5. Use a **stack** ("SIMT stack") of (alternate PC + mask, reconvergence point). After BB1 push (BB3 0011, BB6); after BB2 push (BB5 0100, BB6).
  6. Fetch rule: compute the next PC; if it equals the reconvergence PC on top of the stack, **pop** and fetch from the alternate PC with its mask. Trace: BB1 → BB2 → BB4 (next = BB6 = top's reconv, so pop and fetch BB5) → BB5 (next = BB6, pop and fetch BB3) → BB3 → BB6 at full mask 1111.
- **Finding the reconvergence point**: compile time from CFG analysis (IPDOM). The compiler either marks it or inserts explicit stack push/pop instructions. Hardware usually keeps the stack. Compile-time divergence detection is hard, so a compiler may over-claim divergent branches (see M11.4).
- **Large warps**: warp width is a microarchitectural choice. Wider warps fetch once for more lanes (32, 64, 128 …, essentially wide vector machines), but divergence becomes more likely, so the right width depends on the application.
- **Dynamic warp formation (DWF)**: after divergence, lane utilisation drops (half the lanes in the example). Threads from *different* warps at the *same PC* can be regrouped into a new warp at run time. Challenge: keep each thread in its home lane, because register-file banks are laid out per lane, or regrouping creates register bank conflicts.
Key terms: divergent branch, divergent warp, active mask, basic block, reconvergence point, immediate post-dominator (IPDOM), if-conversion, predication, SIMT stack (alternate PC, reconvergence PC, mask), nested divergence, large warp, dynamic warp formation, lane-aware regrouping, SIMD efficiency.
**[SIMPLIFIED] / paper detail**
- K12 §1.4.2 states the stack entry precisely: "Each stack entry has three fields: the PC address of the reconvergence point, active mask bits, and the next PC address." Its example CFG has branch A, paths B and C, and join D.
- fung2007dwf (abstract): "a realistic hardware implementation that dynamically regroups threads into new warps on the fly following the occurrence of diverging branch outcomes improves performance by an average of 20.7% for an estimated area increase of 4.7%". It also shows that reconverging at "the immediate post-dominator ... obtains a speedup of 93.4% over not reconverging".
- narasiman2011twolevel: the large warp microarchitecture (a large warp whose active threads are packed into sub-warps every cycle). Combined with two-level scheduling it gives "19.1% over traditional GPU cores".
- Modern NVIDIA (Volta+) replaces the classic stack with per-thread PCs and a convergence optimiser (CPG §4.1). A18 ch3 also discusses SIMT deadlock with the stack (a spin-lock within a warp) and stackless designs (heading from a search snippet).
- Slide errors to fix when redrawing: the tables in gpuflow2–4 give BB2's mask as 1110, but the CFG says 1100; `m6l1_divb` lacks the Work-2 → BB4 edge.
Sources: L M6L1; fung2007dwf; narasiman2011twolevel; K12 §1.4.2; A18 ch3; CPG §4.1; PMPP ch10.
Figures (lowyx; redraw)
- `m6l1_divb`: CFG BB#1 1111 "If" → BB#2 1100 "Work-1" (purple) / BB#3 0011 "Work-2" (green) → BB#4 1111 "Reconvergence point". Right: 4 rows × 4 lane arrows: yellow ×4; purple, purple, empty, empty; empty, empty, green, green; yellow ×4.
- `m6l1_divb2`: the CFG ⇒ (big arrow) a straight line of "Set predicate", "(p) Work-1", "(!p) Work-2".
- `m6l1_gpuflow1`: "GPU Execution Flow (1)": the CFG; table PC | mask = BB#1 | 1111, then "?"; lane arrows for BB1 (4 yellow), BB2 (2 purple) and BB3 (2 green).
- `m6l1_gpuflow2`: table BB#1 1111, BB#2 1110 [sic], BB#4 1111; the arrows show no green row (BB3 lost).
- `m6l1_gpuflow3`: table PC | mask | Alternate PC = BB#1 1111 BB#3(0011); BB#2 1110 BB#3(0011); BB#3 0011; the arrows now include the green row and the final full row.
- `m6l1_gpuflow4`: nested CFG (BB#2 → BB#4 1000 Work-3 / BB#5 0100 Work-4; all → BB#6 1111). Table BB#1 1111 BB#3(0011); BB#2 1110 BB#5(0100); BB#4 1000 BB#5(0100); BB#5 0100. Bullets "What if nested?", "Overwrite BB #3's information?".
- `m6l1_gpuflow5`: stacks "After BB #1": [BB#3 (0011) | BB#6]; "After BB #2": [BB#5 (0100) | BB#6] above [BB#3 (0011) | BB#6]. "Use a stack (SIMT stack) to keep track of alternative PC and reconvergence Points".
- `m6l1_gpuflow6`: the stack with the top reconv "BB#6" circled. Execution table PC | Next PC | mask: BB#1 BB#2 1111; BB#2 BB#4 1100; BB#4 **BB#6** 1000; BB#5 **BB#6** 0100; BB#3 BB#6 0011; BB#6 – 1111. Bullets "Check Next PC is the same as reconvergence point / If they match, pop the stack. Fetch from BB #5."
- `m6l1_dynamicwarp`: panels Warp 1 and Warp 2, each 4 rows × 4 lanes. Row 2: Warp 1 purple purple _ _, Warp 2 _ _ purple purple (boxed in red: they can merge into one full warp). Row 3 mirrors this with green.

### M6.2 Register Optimizations
Objectives (L): "Explain the challenges of register file sizes and opportunities"; "Discuss various optimization techniques aimed at increasing the size of register files effectively".
What it teaches
- **Challenge**: threads × registers per SM = 64 KB, 128 KB, even 256 KB. Large means slow and power-hungry. "In the GPUs world, the register file read bandwidth should be equal to the execution bandwidth." Remedies borrowed from CPUs: hierarchy (latency) and resource sharing (size).
- **Observation 1, not all threads are active**: execution is asynchronous, so threads finish at different times and finished threads' registers are dead. Divergent paths use different registers.
- **Observation 2, not all registers are live**: `add r1, r2, #1` then `mov r2, #10`, so R2 is dead after the add. On a CPU the gap is a cycle or two. On a GPU the next instruction of the same warp may come "10s of warp instructions later" (add for w1 b1, w2 b2, w3 b3, w4 b1 … then mov for w1 b1). The dead interval is long.
- **Observation 3, short distance between instructions**: `mov r2, #10; add r3, r2, #20`, where R2 is consumed immediately. A scheduler can shorten the distance further. Does the value need to go to the RF at all?
- **Observation 4, most register values are read only once**: `mov r2, #10; add r2, r2, #20`. "Almost 70% of register values are read only once." Why store them in the main RF?
- **Optimisation 1, hierarchical register file**: (a) a register-file cache (L0/L1 RF above the main RF), small and fast; the main RF can be smaller or the same. (b) A partitioned RF with fast and slow segments, the slow, large part possibly built in non-volatile memory for energy.
- **Optimisation 2, register-file virtualisation**: "Virtualization ~= Resource sharing"; "Only name space needs to be maintained". Many architectural names (Th1 R1, Th2 R1, Th3 R1 → physical R1; Th4–Th6 R2 → physical R2) map onto a small physical RF, keeping program semantics with less hardware.
Key terms: register file size, RF bandwidth, active/inactive thread, live/dead register, value lifetime, producer–consumer distance, read-once value, register file cache (RFC), L0/L1 RF, main register file (MRF), partitioned RF, NVM, register virtualisation, name space vs physical register space, under-provisioning.
**[SIMPLIFIED] / paper detail**
- gebhart2011energy, verbatim: "Up to 70% of values are read only once, and only 10% of values are read more than 2 times. HPC workloads show the highest level of register value reuse with 40% of values being read more than once." Also "up to 40% of all dynamic register values are read only once and within 3 instructions of being produced". Results: "a 6-entry per-thread register file cache reduces the number of reads and writes to the main register file by 50% and 59% respectively ... the active thread count can be reduced by a factor of 4 with minimal impact on performance, resulting in a 36% reduction of register file energy."
- gebhart2011compile replaces the hardware RFC with a compiler-managed **operand register file (ORF)** and a 1-entry-per-thread **last result file (LRF)**: "a compiler controlled register file hierarchy can reduce register file energy by up to 54%, compared to a hardware only caching approach that reduces register file energy by 34%". Its baseline: "128KB register file per processor, with 16 processors per chip. The register file ... consumes 15–20% of the processor's dynamic energy".
- jeon2015rfv: the full text was not obtainable (ACM DL blocked automated access). Secondary records describe shrinking the architected register space into a smaller physical space plus a register-throttling mechanism against deadlock, with negligible slowdown after halving the RF. **Do not print numbers until checked against the paper.**
- K12 §1.4.1 notes that RF caches on GPUs are attractive because "Current GPU architectures do not support precise exceptions, so register files do not have to maintain architectural states".
Numbers: 256 KB RF/SM on V100/A100/H100; A100 27,648 KB and H100 SXM5 33,792 KB per GPU (HWP Table 3); registers per FP32 core: 1024 (V100/A100) vs 512 (H100) (HWP Table 4).
Sources: L M6L2; gebhart2011energy; gebhart2011compile; jeon2015rfv (abstract-level); K12 §1.4.1; A18 ch3.
Figures (lowyx; redraw)
- `m6l2_o2`: "Live/Dead register concept: add r1, r2, #1 (#R2 is no longer live); mov r2, #10". A short CPU timeline (add, mov adjacent) vs a long GPU timeline: add(w1,b1) [red X, "R2 (w1,b1) dead"], add(w2,b2), add(w3,b3), add(w4,b1), …, mov(w1,b1) [blue X, "R2 (w1,b1) Live"]. "Next instruction might be executed 10s of warp instruction later".
- `m6l2_o3`: text "Observation #3: Short Distance between Instructions", with `mov r2, #10; add r3, r2, #20` (#R2 is used immediately).
- `m6l2_o4`: text "Observation #4: Most Register Values are Read Only", with `mov r2, #10; add r2, r2, #20`; "Many instructions use register values only once. Questioning the necessity of storing them in a register file."
- `m6l2_opt1`: a pyramid L0 RF / L1 RF / Main Register File. "Option #1: Register file cache" and "Option #2: Partitioned Register file: Slow and Fast register segments; Slow and large RF can be implemented with NVM".
- `m6l2_opt2`: a "Name Space" column (Th1 R1, Th2 R1, Th3 R1, Th4 R2, Th5 R2, Th6 R2) bracketed onto "Actual Register Space" rows R1 | v and R2 | v.

### M6.3 Unified Register File and Shared Memory
Objectives (L): "Explain optimization opportunities for unified memory and register file"; "Differentiate between register files and memory"; "Review the concept of occupancy in GPU programming".
What it teaches
- **Occupancy review**: SM with 64 KB registers and 32 KB shared memory.
  - Kernel 1 uses 64 registers per thread and no shared memory, so shared memory sits idle.
  - Kernel 2 uses 4 registers per thread and 2 KB shared memory per block, so most of the RF sits idle (the transcript estimates "probably two kilobyte" used).
  - Could a single pool raise occupancy for both?
- **Hardware-managed cache vs software-managed cache**: a hardware cache decides contents by LRU or other policies and needs address tags. A software-managed cache (scratchpad) is placed by the programmer, so it needs no tags; data is either there or not by construction.
- **Register file vs scratchpad**: both store data only, have no tags, and the location is the address. They differ in ports: an instruction reads 2 source registers but memory reads 1 address. RF access patterns are known statically (the instruction names the registers), which gives more optimisation room despite higher read bandwidth.
- **Proposed unified structure**: one storage pool shared by registers and shared memory. Occupancy is then limited by RF + smem together. Requirements: high bandwidth, enough read/write ports, and heavier banking because the two access patterns differ. The flexible sharing relaxes resource constraints.
Key terms: hardware-managed cache, software-managed cache, scratchpad, tag, replacement policy (LRU), location-addressed storage, ports, unified local memory, flexible partitioning, occupancy.
**[SIMPLIFIED] / paper detail**
- gebhart2012unifying unifies **three** structures (register file, scratchpad and primary data cache), not two: "unified local memory with flexible partitioning of capacity across the register file, scratchpad (shared memory in NVIDIA terminology), and cache".
- It depends on prior work: "a two-level warp scheduler and a software-controlled register file hierarchy ... reduce accesses to the main register file by 60%". Result: "a performance benefit as high as 71% along with an energy reduction up to 33%", with "4–71%" for benchmarks that benefit.
- Shipping NVIDIA GPUs unify **L1 data cache + shared memory** only, not the RF:
  - Volta: "a unified data cache and shared memory with a total size of 128 KB (Volta) or 96 KB (Turing)".
  - A100: 192 KB (CC 8.0/8.7) and 128 KB (8.6/8.9).
  - H100: 256 KB, with a shared-memory carve-out of "0, 8, 16, 32, 64, 100, 132, 164, 196 or 228 KB" (CPG CC 7.x/8.x/9.0 sections).
Numbers: carve-outs V100 0/8/16/32/64/96 KB; A100 0/8/16/32/64/100/132/164 KB; H100 up to 228 KB. AWP: "192 KB of combined shared memory and L1 data cache, 1.5x larger than V100 SM". HWP: "256 KB of combined shared memory and L1 data cache, 1.33x larger than A100".
Sources: L M6L3; gebhart2012unifying; CPG CC 7.x, 8.x, 9.0 "Shared Memory"; AWP; HWP; A18 ch4 §4.1 (first-level memory structures: scratchpad and L1 data cache, L1 texture cache, unified texture and data cache; headings from a search snippet).
Figures: none on lowyx for this lesson.

---

## M7 GPU Architecture Optimizations - II

Module objective (L): copied from M6 ("Describe the performance issues related to divergent branches ..."), a copy error. The real topics are GPU virtual memory, UVA/unified memory and warp scheduling.
Readings (L):
- Required: power2014x86 (HPCA 2014, pp. 568–578); narasiman2011twolevel; rogers2012ccws (MICRO 2012, pp. 72–83).
- Optional: gebhart2011energy; ganguly2019interplay (ISCA 2019); jog2013owl (ASPLOS 2013); jog2013orchestrated (ISCA 2013); ausavarungnirun2017mosaic (MICRO 2017); li2021tlb (MICRO 2021); kim2020batch (ASPLOS 2020).
Book sections: A18 ch3 §3.1.3 Warp Scheduling; A18 ch4 (memory system: MMU and address-translation research). CPG "Unified Memory Programming" (legacy) / Part 4 (CUDA 13); BPG §10.1.3–10.1.4.

### M7.1 GPU Virtual Memory
Objectives (L): "Explain the concept of GPU virtual memory and its importance in modern GPU architectures"; "Explain challenges of GPU address translation, including scalability and handling uncoalesced memory accesses"; "Explore hardware optimization opportunities for GPU address translations to improve GPU performance and efficiency".
What it teaches
- **Two aspects of VM**: address translation and page allocation. On a CPU the OS allocates pages. On a GPU, initially the CPU with the GPU driver manages pages, through `cudaMalloc`, `cudaMallocManaged` and `cudaMemcpy`.
- **Translation review**: VA → PA. VPN → PFN/PPN while the page offset (PO) is unchanged. Common page sizes are 4 KB and 2 MB.
- **TLB** caches recent translations. A **PTE** stores the VPN → PFN mapping and lives in memory, so walking for it costs memory accesses. A **TLB miss** triggers a page-table access. A **page fault** means no physical page is mapped yet, so the OS must allocate one.
- **4-level translation** (x86, ARM, GPUs). With a single-level table, entries = 2^(#VPN bits), e.g. 2^48 in the lecture's count. With 4 levels, only the touched tables exist: best case 2^(L4 bits) + 2^(L3 bits) + 2^(L2 bits) + 2^(L1 bits), i.e. thousands of entries instead of trillions. The cost is at least four memory accesses per translation, the **page walk**, done by a hardware **page table walker (PTW)** or in software. Walk order: the L4 index selects the L3 table base, then the L3 index, then L2, then L1 entry = PTE (PFN + metadata), and PA = PFN ‖ offset.
- **GPU VM history**: early GPUs had no VM or a 1:1 mapping. Programmability (UVA) demanded real VM. Translation mirrors the CPU except for **address coalescing**: the memory stage = coalescer → TLB, with a PTW or TLB-miss handler behind it. L1 is typically virtually addressed and L2 physically.
- **Coalescing and TLB accesses** (toy page size 256 B):
  - A coalesced load (R1 = 0, 4, 8, …) gives one request, one TLB access, tag 0x00.
  - An uncoalesced load (R2 = 0, 128, 256, 512, 768, 1024, 1152, 1280) gives 8 requests and, after merging the two in page 0, **7 TLB accesses** for one instruction.
  - "The total number of TLB requests from one warp would be the same as the width" in the uncoalesced case.
- **Challenge, scalability**: one warp's miss can produce many TLB misses, so the PTW needs high bandwidth. One option is a high-bandwidth PTW shared across SMs (private PTW per SM vs shared PTW next to the L2 TLB).
- **Cost reducers**:
  - *Segment mapping*: each program's VA 0x0000–0xFFFF maps to a contiguous physical segment (prog 3 at 0x000000–0x00FFFF, prog 2 at 0x010000–0x01FFFF, prog 1 at 0x020000–0x02FFFF), so translation is "add the upper bits".
  - *Large pages*.
  - *Multi-level TLB hierarchies* (L1 TLB per SM, shared L2 TLB).
- **Large pages**: 4 KB vs 2 MB. The 2 MB offset is 21 bits vs 12. "Number of TLB entry requirement is reduced by 2M/4K (512)". Downside: internal fragmentation (needing 1 KB wastes 3 KB with 4 KB pages, but 2 MB − 1 KB with 2 MB pages).
Key terms: virtual memory, address translation, VA/PA, VPN, PFN/PPN, page offset, page size, TLB, TLB hit/miss, PTE, page table, multi-level (radix) page table, page walk, page table walker (PTW), page fault, address coalescing, virtually indexed L1, physically indexed L2, private vs shared PTW, L1/L2 TLB, segment mapping, large page, TLB reach, internal fragmentation.
**[SIMPLIFIED] / paper detail**
- (a) Index-bit arithmetic for the book: x86-64 4-level paging uses a 48-bit VA = four 9-bit indices + a 12-bit offset. Each table has 512 entries × 8 B = 4 KB. A 2 MB page ends the walk one level early and moves 9 bits into the offset. One 2 MB TLB entry covers 512 × 4 KB pages. The lecture's "12 bits" and "51 → 42 bits" are slide-specific; the slide `m7l1_largepages` draws VPN bits 63..12 vs 63..21.
- (b) power2014x86, verbatim abstract fragments: an AMD A10 APU "with 400 lanes, can require up to 400" unique translations per cycle. Workload findings: "(1) the coalescer and scratchpad memory reduce the translation rate by 6.8x on average), (2) TLB misses occur in bursts (60 concurrently on average), and (3) post-coalescer TLBs have high miss rates (29% average)". Design: "per-compute unit TLBs, a shared highly-threaded page table walker, and a shared page walk cache", with overhead "an average of less than 2%" vs an ideal MMU (4 KB pages, x86-64 page tables).
- (c) ausavarungnirun2017mosaic (multiple page sizes): components are CoCoA (Contiguity-Conserving Allocation), the In-Place Coalescer and CAC (Contiguity-Aware Compaction). Result: "Mosaic improves the performance of homogeneous and heterogeneous multi-application workloads by 55.5% and 29.7% on average, respectively, coming within 6.8% and 15.4% of the performance of an ideal TLB where all TLB requests are hits".
- (d) li2021tlb (multi-GPU): "least-TLB" = a least-inclusive TLB, address-translation sharing with peer GPUs, and IOMMU TLB spilling; "improves the performances, on average, by 23.5% and 16.3%" for single-application and multi-application multi-GPU workloads.
- (e) Slide errors: Th6 R1 = 18 breaks the stride; 1152 = 0x480 belongs to page 0x04, not 0x05; the 0x053F/0x05 row belongs to 1280.
Sources: L M7L1; power2014x86; ausavarungnirun2017mosaic; li2021tlb; A18 ch4.
Figures (lowyx; redraw)
- `m7l1_translation`: "Page size: 4KB, 2MB"; Virtual Address → "Address Translations" → Physical Address; field diagram MSB [VPN | PO] → LSB, translated to [PFN | PO] with PO aligned.
- `m7l1_fourleveltlb`: VA fields Level-4 Index | Level-3 Index | Level-2 Index | Level-1 Index | Page Offset. Four tables L4 → L3 → L2 → L1 stepped down, each index selecting a row whose content points to the next table base; the L1 row is "PFN"; PFN + Page Offset → "PA". Bullets: "1 level of table → 2^(# vpn bits)"; "4 level of tables: the best case: 2^(# level-4 index bits) + 2^(# level-3 index bits) + 2^(# level-2 index bits) + 2^(# level-1 index bits)".
- `m7l1_gpu_vm`: pipeline Front-end (I-cache) | Decode | RF | schedule | Execution Add. Gen | Memory | Write-back. The Memory stage is expanded into "Address Coalescing" → "D-cache" over "TLB" → "PTW" over "TLB Miss handler" → "L2 cache".
- `m7l1_memcoalsece`: "Uncoalesced memory requests can also generate many TLB misses. Assume page size is 256B." Table R1 = 0 4 8 12 16 18 20 24; R2 = 0 128 256 512 768 1024 1152 1280. R1 → Mem[0-63] → TLB access 0x003F → tag 0x00. R2 → Mem[0-63] (0x003F, 0x00), Mem[128+64] (0x00BF, 0x00), Mem[256+64] (0x013F, 0x01), Mem[512+64] (0x023F, 0x02), Mem[768+64] (0x033F, 0x03), Mem[1024+64] (0x043F, 0x04), Mem[1152+64] (0x053F, 0x05 [sic]). "One memory instruction generated 7 TLB accesses."
- `m7l1_challenges`: "Private PTW": each SM has PTW + L1 TLB, with a shared L2 TLB and Memory below. "Shared PTW": SMs have only an L1 TLB; the L2 TLB has a PTW beside it.
- `m7l1_solutions`: physical-address column with three 64 KB segments (orange 0x000000–0x00FFFF Prog #3, blue 0x010000–0x01FFFF Prog #2, green 0x020000–0x02FFFF Prog #1, each VA 0x0000–0xFFFF). Bullets "Segment mapping; Large page sizes; Multiple level hierarchy of TLBs". Shared-PTW TLB diagram.
- `m7l1_largepages`: 4 KB page: VPN bits 63..12, PO 11..0. 2 MB page: VPN 63..21, PO 20..0. "Number of TLB entry requirement is reduced by 2M/4K (512)"; "Downside: memory fragmentation (e.g., 1KB is needed; 4KB paging (4KB-1KB)= 3KB is wasted vs. 2M-1KB is wasted)".

### M7.2 GPU Virtual Memory - UVA
Objectives (L): "Explain Unified Virtual Address Space (UVA)"; "Explore challenges associated with on-demand page allocations".
What it teaches
- **Copy-then-execute model** (early GPUs): `cudaMalloc` + `cudaMemcpy` before the kernel; explicit transfer in pre-kernel preparation.
  - Pro: efficient bulk PCIe transfers that the programmer can optimise.
  - Con: manual page and data management.
- **UVA**: CPU and GPU share one address space, called SVM (shared virtual memory) in OpenCL/CUDA. It improves programmability but requires **dynamic page allocation**.
  - Separate spaces: a CPU buffer and a GPU buffer, with explicit copies.
  - UVA: one logical buffer that both read and write.
- **Page-fault path on a discrete GPU** (`cudaMallocManaged`, on-demand memory management):
  1. The GPU faults (page-fault MSHR in the GPU).
  2. The request goes over PCIe to the CPU.
  3. The CPU OS and GPU driver handle it.
  4. The new mapping is sent back.
  Latency: "tens of milliseconds" in one place and "several tens of microseconds" in another (see the flag).
- **IOMMU background**: lets I/O devices do DMA with virtual addresses (I/O virtualisation). CPU and GPU each have one. GPU memory was once managed only through the IOMMU as a peripheral; with UVA the CPU is also involved.
- **Challenges of on-demand memory**: page management is done by the host. Retrieving the mapping from the CPU's IOMMU costs PCIe communication plus the CPU interrupt service routine, "often taking several tens of microseconds".
- **Reducing on-demand overhead**:
  - Prefetch pages (predict future addresses).
  - Move page-mapping management to the GPU side.
  - CPU–GPU cooperation (the CPU manages large chunks, the GPU manages small pages inside them).
- **Memory prefetching background**: addresses 0x01, 0x02, 0x03 → prefetch 0x04, 0x05. Vector add `a[idx]`, `b[idx]` is sequential, so it prefetches well.
- **Page prefetching**: sequential page prediction (toy page size 512 B). But GPU thread blocks do not execute in order (colours = blocks touching different pages), so simple sequential page prefetch breaks.
- **Tree-based neighbourhood prefetching** (NVIDIA): a 2 MB chunk is split into two 1 MB halves and then into 64 KB nodes. A 4 KB fault in a node fetches the whole 64 KB node (16 pages). If several nodes fault, it promotes to the parent (up to 1 MB). This captures spatial locality but bounds the prefetch size.
- **Oversubscription**: more virtual memory allocated than GPU physical memory, so pages must be evicted. Which ones? Prefetching interacts with eviction, and the problem grows with kernel memory demand.
Key terms: copy-then-execute, explicit data transfer, UVA, SVM, unified memory, `cudaMallocManaged`, on-demand paging, far fault, page-fault MSHR, IOMMU, DMA, I/O virtualisation, interrupt service routine, page prefetching, sequential prefetcher, tree-based neighbourhood prefetcher (TBNp), 64 KB basic block, oversubscription, eviction, pre-eviction.
**[SIMPLIFIED] / paper detail**
- (a) Fault latency: the slide `m7l2_challenge_ondemand` says "several tens of microseconds". kim2020batch, verbatim: "Prior work reports that page fault handling latency ranges from 20µs to 50µs. We find that these numbers are conservative". It measured batch processing time "in the range of 223µs to 553µs with a median of 313µs, of which, GPU runtime fault handling accounts for an average of 46.69%". Use microseconds, not the transcript's "milliseconds".
- (b) The precise TBNp rule (ganguly2019interplay, measured on a GTX 1080 Ti): each `cudaMallocManaged` allocation is split into 64 KB basic blocks forming a full binary tree up to 2 MB. On a far fault, the GMMU validates the 64 KB block (a 4 KB fault group plus a 60 KB prefetch group) and recomputes the valid size of its ancestors. "If GMMU discovers the to-be valid size of a node is strictly greater than 50% of the maximum memory capacity at this level, it tries to balance the valid sizes between the two children of that node", i.e. it prefetches the rest of the other child. "TBNp is an adaptive scheme where the prefetch size can vary from 64KB to 1MB". The lecture's "fetch the upper node" is this >50 % rule.
- (c) ganguly2019interplay result: tree-based pre-eviction plus the hardware prefetcher gives "an average of 93% and 18.5% performance speed-up compared to LRU based 4KB and 2MB page replacement strategies".
- (d) kim2020batch result: batch-aware runtime + hardware (thread-block context switching to enlarge batches, overlapping eviction with migration) gives "an average speedup of 2x over the state-of-the-art page prefetching ... increases the batch size by 2.27x and reduces the total number of batches by 51% ... average batch processing time is reduced by 27%".
- (e) The page numbers in `m7l2_preteching` are illustrative and inconsistent with 512 B pages; redraw them consistently.
Sources: L M7L2; ganguly2019interplay; kim2020batch; BPG §10.1.4; CPG Unified Memory Programming.
Figures (lowyx; redraw)
- `m7l2_cudahost`: not a lecture slide. It is a Canvas screenshot of a Module 8 erratum ("W_depth 20 also means at least 20 x PC registers is needed"). Use it only to correct M8.3.
- `m7l2_uva`: "CPU and GPU share the same address space. Used in OpenCL/CUDA programming model (SVM: Shared Virtual Memory)." Left, "Separate Memory Space": CPU memory with 2 buffers (CPU write/read), GPU memory with 2 buffers (GPU read/write), "copy" arrows between them. Right, "Unified virtual address": one "Unified Memory Space" with 2 buffers read and written by both CPU and GPU, no copies. Bullets: "UVA Increases programmability but requires dynamic page allocations"; "Separated memory space allows for bulk data transfer, fully utilizing PCI-E bandwidth".
- `m7l2_page_fault_handling`: "cudaMallocManaged API". GPU block (SMs with L1 TLBs; L2 TLB, Page Table, Page-fault MSHR; Memory) ⇄ "PCI-E" ⇄ CPU block ("GPU driver and runtime"); "Page fault!" arrow GPU → CPU.
- `m7l2_challenge_ondemand`: CPU ⇄ PCI-E ⇄ GPU; "Page fault!" (GPU → CPU), "New page information" (CPU → GPU); bullets as quoted above.
- `m7l2_pretech`: prefetch bullets and the vectorAdd shared-memory listing.
- `m7l2_preteching`: an array bar A[0x0]…A[0x900] in three colours (blue, orange, green = three thread blocks) mapped to Page 0…Page 9. "Page address can be easily predictable. GPU thread block execution order is not sequential."
- `m7l2_treebase`: tree with root 2MB, children 1MB, leaves 64KB; two leaves under the left 1MB node marked with "Page fault!". "4KB Page fault! Bring the rest of 64KB pages (16 pages) in the same graph node".

### M7.3 GPU Warp Scheduling
Objectives (L): "Explain the fundamentals of GPU warp scheduling policies"; "Explore the challenges and considerations involved in GPU warp scheduling"; "Explain Round-Robin, GTO and other scheduling policies".
What it teaches
- **Multiple ready warps**: the M4 pipeline assumed one ready warp. When several are ready, the warp scheduler picks one.
- **CPU instruction scheduler**: picks among ready instructions in the scheduling queue. Policies: oldest-first; critical-first (loads first, so memory requests start early; or instructions with many dependants first).
- **GPU warp scheduler**: in-order within a warp, but any ready warp may issue, so the dynamic trace looks out of order. Example trace: Inst1 w1, Inst2 w1, Inst1 w2, Inst2 w2, Inst3 w1, Inst1 w3, Inst1 w4, Inst2 w4, Inst3 w2, Inst2 w3, Inst3 w3, Inst3 w4.
- **RR vs GTO**, on the code `comp_inst1; comp_inst2; mem_inst3` with warps w1–w4:
  - *Round-robin*: issue w1 w2 w3 w4 for inst1, then inst2, then inst3. All four memory instructions issue back-to-back, the four misses overlap at the end, nothing is left to hide them, and the pipeline stalls until w1's data returns.
  - *Greedy-then-oldest*: keep issuing one warp (oldest first) until a long-latency event (cache miss, branch, long tensor-core op), then switch to the oldest ready warp. Sequence w1 w1 w1(M), w2 w2 w2(M), …: the first miss starts early, later warps' compute overlaps it, and stall cycles drop, "but benefit depending on the specific program characteristics".
- **Two-level scheduling**: a single-level scheduler searches all ready warps (10s) every cycle, which costs power. Two-level keeps **active warps** (searched) and **pending warps**; only the active queue is searched [Gebhart11, Narasiman11].
- **Scheduling vs cache behaviour**: 4 warps, each repeatedly accessing its own block (A1–A4), with a cache of only 3 blocks and LRU.
  - RR: A1 A2 A3 A4 A1 … evicts each block before reuse, so every access misses (12/12).
  - GTO: A1 A1 A1 A2 A2 A2 …, so only the 4 compulsory misses.
- **Working set**: per-warp working set SS_W with N warps per SM. RR gives SS_W × N. Limiting schedulable warps to SW gives SS_W × SW. GTO's SW is not necessarily 1, because it switches on long-latency events.
- **Cache-conscious scheduling (Rogers 12)**: limit the number of schedulable warps, e.g. on a stall choose only from W1–W3 and start W4 only after they complete.
  - Challenges: (1) thread synchronisation, since `__syncthreads()` needs every warp of the block to arrive, so throttling must not starve warps (deadlock risk); (2) choosing the limit, because more warps mean more TLP but a bigger working set.
- **Other policies**: prefetch-aware scheduling built on two-level (Jog): fetch from **non-consecutive** warps to raise DRAM bank-level parallelism and give prefetches time. CTA-aware scheduling (Jog, OWL): control which CTAs are scheduled.
- Summary (L): RR and GTO; the 2-level scheduler gives "substantial energy savings"; the scheduler shapes the effective cache working set (cache-conscious scheduling); other optimisation opportunities exist.
Key terms: warp scheduler, ready warp, scheduling queue, oldest-first, critical-instruction-first, loose round-robin (LRR), greedy-then-oldest (GTO), long-latency event, two-level scheduler, active/pending warps, fetch group, intra-/inter-warp locality, working set, LRU thrashing, compulsory miss, cache-conscious wavefront scheduling (CCWS), lost intra-wavefront locality detector, static wavefront limiting (SWL), barrier deadlock, prefetch-aware scheduling, CTA-aware scheduling (OWL), bank-level parallelism.
**[SIMPLIFIED] / paper detail**
- (a) Two papers, two motives. narasiman2011twolevel splits warps into **fetch groups** ("32 warps could be split up into 4 fetch groups of 8 warps"), prioritises one group until it stalls, and round-robins within and across groups, so groups reach long-latency operations at different times. That is a *performance* motive: 19.1 % with large warps. gebhart2011energy's two-level active/pending scheduler is the *energy* motive (36 % RF energy with an RFC). The slide cites both together.
- (b) rogers2012ccws defines the baselines verbatim. "LRR Loose round-robin scheduling. Wavefronts are prioritized for scheduling in round-robin order. However, if a wavefront cannot issue during its turn, the next wavefront in round-robin order is given the chance to issue." "GTO A greedy-then-oldest scheduler. GTO runs a single wavefront until it stalls then picks the oldest ready wavefront. The age of a wavefront is determined by the time it is assigned to the core." For ties (same workgroup), the smallest thread IDs win, and "GTO scheduling had the best results" among the greedy variants tried. CCWS is **adaptive**: a "lost intra-wavefront locality detector (LLD) ... alerts the scheduler if its decisions are destroying intra-wavefront locality", per-wavefront locality scores give losing wavefronts "more exclusive access to the L1D", and "Best-SWL" (static limiting) is a separate baseline. Results: "an average 25% fewer L1 data cache misses ... a harmonic mean 24% performance improvement over previously proposed scheduling policies" at "0.17% total chip area"; 63 % harmonic-mean improvement over a simple greedy scheduler. Its motivation figure classifies hits as intra-wavefront vs inter-wavefront locality (128 B L1D lines).
- (c) jog2013orchestrated, verbatim: "The key idea is to separate in time the scheduling of consecutive warps such that they are not executed back-to-back" (prefetch-aware warp scheduling). It gives "25% and 7% average performance improvement over baselines that employ prefetching in conjunction with, respectively, the commonly-employed round-robin scheduler or the recently-proposed two-level warp scheduler" on a 30-core simulated GPGPU.
- (d) jog2013owl: four schemes, namely CTA-aware two-level warp scheduling, locality-aware warp scheduling, bank-level-parallelism-aware warp scheduling, and opportunistic memory-side prefetching, giving "33% average performance improvement compared to the commonly-employed round-robin warp scheduling policy" on a 28-core GPGPU. Motivation: of 38 applications, 19 spend "on average 62% of total cycles ... with no warps executing".
- (e) huang2014gpumech models both RR and GTO (13.2 % and 14.0 % error), connecting this lesson to M8.3.
**Exclusion note (Project 3):** Project 3 asks students to implement warp-scheduler policies (GTO and a CCWS-style policy), and recently also tensor-core timing, in the course's trace-driven MacSim-based simulator. The book explains the policies, their rationale and toy timelines like the ones above. No simulator code, no project-specific parameters (LLD sizes, scoring constants, cutoffs) and no expected cycle counts.
Sources: L M7L3; rogers2012ccws; narasiman2011twolevel; gebhart2011energy; jog2013orchestrated; jog2013owl; A18 ch3 §3.1.3; K12 §1.4.1 (round-robin vs greedy-fetch front-end).
Figures (lowyx; redraw)
- `m7l3_pipeline`: "Review: GPU Pipeline" with "schedule" highlighted. "What happens when multiple warps are ready?" Four scoreboard snapshots with W1–W4 all having Src1 (11, 13, 13, 14) and Src2 (1) ready.
- `m7l3_instruction`: "Scheduling Queue" of Instruction 1–5 → "Scheduler".
- `m7l3_gpu_schedule`: "Static code" (cards warp 1–4, each Inst1–3) vs "Dynamic instruction trace" (the 12-entry interleaving listed above; slide typos "Isnt").
- `m7l3_rr_gto`: code comp_inst1, comp_inst2, mem_inst3. "Round-robin": w1 w2 w3 w4 ×3 with M on all four of the third group, then "stall", with 4 overlapping latency arrows. "Greedy-then-Oldest (GTO): switch when there is a long latency event." w1 w1 w1(M) w2 w2 w2(M) w3 w3 w3(M) w4 w4 w4(M), shorter stall, staggered latency arrows.
- `m7l3_two_lvl`: "Scheduler chooses one warp from multiple active warps (10s of them)"; "Two-level scheduler to improve energy efficiency [Gebhart11, Narasiman11]". Single-level: Warp 1–5 → Scheduler. Two-level: Pending (Warp 11, 12, 13, 4, 5) and Active (Warp 1–3) → Scheduler.
- `m7l3_cache_behavior`: RR sequence A1 A2 A3 A4 ×3 with M under every access; "What if cache can have only 3 cache blocks? With RR, none of warps have cache hits with LRU. What about GTO?"; GTO sequence A1×3 A2×3 A3×3 A4×3 with M only on the first of each: "Only compulsory misses".
- `m7l3_cache_conscious`: "A cache-aware scheduler limits the number of schedulable warps to a small number. In case of a stall, choose from warps W1 – W3, and once all W1-W3 are completed, schedule instructions from W4." Sequence A1 A2 A3 ×3, stall, A1 A2 A3 A4 A4 A4. "Challenges: thread synchronization, ensuring that all warps are executed." Code `__global__ void Kernel(){ // work-1  __synchthreads(); // synchronization  // work-2 }` with the sync highlighted, and a "Thread synch" bar picture.

---

## M8 GPU Simulation

Module objectives (L, verbatim): "Gain an understanding of the fundamental concepts required for modeling GPU architecture simulations."; "Learn how to employ analytical models for performance modeling of GPUs."
Readings (L):
- Required: liu2023photon (MICRO 2023, pp. 1227–1241); williams2009roofline (CACM 52(4), pp. 65–76).
- Optional: eeckhout2010perfeval (Synthesis Lectures, with a Canvas local copy); karkhanis2004firstorder (ISCA 2004); huang2014gpumech (MICRO 2014); hong2009analytical (ISCA 2009).
Book sections: K12 ch2 "Performance Principles" (§2.1 algorithm design models overview, §2.2 Work-Depth Model, §2.3 External Memory Model, §2.4 combined analyses, §2.5 abstract and concrete measures) and ch4 (§4.1.1 Execution Time Modeling, §4.2.4 Roofline Model, §4.2.6 Other GPGPU Performance Modeling Techniques); eeckhout2010perfeval.
Erratum from the course (Canvas screenshot saved as lowyx `m7l2_cudahost`): "For Lesson 3: Analytical Models of GPUs, there is a typo in the video at 3:56. Last bullet should be: W_depth 20 also means at least 20 x PC registers is needed."

### M8.1 GPU Cycle Level Simulation (Part 1)
Objectives (L): "Describe cycle-level performance modeling for CPUs and GPUs"; "Explain queue-based performance modeling"; "Describe the basic simulation code structures for CPUs and GPUs"; "Get ready for the architecture modeling programming project".
What it teaches
- **Six performance-modelling techniques**: cycle-level simulation, event-driven simulation, analytical model, sampling-based techniques, data-based statistical/ML modelling, FPGA-based emulation.
- **Cycle-level simulation**: common in early design. A global clock; each cycle models events (fetch, decode, …). Multiple clock domains are possible (core, memory, NoC).
- **Execution-driven vs trace-driven**:
  - Execution-driven executes instructions during simulation, either *execute-at-fetch* or *execute-at-execute*. Usually indistinguishable, but the designer must choose. It needs no stored traces and can model run-time-dependent behaviour.
  - Trace-driven replays pre-collected traces (simulation decoupled from execution). It is simpler and lighter, and memory-only traces suffice for cache studies. It cannot model run-time-dependent behaviour such as lock acquisition and barriers.
- **Queue-based modelling**: FIFOs between pipeline stages (FE_queue, DE_queue, EX_queue), except the scheduler, which picks among ready instructions and is therefore not a FIFO. Completion wakes dependants (dependence chain and broadcast must be modelled). Caches and memory give memory latency. Execution latency can be a lookup table.
- **Parameters**: stage latency = queue depth; bandwidth (issue/execute width) = how many instructions move between queues per cycle. Instruction latencies are parameters (e.g. ADD 1 cycle, MUL 3 cycles) from the literature, CACTI or RTL; no circuit simulation is needed.
- **MacSim structure** (Georgia Tech CPU/GPU simulator): `main()` creates `macsim_c`, calls `initialize`, loops `while (sim->run_a_cycle());`, then `finalize`. `macsim::run_a_cycle` increments the cycle and calls the CPU, Mem and NoC `run_a_cycle`. The CPU's `run_a_cycle` calls the stages in **reverse order**, WB, Exec, Sch, De, Fe, so each stage consumes last cycle's outputs. The design is a hierarchy of modules.
- **op structure**: each modelled instruction carries an `op` with progress and cycles. `done_cycle = schedule_cycle + latency`, known at schedule time when the latency is fixed. Variable latency (cache misses) comes from the cache simulation.
- **Scheduler modelling**: pick ready instructions subject to resources (FP units, load/store queue entries, cache ports). Multi-cycle ops hold resources across cycles.
- **GPU cycle-level modelling**: the unit is the warp, not the thread (SIMT). Fetch, decode, schedule and execute are per warp instruction. The scheduler takes the head of each warp (in-order within a warp, out-of-order across warps). It must model divergence, the warp/block/kernel concepts and a different scheduler.
- **End of simulation**: a whole thread block goes to one SM. Track thread completion: block done when all its threads finish, kernel done when all blocks finish, application done when all kernels finish.
Key terms: cycle-level simulation, global clock, clock domain, execution-driven, execute-at-fetch/execute-at-execute, trace-driven, trace, queue-based model, FIFO, pipeline depth/width, latency parameter, CACTI, RTL, MacSim, run_a_cycle, op / done_cycle, resource constraint, warp-level modelling, simulation termination.
**Exclusion note (Project 3):** MacSim is the code base of the course simulator project. Describe the structure generically (queues, a reverse-order stage loop, done_cycle). **Do not reproduce MacSim code or its trace format.** The lowyx slide `m8l1_cpu_processor` shows MacSim's `main()` and `run_a_cycle`, which are public on GitHub (gthparch/macsim) but should still be paraphrased, not copied.
Sources: L M8L1; eeckhout2010perfeval; A18 (GPGPU-Sim methodology, chapter unverified).
Figures (lowyx; redraw)
- `m8l1_queue`: "Queue Based Modeling": Front-end → FE_queue → Decode Rename → DE_queue → Schedule → "scheduler" (orange, not a FIFO) → Execution (⇄ Memory) → EX_queue → Write-back.
- `m8l1_cpu_processor`: two code panels (MacSim `main` loop; `run_a_cycle` calling Cpu/Mem/Noc, and Cpu calling Wb, Exec, Sch, De, Fe in that order). Citation "gthparch/macsim".
- `m8l1_example`: a small queue pipeline. "Each modeled instruction has an op data structure ... E.g.) Op->done_cycle = op->schedule_cycle + latency. (Q) what if latency is not fixed? E.g.) Cache misses. After cache simulation (cache hit/miss hierarchy), we can know the memory instruction latency."
- `m8l1_end`: main loop with `sim->finalize()` boxed; the bullets on thread → block → kernel → application completion.

### M8.2 GPU Cycle Level Simulation (Part 2)
Objectives (L): "Describe advanced GPU cycle-level modeling techniques such as divergent warps, coalesced memory"; "Introduce several open source GPGPU simulators".
What it teaches
- **Modelling unit = warp**: I-cache access and PC registers are per warp. Mask bits track which threads participate (resource accounting).
- **Divergence in simulators**:
  - Execution-driven: model the SIMT stack faithfully, and alternative stack designs can be modelled.
  - Trace-driven: follows the trace machine's behaviour. "It's challenging to simulate different divergent branch handling mechanisms than the trace collection's machine." The trace must contain all executed paths with their masks, e.g. BB#1 <1111>, BB#2 <1100>, BB#3 <0011>, BB#4 <1111>.
- **Coalescing model**: merge requests, typically at cache-line granularity (64 B assumed). R1 (consecutive) → 1 request; R2 (128 B apart) → one 64 B request per thread. The number of transactions drives all memory-system modelling.
- **Coalescing in traces**: either list every thread address (0x0, 0x4, 0x8, …) or store a pre-coalesced (base, size). The latter shrinks traces but bakes in one transaction size, so a different microarchitecture needs new traces.
- **Cache hierarchy**: after coalescing, requests go to the TLB, L1 and L2 depending on the microarchitecture. Similar to CPUs, but coalescing is critical.
- **Sectored cache**: fetch one sector (16 B in the toy, out of a 64 B line) instead of the whole line. The sectors share the tag. Benefit: less bandwidth. Cost: less spatial-locality prefetch. In the example, R2's uncoalesced accesses fetch 16 B sectors instead of 64 B lines.
- **Simulators**:

| Name | ISA | Type | Architecture | Source |
|---|---|---|---|---|
| GPGPU-Sim | NVIDIA PTX/SASS | Execution driven | GPGPU only | gpgpu-sim.org |
| Accel-Sim | NVIDIA PTX/SASS | Trace driven | GPGPU and accelerator | accel-sim.github.io |
| MGPU-Sim | AMD GPU | Execution driven | Multi GPUs supported | [ISCA 2019] |
| MacSim | NVIDIA/Intel GPU | Trace driven | Heterogeneous computing | github.com/gthparch/macsim |
| Gem5-GPGPU-Sim | AMD GPU or NVIDIA PTX | Execution driven | Heterogeneous computing | cpu-gpu-sim.ece.wisc.edu |

Key terms: warp-level modelling, mask bits in traces, SIMT stack modelling, coalescing model, transaction size, pre-coalesced trace, cache hierarchy model, sectored cache, sector, tag sharing, GPGPU-Sim, Accel-Sim, MGPUSim, MacSim, gem5.
**[SIMPLIFIED]** The toy sector is 16 B in a 64 B line. NVIDIA uses 32 B sectors in 128 B lines (BPG §10.2.1 "32-byte transactions"). Slide typos: "Mem [102-1027]" should be [1024-1027]; R1 Th6 = 18; the 7 vs 8 request counts disagree with M7.1.
Sources: L M8L2; A18; BPG §10.2.1.
Figures (lowyx; redraw)
- `m8l2_divergent`: the text above plus the small CFG (BB#1 1111, BB#2 1100, BB#3 0011, BB#4 1111) with lane arrows.
- `m8l2_memory_coalescing`: "A 64 B cache line size is already assumed." R1 → Mem[0-63]. R2 → 8 boxes Mem[0-63], Mem[128+64], …, Mem[1280+64].
- `m8l2_cache_hierarchy`: the pipeline with the memory stage expanded (Address Coalescing, D-cache/TLB, PTW/TLB Miss handler, L2 cache). "After addresses are coalesced, memory requests access TLB, L1, L2 caches depending on GPU microarchitecture."
- `m8l2_sector_cache`: "Cache Block (64B)" → four "16 B" sectors. R2 → Mem[0-3], [128-131], [256-259], [512-515], [768-771], [102[4]-1027], [1152-1155]. Bullets: sectored cache brings a sector instead of the block; benefit, reduced bandwidth; drawback, reduced spatial locality; "Share the tag".
- `m8l2_gpu_sim`: the simulator table above.

### M8.3 Analytical Models of GPUs
Objectives (L): review cycle-level simulation; "Analytical model provides the first order of processor design parameters or application performance analysis"; "CPI computation was reviewed"; "Roofline was introduced"; "Compute bounded or memory bandwidth bounded is the most critical factor".
What it teaches
- **Analytical models** need no full execution, capture first-order behaviour, and give insight.
- **First-order GPU design**, worked example: target 1 T dot products/s of `sum += x[i] * y[i]`.
  - Compute: 1 T × (1 mul + 1 add) = 2 TFLOPS = 1 T FMA/s, i.e. 1000 FMA units at 1 GHz or **500 FMA at 2 GHz**.
  - Memory: "two memory bytes" per dot product, so **2 TB/s**.
  - 500 FMA ≈ 16 warps of width 32 (16 × 32 = 512). Either 16 SMs × 1 warp/cycle or 8 SMs × 2 warps/cycle at 2 GHz.
- **Multithreading parameters**: W_width = threads (warps) that can run in one cycle (e.g. 32). W_depth = warps that can be scheduled during one stall cycle. Resident threads per SM = W_width × W_depth.
  - Example `comp_inst1; mem_inst1`: 1 warp stalls on every memory op; 2 warps hide part of the stall; 4 warps hide it fully. W_depth = 1, 2, 4.
- **Hardware constraints**: W_width is set by the number of ALUs (and scheduler width). W_depth is set by registers (and PC registers). W_depth = 20 needs 20 × 32 × (registers per thread) registers and (erratum) at least 20 PC registers.
- **Finding W_depth**: proportional to memory latency. With a 200-cycle latency:
  - 1 compute + 1 memory instruction per warp: 200 / (1 + 1) = **100 warps**;
  - 1 memory per 4 compute: 200 / (1 + 4) = **40 warps**.
- **Number of SMs**: 1 warp × 16 SMs (large, few SMs; big caches) vs 2 warps × 8 SMs (many small SMs; small caches). Same total throughput and cache capacity. A larger cache has a longer access time, but sharing among blocks may raise the hit rate, so it is a trade-off needing finer models.
- **Sub-cores**: one SM split into several sub-cores, each with its own PC, decoder, warp scheduler and SPs, sharing the I-cache, crossbar and big caches (resource management).
- **Roofline**:
  - y = performance, x = arithmetic intensity (FLOP/byte). A slanted memory-bound region (left) meets a flat compute roof ("Hardware's peak FLOPS", right).
  - Vector-sum example: 2 bytes per 1 FLOP gives AI = 0.5, memory-bound.
  - `sum += x[i]*x[i]*y[i]*y[i]` with the same 2 bytes and 4 FLOPs gives AI = 2, moving right toward the compute-bound side.
  - Use it to judge whether there is room to optimise.
- **CPI model**: CPI = CPI_steady + Σ_i freq_i × CPI_event_i (penalties serialised). Example 5-stage in-order: CPI_steady = 1, branch misprediction penalty 3 at 2 %, cache miss penalty 5 at 5 %, so CPI = 1 + 0.02 × 3 + 0.05 × 5 = **1.31**.
- **Multithreaded CPI**: CPI_MT ≈ CPI_single / W_depth (ideal) + resource-contention terms (MSHRs, busy execution units, DRAM bandwidth). Since a GPU extends multithreading, CPI modelling applies.
- **Interval analysis**: an interval = a steady state at the effective dispatch rate + one long-latency event (penalty, during which no instruction executes). The first-order model [ISCA 2004] adds pipeline **drain** and **refill** shapes, which depend on the event (branch misprediction vs cache miss).
- **Interval analysis on GPUs**: treating the GPU as a plain multithreaded processor misses two factors: **branch divergence** (not all lanes active, serialised paths) and **memory divergence** (coalesced vs uncoalesced latency). Newer models add sub-cores, sectored caches and other contention.
Key terms: analytical model, first-order design, FMA, peak FLOPS, bandwidth requirement, W_width, W_depth, resident warps, latency hiding, SM count trade-off, sub-core, Roofline, arithmetic intensity, operational intensity, ridge point, compute-bound, memory-bound, CPI, CPI stack, steady-state CPI, miss-event penalty, MSHR, interval analysis, effective dispatch rate, pipeline drain/refill, branch divergence, memory divergence, MWP, CWP.
**[SIMPLIFIED] / paper detail**
- (a) Roofline: williams2009roofline (TR version) uses **operational intensity**: "the term operational intensity to mean operations per byte of DRAM traffic". Formula, verbatim: "Attainable GFlops/sec = Min(Peak Floating Point Performance, Peak Memory Bandwidth x Operational Intensity)". The ridge point is where the two meet ("these limits are created once per multicore computer, not once per kernel"). The lecture's "arithmetic intensity" counts bytes requested by the program, not DRAM bytes after caching. K12 §4.2.4 also treats Roofline.
- (b) The lecture's byte counts assume 1-byte elements ("2 bytes per 1 FLOPS"). For FP32, `x[i]*y[i]` loads 8 B per 2 FLOPs (AI = 0.25 FLOP/B) and the 4-FLOP variant gives 0.5. The worked 1 T dot-product design then needs 8 TB/s, not 2. Book worked example: V100 FP16 tensor peak 125 TFLOPS / 900 GB/s gives a ridge point of about 139 FLOP/B (the GEMM guide's 138.9).
- (c) hong2009analytical (MWP/CWP), verbatim definitions: "MWP represents the maximum number of warps per SM that can access the memory simultaneously during the time period from right after the SM processor executes a memory instruction from one warp ... until all the memory requests from the same warp are serviced". "CWP represents the number of warps that the SM processor can execute during one memory warp waiting period plus one."
  - Key equations: MWP = MIN(MWP_Without_BW, MWP_peak_BW, N); MWP_Without_BW_full = Mem_L / Departure_delay; MWP_peak_BW = Mem_Bandwidth / (BW_per_warp × #ActiveSM); CWP_full = (Mem_cycles + Comp_cycles) / Comp_cycles; CWP = MIN(CWP_full, N).
  - Three cases: if MWP = CWP = N, Exec = (Mem_cycles + Comp_cycles + Comp_cycles/#Mem_insts × (MWP − 1)) × #Rep; if CWP ≥ MWP (memory-bound), Exec = (Mem_cycles × N/MWP + Comp_cycles/#Mem_insts × (MWP − 1)) × #Rep; if MWP > CWP (compute-bound), Exec = (Mem_L + Comp_cycles × N) × #Rep.
  - Uncoalesced accesses enter via Mem_L_Uncoal = Mem_LD + (#Uncoal_per_mw − 1) × Departure_del_uncoal. Accuracy: 5.4 % (micro-benchmarks) and 13.3 % (applications) geometric-mean error.
- (d) huang2014gpumech: "GPUMech has 13.2% error for modeling the round-robin scheduling policy and 14.0% error for modeling the greedy-then-oldest policy while achieving a 97x faster simulation speed", and it "generates CPI stacks".
- (e) karkhanis2004firstorder: full text not fetched (only a blocked mirror). A search summary reports agreement "within 5.8% of detailed simulation on average and within 13% in the worst case"; verify before printing.
Numbers: GEMM guide "V100 ... FLOPS:B ratio is 138.9"; A100 FP16 tensor 312 TFLOPS / 1555 GB/s ≈ 201 FLOP/B (derived); H100 SXM5 (prelim.) 1000 / 3000 ≈ 333 FLOP/B (derived).
Sources: L M8L3; williams2009roofline; hong2009analytical; huang2014gpumech; karkhanis2004firstorder; K12 ch2, §4.1.1, §4.2.4; eeckhout2010perfeval.
Figures (lowyx; redraw)
- `m8l3_arch1`: a 16-SM GPU with Cache, "500 FMA, 2GHz"; "Channel 2TB/sec" to "DRAM /HBM".
- `m8l3_arch2`: bullets defining W_width and W_depth ("( W_width x W_depth) number of warps are resident in one SM"); a square with W_width across and W_depth down. Timelines for comp_inst1/mem_inst1: "1 warp" [w1 w1(M)] stall ×3; "2 warps" [w1 w1(M) w2 w2(M)] stall ×3; "4 warps" w1 w1 w2 w2 w3 w3 w4 w4 … continuous with no stall.
- `m8l3_arch3`: the four constraint bullets (the last as corrected by the erratum).
- `m8l3_subcore`: GPU core grid → one core zoomed into "I-Cache" over three "Sub-core" panels (PC stack, Decoder, Warp Scheduler, SP (EXE) units), plus "Cross Bar" and "Caches"; "Resource management".
- `m8l3_roffline` [sic, file name]: axes Performance vs "arithmetic intensity (FLOPS/BYTES)"; blue "Memory bounded" left, yellow "Compute bounded" right; roof labelled "Hardware's peak FLOPS"; a star on the slope moving right to a star in the compute region; the two example bullets.
- `m8l3_interval_based`: "Effective dispatch rate" vs "Time": steady state, "Long latency event" drop, "base" / "Penalty" / "Interval" arrows. Lower panel: "Pipeline Drain" ramp down and "Pipeline Refill time" ramp up. Bullets "Interval: one steady state and one long latency event"; "First-ordering Modeling [ISCA 2004]: Model the effect of pipeline drain and refill time".

### M8.4 Accelerating GPU Simulation
Objectives (L): "Describe techniques to accelerate simulation speed"; "Identify challenges in cycle-level simulation"; "Explore techniques for accelerating simulation"; "Describe sampling based techniques".
What it teaches
- **Speed problem**: at 1 KIPS, 10^9 instructions (≈1 s of real execution) take about 28 hours (10^6 s ≈ 11.6 days by plain arithmetic; see the flag). An ML workload that runs for hours natively would take "a century" to simulate.
- **Make the simulator faster**:
  - Parallelise it, with one host thread (P-thread) per simulated core. Memory and the NoC must be communicated or serialised, and most workloads are memory-bound, so memory becomes the bottleneck.
  - Event-driven simulation: process timestamped events from a queue and jump time from event to event. Good for long latencies (I/O, NVM writes).
  - Simplify models: average latencies or throughputs for non-critical events. Example: IPC = issue width with only caches and memory modelled (zsim-style core simplification), or fixed memory latency when studying compute.
  - Sampling.
  - Statistical/ML models.
- **Sampling**: random sampling.
  - Execution-driven: fast-forward or checkpoints.
  - Trace-driven: trace only the sampled windows.
  - State warm-up: caches and branch predictors need warming, or the samples must be long enough.
  - Phase-based sampling: SimPoint picks representatives of repeating phases (phase A high IPC, phase B low IPC; simulate one of each).
- **GPU sampling**: a single thread is too short, but there are many threads, so sample at block level (100 blocks instead of thousands), kernel level (1–2 kernels instead of tens, very effective for ML because kernels repeat hundreds of times), or warp level (fewer warps).
- **Reduce the workload**: fewer iterations (1 instead of 1000 training iterations), smaller inputs (a graph of 10^6 instead of 10^9 nodes), or only the dominant kernels (1–2 functions that take 90 % of the time); micro-benchmarks.
- **Data-driven modelling**: run on hardware to collect IPC, extract features (instruction count, loads, divergent branches …) from hardware counters or a simulator, and fit a statistical/ML model, e.g. cycles = C1 × #inst^e1 + C2 × #FP inst^e2 + C3 × #mem inst^e3.
Key terms: simulation speed (KIPS), parallel simulation, event-driven simulation, event queue, model simplification, zsim, sampling, random sampling, fast-forwarding, checkpoint, warm-up, SimPoint, program phase, block-/kernel-/warp-level sampling, workload reduction, micro-benchmark, data-driven model, feature extraction, hardware performance counters, regression.
**[SIMPLIFIED] / paper detail**
- (a) Arithmetic check: 10^9 instructions / 10^3 IPS = 10^6 s ≈ 278 hours, not 28. The slide's "28 hours" matches 10 KIPS (10^5 s ≈ 27.8 h). Use 10 KIPS or say ≈11.6 days for 1 KIPS.
- (b) liu2023photon (required), verbatim abstract fragments: "Photon incorporates methodologies that automatically consider different levels of GPU execution, such as kernels, warps, and basic blocks. Photon does not require up-front profiling of GPU workloads and utilizes a lightweight online analysis method based on the identification of highly repetitive software behavior ... Photon reduces the simulation time needed to perform one inference of ResNet-152 with batch size 1 from 7.05 days to just 1.7 hours with a low sampling error of 10.7%." It is built on MGPUSim. The authors' slides report up to 24.65× speed-up (average 1.87×) at 6.83 % average error (from search-result summary; verify).
- (c) Compare with the lecture's block/kernel/warp sampling: Photon is the paper-level realisation (kernel sampling + warp sampling + basic-block sampling).
Sources: L M8L4; liu2023photon; eeckhout2010perfeval (sampling, SimPoint).
Figures (lowyx; redraw)
- `m8l4_psim`: four "P-thread" frames, each containing a "Core", all wired to one "Memory". "Each P-thread simulates a core ... Memory/Noc (network on chip) needs to be communicated. Bottlenecks on the memory".
- `m8l4_esim`: "Event queue" holding Event 1 (t2), Event 2 (t4), Event 3 (t3); a timeline t1 → t2 ("Skip") → t3 → t4; a new "Event 4 (t5)" being inserted.
- `m8l4_sample`: sampling bullets plus an IPC-vs-time chart (x 0–40) alternating green Phase-A (high IPC) and purple Phase-B (low IPC) bands; "Program phase based sampling (e.g., Simpoint)".
- `m8l4_ddm`: "Program" → "GPU" → "Performance" (IPC chart); "Program" → "Feature extractions" (# of instructions, # of loads, # of divergent branches …; hardware performance counters) → "Statistical or ML analysis" → Performance; the cycle-count formula bullet.

---

## M9 Multi GPU

Module objectives (L, verbatim): "Understand multi-GPU architecture"; "Understand the challenges of multi-GPU architectures"; "Understand how to increase concurrency on multi-GPUs".
Readings (L):
- Required: arunkumar2017mcmgpu (ISCA 2017, pp. 320–332).
- Optional: NVIDIA NVLink page; "Upgrading Multi-GPU Interconnectivity with the Third-Generation NVIDIA NVSwitch" blog (now redirects elsewhere); GPUDirect RDMA documentation; yu2022multitenant (arXiv 2203.09040); ye2024dlsched (ACM CSUR 56(6)); CUDA MPS overview PDF.
Book sections: A18 ch5 (crosscutting research); PMPP ch20 (heterogeneous cluster programming: MPI + CUDA streams); HWP (NVLink/NVSwitch, MIG); AWP (MIG).

### M9.1 Multi-GPU Hardware
Objectives (L): "Describe multi-GPU architecture"; "Describe the challenges of multi-GPU systems"; "Introduce thread block scheduling and memory management in multi-GPUs"; "Explore alternative communication options in multi-GPUs".
What it teaches
- **Scaling path**: more cores on one die (monolithic GPU), which hits cost and reliability (yield) limits; then multiple GPU chips connected on a silicon interposer or as multi-socket GPUs behind a high-bandwidth switch; then multiple GPU boards over PCIe.
- **Package-level integration**: multi-GPU modules form a larger logical GPU, "continuous performance scaling beyond Moore's law". HBM supplies DRAM bandwidth; system I/O bandwidth is shared; NVIDIA uses NVLink. To the programmer it is still "many SMs" with global memory as one shared space, but memory is **NUMA** (near vs far memory, in latency and bandwidth).
- **Two questions**: where to schedule each thread block, and where to allocate each page. Simple answer: allocate a page in the memory near the block that first touches it (**first-touch**).
- **Worked example** (animation):
  - Thread blocks TB1–TB6 touch pages P-1…P-10: TB1 → P-2, TB2 → P-3, TB3 → P-5, TB4 → P-8, TB5 → P-8 and P-10.
  - Round-robin places TB1–TB4 on GPUs 1–4 and their pages follow first-touch (P-2 on GPU1, P-3 on GPU2, P-5 on GPU3, P-8 on GPU4).
  - TB5 is then scheduled on GPU1 (where TB1 ran). P-10 is allocated locally, but P-8 sits on GPU4, so it is a far access.
  - Fixes: schedule TB5 on GPU4 (locality-aware block scheduling), or migrate pages that see many far accesses.
- **NVLink / NVSwitch**: NVIDIA's GPU-to-GPU protocol, an alternative to PCIe.
  - "4th generation of NVLink provides 900GB/s per GPU and 18 links per GPU (3TB HBM3 memory bandwidth in H100)", so NVLink is about a quarter of HBM bandwidth.
  - Point-to-point does not scale to many GPUs, so NVSwitch chips give all-to-all connectivity with higher bandwidth and lower latency.
- **Memory spaces across boards**: GPUs on different boards hang off PCIe through the CPU, which lacks bandwidth for direct memory sharing, so boards communicate with **RDMA**. This is more like a distributed-memory system (M2).
- **RDMA background**: traditional TCP/IP networking goes through the software stack and uses CPU cycles on both ends (Buffer 1 → CPU1 → network → CPU2 → Buffer 2). **RDMA** (remote direct memory access) is DMA across the network, "host-bypass": RDMA engine to RDMA engine, without either CPU.
- **GPUDirect RDMA**: buffer-to-buffer transfers between GPUs, or between a GPU and other devices (NICs, storage), through the network interface. Inside a node, NVLink/NVSwitch carry GPU–GPU traffic. PCIe alone cannot meet the demand.
Key terms: monolithic GPU, yield, multi-chip module (MCM), GPU module (GPM), multi-socket GPU, silicon interposer, package-level integration, NUMA, near/far memory, first-touch page allocation, page migration, thread block scheduling, NVLink, NVSwitch, PCIe switch, RDMA, host bypass, RDMA engine, GPUDirect RDMA, NIC.
**[SIMPLIFIED] / paper detail**
- (a) arunkumar2017mcmgpu, verbatim abstract: the optimised MCM-GPU "achieves 22.8% speedup and 5x inter-GPM bandwidth reduction when compared to the basic MCM-GPU architecture ... is 45.5% faster than the largest implementable monolithic GPU, and performs within 10% of a hypothetical (and unbuildable) monolithic GPU ... 26.8% faster than an equally equipped Multi-GPU system with the same total number of SMs and DRAM bandwidth".
  - The three optimisations, verbatim: "(i) hardware caches to capture remote traffic in the local GPM, (ii) distributed and batched co-operative thread array (CTA) scheduling to better leverage inter-CTA locality within a GPM, and (iii) first touch page allocation policy to minimize inter-GPM traffic". The cache in (i) is called the "L1.5 cache".
  - Configuration: "a 256 SM GPU out of four GPMs", 3 TB/s total DRAM (768 GB/s local per GPM); inter-GPM bandwidth is studied up to multiple TB/s. The lecture's first-touch and block-locality example is a simplified version of (ii) and (iii).
- (b) NVLink numbers as of 2026 (nvidia.com NVLink page): 4th gen (Hopper) 900 GB/s and 18 links; 5th gen (Blackwell) 1,800 GB/s and 18 links; 6th gen (Vera Rubin) 3,000 GB/s and 36 links. NVLink Switch domains: 8 GPUs (gen 4), 72 (NVL72). The H100 "3 TB/s" is the preliminary HWP figure.
- (c) li2021tlb (M7 optional) studies address translation in exactly this multi-GPU setting.
Sources: L M9L1; arunkumar2017mcmgpu; nvidia.com NVLink page; GPUDirect RDMA docs (v13.4); HWP (NVLink, NVSwitch).
Figures (lowyx; redraw)
- `m9l1_multigpu`: four stages joined by arrows. A small GPU (cores + cache, Mem); "Monolithic GPU" (16 cores + Cache, Mem); "Multi-socket GPUs or Multi-chip GPUs" (2×2 GPUs, each with Mem, an orange "High bandwidth Switch" between rows); "Multi-GPU boards" (GPU board / PCI-E / GPU board). Heading: "To accommodate the high demand for computing power, GPUs have expanded into multi-GPU systems".
- `m9l1_nvlink`: 2×2 GPUs each with outer "Mem", all-to-all blue "High speed connections" (sides + diagonals). Bullets: "High-speed connections (e.g., NVLINK); I/O bandwidth needs to be shared; Programmer's viewpoint: many SMs; Shared memory space; Memory is NUMA (non-uniform memory); Near memory and far memory from the latency's viewpoint".
- `m9l1_tb_s0`, `m9l1_tb_s1`, `m9l1_tb_s2`, `m9l1_tb_s3` (4 frames): the 4-GPU diagram plus a "Memory Space" row P-1…P-10. s1: blocks TB1 (red) → P-2, TB2 → P-3, TB3 → P-5, TB4 (navy) → P-8, TB5 → P-8 and P-10, TB6 unused; touched pages take their block's colour. s2: TB1–TB4 placed on GPUs 1–4 with their pages in local Mem. s3: TB5 replaces TB1 on GPU1, P-10 is added to GPU1's Mem, and a big yellow arrow shows TB5's far access to P-8 on GPU4.
- `m9l1_nvlink1`: bullets as quoted above. Three diagrams: CPU + 2 GPUs via a "PCIe switch" (PCI-E communication); the same plus a direct NVLink between the GPUs; 4 + 4 GPUs fully connected through two "Switch" bars (NVSwitch).
- `m9l1_mem_space`: "Across Multi-GPU boards, it uses RDMA to communicate; Distributed memory systems". CPU on a PCIe switch feeding two 4-GPU NVLink boards; an "RDMA" bracket between the boards' memories.
- `m9l1_rdma`: Buffer 1 → CPU1 → Network → CPU2 → Buffer 2.
- `m9l1_rdma1`: Buffer 1 → RDMA Engine ⇒ (over the Network) ⇒ RDMA Engine → Buffer 2; the CPUs are uninvolved.
- `m9l1_rdma2`: Buffer 1 → GPU1 → Network → GPU2 → Buffer 2; and Buffer 1 → GPU1 → Network → Other devices → Buffer 2.

### M9.2 Concurrency on GPUs
Learning objectives (L): "Describe how to increase GPU utilization, particularly in the context of multi-GPUs"; "Explore diverse strategies for efficiently managing multi-job workloads"; "Discover different GPU concurrency mechanisms: Multi-Instance GPUs (MIG) and Multi Process Service (MPS), and Stream based programming".
What it teaches
- **Utilisation problem**: not every job fills a GPU, which matters in data centres. Traditional data centres run many tenants, but some AI workloads (LLMs) take the whole GPU, so their usage patterns differ. "Some AI workload performance is limited by the slowest task".
- **Mechanisms** (panel figure):
  - **Streams**: one client, multiple streams. Only independent streams run concurrently, with no resource partitioning (SMs, L2 and DRAM all shared).
  - **MPS**: different clients run on different SMs, but L2 and DRAM are shared.
  - **MIG**: the GPU is physically split per client (SMs, L2 slices, DRAM bandwidth).
- **MIG**: several jobs on one large GPU with memory and core isolation for multiple users. It partitions memory, L2 cache ports, DRAM bandwidth and on-chip crossbar ports, giving QoS. "the A100 can host up to 7 instances", which is crucial for multi-tenant cloud providers.
- **MPS**: spatial partitioning since V100 (time-slicing before). Concurrent jobs without strict partitioning, so performance can be unpredictable. It eases porting MPI jobs to CUDA and can beat MIG on utilisation when QoS does not matter.
- **Stream programming**: concurrent kernels, multiple CPU threads submitting work, overlapping communication and computation across streams.
  - Code contrast: the non-stream version is `cudaMemcpy` H2D → `gaussian_pdf<<<…>>>` → `cudaMemcpy` D2H. The stream version creates `cudaStream_t streams[num_streams]`, then for each chunk issues `cudaMemcpyAsync` H2D, the kernel and `cudaMemcpyAsync` D2H on `streams[i % num_streams]` (depth-first launch), then `cudaDeviceSynchronize()`.
  - OpenMP programs port easily to streams. Scheduling across streams costs overhead (dependency checks), so **CUDA Graphs** build the dependency chain before launch.
- **Multi-GPU programming**: allocate per GPU (`cudaSetDevice(i); cudaMalloc(&d_x[i], …)`), copy per GPU, launch the kernel per GPU, then wait for all (`cudaDeviceSynchronize`). Streams can be combined with multiple GPUs.
- **Comparison table** (verbatim from the slide):

| Mechanisms | Stream | MPS | MIG |
|---|---|---|---|
| Partition type | No | Logical | Physical |
| Max Partition | Unlimited | 48 | 7 |
| SM isolation | No | By percentage | Yes |
| Mem BW isolation | No | No | Yes |
| Performance QoS | No | partial | Yes |
| Reconfiguration | Dynamic | Process launch | When idle |

Key terms: utilisation, multi-tenancy, client, stream, concurrent kernel execution, `cudaStreamCreate`, `cudaMemcpyAsync`, depth-first launch, CUDA Graph, MPS, MIG, GPU instance, QoS, time slicing, spatial partitioning, logical vs physical partition, `cudaSetDevice`, `cudaDeviceSynchronize`.
**[SIMPLIFIED] / paper detail**
- (a) The MPS overview PDF (CUDA 13.4 docs), verbatim: "MPS client processes have fully isolated GPU address spaces. MPS supports a limited form of error containment: A fatal GPU fault generated by a Volta MPS client process will be contained within the subset of GPUs shared between all clients with the fatal fault-causing GPU." It also reports the fault to all clients on those GPUs. "MPS supports limited execution resource provisioning" (the "By percentage" row). Limit: "Each MPS server supports up to 60 client CUDA contexts per-device" in the current document, while the slide says 48 (presumably an older documented limit, not verified here). Print the documented number with its version.
- (b) MIG on H100: "Second-Generation Secure MIG", still up to 7 GPU instances, plus confidential computing (HWP).
- (c) The streams and multi-GPU code is adapted from the OLCF "cuda training series" (cited on the slide). Write original examples in the book.
- (d) yu2022multitenant and ye2024dlsched are surveys (multi-tenant inference; DL scheduling in GPU data centres, training and inference). ye2024dlsched (arXiv v3 abstract): "traditional approaches designed for big data or high performance computing workloads can not support DL workloads to fully utilize the GPU resources". Use them for further reading only.
Sources: L M9L2; MPS overview; AWP/HWP MIG sections; CPG streams and CUDA Graphs; PMPP ch20; yu2022multitenant; ye2024dlsched.
Figures (lowyx; redraw)
- `m9l2_gpucon`: four panels. A single kernel (SM with L1 → L2 → DRAM). Streams A/B/C → Scheduler → a GPU of 12 SMs, all tri-striped (L2 and DRAM striped too: no partitioning). MPS: Client 1 and Client 2 → Scheduler → SMs individually coloured per client, with L2 and DRAM shared (white). MIG: the left half of the SMs, L2 and DRAM green for Client 1, the right half yellow for Client 2. Bullets "Multi-stream: no resource partitioning; Multi-Process Service (MPS); Multi-Instance GPU (MIG)".
- `m9l2_gpumulti`: the MIG bullets as quoted; 7 "GPU"+"Memory" instances with App #1 on 1, App #2 on 1, App #3 on 2, App #4 on 3.
- `m9l2_stream`: the non-stream vs stream code above and its bullets.
- `m9l2_multigpu`: the multi-GPU host code with callouts "Malloc for each GPU", "Indicate which device to use from the host side", "Kernel invocation for each GPU", "Wait until all devices finish".
- `m9l2_gpusupport`: the comparison table above.

---

## M10 Compiler Background - I

Module objective and readings (L): "Be able to explain comparisons with other GPU programming"; Required Reading: "OpenCL overview". Both look like placeholders (see sources.md). The lessons themselves cover the GPU compilation flow, PTX, IR and basic blocks, and data-flow analysis (reaching definitions).
Book sections: CPG §3.1 "Compilation with NVCC" (offline compilation, JIT compilation, binary and PTX compatibility); NVCC documentation (compilation trajectory figure); PTX ISA (instruction statements, predicates, setp, special registers); BPG §16 (PTX/cubin compatibility); K12 §1.3.7 PTX. Standard compiler texts (the Dragon book, ch. 8–9) are not on the course list; add a bib entry if cited.
Context: Project 5 (Fall 2025 onward per student reports) implements reaching definitions and liveness in a Python framework. See the exclusion notes.

### M10.1 GPU Compiler Flow
Learning objectives (L): "Demonstrate comprehension of the fundamental process of GPU program compilation"; "Explore the components and stages involved in GPU compilation".
What it teaches
- **Classic flow**: source → front end → IR → optimiser (IR → IR) → back-end code generation (machine-specific optimisation) → target program.
- **GPU flow**: a CUDA file has host and device code. A splitter separates them and each goes through the same pipeline. Device code → NVPTX codegen → PTX assembly. Host code + PTX/cubin → **fat binary**.
- **NVIDIA nvcc trajectory** (from the NVCC docs):
  - Host path: .cu → C++ preprocessor → .cpp4.ii → cudafe++ → .cudafe1.cpp → C++ compiler → .o.
  - Device path, repeated per virtual architecture: C++ preprocessor → .cpp1.ii → cicc → .ptx → ptxas → .cubin; .ptx and .cubin → fatbinary → .fatbin.c, #included into the host stub.
  - Device linker: nvlink → a_dlink.cubin → fatbinary → link.stub → C++ compiler → a_dlink.o.
  - Host linker → executable.
  - Because PTX is a virtual ISA, its target is a "virtual architecture" (compute_XX), while ptxas targets a real one (sm_XX).
- **Open-source CUDA toolchain** (LLVM): host/device splitter; device code: clang → IR optimisation → NVPTX codegen → PTX; host compilation embeds it into a fat binary.
- **Clang**: front-end parser for C-family languages (now extended to others). It produces the **AST**. Example: the AST of Euclid's GCD (`while b ≠ 0: if a > b: a := a − b else: b := b − a; return a`) — statement sequence → while (condition `b ≠ 0`, body branch with condition `a > b`, if-body assign `a := a − b`, else-body assign `b := b − a`) → return a.
- **C++ preprocessor**: text substitution. `#define COURSE_NUMBER 8803` turns `int number = COURSE_NUMBER;` into `int number = 8803;`.
- **IR**: shares infrastructure across languages and architectures, is a good abstraction for optimisation, and carries metadata.
- **PTX vs SASS**:
  - PTX (Parallel Thread Execution) is a virtual, architecture-independent ISA, translated to machine code later, so it has **no register allocation**.
  - SASS ("shader assembly") is the real, architecture-dependent assembly with allocated registers. SASS differs per GPU generation; PTX stays the same.
- **Fat binary**: executables for several architectures plus host code. At run time it is split: the device part goes to the driver, which commonly (re)compiles PTX for the actual GPU (JIT).
Key terms: front end, AST, IR, optimiser, back end, code generation, host/device splitting, nvcc, cudafe++, cicc, ptxas, nvlink, fatbinary, cubin, virtual architecture (compute_XX), real architecture (sm_XX), clang, LLVM, NVPTX, preprocessor, macro, PTX, SASS, fat binary, JIT compilation.
Exact (CPG §3.1.1.2 "Just-in-Time Compilation", verbatim): "Any PTX code loaded by an application at runtime is compiled further to binary code by the device driver. This is called just-in-time compilation ... It is also the only way for applications to run on devices that did not exist at the time the application was compiled". The JIT result is cached in the "compute cache". For cubin and PTX compatibility, see CPG §3.1.2 Binary Compatibility, §3.1.3 PTX Compatibility, §3.1.4 Application Compatibility.
Sources: L M10L1; CPG §3.1; NVCC docs; PTX ISA §1; K12 §1.3.7.
Figures (lowyx; redraw)
- `m10l1_compileflow`: Source program → [Front End] →IR→ [Optimizer] →IR→ [Back-end Code Gen] → Target Program.
- `m10l1_compileflowgpu`: the same pipeline in a big box. "Host/Device code file" splits into Host → mini pipeline → Fat binary, and Device code → mini pipeline → Fat binary. The device back end zooms to "NV PTX Code gen" → "PTX Assembly".
- `m10l1_compileflowgpunvidia`: the nvcc trajectory figure from the NVIDIA docs (as above, with the legend: solid arrow = input file; dash-dot = #include; "Repeat for each .cu input file / each virtual architecture / ptxas and nvlink for each virtual/real architecture combination"; grey = device linker). Redraw simplified; do not copy NVIDIA's figure.
- `m10l1_compileflowgpunvidiahost`: Host/Device code file → Host/Device splitter → Host code, and Device code → Device code Generator (zoom: clang → IR optimization → NVPTX codegen) → PTX assembly; both → Host compilation → Fat binary.
- `m10l1_clang`: the GCD AST described above (operations blue, variables green, constant yellow).
- `m10l1_cpp`: `#define COURSE_NUMBER 8803` substitution, before and after.

### M10.2 PTX
Learning objectives (L): "Explain the basics of PTX"; "Explore PTX instruction format"; "Describe optional predicate information"; "Understand PTX code examples".
What it teaches
- **Instruction format**: zero to four operands, with an optional guard predicate after `@`: `@p opcode;`, `@p opcode a;`, `@p opcode d, a;`, `@p opcode d, a, b;`, `@p opcode d, a, b, c;` (d = destination; a, b, c = sources).
- **setp** writes two destination predicates separated by `|`: `setp.lt.s32 p|q, a, b;` sets p = (a < b) and q = !(a < b).
- **Predicated execution**: GPUs use predication heavily to remove divergent branches.
  - Predicates are optional and declared as `.reg .pred p, q, r;`. All PTX registers are virtual, hence the `.pred` type specifier.
  - `if (i < n) j = j + 1;` becomes `setp.lt.s32 p, i, n; @p add.s32 j, j, 1;` (`lt` = less than).
- **PTX statements**: a statement is a directive (`.target`, `.address_size`, `.function`/`.func`, `.reg`, `.global` …) or an instruction, with an optional label, ending with `;`. Example: `.reg .b32 r1, r2; .global .f32 array[N]; start: mov.b32 r1, %tid.x; shl.b32 r1, r1, 2; ld.global.b32 r2, array[r1]; add.f32 r2, r2, 0.5;`. Every instruction carries a type.
- **Other instructions**: control flow `bra targ1;`, `call func;` (slide typo "all func"), `ret;`; synchronisation `membar`, `fence`; atomics `atom` (e.g. `atom.add.f16`; the type must be given). Special registers: `%ntid` (number of threads in a CTA), `%tid` (thread ID), stack pointer (`%sp` per the slide; check the PTX ISA, which handles stack frames differently). "Please refer to the PTX manual."
Key terms: PTX statement, directive, instruction, label, opcode, operand, guard predicate (`@p`, `@!p`), predicate register (`.pred`), `setp`, comparison operator (`.lt`, `.gt`), type suffix (`.s32`, `.u32`, `.f32`, `.b32`), state space (`.reg`, `.global`, `.shared`, `.param`), `bra`, `call`, `ret`, `membar`/`fence`, `atom`, special registers `%tid`, `%ntid`, `%ctaid`.
Exact (PTX ISA 9.4), verbatim: "PTX instructions generally have from zero to four operands, plus an optional guard predicate appearing after an `@` symbol to the left of the `opcode`". Conditional execution syntax: `@{!}p instruction;`. setp: "Compare two numeric values with a relational operator, and optionally combine this result with a predicate value by applying a Boolean operator."
Sources: L M10L2; PTX ISA (Instruction Statements; Predicated Execution; setp; Special Registers; mma shapes for M12).
Figures (lowyx; redraw)
- `m10l2_ptx`: the format bullets above.
- `m10l2_ptx2`: the predicate bullets, plus `if (i < n) j = j + 1;` → `setp.lt.s32 p, i, n; // p = (i < n)` / `@p add.s32 j, j, 1; // if i < n, add 1 to j`.
- `m10l2_ptx3`: "Example of PTX Code" with the listing above.
- `m10l2_ptx4`: the instruction-category bullets above.

### M10.3 IR and Basic Block
Learning objectives (L): "Describe intermediate representation (IR)"; "Identify basic blocks within code"; "Construct a control flow graph".
What it teaches
- **IR**: typically three-address code, `A = B op C`.
  - LLVM IR: `%result = add i32 %a, %b` (`%result` destination, `add` operation, `i32` result type, `%a`, `%b` sources).
  - PTX: `add.u32 %r1, %r2, %r3` or `add.s32 …` (separate unsigned and signed adds).
- **Basic block**: "a maximum sequence of instruction streams within one entry and one exit". Only the first instruction is reachable from outside; once entered, all of it executes, usually consecutively. The exit is commonly a control-flow instruction. Optimisation within a block is **local**.
- **Flow graph**: nodes are basic blocks and edges are possible execution paths. The entry node is the program's first statement. If/else gives BB1 → BB2, BB3 → BB4.
- **Worked PTX example** (if-else):
  ```
  ld.s32 %r1, [src1]; ld.s32 %r2, [src2];
  setp.gt.s32 %p1, %r1, %r2; @%p1 bra is_greater; bra is_smaller;
  is_greater: mov.s32 %r3, %r1; bra end_if;
  is_smaller: mov.s32 %r3, %r2;
  end_if:
  ```
- **Leader algorithm**: (1) leaders are the first instruction, any target of a conditional or unconditional jump, and any instruction immediately after a jump; (2) a basic block runs from a leader up to the next leader.
  - Result: BB1 = the two loads + setp + `@%p1 bra is_greater`; BB2 = `bra is_smaller`; BB3 = `is_greater: mov; bra end_if`; BB4 = `is_smaller: mov`; BB5 = `end_if:`.
  - CFG: BB1 → BB2 and BB3; BB2 → BB4; BB4 → BB5; BB3 → BB5.
Key terms: intermediate representation, three-address code, LLVM IR, `%` registers, type (`i32`), basic block, single entry/single exit, leader, branch target, fall-through, control flow graph (CFG), entry/exit node, local optimisation.
Note for writers: the lecture's PTX example is fine as a concept, but build the book's exercise on a different program (Project 5 boundary).
Sources: L M10L3; Dragon book §8.4 (basic blocks and flow graphs), if cited.
Figures (lowyx; redraw)
- `m10l3_ir`: the IR bullets above.
- `m10l3_flowgraph`: code `If (cond1) // BB #1 / do work1 // BB #2 / else / do work 3 // BB #3 / BB #4` with the diamond CFG.
- `m10l3_egptx`: the PTX listing ("Question:1 Draw a basic block"; slide label "Is_smaller" mis-capitalised).
- `m10l3_bb`: the leader rules (Step 1 three bullets; Step 2 grouping) with leaders boxed blue and blocks red on the listing.
- `m10l3_egptx2`: the answer, 5 blocks boxed, and the CFG (BB1 → BB2, BB1 → BB3, BB2 → BB4, BB4 → BB5, BB3 → BB5).

### M10.4 Introduction to Data Flow Analysis
Learning objectives (L): "Explain global code optimization"; "Understand example code optimizations"; "Explain the basic concept of data flow analysis"; "Explain the concept of reaching definitions".
What it teaches
- **Local vs global optimisation**: within a basic block vs across blocks. Most global optimisations rely on data-flow analysis, which analyses each block's effect, and analyses differ in the property examined. Every optimisation "must preserve the semantics of the original program".
- **Examples**: removing redundant instructions; copy/constant propagation (which often exposes more redundancy); dead code elimination; code motion; induction-variable detection and strength reduction.
- **Abstraction**: program points before and after each statement; the input state before and the output state after.
- **Transfer functions**: OUT[B] = f_B(IN[B]) with f_B = f_sn ∘ … ∘ f_s1 for forward problems. IN[B] = ∪_{P ∈ pred(B)} OUT[P]. For backward problems, IN[B] = f_B(OUT[B]) and OUT[B] = ∪_{S ∈ succ(B)} IN[S]. Example on the 5-block CFG: BB5's predecessors are BB3 and BB4; BB4's successor is BB5.
- **Reaching definitions**: "A definition d reaches a point p if there is a path from the point immediately following d to p, without being killed (overwritten)." A definition is a variable receiving a value; a use is a read (`a = x + y`: definition a; uses x, y).
- **Gen and kill**: for d: u = v + w, gen_d = {d} and kill_d = all other definitions of u. f_d(x) = gen_d ∪ (x − kill_d).
- **Composition**: f_2(f_1(x)) = (gen_2 ∪ (gen_1 − kill_2)) ∪ (x − (kill_1 ∪ kill_2)). In general, f_B(x) = gen_B ∪ (x − kill_B) with kill_B = kill_1 ∪ … ∪ kill_n and gen_B = gen_n ∪ (gen_{n−1} − kill_n) ∪ … ∪ (gen_1 − kill_2 − … − kill_n).
- **Example CFG** (used in M10.5 and M11.1): ENTRY → B1 {d1: i = m − 1; d2: j = n; d3: a = u1} → B2 {d4: i = i + 1; d5: j = j − 1} → B3 {d6: a = u2} and B4 {d7: i = u3}; B3 → B4; B4 → B2 (back edge) and B4 → EXIT.

| Block | gen | kill |
|---|---|---|
| B1 | {d1, d2, d3} | {d4, d5, d6, d7} |
| B2 | {d4, d5} | {d1, d2, d7} |
| B3 | {d6} | {d3} |
| B4 | {d7} | {d1, d4} |

Key terms: local/global optimisation, data-flow analysis, program point, transfer function, composition, forward/backward problem, predecessor, successor, meet (∪), reaching definition, definition, use, kill, gen set, kill set.
**Exclusion note (Project 5):** this example is the textbook's classic (Dragon book Fig. 9.13) and appears in the lecture. The book should explain the equations and work through **its own** CFG. Do not provide a Python (or any) implementation of reaching definitions or liveness, or code shaped like a project framework.
Sources: L M10L4; Dragon book §9.2 (if cited).
Figures (lowyx; redraw)
- `m10l4_codeopt`: local vs global bullets as quoted.
- `m10l4_trans`: the transfer-function notation above with the 5-block CFG.
- `m10l4_reachdefn`: the reaching-definition bullets (verbatim definition above).
- `m10l4_gnk`: "d: u = v + w" with the gen/kill definitions.
- `m10l4_gnk2`: the B1–B4 CFG with statements d1–d7 and the gen/kill table above.
- `m10l4_gnk_general`: the composition derivation (slide typos "gen_u" for gen_n and "∪-").

### M10.5 Example of Reaching Definitions
Learning objectives (L): "Apply transfer functions for reaching definitions analysis"; "Explore an example of reaching definitions in control flow analysis".
What it teaches
- **Equations**: IN[B] = ∪_{P pred B} OUT[P]; OUT[ENTRY] = ∅ (boundary); OUT[B] = gen_B ∪ (IN[B] − kill_B).
- **Algorithm**: `OUT[ENTRY] = ∅; for each B ≠ ENTRY: OUT[B] = ∅; while (changes to any OUT occur) for each B ≠ ENTRY { IN[B] = ∪ OUT[pred]; OUT[B] = gen_B ∪ (IN[B] − kill_B) }`.
- **Bit-vector walk-through** (d1…d7 written as 3 + 4 bits):

| BB | OUT⁰ | IN¹ | OUT¹ | IN² | OUT² |
|---|---|---|---|---|---|
| B1 | 000 0000 | 000 0000 | 111 0000 | 000 0000 | 111 0000 |
| B2 | 000 0000 | 111 0000 | 001 1100 | 111 0111 | 001 1110 |
| B3 | 000 0000 | 001 1100 | 000 1110 | 001 1110 | 000 1110 |
| B4 | 000 0000 | 001 1110 | 001 0111 | 001 1110 | 001 0111 |
| EXIT | 000 0000 | 001 0111 | 001 0111 | 001 0111 | 001 0111 |

  - The second pass changes OUT[B2] (d6 now reaches B2 via the back edge from B4). A third pass changes nothing, so this is the fixed point.
  - Slide errors: B1's OUT¹ is printed "111 000". The transcript's OUT[B4] "001 01111" has an extra digit. The correct value is 001 0111 (d3, d5, d6, d7).
Key terms: boundary condition, iterative (round-robin) algorithm, fixed point, convergence, bit vector, back edge.
**Exclusion note:** as M10.4. Use a fresh CFG in the book.
Sources: L M10L5; Dragon book §9.2.4 (if cited).
Figures (lowyx; redraw)
- `m10l5_gnk_eg`: the same CFG and gen/kill sets, redrawn.
- `m10l5_cfe`: "Control Flow Equations" as above.
- `m10l5_algo`: the algorithm box ("Iterative process").
- `m10l5_algo_vis`: "Illustration of Reaching Definitions", with the table above (corrected).

---

## M11 Compiler Background - II

Module objective and readings (L): the same placeholders as M10 ("Be able to explain comparisons with other GPU programming"; "OpenCL overview"). The lessons cover liveness, SSA, classic optimisations and divergence analysis.
Book sections: Dragon book §9.2.5 (live-variable analysis), §6.2.4 / §9 (SSA) if cited; Cytron et al. 1991 (dominance-frontier SSA construction) if cited; CPG §7.39 `#pragma unroll`; CPG §5.4.2 (divergence from the programmer's side).
Context: Project 5 (liveness and reaching definitions in recent terms; warp-divergence detection in Spring 2024). See the exclusion notes in M10.4 and M11.4.

### M11.1 Live-Variable Analysis
Learning objectives (L): "Explain the concept of Liveness Analysis"; "Explore the application of Liveness Analysis in register allocation"; "Identify data-flow equations and explain their role in analysis".
What it teaches
- **Liveness** tells which variables are live (their value will be used later) at each program point. Its main use is register allocation: registers only for live variables, fewer spills.
- **Equations**:
  - def_B = variables defined in B before any use; use_B = variables possibly used in B before any definition.
  - IN[EXIT] = ∅ (boundary).
  - IN[B] = use_B ∪ (OUT[B] − def_B): live on entry if used before redefinition in B, or live on exit and not redefined in B.
  - OUT[B] = ∪_{S ∈ succ(B)} IN[S]: live on exit iff live on entry to some successor.
  - The analysis runs **backward**.
- **Algorithm**: `IN[EXIT] = ∅; for each B ≠ EXIT: IN[B] = ∅; while (changes to any IN) for each B ≠ EXIT { OUT[B] = ∪ IN[succ]; IN[B] = use_B ∪ (OUT[B] − def_B) }`.
- **Worked example** (the M10 CFG; uses m, n, u1, u2, u3):

| Block | def | use |
|---|---|---|
| B1 | {i, j, a} | {m, n, u1} |
| B2 | {i, j} | {i, j} |
| B3 | {a} | {u2} |
| B4 | {i} | {u3} |

First pass (backward): OUT[B4] = ∅ → IN[B4] = {u3}; OUT[B3] = {u3} → IN[B3] = {u2, u3}; OUT[B2] = {u2, u3} → IN[B2] = {i, j, u2, u3}; OUT[B1] = {i, j, u2, u3} → IN[B1] = {m, n, u1, u2, u3} = OUT[ENTRY].
- Second pass: B4's successors include B2 via the back edge, so OUT[B4] = {i, j, u2, u3} and IN[B4] = {j, u2, u3}. Then IN[B3] = {j, u2, u3} and OUT[B2] = {j, u2, u3}. IN[B2] is unchanged ({i, j, u2, u3}, because use_B2 = def_B2 = {i, j}), so IN[B1] is unchanged. The third pass changes nothing, so the algorithm stops.
- Note: the slide table shows only the first pass, e.g. OUT[B4] = ∅. The transcript's second pass corrects this through the B4 → B2 edge; take the converged values from it.
- **Register allocation**: in the 4-block diamond (BB1 `a = 10; b = a + 20`; BB2 `c = b + 1; a = 2`; BB3 `a = −1; b = 1`; BB4 `c = c + b`), a is dead after BB1 (redefined in both BB2 and BB3), so its register is reusable after BB1. b is still live at BB2 (used in BB4); if it were dead, its register could be reused too.
- **Spills/fills**: when live values exceed the registers, store them temporarily to the stack and reload. PTX assumes infinitely many virtual registers, so spills appear only after ptxas (SASS, local memory).
- **Summary table**:

| | Reaching definitions | Live variables |
|---|---|---|
| Domain | sets of definitions | sets of variables |
| Direction | forward | backward |
| Transfer function | gen_B ∪ (x − kill_B) | use_B ∪ (x − def_B) |
| Boundary | OUT[ENTRY] = ∅ | IN[EXIT] = ∅ |
| Meet | ∪ | ∪ |
| Equations | OUT[B] = f_B(IN[B]); IN[B] = ∧ OUT[pred(B)] | IN[B] = f_B(OUT[B]); OUT[B] = ∧ IN[succ(B)] |
| Initialise | OUT[B] = ∅ | IN[B] = ∅ |

Key terms: live variable, liveness, backward analysis, def set, use set, boundary condition, register allocation, register reuse, spill, fill, local memory (spill target on NVIDIA), interference.
**Exclusion note (Project 5):** concepts, equations and hand-worked examples on the book's own CFG only; no implementation.
Sources: L M11L1; Dragon book §9.2.5 (if cited); CPG §5.3.2 (local memory used for register spills; verify the wording).
Figures (lowyx; redraw)
- `m11l1_live`: "Data-Flow Equations" for liveness, as above; "Analysis is done in the backward (opposite to the control flow)".
- `m11l1_algo`: the algorithm box.
- `m11l1_live_eg`: the CFG with def/use sets; the first-pass table OUT[ENTRY] = IN[B1] = {m, n, u1, u2, u3}; OUT[B1] = IN[B2] = {i, j, u2, u3}; OUT[B2] = IN[B3] = {u2, u3}; OUT[B3] = IN[B4] = {u3}; OUT[B4] = IN[EXIT] = ∅.
- `m11l1_live_analysis`: the diamond CFG with a, b, c and the bullets "a is dead after BB #1 / Register for a can be reused after BB #1 / b is still live at BB #2 ...".
- `m11l1_summary`: the summary table above.

### M11.2 SSA
Learning objectives (L): "Explain the concept of SSA (Static Single-Assignment) form"; "Explore the basics of converting code to SSA form"; "Explain how to merge values from different paths".
What it teaches
- **SSA**: each variable is defined exactly once (versions a1, a2, b1, c1, c2 …). It is an enhancement of def-use chains, simplifies analyses and optimisations, and is the basis of most compiler IRs.
- **Problem at joins**: if b is defined in both BB2 and BB3, which version does BB4 use? (`c2 = c1 + b?`)
- **φ-function**: merges values from different paths at a join point. Each definition gets a new version and every use takes the latest one. It is implemented at ISA level by moves, select or conditional move. Naively, φ goes at each join (a block with more than one predecessor) for every variable.
- **Conversion example**: BB1 `a1 = 10; b1 = a1 + 20`; BB2 `c1 = b1 + 1; b3 = a1 + 20`; BB3 `a2 = −1; b2 = a2 + 10`; BB4 `b4 = φ(b2, b3); a3 = φ(a1, a2); c2 = φ(c1, c0); c3 = c2 + b4` (c0 is the incoming definition before BB1).
- **When to insert φ**: only where multiple values actually meet. If BB3 had no `a2 = −1`, a3 = φ(a1, a2) would be unnecessary.
- **Path-convergence criterion** (verbatim list): insert φ for a at z when all hold:
  1. a block x contains a definition of a;
  2. a block y ≠ x contains a definition of a;
  3. a nonempty path P_xz from x to z exists;
  4. a nonempty path P_yz from y to z exists;
  5. P_xz and P_yz share no node other than z;
  6. "The node z does not appear within both P_xz and P_yz prior to the end, though it may appear in one or the other."
  Initialisation: "start node has all variable definitions". The criterion is applied iteratively, because inserted φs are themselves definitions.
- **Applying it**: in a variant CFG with BB5 reached from BB2 and BB4, a and b are already merged at BB4. The paths BB1 → BB5 share BB4, so no φ for a or b is needed at BB5. c is redefined, so c = φ(c, c) stays at BB5.
- **φ in LLVM**: `max(a, b)` gives `%retval = phi i32 [%a, %btrue], [%b, %bfalse]` in block `end`. It is lowered to branches or a conditional move depending on the ISA.
Key terms: static single assignment, version, def-use chain, join point, φ-function, path-convergence criterion, iterated criterion, dominance frontier (standard algorithm; not in the lecture), conditional move/select, LLVM `phi`.
**[SIMPLIFIED]** The lecture uses the iterated path-convergence criterion. Production compilers use dominance frontiers (Cytron et al. 1991) to place φs efficiently and pruned/semi-pruned SSA to avoid dead φs. Mention this only with a bib entry. The slides write φ as "∅", which should be φ.
Sources: L M11L2; LLVM LangRef `phi` (if cited).
Figures (lowyx; redraw)
- `m11l2_ssa`: "SSA is an enhancement of the def-use chain. Key feature: variables can be defined only once in SSA form. Common usage: Intermediate Representations (IR) in compilers are typically in SSA form." Diamond CFG before (BB1 a = 10, b = a + 20; BB2 c = b + 1; BB3 a = −1; BB4 c = c + b) and after (a1, b1; c1 = b1 + 1; a2 = −1; c2 = c1 + b1).
- `m11l2_ssa2`: "What if variable bs are defined in both places?" Before/after with `c2 = c1 + b?`.
- `m11l2_phi_func`: the φ bullets (verbatim in the outline above).
- `m11l2_ssa_eg`: three CFGs: original → φ inserted at BB4 (b = φ(b, b); a = φ(a, a); c = φ(c, c); c = c + b) → renamed (as in the conversion example).
- `m11l2_phi_func2`: "When to Insert φ Function?" with `a2 = −1` and `a3 = φ(a1, a2)` struck out; "Iterative path-convergence criterion needs to be considered."
- `m11l2_path_converge`: the six-condition list.
- `m11l2_path_converge2`: "Variable a does not satisfy 2. There is a block y (with y ≠ x) containing a definition of a".
- `m11l2_path_converge3`: the 5-block CFG (BB2 → BB5, BB4 → BB5); φ for b and a struck out at BB5, c = φ(c, c) kept; bullets "From BB #1 to BB#5: Path_1,5 has common path BB #4; Variable a and variable b are merged at BB#4; But variable c is newly defined again".
- `m11l2_llvm`: C `max` and its LLVM IR with `phi` (verbatim above); "Actual Phi function might be implemented with a branch instruction".

### M11.3 Examples of Compiler Optimizations
Learning objectives (L): "Explain the fundamental concepts of compiler optimizations"; "Explore specific optimization techniques, including Loop Unrolling, Function Inlining, and more".
What it teaches
- **Loop unrolling**: `for (i = 0; i < N; i++) S(i);` becomes `for (i = 0; i+4 < N; i += 4) { S(i); S(i+1); S(i+2); S(i+3); }` plus an epilogue `for (; i < N; i++) S(i);`. Benefits: better instruction scheduling, more vectorisation, fewer branches.
- **Function inlining**: `t1 = func1(a)` where func1 calls func2 returning arg*arg becomes `t1 = a*a; t2 = b*b;`. It is inter-procedural and removes stack/call overhead, possibly enabling more optimisation, but it can grow code size.
- **Dead code elimination** (PTX): `mul.f32 c, a, b;` whose result is overwritten before use (`add.f32 c, a, 1.0; div.f32 c, b, 2.0;`) is removed.
- **Constant propagation** (PTX): `mov.f32 a, 5.0; mov.f32 b, 3.0; mul.f32 c, a, b;` becomes `mul.f32 c, 5.0, 3.0;`, which constant folding can then reduce to 15.0. Propagation "often also triggers other optimizations".
- **Strength reduction**: `div.f32 b, a, 2.0` → `mul.f32 b, a, 0.5` (the slide's "divide by 2 → right shift" applies to integers); square via `ex2`-style op → `mul.f32 b, a, a`.
- **Loop-invariant code motion**: `for (…) { cons = 3.14; sum += cons * i; }` becomes `cons = 3.14; for (…) { sum += cons * i; }`, which reduces dynamic instructions. **Induction variable** i controls the loop; its PTX pattern is `add.u32 %r1, %r1, 1`. Induction variables trigger further optimisations (strength reduction, unrolling).
Key terms: loop unrolling, unroll factor, epilogue (remainder) loop, function inlining, inter-procedural analysis, code size, dead code elimination, constant propagation, constant folding, strength reduction, loop-invariant code motion, induction variable.
**[SIMPLIFIED]** (a) The slide `m11l3_sr` labels "divide by 2 → right shift" but shows the float form `div.f32 → mul.f32 by 0.5`. A right shift applies to unsigned and non-negative integers (signed division needs a correction for negatives). (b) `ex2.approx.f32` is 2^x, not a square. The slide's "square → multiplication" example uses the wrong opcode, so present `pow(a, 2)` → `a*a` instead. (c) In DCE, `mul` is dead because c is redefined before any use, which is a liveness argument (link to M11.1).
Sources: L M11L3; CPG §7.39 `#pragma unroll`; PTX ISA (mul, div, ex2).
Figures (lowyx; redraw)
- `m11l3_loop`: before/after unroll code; benefits bullets.
- `m11l3_funcinline`: main/func1/func2 before → `t1 = a*a; t2 = b*b;` after; "Interprocedure analysis; Benefits: reduce the overhead of stack operations; Downside: could increase code size".
- `m11l3_dce`: the PTX `.entry main()` listing with `ld.param`, the dead `mul.f32 c, a, b`, then `add.f32 c, a, 1.0; div.f32 c, b, 2.0; ret;`, and the cleaned version.
- `m11l3_cp`: the PTX listing with `mov.f32 a, 5.0; mov.f32 b, 3.0; mul.f32 c, a, b; add.f32 c, c, 1.0; st.global.f32 [result], c;` → `mul.f32 c, 5.0, 3.0; ...`.
- `m11l3_sr`: the two strength-reduction pairs as printed (see the flag).
- `m11l3_cm`: loop-invariant motion code and "i variable is the loop induction variable; PTX: add.u32 %r1, %r1, 1".

### M11.4 Divergence Analysis
Learning objective (L): "Describe static code analysis techniques to detect warp divergence".
What it teaches
- **Why**: the hardware handles divergence with the SIMT stack (M6.1), but the compiler may need to insert the reconvergence point (IPDOM) statically, so it must know which branches may diverge.
- **History**: divergence analysis predates GPUs. Vectorising loops requires checking that all instructions execute in lockstep, including inside branches. GPUs inherited these vectorisation tests. Simple if-else is easy; complex CFGs plus synchronisation are hard.
- **Thread dependency**: "An expression is thread dependent at a program point p if it may evaluate to different values by different threads at p." Examples: `a = threadIdx; if (a > 4) …` (directly dependent) and `a = threadIdx; c = a % 4; if (c) …` (dependent through c). Both branches may diverge. Thread-ID dependence is the main source of divergent branches.
- **How to check**: follow def-use chains from thread IDs. This is an iterative, data-flow-like reachability analysis: does a thread-ID definition reach the branch condition? Memory-sourced conditions: `a = mem[loc]; if (a) …` diverges only if `loc` itself depends on the thread ID; a uniform `loc` gives a uniform `a`. The output is the set of branches needing reconvergence info.
- **Challenges**: complex CFGs. Over-conservative analysis marks too many branches (even "all loops") as divergent, so compilers must prune non-divergent cases.
Key terms: divergence analysis, warp divergence, thread-dependent (varying) value, uniform value, def-use chain, taint/dependence propagation, reachability, control dependence, vectorisation, lockstep, IPDOM, conservative analysis.
**[SIMPLIFIED]** A sound analysis must also track **control dependence**: a value assigned under a divergent branch becomes varying after the join even if each assignment is uniform (e.g. `b = 1` vs `b = 0` in the lecture's example makes b thread-dependent after the if). The lecture only tracks data dependence. Mention control dependence when writing the concept.
**Exclusion note (Project 5):** Spring 2024's P5 was "Warp Branch Divergence Detection" on traces, and later P5 variants are Python analysis passes. The book explains the concept and the dependence rules with its own examples. No detector algorithm in code or pseudo-code ready to drop into a framework, and no worked solution on trace formats.
Sources: L M11L4; CPG §5.4.2 Control Flow Instructions (verbatim quote in M5.1); PMPP ch10.
Figures (lowyx; redraw)
- `m11l4_db`: "Review: Divergent Branches" bullets ("Within a warp, not all threads need to be executed ... Major differences between SIMD vs. SIMT; Compiler might need to insert reconvergence point, aka: IPDOM (Immediate post dominator)"), the CFG with masks 1111/1100/0011/1111 and the lane-arrow grid.
- `m11l4_td`: the two thread-dependency code examples and the definition bullet (verbatim above).
- `m11l4_check`: "How to Check Thread Dependency?" bullets (def-use chain of thread IDs; iterative search; reachability; `a = mem[loc]; if (a) …`; "Challenges: complex control flow graphs; too conservative analysis: all branches, all loops could be a divergent.").

---

## M12 ML Accelerations On GPUs

Module objective (L, verbatim): "Be able to understand the basic kernels of ML accelerators for GPUs".
Readings (L):
- Required: https://resources.nvidia.com/en-us-tensor-core. This NVIDIA Tensor Core resource hub now redirects to nvidia.com; its whitepaper content corresponds to AWP and HWP.
- Optional: the NVIDIA Deep Learning Performance "Matrix Multiplication Background User's Guide" (GEMM guide); the NVIDIA Ampere architecture whitepaper (AWP).
- Not in the lowyx lists but relevant from Spring 2026: Project 4 "CUDA Programming for ML" (an attention / FlashAttention kernel). Background papers: dao2022flashattention, dao2023flashattention2. See the exclusion note.
Book sections: AWP (Third-Generation Tensor Cores; TF32 and BF16; Fine-Grained Structured Sparsity; Asynchronous Copy; Asynchronous Barrier); HWP (H100 Tensor Core Architecture; Hopper FP8 Data Format; Transformer Engine; Tensor Memory Accelerator; Asynchronous Transaction Barrier); GEMM guide §1–3; CPG §7.24 Warp Matrix Functions; PTX ISA `mma` / `wmma`; PMPP ch16 (deep learning), App. A (numerical considerations); BPG §7.3.

### M12.1 GPU and ML
Learning objectives (L): "Explain the basic operations of machine learning workloads"; "Describe the benefits of GPU for ML workloads".
What it teaches
- **Why GPUs suit ML**:
  - Many FP operations with high data parallelism, and most GPU transistors serve FP throughput.
  - High-bandwidth memory: GPU and memory are directly connected, so HBM is easy to adopt.
  - Flexible formats (tensor formats, BF16, INT4).
  - ML is statistical computing, which fits GPUs' weak memory consistency and lack of precise exceptions; supporting those would cost hardware.
- **DNN operation classes**: element-wise (activations), reductions (pooling, max), dot-product (convolution, GEMM). All are highly data parallel.
- **GEMM**: C = αAB + βC, with A m×k, B k×n, C m×n. α = 1, β = 0 gives C = AB. Used in fully connected and convolution layers.
  - FLOPs: M·N·K FMAs = 2·M·N·K FLOPs.
  - Bytes, FP16 inputs (FP32 accumulate): 2·(MK + NK + MN).
  - **Arithmetic intensity** = 2MNK / (2(MK + NK + MN)). Compare it with the machine's FLOPS/B. This is first-order: it assumes every operand comes from memory, ignoring caches and on-chip reuse.
- **SIMD vs tensor**: a 4×4 matmul with 4 threads, each looping over k: `sum += A[row*N + i] * B[i*N + col]` with the accumulation in the thread's private register, so loops run sequentially per thread. With 16 threads, the sums need a reduction (e.g. through shared memory), adding overhead. A tensor core does it in one instruction, `HMMA.1688.F16`.
- **SIMT matmul cost**: each c_ij = Σ_k a_ik·b_kj needs 4 multiplies and an add tree, so 16 SIMD/SIMT operations for 4×4 versus one tensor operation.
- **Tensor cores**: matrix multiply-accumulate units, hundreds per GPU. Sparsity support raises throughput further. "A100 tensor core can execute 256 of FP16 FMA" per clock. INT8, INT4 and binary 1-bit precisions are added.
- **Systolic arrays** (traditional matmul acceleration):
  - A 4×4 grid of MAC processing elements (PEs). A streams in from the left by rows and B from the top by columns, both **skewed** by one cycle per row or column.
  - Each cycle every PE multiplies its incoming a and b, adds the product to its stationary partial sum (output-stationary), and passes a right and b down.
  - Cycle 1: PE(1,1) computes a11·b11. Cycle 2: a11 moves right to meet b12 at PE(1,2), and PE(1,1) adds a12·b21. And so on.
  - The array is fully busy around cycle 4, and the lecture says about 7 cycles to finish.
- **Transformer Engine** (Hopper): accelerates transformer layers by dynamically scaling tensor data into a representable range, with FP8 support. Just as important is moving data in chunks to keep the tensor cores fed: the **TMA** generates addresses from a copy descriptor.
- Summary (L): SIMD/SIMT can accelerate matmul, dedicated matmul units go further, and keeping memory bandwidth fully used is critical.
Key terms: GEMM, α/β, fully connected layer, convolution layer, element-wise, reduction, dot product, FMA, FLOPs, arithmetic intensity, ops:byte, math-limited, memory-limited, tensor core, MMA, HMMA, warp-level matrix op, systolic array, processing element (PE), output-stationary, skew, fill/drain, Transformer Engine, FP8, TMA, copy descriptor.
**[SIMPLIFIED] / document detail**
- (a) `HMMA.1688.F16` names an **m16n8k8** warp-level MMA shape (PTX: f16 `mma` shapes `.m8n8k4` (PTX 6.4), `.m16n8k8` (6.5), `.m16n8k16` (7.0)), not a 4×4 product. The 4×4×4 figure is the Volta per-tensor-core **datapath** rate. AWP, verbatim: Volta "can execute 64 FP16 fused multiply-add operations (FMAs) with FP32 accumulation per clock, allowing it to compute a mixed-precision 4x4x4 matrix multiplication per clock. Since each Volta SM includes eight Tensor Cores, a single SM delivers 512 FP16 FMA operations per clock" and "Each of the A100 Tensor Cores can execute 256 FP16 FMA operations per clock, allowing it to compute the results for an 8x4x8 mixed-precision matrix multiplication per clock ... each SM in A100 delivers 1024 FP16 FMA operations per clock".
- (b) HWP: "The new fourth-generation Tensor Core architecture in H100 delivers double the raw dense and sparse matrix math throughput per SM, clock-for-clock, compared to A100", with FP8, FP16, BF16, TF32, FP64 and INT8 supported.
- (c) GEMM guide, verbatim: "a total of `2 * M * N * K` FLOPS are required". "Assuming an NVIDIA® V100 GPU and Tensor Core operations on FP16 inputs with FP32 accumulation, the `FLOPS:B` ratio is 138.9 if data is loaded from the GPU's memory." Example: "`M x N x K = 8192 x 128 x 8192` ... the arithmetic intensity is `124.1 FLOPS/B`, lower than V100's `138.9 FLOPS:B`, thus this operation would be memory limited. If we increase the GEMM size to 8192 x 8192 x 8192 arithmetic intensity increases to 2730". Also covers tile quantisation and wave quantisation, and Tensor Core efficiency with dimensions in multiples of 8 for FP16 (on A100, multiples of 64 best).
- (d) Systolic timing for the book (derive explicitly): for an n×n output-stationary array with skewed inputs, the last PE (n,n) receives its last operands at cycle 3n − 2, i.e. 10 for n = 4. The lecture's "about seven" counts differently. State the model you use.
- (e) The slide's AI denominator is printed "MF+NK+MN" (typo for MK + NK + MN).
Numbers (AWP Table 4; HWP Table 3, prelim.):

| | V100 | A100 | H100 SXM5 |
|---|---|---|---|
| Tensor cores/SM | 8 | 4 | 4 |
| FP16 FMA/clk per TC | 64 | 256 | 512 (2× A100 per SM) |
| Peak FP16 tensor TFLOPS (dense / sparse) | 125 | 312 / 624 | 1000 / 2000 |
| Peak TF32 tensor TFLOPS | — | 156 / 312 | 500 / 1000 |
| Peak FP8 tensor TFLOPS | — | — | 2000 / 4000 |
| Peak FP64 tensor TFLOPS | — | 19.5 | 60 |
| Peak INT8 tensor TOPS | — | 624 / 1248 | 2000 / 4000 |
| Peak FP32 (non-tensor) TFLOPS | 15.7 | 19.5 | 60 |

Sources: L M12L1; GEMM guide; AWP; HWP; PTX ISA `mma`; CPG §7.24; PMPP ch16.
Figures (lowyx; redraw)
- `m12l1_gemm`: GEMM bullets (C = αAB + βC; A, B, C are m×k, k×n, m×n; "Popular in fully-connected layers, convolution layers"; "M*N*K fused multiply-adds (FMAs) → 2*M*N*K FLOPS"; "E.g.) FP 16 inputs FP32 accumulator"; Arithmetic Intensity = 2(MNK) / 2(MK + NK + MN); "Use Arithmetic intensity to compare the machine's FLOPS/B").
- `m12l1_tensor`: colour-coded 4×4 A (rows) × B (columns). "4x4 matrix computation; 4 threads and each thread repeats a loop"; the loop code above → "HMMA.1688.F16 / Tensor"; "Sum needs to be stored in a register. Since NVIDIA thread is private, one thread needs to perform accumulation. If 16 threads are performing the work in parallel, the sum variable needs a reduction mechanism."
- `m12l1_simd_matrix`: A(1,1..4) and B(1..4,1) into four multipliers and one adder; C(1,1) = Σ A(1,k)·B(k,1); "16 SIMD/SIMT operations are needed for 4x4 matrix multiplications."
- `m12l1_matrix1`: 4×4 A × B = C with row 1 of A, column 1 of B and c11 highlighted; equations for c11–c14.
- `m12l1_matrix2`: a systolic-array frame. B queues above the 4 columns, skewed (col 1: b11 b21 b31 b41 …; col 4 starts three slots later). A queues left of the 4 rows, skewed (row 1 a11 a12 a13 a14; row 4 three slots later). A 4×4 grid of PEs with right and down arrows. An output grid c11…c44 ("Output names?"). Annotations show partial sums in progress.

### M12.2 Floating Point Formats
Learning objectives (L): "Describe IEEE Floating-point formats"; "Explain the benefits of quantization".
What it teaches
- **FP16 vs FP32**: IEEE single (32-bit) and double (64-bit) serve scientific computing. ML reduces precision because, with the accumulator unchanged, FLOPs stay the same while bytes shrink. FP16 → FP8 halves bytes, which doubles arithmetic intensity. Slide: FP8 inputs + FP32 accumulator give AI = 2MNK / (MK + NK + MN).
- **Quantisation benefits**: less storage, higher arithmetic intensity, and on newer units higher throughput at lower precision (FP8 ≈ 2× FP16). Earlier, quantisation only shrank inputs while FLOPs per cycle stayed the same.
- **FP basics**: 0.0012 = 1.2 × 10^−3 and 0.0000012 = 1.2 × 10^−6 (same fraction, different exponent). In binary the base is 2. Fields: sign | exponent | fraction.
- **Different formats**: total bits = 1 + exponent bits + fraction bits (8, 16, 32, or odd sizes like 19 or 24). More exponent bits give range; more fraction bits give precision.
- **Details**: exponents can be negative or positive (values < 1 or > 1). The sign bit is the value's sign, so the exponent is stored with an **offset (bias)**. Subnormal (denormalised) numbers occur when the exponent field is all zeros.
- **Representation map**: overflow | normal range | (denormal) | underflow | 0 | … on a log scale. Representable values are dense near zero and sparse near the top: precision decreases as magnitude grows.
- **IEEE 754** specifies sign, exponent and fraction layout, special values (±0, ±∞, NaN), denormals, and rounding modes (round up, down, …).
- **Quantisation**: fewer bits mean fewer and cheaper operations. Typically low-precision inputs and a high-precision accumulator. It often leads to non-uniform quantisation, so value transformations are used, e.g. **S2FP8** (shifted and squeezed 8-bit): X_truncated = [2^−β · truncate_FP8(2^β · |X|^α)]^(1/α). This gives more resolution near zero, which matters most in ML.
Key terms: floating point, sign, exponent, bias (offset), fraction/mantissa/significand, normal, subnormal/denormal, underflow, overflow, ±0, ±∞, NaN, rounding mode, IEEE 754, FP64, FP32, FP16, BF16, TF32, FP8 (E4M3, E5M2), FP24, INT8/INT4, quantisation, uniform/non-uniform quantisation, S2FP8, mixed precision, accumulator, dynamic range.
Exact: AWP, verbatim: "BF16 is an alternative to IEEE FP16, and includes an 8-bit exponent, 7-bit mantissa, and 1 sign-bit." TF32: "8-bit exponent (same as FP32), 10-bit mantissa (same precision as FP16) and 1 sign-bit". HWP: "E4M3 with 4 exponent bits, 3 mantissa bits, and 1 sign bit"; "E5M2, with 5 exponent bits, 2 mantissa bits, and 1 sign bit"; "E4M3 supports computations requiring less dynamic range with more precision, while E5M2 provides a wider dynamic range and less precision". HWP also notes "FP8 halves data storage requirements and doubles throughput compared to FP16 or BF16."

Format table for the book (bit counts from the sources above and IEEE 754; derived constants marked):

| Format | Sign/Exp/Frac | Bias | Max normal (derived) | Min normal (derived) |
|---|---|---|---|---|
| FP64 | 1/11/52 | 1023 | ≈1.80 × 10^308 | 2^−1022 |
| FP32 | 1/8/23 | 127 | ≈3.40 × 10^38 | 2^−126 |
| TF32 | 1/8/10 | 127 | ≈3.40 × 10^38 | 2^−126 |
| BF16 | 1/8/7 | 127 | ≈3.39 × 10^38 | 2^−126 |
| FP16 | 1/5/10 | 15 | 65504 | 2^−14 |
| FP8 E5M2 | 1/5/2 | 15 | 57344 | 2^−14 |
| FP8 E4M3 | 1/4/3 | 7 | 448 (OCP/NVIDIA variant; no ∞) | 2^−6 |

(E4M3's 448 and its NaN-only encoding follow the NVIDIA/Arm/Intel FP8 proposal, which is not fetched. Verify against the CUDA `__nv_fp8_e4m3` documentation before printing.)
**[SIMPLIFIED]** (a) The number-line slide uses a toy format with 1/8 spacing for subnormals; state its parameters (e.g. 2 exponent bits and 2 fraction bits) when redrawing. (b) S2FP8 is cambier2020s2fp8 (arXiv 2001.05674; venue reported as ICLR 2020, not verified here). (c) "Rounding modes such as round up and round down" omits the IEEE default, round-to-nearest-even.
Sources: L M12L2; AWP; HWP; BPG §7.3 Numerical Accuracy and Precision; PMPP App. A; cambier2020s2fp8; IEEE 754-2019 (add a bib entry if cited).
Figures (lowyx; redraw)
- `m12l2_mlfp`: the AI bullets (FP16 in / FP32 acc: 2MNK/2(MK+NK+MN); FP8 in: 2MNK/(MK+NK+MN); "Changing the input FP formats can change the arithmetic intensity significantly.").
- `m12l2_floating_basics`: the 1.2 × 10^−3 example and an [s | exp | frac] bar.
- `m12l2_floating_basics_diff`: [s | exp | frac] plus the Wikipedia bfloat16 comparison figure (CC BY-SA 4.0) showing 0.15625 in FP16 (1/5/10), FP32 (1/8/23), bfloat16 (1/8/7), TensorFloat (1/8/10), AMD fp24 (1/7/16), Pixar PXR24 (1/8/15). "Total # of bits = 1 + number of exponent bits + number of fraction bits"; "More exponent bits cover a wider range and more fraction bits cover more precision". Redraw it yourself; the Wikipedia figure is CC BY-SA and would need attribution if reused.
- `m12l2_floating_basics_diff_details`: bias/subnormal bullets and a number line 0–4 with subnormals at 1/8, 2/8, 3/8 and normals 0.5, 0.625, 0.75, 0.875, 1, 1.25, 1.5, 1.75, 2, 2.5, 3, 3.5 (spacing doubles at each power of two).
- `m12l2_floating_rep`: log-scale bands overflow | normal | denormal | underflow | 0 | underflow | denormal | normal | overflow, with a zoom showing representable points spreading out with magnitude.
- `m12l2_quant`: quantisation bullets and the S2FP8 formula.

### M12.3 Tensor Core
Learning objectives (L): "Describe the architecture design methods for ML accelerator components on GPUs"; "Explain the main design criteria".
What it teaches
- **Design questions**: what functionality, what benefit over the existing GPU, how to build the compute units and how many, and how to store and move the data.
- **Common accelerator design steps**:
  1. Identify frequently executed operations (algorithm knowledge or profiling).
  2. Estimate the benefit over the existing data-parallel units (software approaches with existing ISAs vs hardware).
  3. Design the interface: new ISA, data feed, storage format, registers vs memory (private/shared).
  4. Decide whether to merge accelerator components: programmability and usability vs hardware and timing overhead.
- **Matrix-multiply-accumulate unit**: chosen because GEMM dominates ML. SIMD still works row by row. Choices: many small MMA units vs one large one (e.g. a systolic array), weighed against area (taken from other GPU functions) and programmability. NVIDIA started with 4×4. Intel AMX supports 16×16 tiles (lecture). Other vendors have similar units.
- **Unit designs**: a systolic array has fill and drain time, wasteful for small tiles. Option 1: parallel units, 4 FMA units × 16 elements, each computing a row·column. Option 2: pipelining a shared unit (row 1 × col 1, then row 1 × col 2, …, overlapping load, compute and store). Parallel vs pipelined is a throughput/area trade-off.
- **Data storage and movement**: inputs come from memory. Dedicated registers vs shared memory: a 4×4×4 op needs at least 3 × 16 register values, and NVIDIA's thread-private registers complicate it. Using memory close to the unit means moving data from global memory. NVIDIA added an **asynchronous copy** that "loads data directly from global memory into shared memory, optionally bypassing L1 cache, and eliminating the need for intermediate register file (RF) usage", plus **asynchronous barriers**.
- **Sparse operations**: sparse matrices (many zeros) are common in HPC and graph workloads. Software uses compressed formats storing (row, col, value), e.g. (1,3,1), (2,1,2), (3,3,3), (4,2,5) for the 4×4 example. The index overhead motivates simpler formats.
- **Hardware structured sparsity**: pruning raises sparsity. Assume a fixed fraction of non-zeros (50 %), so 16 elements are stored as 8 plus a small index. The toy uses 1 bit per kept value (left/right of a pair): row 1 [0 0 1 0] → [0, 1⟨left⟩]; row 2 [2 0 0 0] → [2⟨left⟩, 0]; row 3 → [0, 3⟨left⟩]; row 4 [0 5 0 0] → [5⟨right⟩, 0]. This simplifies indexing and hardware. SpMV acceleration is an active research topic. Sparsity cuts storage and raises throughput.
- Summary (L): the design trade-offs and steps for ML units on GPUs, GEMM and SpMV.
Key terms: accelerator design, MMA unit, Intel AMX, systolic array, fill/drain, parallel vs pipelined units, operand storage, register pressure, shared memory, asynchronous copy (`cp.async`, `memcpy_async`), asynchronous barrier, TMA, sparse matrix, COO format, CSR (not named in the lecture), pruning, structured sparsity, 2:4 sparsity, metadata index, SpMV.
**[SIMPLIFIED] / document detail**
- (a) AWP, verbatim: "Structure is enforced through a new 2:4 sparse matrix definition that allows two non-zero values in every four-entry vector." "A100 supports 2:4 structured sparsity on rows ... it can be compressed efficiently and reduce memory storage and bandwidth by almost 2x." The lecture's one-bit left/right index is a toy for 1-of-2. For 2:4, each kept value needs a position index within its group of 4; check AWP Fig. 12 / PTX `mma.sp` metadata before stating a bit width. Sparse tensor throughput is quoted as 2× dense (e.g. A100 FP16 312 → 624 TFLOPS).
- (b) Async copy (AWP "Asynchronous Copy"; CPG §7.27–7.28 `memcpy_async` / `cuda::pipeline`) and asynchronous barrier (CPG §7.26). Hopper adds the TMA (CPG §7.29 "Asynchronous Data Copies using Tensor Memory Access (TMA)"; HWP "A single thread creates a copy descriptor before ...") and the asynchronous transaction barrier.
- (c) "NVIDIA started with the 4 by 4 matrix multiplication unit" refers to Volta's per-tensor-core 4×4×4 per clock (AWP quote in M12.1).
- (d) The Intel AMX "16×16" claim is from the lecture and has not been verified in this pass. AMX tiles are 16 rows × 64 bytes; check Intel's documentation before printing.
**Exclusion note (Project 4):** from Spring 2026, Project 4 implements an attention kernel targeting FlashAttention. The book may present attention, softmax, the IO complexity argument and the tiling idea at the level of dao2022flashattention (abstract: "an IO-aware exact attention algorithm that uses tiling to reduce the number of memory reads/writes between GPU high bandwidth memory (HBM) and GPU on-chip SRAM") and dao2023flashattention2 (better work partitioning across thread blocks and warps, "reaching 50-73% of the theoretical maximum FLOPs/s on A100"). **No CUDA attention kernel, no tiling or loop-nest recipe, no online-softmax implementation code, and no performance targets.**
Sources: L M12L3; AWP; HWP; CPG §7.24–7.29; PMPP ch14 (sparse formats), ch16; dao2022flashattention; dao2023flashattention2.
Figures (lowyx; redraw)
- `m12l3_matrix`: the dot-product datapath with "X 16"; "Option 1: Parallel Units 4 FMA units x 16 elements"; "Option 2: Pipelining with future FMA units", with staggered Load | Comp | Store rows for (row 1 × col 1), (row 1 × col 2), (row 1 × col 3).
- `m12l3_storage`: the storage bullets (verbatim above).
- `m12l3_sparse`: the 4×4 matrix [[0,0,1,0],[2,0,0,0],[0,0,3,0],[0,5,0,0]] with COO triples (1,3,1) (2,1,2) (3,3,3) (4,2,5); "With pruning operations, sparsity increases".
- `m12l3_sparse2`: "Structured sparsity: assume only a fixed % of elements are non-zeros. E.g.) Assumption of 50% sparsity (use 1 bit to indicate left or right position)". The 4×4 matrix → the 4×2 compressed matrix above; "Accelerating SpMV (Sparse Matrix-Vector Multiplication) is a big research topic."

---

## Appendix A: assigned papers. What the lecture takes, key numbers, full-text status

| Key | Module | Lecture takes | Key numbers (verbatim from the paper unless noted) | Full text read? |
|---|---|---|---|---|
| fung2007dwf | M6.1 | The SIMT stack with IPDOM reconvergence; dynamic warp formation | DWF +20.7 % at 4.7 % area; IPDOM reconvergence 93.4 % over no reconvergence | yes |
| narasiman2011twolevel | M6.1, M7.3 | Large warps; two-level round-robin over fetch groups | +19.1 % combined; e.g. 32 warps in 4 fetch groups of 8 | yes |
| jeon2015rfv | M6.2 | Register virtualisation: small physical RF, name-space mapping | not verified (ACM DL blocked automated access) | **no** |
| gebhart2011energy | M6.2, M7.3 | Read-once values; RF cache; two-level active/pending scheduler (energy) | Up to 70 % of values read once; 6-entry RFC cuts MRF reads/writes 50 %/59 %; 4× fewer active threads gives −36 % RF energy | yes |
| gebhart2011compile | M6.2 (opt.) | Compiler-managed ORF + LRF hierarchy | RF energy −54 % vs −34 % for hardware-only caching; RF = 15–20 % of dynamic energy | yes (abstract, intro) |
| gebhart2012unifying | M6.3 | Unified RF / scratchpad / L1 pool, partitioned per application | Up to 71 % performance, up to 33 % energy; prior techniques cut MRF accesses by 60 % | yes |
| power2014x86 | M7.1 | Coalescer-filtered per-CU TLBs; shared highly-threaded PTW; page walk cache | 6.8× fewer translations; bursts of 60 misses; 29 % post-coalescer miss rate; < 2 % overhead vs ideal MMU | yes |
| ausavarungnirun2017mosaic | M7.1 (opt.) | Multiple page sizes (CoCoA, In-Place Coalescer, CAC) | +55.5 % / +29.7 % (homogeneous / heterogeneous multi-app); within 6.8 % / 15.4 % of ideal TLB | yes (abstract, intro) |
| li2021tlb | M7.1 (opt.) | least-TLB for multi-GPU (least-inclusive, peer sharing, IOMMU TLB spilling) | +23.5 % (single-app), +16.3 % (multi-app) | yes (abstract, intro) |
| ganguly2019interplay | M7.2 (opt.) | Tree-based neighbourhood prefetcher semantics; prefetch-aware pre-eviction | TBNp prefetch 64 KB–1 MB via the >50 % rule; +93 % / +18.5 % vs LRU 4 KB / 2 MB | yes (abstract, §3) |
| kim2020batch | M7.2 (opt.) | Batched fault handling; thread-block context switching; overlapping eviction | Fault latency 20–50 µs (prior work); batch 223–553 µs (median 313); 2× speed-up; batch size ×2.27; −51 % batches; −27 % batch time | yes (abstract, §2–3) |
| rogers2012ccws | M7.3 | GTO/LRR definitions; adaptive warp throttling with a lost-locality detector | −25 % L1D misses; +24 % HM over prior schedulers (+63 % over greedy); 0.17 % area | yes |
| jog2013orchestrated | M7.3 (opt.) | Prefetch-aware scheduling: separate consecutive warps in time | +25 % vs RR + prefetch; +7 % vs two-level + prefetch (30-core sim.) | yes (abstract) |
| jog2013owl | M7.3 (opt.) | CTA-aware two-level, locality-aware, bank-level-parallelism-aware scheduling + opportunistic prefetch | +33 % vs RR (28-core sim.); 19 of 38 apps idle 62 % of cycles | yes (abstract, intro) |
| liu2023photon | M8.4 | Kernel/warp/basic-block sampling with online analysis | ResNet-152 inference: 7.05 days → 1.7 h at 10.7 % error | yes (abstract) |
| williams2009roofline | M8.3 | min(peak FLOPS, BW × operational intensity) | formula (TR version) | yes (TR) |
| hong2009analytical | M8.3 (opt.) | MWP/CWP model | 5.4 % / 13.3 % GM error; equations in M8.3 | yes |
| huang2014gpumech | M8.3 (opt.) | Interval analysis for GPUs; CPI stacks | 13.2 % (RR) / 14.0 % (GTO) error; 97× faster than simulation | yes (abstract) |
| karkhanis2004firstorder | M8.3 (opt.) | First-order interval model with drain/refill | 5.8 % avg / 13 % worst (search summary only) | **no** (only open copy on typeset.io, which blocked) |
| arunkumar2017mcmgpu | M9.1 | 4-GPM MCM-GPU; L1.5 cache, distributed CTA scheduling, first-touch | +22.8 % and 5× less inter-GPM BW vs basic MCM; +45.5 % vs largest monolithic; within 10 % of unbuildable monolithic; +26.8 % vs multi-GPU | yes |
| yu2022multitenant, ye2024dlsched | M9.2 (opt.) | Surveys (multi-tenant inference; DL cluster scheduling) | — | abstract only |
| dao2022flashattention, dao2023flashattention2 | M12 / P4 background | IO-aware tiled exact attention; better work partitioning | FA2: about 2× FA, 50–73 % of peak FLOPs on A100 | yes (abstracts) |
| cambier2020s2fp8 | M12.2 | Shifted and squeezed FP8 transformation (named on the slide) | formula on slide | metadata only |

---

## Appendix B: margin-number index (each with its source; "prelim." = HWP V1.02 preliminary)

| Number | Value | Source | Used in |
|---|---|---|---|
| Warp size | 32 threads (CC 5.0–9.0) | CPG Table 21 | M1.4, M3.2 |
| Max threads per block | 1024 | CPG Table 21 | M3.1 |
| Block dims | x, y ≤ 1024; z ≤ 64 | CPG Table 21 | M3.1 |
| Grid dims | x ≤ 2^31−1; y, z ≤ 65535 | CPG Table 21 | M3.1 |
| Max warps / SM | 64 (7.0, 8.0, 9.0); 48 (8.6, 8.9); 32 (7.5) | CPG Table 21; HWP Table 4 | M3.2 |
| Max threads / SM | 2048 / 1536 / 1024 | CPG Table 21 | M3.2 |
| Max blocks / SM | 32 (7.0, 8.0, 9.0); 16 (7.5, 8.6) | CPG Table 21; HWP Table 4 | M3.2 |
| Registers / SM | 65,536 × 32-bit = 256 KB | CPG Table 21; AWP; HWP | M3.2, M6.2 |
| Max registers / thread | 255 | CPG Table 21 | M3.2 |
| Shared memory banks | 32 banks × 32 bit per clock | BPG §10.2.3.1 | M4.2 |
| Max shared / SM | 96 KB (V100), 164 KB (A100), 100 KB (8.6), 228 KB (H100) | CPG Table 21 / CC sections | M3.2, M6.3 |
| L1 + shared / SM | 128 KB (V100), 96 KB (Turing), 192 KB (A100), 128 KB (8.6), 256 KB (H100) | CPG CC sections; AWP; HWP | M6.3 |
| Constant memory | 64 KB (8 KB per-SM cache working set) | CPG Table 21 | M3.1 |
| Local memory / thread | 512 KB max | CPG Table 21 | M3.1, M11.1 |
| Coalescing granularity | 32-byte transactions (CC ≥ 6.0) | BPG §10.2.1 | M4.4, M8.2 |
| Memory transactions | 32, 64, 128 B, naturally aligned | CPG §5.3.2 | M4.4 |
| Shared vs uncached global latency | ~100× lower | harris2013sharedmem | M4.2 |
| Tesla/Fermi latencies | shared 4–32 cycles; global 100s of cycles; constant/texture hit 4 cycles | K12 Table 1.4 | M3.1, M4.2 |
| G80 SM | 8 lanes (warp in 4 cycles); 16 KB shared; RF 32 KB or 64 KB (K12 inconsistent) | K12 §1.2.1, §1.4.1 | M1.4, M4.3 |
| Fermi RF | 128 KB / SM, 2 MB total | K12 §1.4.1 | M4.2 |
| RF read bandwidth example | 1 TFLOP/s × 2 reads × … = 64 TB/s | K12 §1.4.1 | M4.2 |
| SMs | P100 56, V100 80, A100 108, H100 SXM5 132 (PCIe 114) | AWP Table 4; HWP Table 3 | M1.5 |
| FP32 cores / SM | 64 (P100, V100, A100); 128 (H100) | AWP; HWP | M1.5 |
| Tensor cores / SM | 8 (V100), 4 (A100, H100) | AWP; HWP | M12.1 |
| FP16 FMA / clk / TC | 64 (V100, 4×4×4), 256 (A100, 8×4×8), 2× A100 per SM (H100) | AWP; HWP | M12.1 |
| FP16 tensor TFLOPS | 125 (V100); 312 / 624 sparse (A100); 1000 / 2000 (H100 prelim.) | AWP; HWP | M12.1 |
| FP8 tensor TFLOPS | 2000 / 4000 (H100 prelim.) | HWP Table 3 | M12.1 |
| HBM bandwidth | 720 GB/s (P100), 900 (V100; 898 computed), 1555 (A100 40 GB), 3000 (H100 SXM5 prelim.) | AWP; BPG §9.2.1; HWP | M4.4, M9.1 |
| L2 | 4 MB (P100), 6 MB (V100), 40 MB (A100), 50 MB (H100) | AWP; HWP | M1.5 |
| Transistors | 15.3 B, 21.1 B, 54.2 B, 80 B | AWP; HWP | M1.5 |
| TDP | 300 W (P100, V100), 400 W (A100), 700 W (H100 SXM5 prelim.) | AWP; HWP | M1.5 |
| V100 ops:byte | 138.9 FLOPS/B | GEMM guide | M8.3, M12.1 |
| NVLink per GPU | 900 GB/s, 18 links (gen 4, Hopper); 1.8 TB/s (gen 5); 3 TB/s, 36 links (gen 6) | nvidia.com NVLink | M9.1 |
| NVLink vs PCIe | NVLink 4 = 7× PCIe Gen 5 | HWP | M5.1, M9.1 |
| PCIe (2012) | Gen 2 "4 Gbit/s", Gen 3 "8 Gbit/s" (per lane) | K12 §1.2 | M1.1 |
| MIG instances | up to 7 (A100, H100) | AWP; HWP | M9.2 |
| MPS clients | 60 per device (current docs); slide says 48 | MPS overview | M9.2 |
| Thread block cluster | up to 16 blocks (H100) | HWP Table 4 | M3.1, M5.1 |
| UVM fault latency | 20–50 µs (prior work); batch 223–553 µs | kim2020batch | M7.2 |
| TBNp prefetch size | 64 KB to 1 MB within a 2 MB region | ganguly2019interplay | M7.2 |
| GPU MMU | 6.8× fewer translations; 60 concurrent misses; 29 % miss rate; < 2 % overhead | power2014x86 | M7.1 |
| Large page | 2 MB / 4 KB = 512× TLB reach | lecture slide; arithmetic | M7.1 |
| Read-once register values | up to 70 % | gebhart2011energy | M6.2 |
| Simulation speed | 10^9 instr at 1 KIPS = 10^6 s (the slide's 28 h needs 10 KIPS) | arithmetic | M8.4 |
| Photon | 7.05 days → 1.7 h, 10.7 % error | liu2023photon | M8.4 |
| CCWS | −25 % L1D misses, +24 % HM | rogers2012ccws | M7.3 |

## Appendix C: slide and transcript errata found (fix silently when redrawing; never reproduce)

- M2.3: `#pragma omp atomic counter++;` is on one line; the statement must go on the next line.
- M3.1: kernel listing `__global` (missing underscores) and a missing `;`; `prinf`, `threaddx.x` on the SPMD slides; `__synchthreads()` (sic, also M7.3); `<<<1 ,1,>>>` (stray comma).
- M3.2: the transcript's "641,024/6432" means (64 × 1024)/(64 × 32); "64 kilobyte of register files" means 64 K registers.
- M4.2: `m4l2_variable` Case 2 is mislabelled (Th5 column, no Th6).
- M4.3: `sub r2, r,2,1` should be `sub r2, r2, 1`; R2 for Th1–Th4 shown as 3 in later frames (should stay 2); in scoreboard9, w3 lane 1 is shown ready despite mask 0111.
- M4.4 / M7.1 / M8.2: R1 addresses 0 4 8 12 16 **18** 20 24 (should be consecutive words); R2 jumps 256 → 512; the 1152 row is mapped to page 0x05 (it is 0x04); 7 vs 8 requests between slides; sector slide "Mem [102-1027]" should be [1024-1027].
- M6.1: gpuflow tables give BB2 mask 1110 (CFG says 1100); `m6l1_divb` misses the Work-2 → BB4 edge.
- M7.1: index-bit arithmetic ("12 bits", "51 → 42 bits") should be re-derived (48-bit VA, 9-bit indices, 12- or 21-bit offsets).
- M7.2: fault latency appears as both "tens of milliseconds" and "several tens of microseconds" (microseconds is right); page numbering in `m7l2_preteching` is inconsistent with 512 B pages; `A[0x[700]`.
- M7.3: "Isnt2/Isnt3" in the dynamic trace.
- M8.3: W_depth erratum (at least 20 PC registers) from the course's Canvas page; dot-product "2 bytes" assumes 1-byte elements.
- M8.4: "28 hours at 1 KIPS for 10^9 instructions" is 10× off.
- M10.2: "all func;" should be `call func;`.
- M10.3: label `Is_smaller` vs `is_smaller`.
- M10.4: composition slide "gen_u" should be gen_n; "∪-".
- M10.5: B1 OUT¹ printed "111 000"; transcript OUT[B4] "001 01111".
- M11.2: φ drawn as "∅".
- M11.3: strength-reduction slide shows `div.f32 → mul.f32 0.5` under "right shift"; `ex2.approx.f32` is 2^x, not square.
- M12.1/12.2: AI denominator "MF+NK+MN" should be MK + NK + MN; "NVIDA".
- M12.2: "19" among total bit widths; the PXR24 row of the borrowed Wikipedia figure (bits illegible).
- Module objectives: M2 copies M1, M5 copies M4, M7 copies M6, and M10/M11 are placeholders.
