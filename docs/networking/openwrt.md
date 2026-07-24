

# ASUS RT N12+b1


## windows 
- change IP 192.168.1.75/24
- subnet: 255.255.255.0



## enable tftp at windows features
## after tftp is enable run this command and make sure you are in the dir with your firmware.bin

### run this command:
tftp -i 192.168.1.1 PUT firmware.bin


# enter web ui
http://192.168.1.1/cgi-bin/luci/

## default creds
username: root
password: admin




# DNS redirection

uci add firewall redirect
uci set firewall.@redirect[-1].name='Force-DNS-UDP'
uci set firewall.@redirect[-1].src='lan'
uci set firewall.@redirect[-1].src_dport='53'
uci set firewall.@redirect[-1].proto='udp'
uci set firewall.@redirect[-1].dest='wan'
uci set firewall.@redirect[-1].dest_ip='1.1.1.1'
uci set firewall.@redirect[-1].dest_port='53'

uci add firewall redirect
uci set firewall.@redirect[-1].name='Force-DNS-TCP'
uci set firewall.@redirect[-1].src='lan'
uci set firewall.@redirect[-1].src_dport='53'
uci set firewall.@redirect[-1].proto='tcp'
uci set firewall.@redirect[-1].dest='wan'
uci set firewall.@redirect[-1].dest_ip='1.1.1.1'
uci set firewall.@redirect[-1].dest_port='53'

uci commit firewall
/etc/init.d/firewall restart

## Network → Interfaces → LAN → DHCP Server → Advanced Settings

6,1.1.1.1,1.0.0.1


### localonly: 6,192.168.1.212