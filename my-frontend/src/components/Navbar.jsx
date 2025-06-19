
/**
 * Navbar component: renders the application’s navigation bar.
 *
 * Props:
 * - searchValue: current value of the search input.
 * - onSearch: function called with the search query.
 *
 * Features:
 * - Displays the Athletica logo linking to home.
 * - Includes a link to the athletes page.
 * - Provides a search input and button that invoke onSearch.
 * - Uses AuthContext to determine authentication state.
 *   - When authenticated: shows profile icon and logout button.
 *   - When not authenticated: shows login button.
 */

import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import './Navbar.css';

import logoIcon from '../assets/logo.png';
import avatarIcon from '../assets/avatar.png';

export default function Navbar({ searchValue, onSearch }) {
  const navigate = useNavigate();
  const { isAuthenticated, logoutContext } = useAuth();

  const handleLogout = () => {
    logoutContext();
    navigate('/');
  };

  return (
    <nav className="navbar">
      <div className="navbar-container">
        {/* Logo linking to home */}
        <Link to="/" className="navbar-logo">
          <img src={logoIcon} alt="Athletica Logo" className="logo-icon" />
          <span className="logo-text">Athletica</span>
        </Link>

        {/* Link to athletes page */}
        <Link to="/athletes" className="navbar-link">
          Atletas
        </Link>

        {/* Search input */}
        <div className="navbar-search">
          <input
            type="text"
            placeholder="Buscar atleta..."
            value={searchValue}
            onChange={e => onSearch(e.target.value)}
          />
          <button onClick={() => onSearch(searchValue)}>🔍</button>
        </div>

        {/* User actions */}
        <div className="navbar-actions">
          {isAuthenticated ? (
            <>
              <Link to="/profile">
                <img src={avatarIcon} alt="Profile" className="avatar-icon" />
              </Link>
              <button onClick={handleLogout} className="logout-button">
                Cerrar Sesión
              </button>
            </>
          ) : (
            <Link to="/login" className="login-button-link">
              <button className="login-button">Iniciar Sesión</button>
            </Link>
          )}
        </div>
      </div>
    </nav>
  );
}
