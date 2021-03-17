#!/bin/bash

song=$(playerctl metadata --format "Title: {{ title }}\nArtist: {{ artist }}")
notify-send "Spotify" "$song"
