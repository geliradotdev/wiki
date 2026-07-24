# calibre-web



# configuration

sudo docker run -d \
  --name=calibre-web \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Asia/Manila \
  -p 8083:8083 \
  -v /srv/dev-disk-by-uuid-3bf31d1c-0042-4cd3-b4ac-200ee0fc3205/docker/calibre-web/config:/config \
  -v /srv/dev-disk-by-uuid-3bf31d1c-0042-4cd3-b4ac-200ee0fc3205/docker/calibre-web/books:/books \
  --restart unless-stopped \
  linuxserver/calibre-web:latest




# create folders in network drives
- mkdir -p /srv/<network-drive>/docker/calibre/config
- mkdir -p /srv/<network-drive>/docker/calibre/books


# To enter the running container:
sudo docker exec -it calibre-web sh


# Download a used metadata.db 


curl -L -o metadata.db https://github.com/janeczku/calibre-web/raw/master/library/metadata.db


# persmissions
## make folder writable
- chmod 777 

## make file writable
- chmod 666


