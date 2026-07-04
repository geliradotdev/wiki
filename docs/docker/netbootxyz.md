# netboot.xyz




docker run -d \
  --name netboot \
  -p 3000:3000 \
  -p 8888:80 \
  -p 69:69/udp \
  -v /srv/dev-disk-by-uuid-3bf31d1c-0042-4cd3-b4ac-200ee0fc3205/docker/netboot/config:/config \
  -v /srv/dev-disk-by-uuid-3bf31d1c-0042-4cd3-b4ac-200ee0fc3205/docker/netboot/assets:/assets \
  --restart unless-stopped \
  ghcr.io/netbootxyz/netbootxyz:latest