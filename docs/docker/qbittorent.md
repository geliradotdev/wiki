# Qbittorrent




# command
docker run -d \
  --name=qbit \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Asia/Manila \
  -e WEBUI_PORT=8080 \
  -p 9090:8080 \
  -p 6881:6881 \
  -p 6881:6881/udp \
  -v /srv/dev-disk-by-uuid-3bf31d1c-0042-4cd3-b4ac-200ee0fc3205/docker/qbit/config:/config \
  -v /srv/dev-disk-by-uuid-3bf31d1c-0042-4cd3-b4ac-200ee0fc3205/docker/downloads:/downloads \
  --restart unless-stopped \
  lscr.io/linuxserver/qbittorrent:latest


# add values to config/qBittorrent/qBittorent.conf
[PREFERENCE]
- WebUI\HostHeaderValidation=false
-   

# get temporary password (ADMIN)
- docker logs qbit | grep password