#!/bin/bash

file="Phish-Mac.pyw"

dir=$(dirname "$(find ~  -name "$file" 2>/dev/null)")
echo "lets: $dir"
if [ -z $dir ]; then
  echo "oh no"
else
  cd "$dir" && python3 "$file"
fi

