
# Headline





docker run -d \
  --name portainer \
  --restart unless-stopped \
  -p 9443:9443 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /srv/dev-disk-by-uuid-3bf31d1c-0042-4cd3-b4ac-200ee0fc3205/portainer:/data \
  portainer/portainer-ce:latest
