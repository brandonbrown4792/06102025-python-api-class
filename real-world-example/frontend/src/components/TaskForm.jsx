import { useEffect, useState } from 'react';
import { useNavigate, useParams, Link } from 'react-router-dom';
import { API_URL } from '../api';

function TaskForm() {
  const [title, setTitle] = useState('');
  const [completed, setCompleted] = useState(false);
  const [error, setError] = useState('');
  const navigate = useNavigate();
  const { id } = useParams();

  useEffect(() => {
    if (id) {
      fetch(`${API_URL}/api/todos/${id}`)
        .then(res => {
          if (!res.ok) throw new Error('Task not found');
          return res.json();
        })
        .then(data => {
          setTitle(data.title);
          setCompleted(data.completed);
        })
        .catch(error => {
          console.error('Error fetching task:', error);
          setError('Failed to load task');
        });
    }
  }, [id]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');

    try {
      const method = id ? 'PUT' : 'POST';
      const url = id ? `${API_URL}/api/todos/${id}` : `${API_URL}/api/todos`;

      const response = await fetch(url, {
        method,
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title, completed }),
      });

      if (!response.ok) throw new Error('Failed to save task');

      navigate('/');
    } catch (error) {
      console.error('Error saving task:', error);
      setError('Failed to save task. Please try again.');
    }
  };

  return (
    <div className="task-form-container">
      <h1>{id ? 'Edit Task' : 'Create New Task'}</h1>
      {error && <div className="error-message">{error}</div>}
      <form onSubmit={handleSubmit} className="task-form">
        <div className="form-group">
          <label htmlFor="title">Task Title:</label>
          <input
            id="title"
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
            placeholder="Enter task title"
            className="form-input"
          />
        </div>
        <div className="form-group checkbox-group">
          <label className="checkbox-label">
            <input
              type="checkbox"
              checked={completed}
              onChange={(e) => setCompleted(e.target.checked)}
              className="checkbox-input"
            />
            <span>Mark as completed</span>
          </label>
        </div>
        <div className="form-actions">
          <button type="submit" className="button primary">
            {id ? 'Update Task' : 'Create Task'}
          </button>
          <Link to="/" className="button secondary">Cancel</Link>
        </div>
      </form>
    </div>
  );
}

export default TaskForm;
