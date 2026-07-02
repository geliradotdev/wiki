
# nextcloud documentation

# create a di
sudo mkdir -p /srv/dev-disk-by-uuid-3bf31d1c-0042-4cd3-b4ac-200ee0fc3205/nextcloud/app 


sudo docker run -d \
  --name nextcloud \
  --restart unless-stopped \
  -p 8080:80 \
  -v /srv/dev-disk-by-uuid-3bf31d1c-0042-4cd3-b4ac-200ee0fc3205/nextcloud/app:/var/www/html \
  nextcloud:apache


