# calibre-web


# configuration
sudo docker run -d \
  --name=calibre-web \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Asia/Manila \
  -p 8083:8083 \
  -v ~/calibre/config:/config \
  -v ~/calibre/books:/books \
  --restart unless-stopped \
  lscr.io/linuxserver/calibre-web:latest






# To enter the running container:
sudo docker exec -it calibre-web sh


# Download a used metadata.db 
curl -L -o /books/metadata.db https://github.com/janeczku/calibre-web/raw/master/library/metadata.db
