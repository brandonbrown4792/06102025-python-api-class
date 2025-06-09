from flask import Flask

app = Flask(__name__)

# Sample employee data
employees = {
    'alice': {'name': 'Alice Johnson', 'role': 'Software Engineer'},
    'bob': {'name': 'Bob Smith', 'role': 'Product Manager'},
    'carol': {'name': 'Carol Lee', 'role': 'UX Designer'}
}

# Home route - list all employees
@app.route('/')
def index():
    employee_list = ''.join([f"<li><a href='/employee/{key}'>{data['name']}</a></li>" for key, data in employees.items()])
    return f"<h1>Company Directory</h1><ul>{employee_list}</ul>"

# Dynamic route - show employee profile
@app.route('/employee/<string:name>')
def show_profile(name):
    employee = employees.get(name)
    if employee:
        return f"<h1>{employee['name']}</h1><p>Role: {employee['role']}</p>"
    else:
        return "<h1>Employee not found</h1>", 404

if __name__ == '__main__':
    app.run(port=5555, debug=True)