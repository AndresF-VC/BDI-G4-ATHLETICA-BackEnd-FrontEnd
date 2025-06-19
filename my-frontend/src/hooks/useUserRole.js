/**
 * Custom hook to retrieve the current user's role from the JWT access token.
 *
 * - Checks authentication status via AuthContext.
 * - Reads the 'accessToken' from localStorage.
 * - Decodes the token to extract the 'role' claim.
 * - Returns the role string, or null if unauthenticated or token is invalid.
 */

import { jwtDecode } from 'jwt-decode';
import { useAuth } from '../context/AuthContext';

export const useUserRole = () => {
  const { isAuthenticated } = useAuth();
  

  if (!isAuthenticated) {
    return null;
  }

  const token = localStorage.getItem('accessToken');

  if (token) {
    try {
      const decodedToken = jwtDecode(token);
      return decodedToken.role;
    } catch (error) {
      console.error('Token inválido:', error);
      return null;
    }
  }

  return null;
};