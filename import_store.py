import pandas as pd
import psycopg2
import flask
from flask import jsonify
# creates flask application object which conbtains data of the application and also the methods.
app = flask.Flask(__name__)
# Starts the debugger, if the code is malformed we get an error. 
app.config["DEBUG"] = True
@app.route('/create_table', methods=['GET'])
def load_data():

    data = pd.read_csv("/Users/jofinajijinintern/Documents/test_ran/fictional_sample.csv")
    df = pd.DataFrame(data)
    conn = psycopg2.connect(host="localhost", port = 5432, database="test", user="postgres", password="postgres")
    # Create a cursor object
    cur = conn.cursor() 
    # Create Table
    cur.execute("""CREATE TABLE fiction (first_name VARCHAR(50),last_name VARCHAR(50),
            email VARCHAR(50),location VARCHAR(50), visited_date DATE NOT NULL)""")

    # Loading a pandas dataframe into the database.
    for row in df.itertuples():          
        cur.execute("""INSERT INTO fiction (first_name,last_name, email,location, visited_date)
                   VALUES (%s,%s,%s,%s,%s)""",
                   (row.first_name, 
                    row.last_name,
                    row.email,
                    row.location,
                    row.visited_date))
    conn.commit()
    return ("Imported csv file and loaded in the postgres database")
if __name__ == '__main__':
    app.run(debug=True)
# 