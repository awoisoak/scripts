#!/bin/bash
# https://community.wanikani.com/t/new-and-improved-wallpaper-generator/37321
wget -q --tries=10 --timeout=20 --spider http://google.com
if [[ $? -eq 0 ]]; then
        echo "Retrieving last Wanikani wallpaper..."
        path=$(cd "$(dirname "$1")"; pwd -P)/$(basename "$1")$(dirname "$0")/wallpaper.png
	cd "$(dirname "$0")"
	curl -s -A "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36" -o "wallpaper.png" "http://wkw.natural20design.com/?k={{YOUR_API_KEY}}&d=1"
	osascript -e "tell application \"System Events\" to tell every desktop to set picture to \"$path\""
	killall Dock
else
        echo "No internet connection, couldn't download last Wanikani wallpaper :("
fi





