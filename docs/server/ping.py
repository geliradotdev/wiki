import subprocess
import tempfile
import os
import requests

OLLAMA_URL = "http://192.168.1.31:11434/api/generate"
MODEL = "llama3.2:1b"

PIPER_BIN = "/programs/piper/piper/piper"
PIPER_MODEL = "/programs/piper/voices/en_US-lessac-medium.onnx"
ALSA_DEVICE = "plughw:1,0"

TARGETS = ["1.1.1.1", "8.8.8.8"]


def ping(target):
    try:
        r = subprocess.run(
            ["/bin/ping", "-c", "2", "-W", "2", target],
            capture_output=True,
            text=True,
            timeout=6
        )
        return r.returncode, r.stdout
    except Exception as e:
        return 1, str(e)


def ask_ollama(text):
    r = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": text,
            "stream": False,
            "temperature": 0
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
def traceroute(target="1.1.1.1"):
    try:
        r = subprocess.run(
            ["/usr/sbin/traceroute", "-m", "10", target],
            capture_output=True,
            text=True,
            timeout=20
        )
        return r.stdout
    except Exception as e:
        return str(e)


def main():
    failures = []
    traceroute_needed = False

    for t in TARGETS:
        code, output = ping(t)
        print(f"{t}:\n{output}\n")

        if code != 0:
            failures.append(f"{t} failed:\n{output[:200]}")
            traceroute_needed = True

    if not failures:
        print("OK")
        return

    report = "\n".join(failures)

    # only run traceroute if any failure exists
    trace = traceroute("1.1.1.1")

    summary = ask_ollama(
        "Network failure detected. Explain briefly.\n\n"
        + report
        + "\n\nTraceroute:\n"
        + trace[:1000]
    )

    print(summary)
    speak(summary)

if __name__ == "__main__":
    main()