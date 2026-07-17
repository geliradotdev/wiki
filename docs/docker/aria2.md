
# aria2 command
docker run -d \
  --name aria2 \
  --restart unless-stopped \
  -p 6800:6800 \
  -p 6888:6888 \
  -p 6888:6888/udp \
  -e RPC_SECRET=changeme123 \
  -e RPC_PORT=6800 \
  -e LISTEN_PORT=6888 \
  -e DISK_CACHE=64M \
  -e IPV6_MODE=false \
  -v "/srv/dev-disk-by-uuid-3bf31d1c-0042-4cd3-b4ac-200ee0fc3205/docker/aria2/aria2-config:/config" \
  -v "/srv/dev-disk-by-uuid-3bf31d1c-0042-4cd3-b4ac-200ee0fc3205/docker/downloads:/downloads" \
  p3terx/aria2-pro



# ariaNg command
docker run -d \
  --name ariang \
  --restart unless-stopped \
  -p 6880:8080 \
  hurlenko/aria2-ariang