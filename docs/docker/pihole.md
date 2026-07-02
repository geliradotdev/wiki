# Pihole DNS server


# run command


docker run -d \
  --name pihole \
  --network host \
  -e TZ="Asia/Manila" \
  -e FTLCONF_webserver_api_password='admin' \
  -e FTLCONF_webserver_port='8889o,[::]:8889o' \
  -v /srv/dev-disk-by-uuid-542ef619-5db5-447f-87ec-e423fbd57da0/pihole/etc-pihole:/etc/pihole \
  -v /srv/dev-disk-by-uuid-542ef619-5db5-447f-87ec-e423fbd57da0/pihole/etc-dnsmasq.d:/etc/dnsmasq.d \
  --restart unless-stopped \
  --cap-add NET_ADMIN \
  pihole/pihole:latest


# disable DNS resolver
sudo systemctl stop systemd-resolved
sudo systemctl disable --now systemd-resolved


# make directory
mkdir -p /srv/dev-disk-by-uuid-542ef619-5db5-447f-87ec-e423fbd57da0/pihole/etc-pihole
mkdir -p /srv/dev-disk-by-uuid-542ef619-5db5-447f-87ec-e423fbd57da0/pihole/etc-dnsmasq.d

