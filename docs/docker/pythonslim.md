

# pythonslim for script tools


docker run -d \
  --name pytools \
  --restart unless-stopped \
  --device /dev/snd \
  --group-add audio \
  -v /srv/dev-disk-by-uuid-3bf31d1c-0042-4cd3-b4ac-200ee0fc3205/docker/pytools/scripts:/scripts \
  -v /srv/dev-disk-by-uuid-3bf31d1c-0042-4cd3-b4ac-200ee0fc3205/docker/pytools/programs:/programs \
  python:3-slim \
  tail -f /dev/null

# mounted folders
/srv/dev-disk-by-uuid-3bf31d1c-0042-4cd3-b4ac-200ee0fc3205/docker/pytools/scripts:/scripts
/srv/dev-disk-by-uuid-3bf31d1c-0042-4cd3-b4ac-200ee0fc3205/docker/pytools/programs:/programs



# required dependency
apt update && apt install -y alsa-utils
apt update && apt install -y curl wget xz-utils libstdc++6 libgcc-s1 alsa-utils
pip install piper

# testing hardware

## speaker test
speaker-test -D plughw:1,0 -t sine -f 440 -l 1
speaker-test -D plughw:1,0 -t wav


# piper

## make a piper folder
mkdir -p /programs/piper /programs/piper/voices
cd /programs/piper

## Download Piper binary for Linux x86_64
wget -O piper.tar.gz https://github.com/rhasspy/piper/releases/download/2023.11.14-2/piper_linux_x86_64.tar.gz
tar -xzf piper.tar.gz

## Download one English TTS voice model + config
cd /programs/piper/voices
wget https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/lessac/medium/en_US-lessac-medium.onnx
wget https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/lessac/medium/en_US-lessac-medium.onnx.json


# TEST PIPER
echo 'Hello from Piper in Docker.' | /programs/piper/piper/piper \
  --model /programs/piper/voices/en_US-lessac-medium.onnx \
  --output_file /tmp/test.wav

## play test
aplay -D plughw:1,0 /tmp/test.wav



# TO ACCESS lama
apt update && apt install -y iputils-ping
ping -c 4 internal ip
