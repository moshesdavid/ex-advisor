#!/bin/bash
while true; do
    git add .
    git commit -m "autosave $(date +'%Y-%m-%d %H:%M:%S')" >/dev/null 2>&1
    git push >/dev/null 2>&1
    sleep 300
don

chmod +x autosave.sh


./autosave.sh &