#!/bin/bash

file_name="$HOME/Documents/Notes/task-$(date +%d-%m-%Y).md"

if [ ! -f $file_name ]; then
    echo -e "---\ntitle: Note\nauthor: Sarthak Dash\ndate: $(date +%Y-%m-%d)\n---" > $file_name
fi

flatpak run org.gnome.gitlab.somas.Apostrophe $file_name
