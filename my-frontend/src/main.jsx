/**
 * Main React application entry point:
 * - Imports core dependencies (React, ReactDOM, React Router, and AuthProvider).
 * - Loads global styles.
 * - Creates the React root and renders the App component wrapped in:
 *   1. React.StrictMode for extra development checks.
 *   2. BrowserRouter for client-side routing.
 *   3. AuthProvider to supply authentication context to the entire app.
 */

import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import App from './App.jsx';
import { AuthProvider } from './context/AuthContext.jsx'; 
import './index.css';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter>
      <AuthProvider> {/* <-- 2. WRAP YOUR APP */}
        <App />
      </AuthProvider>
    </BrowserRouter>
  </React.StrictMode>
);