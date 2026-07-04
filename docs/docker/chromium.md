# chromium

docker run -d \
  --name=chrome \
  --security-opt seccomp=unconfined \
  --shm-size=2g \
  -p 3000:3000 \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Asia/Manila \
  -e CHROME_CLI=https://google.com \
  -v /srv/dev-disk-by-uuid-3bf31d1c-0042-4cd3-b4ac-200ee0fc3205/docker/chromium:/config \
  --restart unless-stopped \
  lscr.io/linuxserver/chromium:latest