import pandas as pd
import psycopg2
import flask
import datetime
from flask import jsonify
# creates flask application object which conbtains data of the application and also the methods.
app = flask.Flask(__name__)
# Starts the debugger, if the code is malformed we get an error. 
app.config["DEBUG"] = True
@app.route('/query', methods=['GET'])
def query_data():
    conn = psycopg2.connect(host="localhost", port = 5432, database="test", user="postgres", password="postgres")
    # Create a cursor object
    cur = conn.cursor() 
    cur.execute("""SELECT first_name, last_name, email, location, count(location), visited_date FROM fiction 
                 GROUP BY first_name, last_name, email, location, visited_date 
                 ORDER BY visited_date""") 
    query_results = cur.fetchall() 
    # Converting list of tuples to key value pair
    def get_list_of_dict(keys, list_of_tuples):
        list_of_dict = [dict(zip(keys, values)) for values in list_of_tuples]
        return list_of_dict
    keys = ("first_name", "last_name", "email","location", "count", "visited_date")
    data =get_list_of_dict(keys, query_results)       
    return jsonify({"result":data})
# method that runs the application server.
if __name__ == '__main__':
    app.run(debug=True)