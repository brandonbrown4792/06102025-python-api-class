import { useEffect, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import TaskItem from './TaskItem';

function TaskList() {
  const [tasks, setTasks] = useState([]);
  const navigate = useNavigate();

  const fetchTasks = async () => {
    try {
      const res = await fetch('http://localhost:5000/api/todos');
      const data = await res.json();
      setTasks(data);
    } catch (error) {
      console.error('Error fetching tasks:', error);
    }
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  const handleDelete = async (id) => {
    if (window.confirm('Are you sure you want to delete this task?')) {
      try {
        await fetch(`http://localhost:5000/api/todos/${id}`, {
          method: 'DELETE',
        });
        await fetchTasks();
        navigate('/');
      } catch (error) {
        console.error('Error deleting task:', error);
      }
    }
  };

  const handleToggleComplete = async (task) => {
    try {
      await fetch(`http://localhost:5000/api/todos/${task.id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          ...task,
          completed: !task.completed
        }),
      });
      await fetchTasks();
    } catch (error) {
      console.error('Error updating task:', error);
    }
  };

  return (
    <div>
      <h1>Task List</h1>
      <Link style={{marginBottom: '40px'}} to="/tasks/new" className="button">Create New Task</Link>
      <div className="task-list">
        {tasks.length === 0 ? (
          <p className="no-tasks">No tasks yet. Create one to get started!</p>
        ) : (
          tasks.map((task) => (
            <TaskItem
              key={task.id}
              task={task}
              onDelete={handleDelete}
              onToggleComplete={handleToggleComplete}
            />
          ))
        )}
      </div>
    </div>
  );
}

export default TaskList; 