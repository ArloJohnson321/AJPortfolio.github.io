# AJPortfolio.github.io

Your portfolio is now set up for **GitHub Pages** in both common configurations:

- root publish source (`/ (root)`)
- docs publish source (`/docs`)

This repo includes:

- `index.html` + `assets/style.css` (root mode)
- `docs/index.html` + `docs/assets/style.css` (docs mode)
- `.nojekyll` to avoid Jekyll transforming files unexpectedly

## Why you were seeing README instead of your site

GitHub Pages renders README content when the selected Pages source does not include an `index.html` in that source directory/branch.

## Fix in GitHub settings

Go to **Repo → Settings → Pages** and set:

- **Source:** Deploy from a branch
- **Branch:** your default branch (usually `main`)
- **Folder:** either `/ (root)` **or** `/docs`

Then save and wait ~1–2 minutes for deploy.

## Local preview

```bash
python3 -m http.server 8000
```

Then open: `http://127.0.0.1:8000/`

## About the Django files

Your Django scaffold is still in this repo (`manage.py`, `config/`, `portfolio/`) for future backend deployment on a platform like Render, Railway, or Fly.io.
