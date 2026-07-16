# Catalog Sync

## Trigger
On demand: "Sync catalog from wellthlab.shop"

## Instructions
1. Fetch https://wellthlab.shop/collections/all
2. Fetch https://wellthlab.shop/collections.json
3. For each product, fetch `https://wellthlab.shop/products/{handle}` and extract:
   - name, price, compare_at, benefits, who_its_for, key_ingredients, best_use_cases
4. Update `products/catalog.yaml` with any changes
5. Log sync date at top of catalog file

## Note
Shopify `products.json` endpoint may return 500 — use page scraping as fallback.
