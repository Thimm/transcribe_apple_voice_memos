# Transcribe voice messages to text
## Intention
Every time I go on a walk, I'm recording voice messages to myself. It would be great if I could have these voice messages on my computer as text files so I can search through them and use them in my notes keeping app Obsidian. For that I've created this small little project that uses Automator to run a script that transcibes and summarized the voice message and then saves it to a text file.

## How it works
I record a message on either my phone or my computer. The message is a m4a file and is synced to my computer via iCloud. The file is saved in the folder `~/Library/Group Containers/group.com.apple.VoiceMemos.shared/Recordings/`.
The script is triggered by a folder action. And this folder action is running a script that calls a python script that takes the voice message, converts it to a wav file, transcribes it, summarizes it with ollama and saves it to a text file.


## Restrictions
- Only works on macOS
- Tested only on MacBook Pro (M3)


## Installation
1. Install ffmpeg `brew install ffmpeg`
2. Install [oolama](https://ollama.ai/download/Ollama-darwin.zip)
3. Install whisper.cpp by following the instructions in the [Readme for Core ML support]((https://github.com/ggerganov/whisper.cpp?tab=readme-ov-file#core-ml-support))
4. Allow terminal to access voice memos folder, otherwise the Terminal is not allowed to access the voice memos folder and the script will not work.
  - Open System Preferences
  - Select Security & Privacy
  - Select Privacy
  - Select Files and Folders
  - Select Terminal
5. Add Automator folder action.
  - Open Automator
  - File > Open > Select the file `Transcribe.workflow` in this repo
  - Save the workflow
6. Setup the folder so that it runs the script
  - Open `~/Library/Group Containers/group.com.apple.VoiceMemos.shared/` in Finder.
  - Right click on the folder `Recordings` and select `Services > Folder Actions Setup`
  - Select the workflow `Transcribe`
  - Confirm Service and select "Transcribe" again

> [!IMPORTANT]  
> Now all your voice memos will be transcribe locally.

