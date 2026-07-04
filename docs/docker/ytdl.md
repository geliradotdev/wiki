
# youtubedbl-material
docker run -d \
  --name=ytdlp \
  -p 17442:17442 \
  -v /srv/dev-disk-by-uuid-542ef619-5db5-447f-87ec-e423fbd57da0/docker/ytdlp/appdata:/app/appdata \
  -v /srv/dev-disk-by-uuid-542ef619-5db5-447f-87ec-e423fbd57da0/docker/ytdlp/audio:/app/audio \
  -v /srv/dev-disk-by-uuid-542ef619-5db5-447f-87ec-e423fbd57da0/docker/ytdlp/video:/app/video \
  --restart unless-stopped \
  tzahi12345/youtubedl-material:latest

# create directories
mkdir -p /srv/dev-disk-by-uuid-542ef619-5db5-447f-87ec-e423fbd57da0/docker/ytdlp/appdata 
mkdir -p /srv/dev-disk-by-uuid-542ef619-5db5-447f-87ec-e423fbd57da0/docker/ytdlp/audio 
mkdir -p /srv/dev-disk-by-uuid-542ef619-5db5-447f-87ec-e423fbd57da0/docker/ytdlp/video