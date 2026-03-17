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

## Quick verify checklist

1. Confirm Pages source matches where `index.html` exists (`/` or `/docs`).
2. Open `https://<username>.github.io/<repo>/` in an incognito window.
3. If you still see the old page, hard refresh (`Ctrl+Shift+R`) and wait another minute.

## Local preview

```bash
python3 -m http.server 8000
```

Open `http://127.0.0.1:8000/`.

## Django note

The Django scaffold (`manage.py`, `config/`, `portfolio/`) remains in this repo for backend hosting (Render/Railway/Fly.io). GitHub Pages can only host static files.
