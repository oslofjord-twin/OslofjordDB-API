#!/bin/bash

bash /mnt/data/scripts/emptyFolder.sh

bash /mnt/data/scripts/ecCopy.sh

python3 /mnt/data/Oslofjord/OslofjordDB/db/scripts/dataToCSV_ec.py
