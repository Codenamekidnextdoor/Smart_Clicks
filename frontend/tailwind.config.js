/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        // SmartClick Dark Theme
        bg: {
          DEFAULT: '#0a0a0a',
          surface: '#141414',
          surface2: '#1e1e1e',
          surface3: '#282828',
        },
        border: {
          DEFAULT: '#2a2a2a',
          accent: '#1a4a2a',
          blue: '#1a2e3a',
          red: '#4a1a1a',
        },
        accent: {
          DEFAULT: '#00e676',
          hover: '#1e4a1e',
          dark: '#152b15',
        },
        blue: {
          DEFAULT: '#40c4ff',
          dark: '#0d1f2d',
          hover: '#1a2e3a',
        },
        red: {
          DEFAULT: '#ff5252',
          dark: '#2b1515',
          hover: '#4a1e1e',
        },
        orange: {
          DEFAULT: '#ffab40',
          dark: '#2d1f0d',
          hover: '#3a2a0d',
        },
        purple: {
          DEFAULT: '#ce93d8',
          dark: '#1e0d2d',
          hover: '#2a1a3a',
        },
        text: {
          DEFAULT: '#ffffff',
          secondary: '#b0b0b0',
          tertiary: '#5a5a5a',
          muted: '#9e9e9e',
        },
      },
      fontFamily: {
        sans: ['Segoe UI', 'system-ui', 'sans-serif'],
        mono: ['Consolas', 'Monaco', 'monospace'],
      },
      borderRadius: {
        'sm': '6px',
        'DEFAULT': '8px',
        'lg': '10px',
        'xl': '12px',
      },
      boxShadow: {
        'popup': '0 8px 32px rgba(0, 0, 0, 0.4)',
        'card': '0 4px 16px rgba(0, 0, 0, 0.2)',
      },
      animation: {
        'fade-in': 'fadeIn 0.2s ease-out',
        'slide-up': 'slideUp 0.3s ease-out',
        'pulse-slow': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { transform: 'translateY(10px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
      },
    },
  },
  plugins: [],
}

// Made with Bob
