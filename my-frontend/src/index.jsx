/**
 *  Punto de entrada de la aplicación React.
 * - Importa dependencias principales (React, ReactDOM, React Router) y estilos globales.
 * - Obtiene el contenedor DOM donde se montará la app.
 * - Crea el root de React con createRoot y renderiza el componente App.
 * - Envuelve App en BrowserRouter para habilitar el enrutamiento en el cliente.
 */

import React from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter } from 'react-router-dom'
import App from './App'
import 'react-responsive-carousel/lib/styles/carousel.min.css'
import './index.css' 

const container = document.getElementById('root')
const root = createRoot(container)
root.render(
  <BrowserRouter>
    <App />
  </BrowserRouter>
)
