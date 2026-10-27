#!/bin/sh
# Transcribe an audio file locally with OpenAI's Whisper (large-v3-turbo) through mlx-whisper on Apple silicon.
# Needs: Apple silicon Mac, ffmpeg (brew install ffmpeg), Python 3.
python3 -m venv .venv && . .venv/bin/activate
pip install mlx-whisper
mlx_whisper "$1" --model mlx-community/whisper-large-v3-turbo --language en --output-format txt --condition-on-previous-text False
