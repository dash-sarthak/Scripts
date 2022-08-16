#!/bin/sh
mkdir /home/sarthak/Music/$1
cd /home/sarthak/Music/$1
yt-dlp -x --audio-format mp3 -o '%(title)s.%(ext)s' $2 --embed-thumbnail --add-metadata
