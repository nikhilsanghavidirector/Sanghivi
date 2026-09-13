import { defineConfig } from 'vite';
import { readdirSync } from 'fs';

const htmlPages = readdirSync('.')
  .filter(f => f.endsWith('.html'));

export default defineConfig({
  root: '.',
  base: './',
  server: {
    port: 5173,
    open: false,
  },
  build: {
    outDir: 'dist',
    rollupOptions: {
      input: htmlPages,
    },
  },
});
