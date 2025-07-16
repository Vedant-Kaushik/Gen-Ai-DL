module.exports = {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        "apple-blue": "#007AFF",
        dark: {
          50: "#18181B",
          100: "#27272A",
          200: "#3F3F46",
          300: "#52525B",
          400: "#71717A",
          500: "#A1A1AA",
          600: "#D4D4D8",
          700: "#E4E4E7",
          800: "#F4F4F5",
          900: "#FAFAFA",
        },
      },
      animation: {
        "slide-up": "slide-up 0.4s cubic-bezier(0.4, 0, 0.2, 1) both",
      },
      keyframes: {
        "slide-up": {
          "0%": { transform: "translateY(30px)", opacity: "0" },
          "100%": { transform: "translateY(0)", opacity: "1" },
        },
      },
    },
  },
  plugins: [],
};
