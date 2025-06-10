from flask import Flask, request, jsonify
import json
import uuid
import os
from models import Task
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)

DB_FILE = './db.json'

# Initialize DB if not exists
if not os.path.exists(DB_FILE):
    with open(DB_FILE, 'w') as f:
        json.dump({"todos": []}, f)

def read_db():
    with open(DB_FILE, 'r') as f:
        data = json.load(f)
        # Convert dictionary data to Task objects
        tasks = []
        for task_data in data.get('todos', []):
            task = Task(task_data['title'], task_data['completed'])
            task.id = task_data['id']  # Preserve the ID
            tasks.append(task)
        return tasks

def write_db(tasks):
    # Convert Task objects to dictionaries
    task_dicts = []
    for task in tasks:
        task_dict = {
            'id': task.id,
            'title': task.title,
            'completed': task.completed
        }
        task_dicts.append(task_dict)
    
    with open(DB_FILE, 'w') as f:
        json.dump({"todos": task_dicts}, f, indent=4)

@app.route('/api/todos', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_todos():
    tasks = read_db()
    return jsonify([{
        'id': task.id,
        'title': task.title,
        'completed': task.completed
    } for task in tasks])

@app.route('/api/todos/<todo_id>', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_todo(todo_id):
    tasks = read_db()
    task = next((t for t in tasks if t.id == todo_id), None)
    if not task:
        return jsonify({'error': 'Todo not found'}), 404
    return jsonify({
        'id': task.id,
        'title': task.title,
        'completed': task.completed
    })

@app.route('/api/todos', methods=['POST'])
@cross_origin(supports_credentials=True)
def create_todo():
    tasks = read_db()
    todo_data = request.get_json()
    new_task = Task(todo_data.get('title', ''), todo_data.get('completed', False))
    new_task.id = str(uuid.uuid4())
    tasks.append(new_task)
    write_db(tasks)
    return jsonify({
        'id': new_task.id,
        'title': new_task.title,
        'completed': new_task.completed
    }), 201

@app.route('/api/todos/<todo_id>', methods=['PUT'])
@cross_origin(supports_credentials=True)
def update_todo(todo_id):
    tasks = read_db()
    todo_data = request.get_json()
    task = next((t for t in tasks if t.id == todo_id), None)
    if not task:
        return jsonify({'error': 'Todo not found'}), 404
    
    if 'title' in todo_data:
        task.title = todo_data['title']
    if 'completed' in todo_data:
        if todo_data['completed']:
            task.complete_task()
        else:
            task.uncomplete_task()
    
    write_db(tasks)
    return jsonify({
        'id': task.id,
        'title': task.title,
        'completed': task.completed
    })

@app.route('/api/todos/<todo_id>', methods=['DELETE'])
@cross_origin(supports_credentials=True)
def delete_todo(todo_id):
    tasks = read_db()
    updated_tasks = [t for t in tasks if t.id != todo_id]
    if len(tasks) == len(updated_tasks):
        return jsonify({'error': 'Todo not found'}), 404
    write_db(updated_tasks)
    return jsonify({'message': 'Todo deleted'})

if __name__ == '__main__':
    app.run(debug=True)
