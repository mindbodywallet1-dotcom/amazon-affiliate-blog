import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  site: 'https://wellthlab.blog',
  integrations: [tailwind()],
});
