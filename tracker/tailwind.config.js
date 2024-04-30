/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
            "./templates/*.html",],
  theme: {
    extend: {},
    colors:{
      body:'#f0f4f8',
      nav : '#2d3748',
      link:'#ffffff',
      button:'#48bb78',
      button_hover:'#38a169'
    }
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}
