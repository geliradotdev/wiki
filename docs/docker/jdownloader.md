# JDownloader 

docker run -d \
  --name=jdownloader-2 \
  -p 5800:5800 \
  -v /srv/dev-disk-by-uuid-542ef619-5db5-447f-87ec-e423fbd57da0/docker/jdownloader/config:/config \
  -v /srv/dev-disk-by-uuid-542ef619-5db5-447f-87ec-e423fbd57da0/docker/jdownloader/output:/output \
  --restart unless-stopped \
  jlesage/jdownloader-2

# create directoriers

mkdir -p /srv/dev-disk-by-uuid-542ef619-5db5-447f-87ec-e423fbd57da0/docker/jdownloader/config
mkdir -p /srv/dev-disk-by-uuid-542ef619-5db5-447f-87ec-e423fbd57da0/docker/jdownloader/output