#!/bin/bash

op_file="${1%.*}.html"
pandoc --standalone -f markdown -t html5 -o $op_file $1 -c /home/sarthak/scripts/md2html/pandoc-style.css
