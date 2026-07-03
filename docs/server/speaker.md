


# OLLAMA TO SPEAK
apt install -y python3 python3-pip alsa-utils curl
pip install requests



apt install -y python3-venv python3-full
python3 -m venv /opt/ollama-voice

/opt/ollama-voice/bin/python voice.py   


/opt/ollama-voice/bin/python tools.py

/opt/ollama-voice/bin/python  ping.py

source /opt/ollama-voice/bin/activate