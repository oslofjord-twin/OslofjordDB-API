#!/bin/bash
cd /mnt/data/txt_files
source /mnt/data/key.txt

tacl_output=$(tacl ec260 --download-list --api-key $EC_API_KEY)

echo "$tacl_output"

while read -r line; do
    if [[ $line == *".txt"* ]]; then
        file_name=$(echo "$line" | awk '{print $2}')
        echo "The extracted file name is: $file_name"
        
        if [ -f "/mnt/data/txt_files/$file_name" ]; then
            echo "File exists, stops copying and does not insert new data"
            exit 1
        fi
        # Add any additional processing here for each downloaded file
    fi
done <<< "$tacl_output"


bash /mnt/data/Oslofjord/OslofjordDB-API/db/scripts/emptyFolder.sh

bash /mnt/data/Oslofjord/OslofjordDB-API/db/scripts/ecCopy.sh

python3 /mnt/data/Oslofjord/OslofjordDB-API/db/scripts/dataToCSV_ec.py

python3 /mnt/data/Oslofjord/OslofjordDB-API/db/scripts/insert.py
