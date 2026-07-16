/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,ts,tsx}'],
  theme: {
    extend: {
      colors: {
        amazon: {
          DEFAULT: '#FF9900',
          dark: '#E47911',
        },
      },
    },
  },
  plugins: [require('@tailwindcss/typography')],
};
