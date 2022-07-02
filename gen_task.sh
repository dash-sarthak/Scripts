#!/bin/bash

file_name="$HOME/Desktop/Tasks/task-$(date +%d-%m-%Y).md"

if [ ! -f $file_name ]; then
    echo -e "---\ntitle: Task\nauthor: Sarthak Dash\ndate: $(date +%Y-%m-%d)\n---" > $file_name
fi

nvim -c "norm G2o" \
    -c "norm zz" \
    -c "startinsert" $file_name
