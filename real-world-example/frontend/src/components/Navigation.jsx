import { Link } from 'react-router-dom';

function Navigation() {
  return (
    <nav className="main-nav">
      <Link to="/" className="nav-link">Home</Link>
    </nav>
  );
}

export default Navigation; 