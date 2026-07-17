


# first 
echo -e "nameserver 127.0.0.1" | sudo tee /etc/resolv.conf


# command

docker run -d \
  --name adguardhome \
  --restart unless-stopped \
  -v /srv/dev-disk-by-uuid-542ef619-5db5-447f-87ec-e423fbd57da0/adguardhome/work:/opt/adguardhome/work \
  -v /srv/dev-disk-by-uuid-542ef619-5db5-447f-87ec-e423fbd57da0/adguardhome/conf:/opt/adguardhome/conf \
  -p 53:53/tcp \
  -p 53:53/udp \
  -p 1280:80/tcp \
  -p 3000:3000/tcp \
  -p 12443:443/tcp \
  -p 443:443/udp \
  -p 784:784/udp \
  -p 8853:8853/udp \
  adguard/adguardhome