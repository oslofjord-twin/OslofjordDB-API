import csv
import os


def csvToSQL():
    csv_folder = './OslofjordDB-API/db/data/' 
    sql_file = './OslofjordDB-API/db/scripts/load_data.sql'

    table_name = ['turbidity', 'salinity']
    columns = [['record_time', 'record_number', 'sensor_status', 'turbidity', 'temperature', 'txc_amp', 'c1_amp', 'c2_amp', 'raw_temp', 'location'], 
    ['record_time', 'record_number', 'sensor_status', 'conductivity', 'temperature', 'location']]


    with open(sql_file, 'w') as sql_file:
        for csv_file in os.listdir(csv_folder):
            if csv_file.endswith('.csv'):
                with open(csv_folder + csv_file, 'r') as file:
                    csv_data = csv.reader(file)
                    sensor = next(csv_data)
                    next(csv_data) # skip header row

                    if (sensor[0] == "turbidity"):
                        n = 0
                    else:
                        n = 1   


                    query = "INSERT INTO {} ({}) VALUES\n".format(table_name[n], ', '.join(columns[n]))
                    for row in csv_data:
                        values = ", ".join(["'{}'".format(value) for value in row])
                        query += "({}),\n".format(values)

                    # Remove the trailing comma and new line character and add a semicolon at the end of the query
                    query = query[:-2] + ";\n"    
                    sql_file.write(query)
        
        for i in table_name:
            id_query = "\nUPDATE {} \nSET grid_id = (select grid.id \nFROM grid, {} \nWHERE st_intersects({}.location, grid.geom)\nLIMIT 1);".format(i, i, i)

            sql_file.write(id_query)
        
        sql_file.write("\n\n")

csvToSQL()
