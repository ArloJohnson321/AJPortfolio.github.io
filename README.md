# AJPortfolio.github.io

This repository now includes a **GitHub Pages-ready portfolio** at the repository root:

- `index.html`
- `assets/style.css`

GitHub Pages serves static files, so adding `index.html` ensures your site loads your portfolio instead of only rendering the README.

## Local preview

```bash
python3 -m http.server 8000
```

Then open: `http://127.0.0.1:8000/`

## About the Django files

Your Django scaffold is still in this repo (`manage.py`, `config/`, `portfolio/`) for future backend deployment on a platform like Render, Railway, or Fly.io.
