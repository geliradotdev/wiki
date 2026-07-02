# Qbittorrent




# command
docker run -d --name=qbit -e PUID=1000 -e PGID=1000 -e TZ=Asia/Manila -p 9090:8080 -p 6881:6881 -p 6881:6881/udp -v /srv/dev-disk-by-uuid-542ef619-5db5-447f-87ec-e423fbd57da0/docker/qbittorrent/config:/config -v /srv/dev-disk-by-uuid-542ef619-5db5-447f-87ec-e423fbd57da0/docker/qbittorrent/downloads:/downloads lscr.io/linuxserver/qbittorrent:latest



# add values to config/qBittorrent/qBittorent.conf
[PREFERENCE]
- WebUI\HostHeaderValidation=false
- WebUI\CSRFProtection=false

# get temporary password (ADMIN)
- docker logs qbit | grep password