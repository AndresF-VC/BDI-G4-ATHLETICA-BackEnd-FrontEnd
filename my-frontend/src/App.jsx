/**
 * App component: sets up the main application layout and routes.
 *
 * - Manages global search state passed to Home and Navbar.
 * - Renders the Navbar with search props.
 * - Defines client-side routes:
 *   - "/" renders Home with search capability.
 *   - "/athlete/:id" renders detailed athlete view.
 *   - "/login" and "/register" render authentication pages.
 *   - "/profile" renders the user's profile page.
 *   - "/athletes" lists athletes.
 *   - "/athletes/new" and "/athletes/edit/:id" render athlete creation and editing pages.
 */

import React, { useState } from 'react';
import { Routes, Route } from 'react-router-dom';


import Navbar from './components/Navbar.jsx';
import Home from './Home';
import AthleteDetail from './AthleteDetail';
import LoginPage from './components/LoginPage.jsx';
import RegisterPage from './components/RegisterPage.jsx';
import ProfilePage from './components/ProfilePage.jsx'; 
import AthleteListPage from './components/AthleteListPage.jsx';
import AthleteCreatePage from './components/AthleteCreatePage.jsx'; 
import AthleteEditPage from './components/AthleteEditPage.jsx';   

export default function App() {
  const [search, setSearch] = useState('');

  return (
    <>
      <Navbar searchValue={search} onSearch={setSearch} />

      <Routes>
        {/* Rutas originales */}
        <Route path="/" element={<Home searchValue={search} />} />
        <Route path="/athlete/:id" element={<AthleteDetail />} />
        
        {/* Rutas de autenticación */}
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />
        
        {/* ======================================= */}
        {/* =========   NUEVA RUTA AÑADIDA    ========= */}
        {/* ======================================= */}
        <Route path="/profile" element={<ProfilePage />} />
        <Route path="/athletes" element={<AthleteListPage />} />
        <Route path="/athletes/new" element={<AthleteCreatePage />} />   
        <Route path="/athletes/edit/:id" element={<AthleteEditPage />} />
      </Routes>
    </>
  );
}