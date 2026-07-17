#


cat <<EOF > /etc/systemd/system/piper-alarm.service
[Unit]
Description=Piper 5AM alarm announcement
After=sound.target

[Service]
Type=oneshot
WorkingDirectory=/srv/dev-disk-by-uuid-3bf31d1c-0042-4cd3-b4ac-200ee0fc3205/docker/pytools/piper
ExecStart=/bin/bash -c 'echo "Attention. Zero five hundred hours. This is not a drill. All personnel are to wake immediately and assume readiness. The situation is active. You will move now. Secure yourself, secure your gear, and prepare for immediate deployment. No delay is authorized. No hesitation is permitted. Stand up. Dress fast. Hydrate. Check your equipment and confirm readiness. Review your objectives and prepare for execution. This is a controlled escalation into operational status. You are transitioning from rest to active duty. Maintain discipline. Maintain speed. Movement is required. You will not remain idle. You will not return to bed. Final instruction. Reveille is in effect. You are on the clock. Move." | ./piper/piper --model ./voices/en_US-lessac-medium.onnx --output-raw | aplay -D plughw:1,0 -r 22050 -f S16_LE -t raw -'

EOF

/etc/systemd/system/piper-alarm.timer

[Unit]
Description=Run Piper alarm every day at 5:00 AM

[Timer]
OnCalendar=*-*-* 05:00:00
Persistent=true
Unit=piper-alarm.service

[Install]
WantedBy=timers.target


sudo systemctl daemon-reload
sudo systemctl enable --now piper-alarm.timer
sudo systemctl list-timers --all | grep piper-alarm


# test
sudo systemctl start piper-alarm.service



# quick checks
## always reload after applying 
systemctl daemon-reload

It’s set correctly. The timer is active and the next run is scheduled for Sun 2026-07-05 05:00:00 PDT.

Useful checks:

systemctl status piper-alarm.timer
systemctl status piper-alarm.service
journalctl -u piper-alarm.service -n 50 --no-pager

If you want to verify the exact spoken text now, run:

# test the voice
sudo systemctl start piper-alarm.service

One note: your server shows PDT. If you actually want 5:00 AM local Philippines time, set the server timezone first:

sudo timedatectl set-timezone Asia/Manila
timedatectl

Then restart the timer:

sudo systemctl restart piper-alarm.timer
sudo systemctl list-timers --all | grep piper-alarm