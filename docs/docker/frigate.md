
## docker command


sudo docker run -d \
  --name frigate \
  --restart unless-stopped \
  --privileged \
  --shm-size=256m \
  -p 5000:5000 \
  -p 8554:8554 \
  -p 8555:8555/tcp \
  -p 8555:8555/udp \
  -v /docker/frigate/config:/config \
  -v /docker/frigate/media:/media/frigate \
  -v /etc/localtime:/etc/localtime:ro \
  ghcr.io/blakeblackshear/frigate:stable