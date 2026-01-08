const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
  const browser = await puppeteer.launch({
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  const page = await browser.newPage();
  
  const htmlPath = path.resolve(__dirname, 'index.html');
  await page.goto('file://' + htmlPath, { waitUntil: 'networkidle0' });
  
  await page.pdf({
    path: 'alpana-chaphalkar-resume.pdf',
    format: 'A4',
    printBackground: true,
    preferCSSPageSize: true,
    margin: { top: 0, right: 0, bottom: 0, left: 0 }
  });
  
  await browser.close();
  console.log('PDF generated successfully!');
})();
