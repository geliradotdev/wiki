$dt = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

git add .
git commit -m "time $dt"
git push -u origin main