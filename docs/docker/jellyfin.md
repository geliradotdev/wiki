

# jellyfin


# make dir
mkdir -p /srv/dev-disk-by-uuid-3bf31d1c-0042-4cd3-b4ac-200ee0fc3205/docker/jellyfin/config
mkdir -p /srv/dev-disk-by-uuid-3bf31d1c-0042-4cd3-b4ac-200ee0fc3205/docker/jellyfin/cache


# run command
docker run -d \
  --name jellyfin \
  -p 8096:8096 \
  -v /srv/dev-disk-by-uuid-3bf31d1c-0042-4cd3-b4ac-200ee0fc3205/docker/jellyfin/config:/config \
  -v /srv/dev-disk-by-uuid-3bf31d1c-0042-4cd3-b4ac-200ee0fc3205/docker/jellyfin/cache:/cache \
  --restart unless-stopped \
  jellyfin/jellyfin