
## docker command


docker run -d \
  --name frigate \
  --restart=unless-stopped \
  --privileged \
  --shm-size=256mb \
  -p 5000:5000 \
  -p 8554:8554 \
  -p 8555:8555/tcp \
  -p 8555:8555/udp \
  -v /srv/dev-disk-by-uuid-3bf31d1c-0042-4cd3-b4ac-200ee0fc3205/docker/frigate/config:/config \
  -v /srv/dev-disk-by-uuid-3bf31d1c-0042-4cd3-b4ac-200ee0fc3205/docker/frigate/media:/media/frigate \
  -v /etc/localtime:/etc/localtime:ro \
  ghcr.io/blakeblackshear/frigate:stable