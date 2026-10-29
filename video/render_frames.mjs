// Screenshots each SVG frame with headless Microsoft Edge through Playwright.
// Usage: PLAYWRIGHT_MODULE=<path to playwright> node render_frames.mjs <svg dir> <png dir>
import { createRequire } from 'node:module';
import { readdirSync, readFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const require = createRequire(import.meta.url);
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const [src, out] = process.argv.slice(2);
mkdirSync(out, { recursive: true });
const browser = await chromium.launch({ channel: 'msedge' });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
await page.setContent('<html><body style="margin:0;background:#F7F5F0"></body></html>');
const files = readdirSync(src).filter((f) => f.endsWith('.svg')).sort();
for (const f of files) {
  await page.evaluate((svg) => { document.body.innerHTML = svg; }, readFileSync(join(src, f), 'utf8'));
  await page.screenshot({ path: join(out, f.replace('.svg', '.png')) });
}
await browser.close();
console.log('rendered', files.length);
