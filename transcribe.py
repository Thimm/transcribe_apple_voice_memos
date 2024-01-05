import sys
import subprocess
from pathlib import Path

WHISPER_MODEL_PATH = "~/whisper.cpp/models/ggml-large-v3.bin"
WHISPER_EXECUTABLE_PATH = "~/whisper.cpp/main"


class SubprocessError(Exception):
    pass


def run_subprocess(cmd, error_msg, shell=False):
    process = subprocess.run(cmd, capture_output=True, shell=shell)
    if process.returncode != 0:
        raise SubprocessError(f"{error_msg[:200]}: {process.stderr.decode()[:200]}")
    return process.stdout.decode()


def convert_to_wav(input_file):
    temp_file_path = Path("/tmp") / f"{input_file.stem}.wav"
    cmd = [
        "/opt/homebrew/bin/ffmpeg",
        "-i",
        str(input_file),
        "-acodec",
        "pcm_s16le",
        "-ar",
        "16000",
        "-y",
        str(temp_file_path),
    ]
    run_subprocess(cmd, "ffmpeg failed")
    return temp_file_path


def transcribe(wav_file):
    whisper_executable = Path(WHISPER_EXECUTABLE_PATH).expanduser()
    model_path = Path(WHISPER_MODEL_PATH).expanduser()
    cmd = [
        str(whisper_executable),
        "--no-timestamps ",
        "-m",
        str(model_path),
        "-l",
        "auto",
        "-f",
        f'"{str(wav_file)}"',
    ]
    transcript = run_subprocess(" ".join(cmd), "whisper failed", shell=True)
    return transcript


def summarize(transcript_txt):
    prompt = "Write a concise summary of the text, return your responses with 5 lines that cover the key points of the text."
    llm_input = f"{prompt}\n```{transcript_txt}```\SUMMARY:"

    cmd = ["/usr/local/bin/ollama", "run", "llama2:13b-chat", llm_input]
    summary = run_subprocess(cmd, "ollama failed")
    return summary


def style_markdown(transcript, summary):
    markdown = f"""# Summary
{summary.strip()} 

# Transcript
{transcript.strip()}
"""
    return markdown


def main(input_file_path, output_folder_path):
    output_folder_path.mkdir(parents=True, exist_ok=True)
    wav_file_path = convert_to_wav(input_file_path)
    transcript_txt = transcribe(wav_file_path)
    summary_txt = summarize(transcript_txt)
    markdown = style_markdown(transcript_txt, summary_txt)
    output_file_path = output_folder_path / f"{input_file_path.stem.split('-')[0]}.md"
    output_file_path.write_text(markdown)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python transcribe.py [input file] [output folder]")
        sys.exit(1)
    main(Path(sys.argv[1]), Path(sys.argv[2]))
