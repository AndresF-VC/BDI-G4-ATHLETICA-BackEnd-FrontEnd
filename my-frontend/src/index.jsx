/**
 * React application entry point:
 * - Imports core dependencies (React, ReactDOM, React Router) and global styles.
 * - Retrieves the DOM container where the app will mount.
 * - Creates the React root and renders the App component.
 * - Wraps App in BrowserRouter to enable client-side routing.
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
