/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./Ecommerse/**/*.{html,js}",
    "./node_modules/flowbite/**/*.js",
    "./Ecommerse/**/forms.py",
  ],
  theme: {
    extend: {},
  },
  plugins: [
      require('flowbite/plugin')
  ]
}
