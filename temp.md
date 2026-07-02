sudo docker run -d \
  --name=calibre-web \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Asia/Manila \
  -p 8083:8083 \
  -v /srv/dev-disk-by-uuid-542ef619-5db5-447f-87ec-e423fbd57da0/docker/calibre-web/config:/config \
  -v /srv/dev-disk-by-uuid-542ef619-5db5-447f-87ec-e423fbd57da0/docker/calibre-web/books:/books \
  --restart unless-stopped \
  lscr.io/linuxserver/calibre-web:latest


- mkdir -p /srv/dev-disk-by-uuid-542ef619-5db5-447f-87ec-e423fbd57da0/docker/calibre-web/config
- mkdir -p /srv/dev-disk-by-uuid-542ef619-5db5-447f-87ec-e423fbd57da0/docker/calibre-web/books

curl -L -o /books/metadata.db https://github.com/janeczku/calibre-web/raw/master/library/metadata.db
