import { defineCollection, z } from 'astro:content';

const affiliate = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    type: z.enum(['review', 'roundup', 'comparison']),
    primary_keyword: z.string(),
    asins: z.array(z.string()),
    published: z.boolean().default(false),
    hero_cta_text: z.string().optional(),
    verdict: z.string().optional(),
    quick_pick_asin: z.string().optional(),
    comparison_winner: z.string().optional(),
    updated: z.string().optional(),
  }),
});

export const collections = { affiliate };
