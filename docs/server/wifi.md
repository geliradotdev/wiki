To see what networking tools you have installed, run:



ls /sbin /usr/sbin /usr/bin | grep -E "iw|wireless|wpa|dhclient|dhcpcd|nmcli"



Paste the output, and I'll determine the best way to proceed.



i have dhcpcd, wpa\_action, wpa\_cli wpa supplicant, wpa\_passphrase , dhcpcd wpa acton



That's enough to connect.



If you know your Wi-Fi name (SSID) and password, run:



sudo wpa\_passphrase "YourSSID" "YourPassword" | sudo tee /etc/wpa\_supplicant/wpa\_supplicant.conf



Then:



sudo wpa\_supplicant -B -i wlp1s0 -c /etc/wpa\_supplicant/wpa\_supplicant.conf



Then obtain an IP address:



sudo dhcpcd wlp1s0



Check if you're connected:



ip addr show wlp1s0

ping -c 4 8.8.8.8



If you don't know the exact SSID, use wpa\_cli to scan:



wpa\_cli -i wlp1s0 scan

sleep 5

wpa\_cli -i wlp1s0 scan\_results



If scan\_results says it can't connect to wpa\_supplicant, start it first:



sudo wpa\_supplicant -B -i wlp1s0







## Troubleshooting

OMV Wi-Fi Static IP Setup Troubleshooting Log

Goal



Configure OpenMediaVault (Debian) to automatically connect using wireless interface:



Interface: wlp1s0

Static IP: 172.31.255.16/26

Gateway: 172.31.255.1



Before troubleshooting, the server required manual commands after every reboot:



wpa\_supplicant -B -i wlp1s0 -c /etc/wpa\_supplicant/wpa\_supplicant.conf



ip addr add 172.31.255.16/26 dev wlp1s0



ip route add default 172.31.255.1



The objective was to automate these steps during boot.



Step 1 — Verify the Wireless Interface



Check that the Wi-Fi adapter exists:



ip link show wlp1s0



Bring the interface up if needed:



ip link set wlp1s0 up



Check if Wi-Fi is blocked:



rfkill list



Expected:



Soft blocked: no

Hard blocked: no

Step 2 — Configure Wi-Fi Authentication



Create the WPA configuration:



nano /etc/wpa\_supplicant/wpa\_supplicant.conf



Example:



ctrl\_interface=/run/wpa\_supplicant

update\_config=1

country=PH



network={

&#x20;   ssid="YOUR\_WIFI\_SSID"

&#x20;   psk="YOUR\_WIFI\_PASSWORD"

}



Manual test:



wpa\_supplicant -B -i wlp1s0 -c /etc/wpa\_supplicant/wpa\_supplicant.conf



Verify connection:



iw dev wlp1s0 link



Expected:



Connected to xx:xx:xx:xx:xx:xx

SSID: YOUR\_WIFI\_SSID



At this point, Wi-Fi connection worked, but no IP was assigned automatically.



Step 3 — Test Manual IP Configuration



The following commands successfully gave the server network access:



ip addr add 172.31.255.16/26 dev wlp1s0



ip route add default 172.31.255.1



The issue was that these commands disappeared after reboot.



Step 4 — Attempt Standard Network Configuration



Initial options considered:



systemd-networkd



Example:



/etc/systemd/network/25-wlp1s0.network

\[Match]

Name=wlp1s0



\[Network]

Address=172.31.255.16/26

Gateway=172.31.255.1

DNS=8.8.8.8

DNS=1.1.1.1

Netplan



Not applicable because the system is OpenMediaVault/Debian, not Ubuntu.



OMV manages networking differently, so manually modifying normal network files could be overwritten.



Step 5 — Create a Systemd Service



Because OMV was not automatically assigning the static IP, a custom service was created.



Create:



nano /etc/systemd/system/wifi-static-ip.service



Initial version:



\[Unit]

Description=Configure static IP for wlp1s0

After=wpa\_supplicant@wlp1s0.service

Wants=wpa\_supplicant@wlp1s0.service



\[Service]

Type=oneshot

ExecStart=/sbin/ip addr add 172.31.255.16/26 dev wlp1s0

ExecStart=/sbin/ip route add default via 172.31.255.1

RemainAfterExit=yes



\[Install]

WantedBy=multi-user.target



Enable the service:



systemctl daemon-reload



systemctl enable wifi-static-ip.service

Step 6 — Troubleshoot Default Route



The IP address worked, but the gateway was not added.



The original route command:



ip route add default 172.31.255.1



was incomplete.



Correct syntax:



ip route add default via 172.31.255.1 dev wlp1s0



The service was updated to:



ExecStart=/bin/bash -c '/sbin/ip route add default via 172.31.255.1 dev wlp1s0 || true'

Step 7 — Fix Boot Timing Issue



Problem:



The service started before Wi-Fi finished connecting.



Solution:



Add a delay and prevent failures if the IP or route already exists.



Final service:



\[Unit]

Description=Configure static IP for wlp1s0

After=wpa\_supplicant@wlp1s0.service

Wants=wpa\_supplicant@wlp1s0.service



\[Service]

Type=oneshot

ExecStart=/bin/bash -c 'sleep 5; /sbin/ip addr add 172.31.255.16/26 dev wlp1s0 || true'

ExecStart=/bin/bash -c '/sbin/ip route add default via 172.31.255.1 dev wlp1s0 || true'

RemainAfterExit=yes



\[Install]

WantedBy=multi-user.target



Reload and restart:



systemctl daemon-reload



systemctl enable wifi-static-ip.service



systemctl restart wifi-static-ip.service

Step 8 — Verify Configuration



Check IP:



ip addr show wlp1s0



Expected:



inet 172.31.255.16/26



Check route:



ip route



Expected:



default via 172.31.255.1 dev wlp1s0



Check Wi-Fi:



iw dev wlp1s0 link



Expected:



Connected to ...

SSID: YOUR\_WIFI\_SSID

Final Boot Process



After reboot, the automatic sequence is now:



Server powers on

&#x20;       |

&#x20;       v

wpa\_supplicant starts

&#x20;       |

&#x20;       v

wlp1s0 connects to Wi-Fi

&#x20;       |

&#x20;       v

wifi-static-ip.service starts

&#x20;       |

&#x20;       v

172.31.255.16/26 assigned

&#x20;       |

&#x20;       v

Default gateway 172.31.255.1 added

&#x20;       |

&#x20;       v

Server becomes reachable through Wi-Fi

Final Verification After Reboot



Run:



reboot



After login:



ip addr show wlp1s0



ip route



iw dev wlp1s0 link



systemctl status wifi-static-ip.service



The system is considered complete when:



Wi-Fi connects automatically

172.31.255.16/26 appears automatically

default via 172.31.255.1 dev wlp1s0 appears automatically

No manual ip addr add or ip route add commands are required anymore.



# Change Static Ip
sudo nano /etc/systemd/system/wifi-static-ip.service