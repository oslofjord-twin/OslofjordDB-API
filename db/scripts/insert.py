import csv
import os
import psycopg2
import time



def insert_data_from_csv(csv_file_path, db_params):
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()

    # Open the CSV file
    with open(csv_file_path, 'r') as f:
        reader = csv.reader(f)
        table_name = next(reader)  # Skip the header row
        table_name = table_name[0]
        next(reader)

        if (table_name == "turbidity"):
            args_str = ','.join(cur.mogrify("(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", i).decode('utf-8')
                for i in reader)
        else:
            args_str = ','.join(cur.mogrify("(%s, %s, %s, %s, %s, %s)", i).decode('utf-8')
                for i in reader)

        if(table_name == "turbidity"):
            cur.execute(f"""
                        INSERT INTO {table_name} 
                        (record_time, record_number, sensor_status, turbidity, 
                        temperature, txc_amp, c1_amp, c2_amp, raw_temp, location) VALUES """ + args_str) 
        else:
            cur.execute(f"""
                        INSERT INTO {table_name} 
                        (record_time, record_number, sensor_status, conductivity, 
                        temperature, location) VALUES """ + args_str)

        conn.commit()
    # Close the database connection
    cur.close()
    conn.close()
    print("All data inserted successfully")

def update_grid_id(db_params):
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()
    try:
        # Prepare the INSERT statement
        cur.execute("""
            update salinity
            set grid_id = (select grid.id
            from grid, salinity
            where st_intersects(salinity.location, grid.geom)
            limit 1)
            where salinity.grid_id IS NULL;
        """)

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while updating salinity table:", error)
        conn.rollback()  # rolling back in case of exception
    
    conn.commit()

    try:
        # Prepare the INSERT statement
        cur.execute("""
            update turbidity
            set grid_id = (select grid.id
            from grid, turbidity
            where st_intersects(turbidity.location, grid.geom)
            limit 1)
            where turbidity.grid_id IS NULL;
        """)

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while updating salinity table:", error)
        conn.rollback()  # rolling back in case of exception

    conn.commit()
    cur.close()
    conn.close()
    print("All data updated successfully")

# Database connection parameters
db_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'postgrespassword',
    'host': '172.17.0.1',
    'port': '5432'  # default PostgreSQL port is 5432
}

# CSV file path
input_dir = '/mnt/data/csv_files/'

for csv_file in os.listdir(input_dir):
    if csv_file.endswith('.csv'):
        input_file = os.path.join(input_dir, csv_file)
        print(f"Inserting file: {input_file}")
        # Call the function
        insert_data_from_csv(input_file, db_params)

# t = time.perf_counter()
# insert_data_from_csv('/mnt/data/csv_files/20240410T000001_sal.csv', db_params)
# insert_data_from_csv('/mnt/data/csv_files/20240410T000013_turb.csv', db_params)
update_grid_id(db_params)
# fin = time.perf_counter() - t
# print(f"Time used: {fin}")
# insert_data_from_csv("/mnt/data/csv_files/20240403T165557_sal.csv", db_params)