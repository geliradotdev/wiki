



# command 

docker run -d \
  --name bitwarden \
  -v /srv/dev-disk-by-uuid-3bf31d1c-0042-4cd3-b4ac-200ee0fc3205/docker/bitwarden:/etc/bitwarden \
  -p 8888:8080 \
  --env-file /srv/dev-disk-by-uuid-3bf31d1c-0042-4cd3-b4ac-200ee0fc3205/docker/bitwarden/settings.env \
  --restart unless-stopped \
  ghcr.io/bitwarden/lite


# make env
nano /srv/dev-disk-by-uuid-3bf31d1c-0042-4cd3-b4ac-200ee0fc3205/docker/bitwarden/settings.env

# config permission
chown -R root:root /srv/dev-disk-by-uuid-3bf31d1c-0042-4cd3-b4ac-200ee0fc3205/docker/bitwarden
chmod 700 /srv/dev-disk-by-uuid-3bf31d1c-0042-4cd3-b4ac-200ee0fc3205/docker/bitwarden
chmod 600 /srv/dev-disk-by-uuid-3bf31d1c-0042-4cd3-b4ac-200ee0fc3205/docker/bitwarden/settings.env

# get key from: https://bitwarden.com/host/
BW_DOMAIN=http://192.168.1.31:8888
BW_DB_PROVIDER=sqlite
BW_INSTALLATION_ID=
BW_INSTALLATION_KEY=
BW_DB_FILE=/etc/bitwarden/vault.db