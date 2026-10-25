/** @type {import('tailwindcss').Config} */
module.exports = {
  theme: {
    extend: {
      colors: {
        imad: {
          primary: '#0066FF',
          accent: '#00F5A0',
          dot: '#00FFC2',
          sky: '#38BDF8',
          bg: '#070B14',
          surface: '#0B0F19',
          card: '#111827',
          hover: '#162032',
          border: '#1E293B',
          amber: '#FFB703',
          coral: '#FF2A55'
        }
      },
      fontFamily: {
        heading: ['Plus Jakarta Sans', 'sans-serif'],
        body: ['Inter', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace']
      }
    }
  }
};
