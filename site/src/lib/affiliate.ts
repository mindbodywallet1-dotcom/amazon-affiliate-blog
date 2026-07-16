import fs from 'node:fs';
import path from 'node:path';
import { parse as parseYaml } from 'yaml';

export interface AffiliateConfig {
  associate_tag: string;
  site_url: string;
  disclosure_short: string;
  disclosure_full: string;
}

export interface AsinData {
  asin: string;
  title: string;
  niche?: string;
  price_band?: string;
  rating?: number;
  review_count?: number;
  affiliate_url?: string;
  pros?: string[];
  cons?: string[];
  best_for?: string;
}

const repoRoot = path.resolve(import.meta.dirname, '../../../');

function readYamlFile<T>(filePath: string): T | null {
  if (!fs.existsSync(filePath)) return null;
  return parseYaml(fs.readFileSync(filePath, 'utf8')) as T;
}

export function getAffiliateConfig(): AffiliateConfig {
  const configPath = path.join(repoRoot, 'affiliate', 'config.yaml');
  const examplePath = path.join(repoRoot, 'affiliate', 'config.example.yaml');
  const config =
    readYamlFile<AffiliateConfig>(configPath) ??
    readYamlFile<AffiliateConfig>(examplePath);

  if (!config) {
    throw new Error('Missing affiliate/config.yaml or config.example.yaml');
  }

  return config;
}

export function buildAmazonUrl(asin: string, tag?: string): string {
  const config = getAffiliateConfig();
  const associateTag = tag ?? config.associate_tag;
  return `https://www.amazon.com/dp/${asin}?tag=${associateTag}`;
}

export function getAsinData(asin: string): AsinData | null {
  const asinPath = path.join(repoRoot, 'affiliate', 'asins', `${asin}.yaml`);
  const data = readYamlFile<AsinData>(asinPath);
  if (!data) return null;

  if (!data.affiliate_url) {
    data.affiliate_url = buildAmazonUrl(asin);
  }

  return data;
}

export function getAsinDataList(asins: string[]): AsinData[] {
  return asins
    .map((asin) => getAsinData(asin))
    .filter((item): item is AsinData => item !== null);
}
