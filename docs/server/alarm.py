import subprocess
import tempfile
import os
import requests

OLLAMA_URL = "http://ollama:11434/api/generate"
MODEL = "llama3.2:1b"

PIPER_BIN = "/programs/piper/piper/piper"
PIPER_MODEL = "/programs/piper/voices/en_US-lessac-medium.onnx"
ALSA_DEVICE = "plughw:1,0"


def ask_ollama(prompt):
    r = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False,
            "temperature": 0.9
        },
        timeout=30
    )
    return r.json()["response"].strip()


def speak(text):
    tmp = None
    try:
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
            tmp = f.name

        subprocess.run(
            [PIPER_BIN, "--model", PIPER_MODEL, "--output_file", tmp],
            input=text,
            text=True,
            check=True
        )

        subprocess.run(["aplay", "-D", ALSA_DEVICE, tmp], check=True)

    finally:
        if tmp and os.path.exists(tmp):
            os.remove(tmp)


def get_system_datetime():
    result = subprocess.run(
        ["date", "+%Y-%m-%d %H:%M:%S"],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()


def main():
    system_time = get_system_datetime()

    print("System datetime:", system_time)

    prompt = (
            "Output EXACTLY 3 lines:\n"
            "Line 1 must be a natural sentence stating today's system date and time including hours, minutes, and seconds.\n"
            "Line 2 must be an original Stoic-style quote (no labels, no prefixes).\n"
            "Line 3 must be a randomly generated short Stoic story (3–5 sentences, grounded, philosophical, original, no labels).\n\n"
            "Rules:\n"
            "- No extra text\n"
            "- No explanations\n"
            "- No formatting\n"
            "- No translation\n\n"
            f"System time: {system_time}"
        )

    response = ask_ollama(prompt)

    print(response)
    speak(response)


if __name__ == "__main__":
    main()
