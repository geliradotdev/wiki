
# youtubedbl-material
docker run -d \
  --name=youtubedl-material \
  -p 17442:17442 \
  -v /srv/dev-disk-by-uuid-542ef619-5db5-447f-87ec-e423fbd57da0/docker/youtube-material/appdata:/app/appdata \
  -v /srv/dev-disk-by-uuid-542ef619-5db5-447f-87ec-e423fbd57da0/docker/youtube-material/audio:/app/audio \
  -v /srv/dev-disk-by-uuid-542ef619-5db5-447f-87ec-e423fbd57da0/docker/youtube-material/video:/app/video \
  --restart unless-stopped \
  tzahi12345/youtubedl-material:latest

# create directories
mkdir -p /srv/dev-disk-by-uuid-542ef619-5db5-447f-87ec-e423fbd57da0/docker/youtube-material/appdata 
mkdir -p /srv/dev-disk-by-uuid-542ef619-5db5-447f-87ec-e423fbd57da0/docker/youtube-material/audio 
mkdir -p /srv/dev-disk-by-uuid-542ef619-5db5-447f-87ec-e423fbd57da0/docker/youtube-material/video