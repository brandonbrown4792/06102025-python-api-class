import { Link } from 'react-router-dom';

function TaskItem({ task, onDelete, onToggleComplete }) {
  return (
    <div className="task-item">
      <div className="task-content">
        <div className="task-info">
          <input
            type="checkbox"
            checked={task.completed}
            onChange={() => onToggleComplete(task)}
            className="task-checkbox"
          />
          <span style={{ color: 'black', marginRight: '20px' }}>
            {task.title}
          </span>
        </div>
        <div className="task-actions">
          <Link to={`/tasks/${task.id}/edit`} className="button">Edit</Link>
          <button 
            onClick={() => onDelete(task.id)} 
            className="button delete"
          >
            Delete
          </button>
        </div>
      </div>
    </div>
  );
}

export default TaskItem; 