

# initial Run these commands
nvram get productid
nvram get buildno
nvram get lan_ifname

## Then check firewall support
iptables -t nat -L -n

## Also check if ASUS startup scripts are enabled
nvram get jffs2_scripts

## Your next step is just to paste the output of
nvram get productid
nvram get buildno
nvram get lan_ifname
iptables -t nat -L -n



# Iptables
->> iptables -t nat -A PREROUTING -i br0 -p udp --dport 53 -j DNAT --to-destination <dns server ip>

-->> iptables -t nat -A PREROUTING -i br0 -p tcp --dport 53 -j DNAT --to-destination <dns server ip>


## run:
iptables -t nat -A PREROUTING -i br0 -p udp --dport 53 -j DNAT --to-destination 172.16.255.99

iptables -t nat -A PREROUTING -i br0 -p tcp --dport 53 -j DNAT --to-destination 172.16.255.99

## check after 
iptables -t nat -L PREROUTING -n


# NOTE
Important: these rules are temporary. They disappear after reboot.

## To make them permanent on ASUSWRT, first check JFFS

nvram get jffs2_scripts

## If it returns

1
## we can create
/jffs/scripts/firewall-start


# Try creating the scripts directory manually:
mkdir -p /jffs/scripts

## Create the firewall script
cat > /jffs/scripts/firewall-start <<'EOF'
#!/bin/sh

iptables -t nat -A PREROUTING -i br0 -p udp --dport 53 -j DNAT --to-destination 172.16.255.99
iptables -t nat -A PREROUTING -i br0 -p tcp --dport 53 -j DNAT --to-destination 172.16.255.99
EOF
## make it executable
chmod 755 /jffs/scripts/firewall-start


## check
iptables -t nat -L PREROUTING -n



# further learning

cat > /jffs/scripts/services-start <<'EOF'
#!/bin/sh

iptables -t nat -A PREROUTING -i br0 -p udp --dport 53 -j DNAT --to-destination 172.16.255.99
iptables -t nat -A PREROUTING -i br0 -p tcp --dport 53 -j DNAT --to-destination 172.16.255.99
EOF

chmod 755 /jffs/scripts/services-start



# another one

This changes the situation. Your firmware does have JFFS script support internally.

Important findings:

start_script
checking for user scripts: '%s'
/jffs/etc/config

The firmware is not using the newer ASUS format:

/jffs/scripts/firewall-start

It is using the older ASUSWRT script system:

/jffs/etc/config/

Create a startup script there.

First check the directory:

ls -la /jffs/etc/config

Then create a firewall script:

mkdir -p /jffs/etc/config

cat > /jffs/etc/config/firewall.sh <<'EOF'
#!/bin/sh

iptables -t nat -A PREROUTING -i br0 -p udp --dport 53 -j DNAT --to-destination 172.16.255.99
iptables -t nat -A PREROUTING -i br0 -p tcp --dport 53 -j DNAT --to-destination 172.16.255.99
EOF

chmod 755 /jffs/etc/config/firewall.sh

Now test it manually:

/jffs/etc/config/firewall.sh

Check:

iptables -t nat -L PREROUTING -n

If the rules appear, reboot and test persistence.

Your rc binary clearly contains:

start_script
checking for user scripts

so this is the correct path to investigate.




# another two
Your BusyBox strings does not support -t, so ignore that.

We know:

/jffs is persistent.
/jffs/etc/config/firewall.sh runs correctly.
The firmware has start_script.

Now we need to see if the script loader actually runs files in /jffs/etc/config.

Try this simple test script:

cat > /jffs/etc/config/test.sh <<'EOF'
#!/bin/sh
echo "SCRIPT_RAN" >> /tmp/script_test.log
EOF

chmod 755 /jffs/etc/config/test.sh