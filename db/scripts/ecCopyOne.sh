#! usr/bin/bash
source ~/.zshrc

tacl_output=$(tacl ec260 --download-list --api-key $EC_API_KEY)

echo "$tacl_output"


file_name=$(echo "$tacl_output" | awk '/\.txt/ {print $2}')

echo "The extracted file name is: $file_name"

tacl ec260 --download "$file_name" --api-key $EC_API_KEY
