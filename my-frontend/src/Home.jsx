import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import { Carousel } from 'react-responsive-carousel';
import 'react-responsive-carousel/lib/styles/carousel.min.css';
import './Home.css';

import athlete1 from './assets/athlete1.png';
import athlete2 from './assets/athlete2.png';
import athlete3 from './assets/athlete3.png';

export default function Home({ searchValue }) {
  const navigate = useNavigate();
  const [athletes, setAthletes] = useState([]);
  const [filtered, setFiltered] = useState([]);

  const images = [athlete1, athlete2, athlete3];

  useEffect(() => {
    axios
      .get('/api/athletes/')
      .then(res => setAthletes(res.data))
      .catch(() => setAthletes([]));
  }, []);

  useEffect(() => {
    const term = searchValue.trim().toLowerCase();
    setFiltered(
      !term
        ? athletes
        : athletes.filter(a => a.name.toLowerCase().includes(term))
    );
  }, [searchValue, athletes]);

  return (
    <div className="home-container">
      <div className="content">
        <aside className="sidebar">
          {filtered.length > 0 ? (
            <ul className="results-list">
              {filtered.map(a => (
                <li
                  key={a.athlete_id}
                  onClick={() => navigate(`/athlete/${a.athlete_id}`)}
                >
                  {a.name}
                </li>
              ))}
            </ul>
          ) : (
            <p>No se encontraron atletas</p>
          )}
        </aside>

        <main className="main-area">
          <div className="carousel-wrapper">
            <Carousel
              autoPlay
              infiniteLoop
              interval={4000}
              showThumbs={false}
              showStatus={false}
              transitionTime={800}
            >
              {images.map((src, i) => (
                <div key={i}>
                  <img src={src} alt={`Atleta ${i + 1}`} />
                </div>
              ))}
            </Carousel>
          </div>
          <h1 className="main-title">Athletica</h1>
        </main>
      </div>
    </div>
  );
}
