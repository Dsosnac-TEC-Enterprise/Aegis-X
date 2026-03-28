import React, { createContext, useContext } from 'react';

const ThemeContext = createContext();

export const ThemeProvider = ({ children }) => {
  const theme = {
    colors: {
      background: '#050505',
      surface: '#0d0d0d',
      primary: '#00ff41', // Matrix Green
      secondary: '#ff0055', // Cyber Neon Pink
      text: '#e0e0e0',
      muted: '#444444',
      border: '#1a1a1a',
      error: '#ff3333',
    },
    fonts: {
      mono: 'monospace',
    }
  };

  return (
    <ThemeContext.Provider value={theme}>
      {children}
    </ThemeContext.Provider>
  );
};

export const useTheme = () => useContext(ThemeContext);
