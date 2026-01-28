/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/templates/**/*.html",
    "./app/static/**/*.js"
  ],
  theme: {
    extend: {
      colors: {
        primary: "#005A9C", // Lumina Blue
        "primary-dark": "#00477D",
        "dark-bg": "#111827",
        "dark-surface": "#1F2937",
        "dark-border": "#374151"
      }
    },
  },
  plugins: [],
  darkMode: 'class',
}
