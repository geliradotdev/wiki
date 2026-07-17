

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


nft add rule inet fw4 dstnat iifname "br-lan" udp dport 53 dnat ip to 192.168.1.212

nft add rule inet fw4 dstnat iifname "br-lan" tcp dport 53 dnat ip to 192.168.1.212
