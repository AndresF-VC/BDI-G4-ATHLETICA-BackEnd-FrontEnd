// src/App.jsx

import React, { useState } from 'react';
import { Routes, Route } from 'react-router-dom';

// Importación de componentes y páginas
import Navbar from './components/Navbar.jsx';
import Home from './Home';
import AthleteDetail from './AthleteDetail';
import LoginPage from './components/LoginPage.jsx';
import RegisterPage from './components/RegisterPage.jsx';
import ProfilePage from './components/ProfilePage.jsx'; // <-- Nueva página de perfil importada
import AthleteListPage from './components/AthleteListPage.jsx';
import AthleteCreatePage from './components/AthleteCreatePage.jsx'; // <-- IMPORTA
import AthleteEditPage from './components/AthleteEditPage.jsx';   // <-- IMPORTA 

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