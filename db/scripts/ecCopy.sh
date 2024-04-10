#!/usr/bin/bash
source ~/.zshrc

tacl_output=$(tacl ec260 --download-list --api-key $EC_API_KEY)

echo "$tacl_output"


# Extract the .txt file names from the tacl_output and download each file
while read -r line; do
    if [[ $line == *".txt"* ]]; then
        file_name=$(echo "$line" | awk '{print $2}')
        echo "The extracted file name is: $file_name"
        
        # Download the file using tacl command
        tacl ec260 --download "$file_name" --api-key $EC_API_KEY
        
        # Add any additional processing here for each downloaded file
    fi
done <<< "$tacl_output"
