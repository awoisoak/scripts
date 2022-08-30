#!/bin/bash 
read -p "Enter the Location name : " location
ls | cat -n | while read n f; do mv "$f" "$location $n.jpg"; done 
