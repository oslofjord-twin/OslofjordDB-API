import csv
import re
import os
from dataToSQL import *

# Input text file and output CSV file names


# Open the input and output files

def txtToCSV(input_file, output_file):
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        # Create a CSV writer
        csv_writer = csv.writer(outfile)

        # Write the header row
        for i in range(13):
            infile.readline()
        filetype = infile.readline()
        filetype = filetype.strip()

        if(filetype == "Conductivity Sensor #399"):
            csv_writer.writerow(["salinity"])
            csv_writer.writerow(['Record time', 'Record number', 'Sensor status', 'Conductivity', 'Temperature'])
            infile.readline()
            for line in infile:
                # Split the line into columns using tab as the delimiter (adjust as needed)
                columns = line.strip()
                columns = re.split(r'\t+', columns)
                # columns[0] = re.sub(" ", "T", columns[0])
                # columns[0] = columns[0] + "Z"
                csv_writer.writerow(columns)
            
            return "salinity"

        elif(filetype == "Turbidity Sensor #78"):
            csv_writer.writerow(["turbidity"])
            csv_writer.writerow(['Record time', 'Record number', 'Sensor status', 'Turbidity', 'Temperature', "TXC Amp", "C1Amp", "C2Amp", "RawTemp"])
            infile.readline()
            for line in infile:
                # Split the line into columns using tab as the delimiter (adjust as needed)
                columns = line.strip()
                columns = re.split(r'\t+', columns)
                csv_writer.writerow(columns)
            
            return "turbidity"

        # Read the input text file and write data to the CSV file
        



if __name__ == "__main__":

    input_dir = "db/txt_files/"
    output_dir = "db/data/"
    
    for filename in os.listdir(input_dir):
        if filename.endswith('.txt'):
            input_file = os.path.join(input_dir, filename)
            output_file = os.path.join(output_dir, filename[:-4] + '.csv')
            txtToCSV(input_file, output_file)
            # read_csv_and_insert(output_file, sensor)
            # print("Converted to csv")
    
    csvToSQL()

    print("Data converted to csv and sql")
            

