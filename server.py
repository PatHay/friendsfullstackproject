from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'full_friendsdb')
@app.route('/')
def index():
    query = "SELECT * FROM friends"  #define your query
    friends = mysql.query_db(query)  #run query with query_db()
    return render_template('index.html', all_friends=friends)  #pass data to our template

@app.route('/friends/<friend_id>')
def show(friend_id):
    # Write query to select specific user by id. At every point where
    # we want to insert data, we write ":" and variable name.
    query = "SELECT * FROM friends WHERE id = :specific_id"
    # Then define a dictionary with key that matches :variable_name in query.
    data = {'specific_id': friend_id}
    # Run query with inserted data.
    friends = mysql.query_db(query, data)
    # Friends should be a list with a single object,
    # so we pass the value at [0] to our template under alias one_friend.
    return render_template('index.html', one_friend=friends[0])

@app.route('/friends', methods=['POST'])
def create():
    # Write query as a string. Notice how we have multiple values
    # we want to insert into our query.
    query = "INSERT INTO friends (name, age, friend_since, year, created_at, updated_at) VALUES (:name, :age, :friend_since, :year, NOW(), NOW())"
    # We'll then create a dictionary of data from the POST data received.
    data = {
             'name': request.form['name'],
             'age': request.form['age'],
             'friend_since':  request.form['friend_since'],
             'year': request.form['year']
           }
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/remove_friend/<friend_id>', methods=['GET'])
def delete(friend_id):
    query = "DELETE FROM friends WHERE id = :id" #data to inject ( the : ) is the variable id
    data = {'id': friend_id} #data in my query_db function(query, data) is defined as the variable i used above in the query as the key and the data to pass is friend_id which is what they pass above in the url
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)