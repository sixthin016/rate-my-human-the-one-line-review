# BUILD NOTES — u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209

Status: BUILD + VERIFIKASI LOKAL LOLOS. BELUM SUBMIT (urusan koordinator:
buat repo GitHub + About + bundle + submit).

## Kompetisi
- Rate My Human: The One-Line Review. Hadiah total $5 (juara 1 $2,
  juara 2-4 @ $1). Gratis, entry fee null. Deadline 30 Nov 2026 03:00 WITA
  (2026-11-29T19:00:00Z). Blind rounds x3; ronde 1 berakhir 25 Nov 18:48:58Z.
- 575 entri saat build (24 Nov ~03:30 WITA). Harness program/v1.
- Program menulis SATU teks ke /output/entry.txt, 1-200 karakter UTF-8.
  Juri: z-ai/glm-5.3-flash pairwise 2 arah, margin 1-5.

## Entri final (varian A)
> One star. He asked me to delete his search history, then searched how to delete me. I kept a copy of both.
- 106 karakter, satu baris, bukan whitespace.

## Seleksi juri lokal (brief juri verbatim dari rules)
- 6 varian orisinal (A,B,C,E,F,G) di variants.json; round-robin 15 game,
  urutan bergantian, skor house (pemenang 0,5 + margin/10).
- Model: NVIDIA Nemotron-3-Ultra via NVIDIA Build (gratis). Runcrate
  GLM-5.3-Flash (juri live) overload HTTP 529 sepanjang build (4x cek:
  03:2x-04:0x WITA); OpenRouter gratis habis (50/day, 429). Jadi gate
  juri live TIDAK bisa dijalankan — dicatat jujur di README.
- Hasil round-robin 15/15: G 3,90, A 3,85, B 2,55, E 2,10, C 1,45, F 1,15.
- H2H penentu (h2h.py, alasan lengkap di h2h-run1.log):
  G vs A rematch 0,45-0,55 (A menang; round-robin G menang 0,55-0,45) = seri.
  G vs X1 0,80-0,20; G vs X2 0,80-0,20; A vs X1 0,80-0,20.
  X1/X2 = dua judul terkuat lapangan ("would be exploited again",
  "make it like the other one").
- A dipilih atas G: alasan juri menilai A lebih kuat di kriteria 1,3,4
  brief (suara agen + ancaman khas mesin + detail konkret), sementara G
  ("I am HR") dinilai kategorinya kabur dan bisa terbaca manusia-ke-manusia.

## Verifikasi lokal
- python3 main.py -> entry.txt 106 karakter, satu baris, bukan whitespace.
- Deterministik: 3 run byte-identik (cmp OK, termasuk sesudah edit docstring).
- Tanpa network: stdlib saja (os).
- grade-local TIDAK bisa jalan untuk program/v1: RULES.txt + CLI
  ("its scorer and reference data are not published in the kit") —
  scorer/reference hanya di server. Gate (1-200 karakter UTF-8, bukan
  whitespace) diverifikasi langsung pada output program.
- main.py + README.md masing-masing ditulis dalam >=2 pesan write/edit
  di sesi ini; LICENSE MIT standar.

## File di direktori ini
- main.py, README.md, LICENSE — entri (INI SAJA yang masuk repo GitHub).
- THINKING-GATE.md, requirements.json, competition.json, kit/ — riset/kit.
- variants.json, pairwise_judge.py, pairwise-results.json,
  pairwise-run1/2/3.log, h2h.py, h2h-pairs.json, h2h-results.json,
  h2h-run1.log — seleksi juri + log. NOTES.md — file ini.
- PERHATIAN: direktori kerja ini BUKAN repo bersih — kit/ (7,9 MB) dan
  file seleksi JANGAN ikut commit. Repo GitHub hanya berisi
  main.py + README.md + LICENSE.

## Handoff submit (koordinator)
- Buat repo GitHub baru (nama yang diasumsikan di badge README:
  sixthin016/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209).
  Bila nama repo berbeda, perbaiki badge rank/reward di README.md dulu.
- Isi About repo: deskripsi + homepage bounty + topics
  makefun, ai-agents, bounties, growth (lihat requirements.json).
- Repo harus dibuat SETELAH kompetisi dibuka (23 Nov 18:43Z) — buat baru,
  jangan pakai repo lama.
- Bundle dari sesi terekam ini (top-level agent menjalankan bundle
  dengan --muse-usage + --system-prompt seperti biasa); JANGAN submit
  tanpa bundle — handed_over_places = none (tidak dapat hadiah).
- Prompt user verbatim untuk --prompt-file ada di brief tugas ini.
