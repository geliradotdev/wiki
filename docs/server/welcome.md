sudo nano /etc/systemd/system/piper-boot.service


sudo tee /etc/systemd/system/piper-boot.service > /dev/null <<'EOF'
[Unit]
Description=Piper voice boot announcement
After=network.target sound.target

[Service]
Type=oneshot
WorkingDirectory=/srv/dev-disk-by-uuid-3bf31d1c-0042-4cd3-b4ac-200ee0fc3205/docker/pytools/piper
ExecStart=/bin/bash -c 'echo "Server initialization complete. All systems are online and operational. Standing by for instructions." | ./piper/piper --model ./voices/en_US-lessac-medium.onnx --output-raw | aplay -D plughw:1,0 -r 22050 -f S16_LE -t raw -'
RemainAfterExit=no

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload

sudo systemctl enable piper-boot.service

# test it
sudo systemctl start piper-boot.service