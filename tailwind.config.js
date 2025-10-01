/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {
      backgroundImage: {
        'radial-at-center': 'radial-gradient(ellipse at center, var(--tw-gradient-stops))',
      },
    },
  },
  plugins: [],
}