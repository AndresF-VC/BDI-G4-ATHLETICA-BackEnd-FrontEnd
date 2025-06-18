// src/main.jsx

import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import App from './App.jsx';
import { AuthProvider } from './context/AuthContext.jsx'; // <-- 1. IMPORTA EL PROVEEDOR
import './index.css';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter>
      <AuthProvider> {/* <-- 2. ENVUELVE TU APP */}
        <App />
      </AuthProvider>
    </BrowserRouter>
  </React.StrictMode>
);