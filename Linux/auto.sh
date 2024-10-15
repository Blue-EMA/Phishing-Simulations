#!/bin/bash

file="Phishing-Simulations-MacOS.pyw"

# Find the directory containing the file
dir=$(dirname "$(find ~ -name "$file" 2>/dev/null)")

if [ -z "$dir" ]; then
    echo "File not found."
else
    chmod +x -R "$dir"
    cd "$dir" && /usr/bin/python3 "$file"
fi
