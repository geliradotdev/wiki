# Pihole DNS server


# run command
docker run -d \
  --name pihole \
  --network host \
  --restart unless-stopped \
  --user root \
  -e TZ=Asia/Manila \
  -e FTLCONF_webserver_api_password=admin \
  -e FTLCONF_webserver_port="8889,[::]:8889" \
  -e DNSMASQ_USER=pihole \
  -e FTL_CMD=no-daemon \
  -v /srv/dev-disk-by-uuid-542ef619-5db5-447f-87ec-e423fbd57da0/pihole/etc-pihole:/etc/pihole \
  -v /srv/dev-disk-by-uuid-542ef619-5db5-447f-87ec-e423fbd57da0/pihole/etc-dnsmasq.d:/etc/dnsmasq.d \
  pihole/pihole:latest

## configure DoT and DoH
docker run -d \
  --name dnsproxy \
  --network host \
  --restart unless-stopped \
  adguard/dnsproxy \
  -u https://cloudflare-dns.com/dns-query \
  -u tls://1.1.1.1 \
  -u tls://1.0.0.1 \
  -l 127.0.0.1 \
  -p 5053

## configure it on DNS pihole
127.0.0.1#5053


### test
dig @127.0.0.1 -p 5053 whoami.cloudflare.com TXT


dig @127.0.0.1 google.com



# disable DNS resolver & To prevent it from ever starting automatically, mask it:
sudo systemctl stop systemd-resolved
sudo systemctl disable --now systemd-resolved
sudo systemctl mask systemd-resolved

## verify
systemctl is-enabled systemd-resolved
### It should return: mask
### Also ensure /etc/resolv.conf is not a symlink to the stub resolver:
ls -l /etc/resolv.conf

#### If it points to:/run/systemd/resolve/stub-resolv.conf
replace it with a regular file:
sudo rm /etc/resolv.conf
echo -e "nameserver 1.1.1.1\nnameserver 1.0.0.1" | sudo tee /etc/resolv.conf

docker restart pihole

# enable DNS resolver
sudo systemctl start systemd-resolved
sudo systemctl enable --now systemd-resolved

# make directory
mkdir -p /srv/dev-disk-by-uuid-542ef619-5db5-447f-87ec-e423fbd57da0/pihole/etc-pihole
mkdir -p /srv/dev-disk-by-uuid-542ef619-5db5-447f-87ec-e423fbd57da0/pihole/etc-dnsmasq.d



