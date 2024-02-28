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
        for i in range(7):
            line = infile.readline()
            if (i == 1):
                filetype = line
                filetype = filetype.strip()
                filetype = re.split("\t", filetype)

        coordinate = infile.readline()
        for i in range(3):
            infile.readline()

        coordinate = coordinate.strip()
        coordinate = re.split("\t", coordinate)
        coordinate = coordinate[1]
        coordinate = coordinate.split(",")
        tempCor = coordinate[0]
        coordinate[0] = coordinate[1]
        coordinate[1] = tempCor

        coordinate = ' '.join(coordinate)
        # print(coordinate)

        loc = f"POINT({coordinate})"

        if(filetype[1] == "Conductivity Sensor"):
            csv_writer.writerow(["salinity"])
            csv_writer.writerow(['Record time', 'Record number', 'Sensor status', 'Conductivity', 'Temperature', "Location"])
            infile.readline()
            for line in infile:
                # Split the line into columns using tab as the delimiter (adjust as needed)
                columns = line.strip()
                columns = re.split(r'\t+', columns)
                # columns[0] = re.sub(" ", "T", columns[0])
                columns[0] = columns[0] + "+01"
                columns.append(loc)
                csv_writer.writerow(columns)
            
            return "salinity"

        elif(filetype[1] == "Turbidity Sensor"):
            csv_writer.writerow(["turbidity"])
            csv_writer.writerow(['Record time', 'Record number', 'Sensor status', 'Turbidity', 'Temperature', "TXC Amp", "C1Amp", "C2Amp", "RawTemp", "Location"])
            infile.readline()
            for line in infile:
                # Split the line into columns using tab as the delimiter (adjust as needed)
                columns = line.strip()
                columns = re.split(r'\t+', columns)
                columns[0] = columns[0] + "+01"
                columns.append(loc)
                csv_writer.writerow(columns)
            
            return "turbidity"

        # Read the input text file and write data to the CSV file
        



if __name__ == "__main__":

    input_dir = "../mnt/data/txt_files/"
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
            

