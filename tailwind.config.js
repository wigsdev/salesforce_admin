const path = require('path');

// Function to normalize paths to use forward slashes (required for fast-glob on Windows)
const normalize = (p) => p.replace(/\\/g, '/');

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    normalize(path.join(__dirname, "app/templates/**/*.html")),
    normalize(path.join(__dirname, "app/static/**/*.js"))
  ],
  darkMode: 'class', // Usar clase .dark para activar modo oscuro
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: "#667eea", // Restore original primary
          dark: "#5a67d8",
          600: "#3182ce"
        },
        secondary: "#764ba2",
        accent: "#ed64a6",
        dark: {
          bg: "#111827",
          surface: "#1F2937",
          border: "#374151"
        }
      }
    },
  },
  plugins: [],
}
