from datetime import datetime
import subprocess

dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

subprocess.run(["git", "add", "."], check=True)
subprocess.run(["git", "commit", "-m", f"time {dt}"], check=True)
subprocess.run(["git", "push", "-u", "origin", "main"], check=True)