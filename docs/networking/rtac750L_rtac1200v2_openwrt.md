


# note
rt-ac750L && rt-ac1200v2 is the same chipset




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



# apk add luci-app-sqm sqm-scripts


# https://openwrt.org/toh/hwdata/asus/asus_rt-ac1200_v2