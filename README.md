# Transcribe voice messages to text

## Overview
This project automates the transcription and summarization of voice memos into text files. It's designed for people like me who record voice memos while walking and wish to integrate these recordings into a note-keeping app like Obsidian. The solution uses macOS's Automator to execute a script that processes these voice memos, leveraging technologies like ffmpeg, ollama, and whisper.cpp.

## Functionality
Voice memos, recorded on either a phone or computer in m4a format, are synced to a macOS computer via iCloud. These files are located in ~/Library/Group Containers/group.com.apple.VoiceMemos.shared/Recordings/. A folder action triggers a Python script which:

1. Converts the m4a file to wav format.
2. ranscribes the audio.
3. .Summarizes the content using ollama.
4. Saves the output as a text file.

## Limitations
- Compatibility: Exclusively for macOS.
- Testing: Confirmed functionality on MacBook Pro (M3).


## Setup Guide
- ffmpeg Installation: Run `brew install ffmpeg`.
- Ollama Installation: Download from [Ollama](https://ollama.ai/download/Ollama-darwin.zip).
- Whisper.cpp Installation: Follow the [Readme for Core ML support]((https://github.com/ggerganov/whisper.cpp?tab=readme-ov-file#core-ml-support).
- Terminal Access Configuration:
  - Navigate to System Preferences > Security & Privacy > Privacy.
  - Go to Files and Folders.
  - Grant Terminal access to the voice memos folder.
- Automator Folder Action:
  - Open Automator, select File > Open, and choose Transcribe.workflow from this repo.
  - Save the workflow.
- Script Activation:
  - Go to ~/Library/Group Containers/group.com.apple.VoiceMemos.shared/.
  - Right-click Recordings, select Services > Folder Actions Setup.
  - Choose and confirm the Transcribe workflow.


**Now all your voice memos will be transcribed locally.**

