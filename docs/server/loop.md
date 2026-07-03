# LOOPING SCRIPT

nano /root/ping_loop.sh

Content:

#!/bin/bash

LOG="/var/log/ping.log"
PY="/opt/ollama-voice/bin/python"
APP="/root/ping.py"

while true; do
  echo "---- $(date) ----" >> "$LOG"
  $PY "$APP" >> "$LOG" 2>&1
  sleep 30
done



Make executable:

chmod +x /root/ping_loop.sh

Run in background:

nohup /root/ping_loop.sh >/dev/null 2>&1 &

View output:

tail -f /var/log/ping.log

Stop:

pkill -f ping_loop.sh