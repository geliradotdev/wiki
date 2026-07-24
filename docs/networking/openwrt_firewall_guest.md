






# allow DNS & DHCP

## Network → Firewall → Traffic Rules → Add

name: Allow Family DHCP
protocol: UDP
source zone: family
source address: leave blank
source port: 68
destination zone: device (input)
destination address: leave blank
destination port: 67
action: accept


name: Allow DNS
protocol: TCP + UDP
source zone: family
source address: leave blank
source port: leave blank
destination zone: device (input)
destination address: leave blank
destination port: 53
action: accept

