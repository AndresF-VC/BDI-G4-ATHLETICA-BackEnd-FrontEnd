import React from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter } from 'react-router-dom'
import App from './App'
import 'react-responsive-carousel/lib/styles/carousel.min.css' // estilos del carrusel
import './index.css' // si quieres añadir estilos globales

const container = document.getElementById('root')
const root = createRoot(container)
root.render(
  <BrowserRouter>
    <App />
  </BrowserRouter>
)
