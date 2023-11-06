# OslofjordDB
OslofjordDB

## Installation
Here i will explain step by step how to install the docker container with some data in the database.

1. Install docker desktop
2. Pull this repository
3. Enter repository
4. Now you need to add the txt files containing the salinity and turbidity data to the txt_files folder. Currently it only support the salinity and turbidity data. The data files can be found on the google drive or in educloud. 
5. Now we can run the first python script to convert the txt files to csv files and generate the SQL file that inserts the data. Run the following code:  
` python3 scripts/dataToCsv_postgre.py `

6. Before we build the docker image it can be smart to change the password in the Dockerfile. The password will later be used to connect to the database.
7. When that is finished can we run the docker build command to generate the docker image:
   
   `docker build -t oslofjorddb:latest .`  
Don't forget the dot at the end to indicate that it should build from the current folder.
When that s finished can we go on the the last step.

1. Now you have to start the docker container using the docker image you just generated.  
`docker run --name oslofjorddb -d -p 5432:5432 oslofjorddb:latest`  
If you now open your docker desktop app you should be able to see the conatiner running under the container tab. 

Now you should be able to connect to the database using some database manager. I use QGIS but DBeaver is also an alternative.

To connect you need to insert the name of the database, the host and port and which database to access. You also need to insert username and password when prompted. 

- Username: postgres
The password is stored in the Dockerfile, if you did not change it, just use the standard password that was already writen in the file.  

![](images/qgis.png)