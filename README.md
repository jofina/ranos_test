# ranos_test

Two API's have been designed:
import_store -
Initializes connection with PostgresSQL, please do ensure the right user, password  
and database name is used for your PostgresSQL application. Port used is default
5432.
This API helps to read a .csv file, convert it to Pandas dataframe.
Creates an SQL table and loads the values from the Pandas dataframe into sql.

query_db
This API is designed to be used for sending queries and receiving the output
in the form of JSON format.

requirement.txt
Please use the text file to install the libraries  necessary for this API.
 pip install -r requirement.txt


