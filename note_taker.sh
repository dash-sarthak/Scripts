#!/bin/sh

file_name="$HOME/Documents/Notes/notes/note-$(date +%d-%m-%Y).md"

if [ ! -f $file_name ]; then
    echo -e "---\ntitle: Note\nauthor: Sarthak Dash\ndate: $(date +%Y-%m-%d)\n---\n" > $file_name
fi

gnome-text-editor -n $file_name

