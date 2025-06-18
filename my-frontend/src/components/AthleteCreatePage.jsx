import React from 'react';
import { useNavigate } from 'react-router-dom';
import AthleteForm from './AthleteForm';
import { createAthlete } from '../api/athletes';

export default function AthleteCreatePage() {
  const navigate = useNavigate();
  const handleCreate = async (athleteData) => {
    await createAthlete(athleteData);
    navigate('/athletes');
  };
  return <AthleteForm onSubmit={handleCreate} />;
}