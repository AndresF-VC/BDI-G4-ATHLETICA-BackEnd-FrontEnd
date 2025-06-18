/**
 *   Punto de entrada principal de la aplicación React.
 * - Importa dependencias (React, ReactDOM, React Router y el proveedor de autenticación).
 * - Carga estilos globales.
 * - Inicializa el root de React y renderiza la aplicación envuelta en:
 *   1. React.StrictMode para activar comprobaciones adicionales en desarrollo.
 *   2. BrowserRouter para habilitar el enrutamiento en el cliente.
 *   3. AuthProvider para proporcionar el contexto de autenticación a toda la aplicación.
 */
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