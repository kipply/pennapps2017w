#!/bin/bash
cd "${0%/*}" # Go to this directory
echo /usr/bin/python3 generate_story.py $1 $2