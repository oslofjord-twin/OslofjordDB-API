#!/bin/bash

# Array of folder paths to be deleted
folder_paths=(
    "/mnt/data/txt_files"
    "/mnt/data/csv_files"
    # Add more folder paths as needed
)

# Iterate through each folder path and delete its contents
for folder_path in "${folder_paths[@]}"; do
    if [[ -n "$folder_path" ]]; then
        # Delete the contents of the folder
        rm -rf "${folder_path:?}/"*
        echo "Contents of \"$folder_path\" deleted successfully."
    else
        echo "Folder path is empty. Please provide a valid folder path."
    fi
done

