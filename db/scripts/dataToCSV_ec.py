import csv
import re
import os
from dataToSQL import *


# Open the input and output files

def txtToCSV(input_file, output_file):
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        # Create a CSV writer
        csv_writer = csv.writer(outfile)
        # print("current file: " + input_file)
        check_line = None
        # Write the header row
        for i in range(7):
            line = infile.readline()
            if (i == 1):
                filetype = line
                filetype = filetype.strip()
                filetype = re.split("\t", filetype)

        coordinate = infile.readline()
        for i in range(4):
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
        coordinate = "10.624583 59.658233"

        loc = f"POINT({coordinate})"

        if(filetype[1] == "Conductivity Sensor"):
            csv_writer.writerow(["salinity"])
            csv_writer.writerow(['Record time', 'Record number', 'Sensor status', 'Conductivity', 'Temperature', "Location"])
            
            curr_pos = infile.tell()
            check_line = infile.readline()

            if check_line == "\r\n":
                infile.readline()
                infile.readline()
            else:
                infile.seek(curr_pos)

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
            
            curr_pos = infile.tell()
            check_line = infile.readline()

            if check_line == "\r\n":
                infile.readline()
                infile.readline()
            else:
                infile.seek(curr_pos)

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

    input_dir = "/mnt/data/txt_files/"
    output_dir = "/mnt/data/csv_files/"
    
    for filename in os.listdir(input_dir):
        if filename.endswith('.txt'):
            input_file = os.path.join(input_dir, filename)
            # print("Input file: " + input_file)
            output_file = os.path.join(output_dir, filename[:-4] + '.csv')
            # print("Output file: " + output_file)
            txtToCSV(input_file, output_file)
            # read_csv_and_insert(output_file, sensor)
            # print("Converted to csv")

    # input_file = "/mnt/data/txt_files/20240403T165557_sal.txt"
    # output_file = "/mnt/data/csv_files/20240403T165557_sal.csv"
    # txtToCSV(input_file, output_file)

    print("Data converted to csv")