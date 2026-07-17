

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
  -v /srv/dev-disk-by-uuid-3bf31d1c-0042-4cd3-b4ac-200ee0fc3205/docker/downloads:/downloads \
  --restart unless-stopped \
  jellyfin/jellyfin


docker run -d \
  --name jellyseerr \
  -p 5055:5055 \
  -v /srv/dev-disk-by-uuid-3bf31d1c-0042-4cd3-b4ac-200ee0fc3205/docker/jellyseerr/config:/app/config \
  --restart unless-stopped \
  fallenbagel/jellyseerr:latest


  
# repo
https://raw.githubusercontent.com/kinggeorges12/JellyBridge/refs/heads/main/manifest.json