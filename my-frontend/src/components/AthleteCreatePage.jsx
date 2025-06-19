/**
 * AthleteCreatePage component: displays the form for creating a new athlete.
 *
 * - Uses AthleteForm to collect athlete data.
 * - Calls createAthlete API on submit.
 * - Redirects to the athletes list page upon successful creation.
 */

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