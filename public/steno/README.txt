Real test, 26 Oct 2026, M5 Max 64 GB, mlx-whisper 0.4.3, mlx-community/whisper-large-v3-turbo.
Audio: LibriVox "Alice's Adventures in Wonderland" chapters 1-4 (public domain), 60 min 33 s.
Wall time of the whole CLI run: 28.9 s, then 28.27 s and 28.18 s (timings.txt). ~128x real time.
Word error rate vs the Project Gutenberg text: 4.16% (wer.txt); part of that is LibriVox announcements, contractions and punctuation style, not mishearings.
Claude Haiku summary: haiku-summary.json (5.6 s, $0.007 API-equivalent).
First run also downloads the model weights. Speed depends on your Mac.
