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


@app.route('/tasks', methods=['GET'])
def get_tasks():
    cursor = db.cursor()
    query = "SELECT * FROM tasks"
    cursor.execute(query)
    tasks = cursor.fetchall()
    return jsonify(tasks), 200


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    cursor = db.cursor()
    query = "DELETE FROM tasks WHERE id=%s"
    cursor.execute(query, (task_id, ))
    db.commit()
    return jsonify({"message": "zadanie pomyslnie usuniete"}), 200


@app.route('/tasks/<int:task_id>/completed', methods=['PUT'])
def update_task_completed(task_id):
    completed = request.json['completed']
    print(completed)
    cursor = db.cursor()
    query = "UPDATE tasks SET completed=%s WHERE id=%s"
    cursor.execute(query, (completed, task_id))
    db.commit()
    return jsonify({"message": "zadanie pomyślnie zmienione"})


if __name__ == '__main__':
    app.run(debug=True)