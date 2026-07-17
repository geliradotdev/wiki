echo 0 > /sys/class/backlight/intel\_backlight/brightness


No. Running:

brightnessctl set 0%

will only change the brightness for the current session. It will not automatically run after reboot.

To run it on boot, create a systemd service:

nano /etc/systemd/system/brightness.service

Add:

[Unit]
Description=Set screen brightness

[Service]
Type=oneshot
ExecStart=/usr/bin/brightnessctl set 0%

[Install]
WantedBy=multi-user.target

Enable it:

systemctl enable brightness.service

Test it:

systemctl start brightness.service

Note: setting brightness to 0% may make the screen completely black, so if something goes wrong you may need to use another method (SSH, for example) to restore it:

brightnessctl set 50%