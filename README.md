# Resume as Code

A modern, professional resume website built with a data-driven approach. Manage your resume content in YAML files and automatically generate both website and PDF version.

## 🌐 Live Demo

**Website:** [https://xplorinrolypoly.github.io/resume/](https://xplorinrolypoly.github.io/resume/)

**PDF:** [alpana-chaphalkar-resume.pdf](alpana-chaphalkar-resume.pdf)

## ✨ Features

- **Data-Driven**: Resume content stored in structured YAML files
- **Automated Generation**: HTML is automatically generated from templates using Jinja2
- **PDF Export**: Automated PDF generation using Puppeteer
- **Dark Mode**: Toggle between light and dark themes (preference saved locally)
- **Professional Styling**: Clean, modern design with professional blue color scheme
- **Responsive Layout**: Optimized for both screen and print/PDF
- **GitHub Actions**: Automated deployment and PDF generation on every push
- **Interactive Elements**: Clickable links for companies, institutions, and certifications
- **Icon Integration**: Font Awesome icons for social links

## 📁 Project Structure

```
resume/
├── data/                      # YAML data files
│   ├── experience.yml         # Work experience
│   ├── education.yml          # Education background
│   ├── certifications.yml     # Professional certifications
│   └── languages.yml          # Language proficiencies
├── templates/
│   └── index.html.j2          # Jinja2 template for HTML generation
├── scripts/
│   ├── render.py              # Python script to render HTML from YAML
│   ├── generate-pdf.js        # Node.js script for PDF generation
│   └── dark-mode.js           # Dark mode toggle functionality
├── .github/
│   └── workflows/
│       └── generate-pdf.yml   # GitHub Actions workflow
├── style.css                  # CSS stylesheet with dark mode support
├── index.html                 # Generated HTML (auto-generated)
└── alpana-chaphalkar-resume.pdf  # Generated PDF (auto-generated)
```

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Node.js and npm
- Git

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/xPlorinRolyPoly/resume.git
   cd resume
   ```

2. **Install Python dependencies**
   ```bash
   pip install jinja2 PyYAML
   ```

3. **Install Node.js dependencies**
   ```bash
   npm install puppeteer
   ```

4. **Edit your resume data**
   - Update YAML files in the `data/` directory
   - Modify `templates/index.html.j2` if needed

5. **Generate HTML**
   ```bash
   python scripts/render.py
   ```

6. **Generate PDF (optional)**
   ```bash
   node scripts/generate-pdf.js
   ```

7. **View locally**
   - Open `index.html` in your browser

## 📝 Customization

### Update Resume Content

Edit the YAML files in the `data/` directory:

- **experience.yml**: Add your work experience with job title, company, dates, and bullet points
- **education.yml**: Add your degrees, institutions, and graduation dates
- **certifications.yml**: List your professional certifications with URLs
- **languages.yml**: List languages and proficiency levels

### Modify Styling

Edit `style.css` to customize:
- Color scheme (CSS variables in `:root`)
- Typography and spacing
- Dark mode colors
- Layout and responsive design

### Update Template

Modify `templates/index.html.j2` to change:
- HTML structure
- Section order
- Contact information
- Icons and links

## 🤖 Automated Deployment

This repository uses GitHub Actions to automatically:

1. **Render HTML** from YAML data using Jinja2
2. **Generate PDF** from the HTML using Puppeteer
3. **Commit** both files back to the repository
4. **Deploy** to GitHub Pages

### Workflow Triggers

- Automatic: On every push to the `main` branch (except for changes only to README.md, .gitignore, .pdf, or .nojekyll files)
- Manual: Via GitHub Actions "Run workflow" button

## 🎨 Dark Mode

The resume includes a built-in dark mode toggle:
- Click the moon/sun icon in the top-right corner
- Preference is saved in browser localStorage
- Navy blue color scheme (not black) for better readability

## 🖨️ Print Optimization

The CSS includes print-specific optimizations:
- Proper page breaks and margins
- URLs hidden for certain links (certifications, institutions, companies)
- Dark mode toggle button hidden
- A4 page size formatting

## 📄 License

This project structure and code is open source and available for anyone to use.

## 🤝 Contributing

Feel free to fork this repository and adapt it for your own resume!

## 📧 Contact

**Alpana Chaphalkar**
- Email: alpanachaphalkar@gmail.com
- LinkedIn: [linkedin.com/in/alpana-chaphalkar-0506b741](https://www.linkedin.com/in/alpana-chaphalkar-0506b741/)
- GitHub: [@xPlorinRolyPoly](https://github.com/xplorinrolypoly)
- YouTube: [@xplorinrolypoly](https://www.youtube.com/@xplorinrolypoly)
