#!/bin/bash

name=$( echo $1 | cut -d'.' -f 1 )

g++ -o $name $1
