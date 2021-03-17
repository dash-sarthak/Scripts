#!/bin/sh

file_name="$HOME/Desktop/Writings/writeup-$(date +%d-%m-%Y).md"

if [ ! -f $file_name ]; then
    echo "# UNTITLED - $(date +%Y-%m-%d)" > $file_name
fi

nvim -c ":Goyo" \
    -c "norm G2o" \
    -c "norm zz" \
    -c "startinsert" $file_name

