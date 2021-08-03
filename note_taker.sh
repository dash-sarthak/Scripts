#!/bin/sh

file_name="$HOME/Notes/note-$(date +%d-%m-%Y).md"

if [ ! -f $file_name ]; then
    echo "# Notes for $(date +%Y-%m-%d)" > $file_name
fi

nvim -c "norm Go" \
    -c "norm Go## $(date +%H:%M)" \
    -c "norm Go" \
    -c "norm zz" \
    -c "startinsert" $file_name
