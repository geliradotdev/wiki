import requests
import subprocess
import tempfile
import os
import json
import shlex

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2:1b"

PIPER_BIN = "/opt/piper/piper/piper"
PIPER_MODEL = "/opt/piper/voices/en_US-lessac-medium/en_US-lessac-medium.onnx"
ALSA_DEVICE = "plughw:1,0"

ALLOWED_COMMANDS = {
    "ls", "pwd", "whoami", "date", "uptime",
    "cat", "echo", "grep", "find", "ping"
}

MAX_ARGS = 10


def ask_ollama(prompt):
    r = requests.post(OLLAMA_URL, json={
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    })
    r.raise_for_status()
    return r.json()["response"]


def run_shell(cmd):
    parts = shlex.split(cmd)

    if not parts:
        return "empty command"

    base = parts[0]
    if base not in ALLOWED_COMMANDS:
        return "blocked: command not allowed"

    if len(parts) > MAX_ARGS:
        return "blocked: too many arguments"

    try:
        result = subprocess.run(
            parts,
            shell=False,
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.stdout + result.stderr
    except Exception as e:
        return f"error: {str(e)}"


def speak(text):
    wav_path = tempfile.mktemp(suffix=".wav")
    try:
        subprocess.run(
            [PIPER_BIN, "--model", PIPER_MODEL, "--output_file", wav_path],
            input=text,
            text=True,
            check=True
        )
        subprocess.run(
            ["aplay", "-D", ALSA_DEVICE, wav_path],
            check=True
        )
    finally:
        if os.path.exists(wav_path):
            os.remove(wav_path)


def parse_reply(reply):
    try:
        return json.loads(reply)
    except:
        return {"type": "text", "text": reply}

def extract_cmd(text):
    try:
        data = json.loads(text)
        if isinstance(data, dict) and "cmd" in data:
            return data["cmd"], True
        if isinstance(data, dict):
            return data.get("text", ""), False
    except:
        pass

    return text, False


def main():
    while True:
        user = input("You: ").strip()
        if user in {"exit", "quit"}:
            break

        prompt = f"""
You are a senior IT support assistant and personal assistant.

You may either:
1. Output a Linux command if needed
2. Or answer normally

If using a command, respond EXACTLY like:
{{"cmd":"<command>"}}

Otherwise respond normally as plain text.

User: {user}
"""

        reply = ask_ollama(prompt).strip()
        content, is_cmd = extract_cmd(reply)

        if is_cmd:
            print(f"[CMD] {content}")
            output = run_shell(content)
            print(output)
            speak(output)
        else:
            print(content)
            speak(content)

if __name__ == "__main__":
    main()
