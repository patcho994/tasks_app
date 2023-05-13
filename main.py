import database
from flask import Flask, request, jsonify


app = Flask(__name__)
db = database.create_connection()


@app.route('/tasks', methods=['POST'])
def add_task():
    title = request.json['title']
    cursor = db.cursor()
    query = "INSERT INTO tasks (title) VALUES (%s)"
    cursor.execute(query, (title, ))
    db.commit()
    return jsonify({"message": "zadanie dodane pomyslnie"}), 201


if __name__ == '__main__':
    app.run(debug=True)