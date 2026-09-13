# KP Sanghvi Group — Static Website

A complete, production-ready **static website** that recreates the KP Sanghvi Group
brand and website, plus a new **Directors** page you can edit by hand.

It is built with only **HTML, CSS, vanilla JavaScript and images** — no frameworks,
no database, no backend, no build step. It works by simply opening `index.html`,
and uploads directly to any normal web host (e.g. Hostinger `public_html`).

---

## 1. What this project is

A multi-page brochure website for the KP Sanghvi Group:

| Page | File |
|------|------|
| Home | `index.html` |
| About Us | `about.html` |
| Our Journey (timeline) | `our-journey.html` |
| Diamond | `diamonds.html` |
| Jewellery | `jewellery.html` |
| Infrastructure | `infrastructure.html` |
| Energy Systems | `energy.html` |
| **Directors (new, editable)** | `directors.html` |
| Sustainability | `sustainability.html` |
| News & Events | `news-events.html` |
| Contact Us | `contact.html` |
| Terms / Privacy / Cookies / Sitemap | `terms.html`, `privacy.html`, `cookies.html`, `sitemap.html` |

Shared design system:

- `css/style.css` — layout, colours, typography, components
- `css/responsive.css` — all responsive/mobile rules
- `css/animations.css` — subtle scroll & hover animations
- `js/main.js` — sticky header, mobile menu, hero slider, scroll reveals, form handling

> `generate.py` and `content.py` are **optional authoring helpers** used to build the
> HTML. You do **not** need them to run or host the site — the `.html` files are final
> and standalone. Python is not required to view or deploy the website.

---

## 2. How to open it locally

Just double-click **`index.html`** — it opens in your web browser. That's it.

(Optional) To preview it exactly as a server would, you can run a tiny local server:

```
cd kp-sanghvi
python3 -m http.server 8000
```

then open `http://localhost:8000` in your browser.

---

## 3. How to upload it to Hostinger

1. Log in to Hostinger and open **hPanel → File Manager** (or use FTP).
2. Go into the **`public_html`** folder.
3. Upload **everything inside this project folder** (all `.html` files and the
   `css`, `js` and `assets` folders) into `public_html`.
   - Tip: zip the folder's contents, upload the zip, then "Extract" inside `public_html`.
4. Make sure **`index.html` sits directly inside `public_html`** (not in a sub-folder).
5. Visit your domain — the website is live. No database or PHP setup is needed.

---

## 4. Where the images are stored

```
assets/
  logos/                 ← the KP Sanghvi logos
  icons/                 ← the six "Our Ethos" icons
  images/
    home/                ← hero photos, crest, 60-years badge, watermark
    diamonds/  jewellery/  infrastructure/  energy/   ← business photos
    directors/           ← YOUR director photos go here
```

---

## 5. How to replace an image

1. Put your new image into the correct folder above (keep a similar shape/size).
2. Either **give it the exact same filename** as the old image (easiest — nothing
   else to change), **or** open the page's `.html` file and update the `src="..."`
   to your new filename.
3. Save. Refresh the page in your browser.

---

## 6. How to ADD a director  ⭐ (most important)

Everything happens in **`directors.html`**. No code, no database.

1. Put the photograph in:
   ```
   assets/images/directors/
   ```
   Recommended: portrait photo, about **800 × 1000 px**, `.jpg`.
   Suggested names: `director-01.jpg`, `director-02.jpg`, `director-03.jpg`, …

2. Open **`directors.html`** and find the block that starts with:
   ```
   <!-- ===== DIRECTOR CARD (copy this whole block to add a director) ===== -->
   ```

3. **Copy** one whole `director-card` block:
   ```html
   <div class="director-card reveal">
     <div class="director-image">
       <img src="assets/images/directors/director-01.jpg" alt="Director Name" loading="lazy"
            onerror="...">
     </div>
     <div class="director-info">
       <h3>Director Name</h3>
       <p>Director Designation</p>
     </div>
   </div>
   ```

4. Paste it where you want the new director to appear (inside `<div class="director-grid">`).

5. Change **three things**:
   - the image filename in `src="assets/images/directors/....jpg"`
   - the name inside `<h3>...</h3>`
   - the designation inside `<p>...</p>`
   - (also update `alt="..."` to the director's name — good for accessibility/SEO)

6. Save the file. Done. The grid automatically arranges **3 per row on desktop,
   2 on tablet, 1 on mobile**.

> **No photo yet?** Leave the card as-is. If an image file is missing, the card
> automatically shows an elegant gold placeholder silhouette — nothing looks broken.

### How to change a director's NAME
Open `directors.html`, find that director's card, edit the text between
`<h3>` and `</h3>`.

### How to change a director's DESIGNATION
In the same card, edit the text between `<p>` and `</p>` (just under the name).

### How to REMOVE a director
Delete that director's entire `<div class="director-card"> … </div>` block.

---

## 7. How to change contact information

- **Phone / email / address shown in the footer of every page:** these are defined
  once in the site's page template. The quickest way to change them everywhere is a
  find-and-replace across all `.html` files for the old value (e.g. `info@kpsanghvi.com`
  or `+91-22-6123 3333`) → your new value.
- **The full office list and the head-office block** live in `contact.html`. Open it
  and edit the address text directly.
- **The map** on the contact page is a Google Maps embed. To point it elsewhere,
  change the `src="https://maps.google.com/maps?q=...&output=embed"` inside the
  `<iframe>` in `contact.html` (put your address after `q=`).

---

## 8. How to change navigation

The menu is the same on every page. Each page's header lists the menu items as a
simple list of links, for example:

```html
<li class="has-dropdown"><a href="diamonds.html">Businesses ▾</a>
  <ul class="dropdown">
    <li><a href="diamonds.html">Diamond</a></li>
    ...
  </ul>
</li>
```

To rename a menu item, edit its link text. To add a page to the menu, copy a
`<li>...</li>` line and point it at your new `.html` file. Do this in each page's
`<nav class="primary-nav">` block (or, if you use the helper, edit the `NAV` list in
`generate.py` and re-run `python3 generate.py`).

The mobile menu and dropdowns work automatically from this same markup — no extra steps.

---

## 9. How to connect the contact form later

The site is static, so the contact form (`#contact-form` in `contact.html`) does
**not** send email on its own — by design there is no backend. When you're ready to
receive submissions, pick any **no-backend form service** and wire it up in one of
these easy ways:

**Option A — Formspree (or similar), no code:**
1. Create a free form at https://formspree.io and copy your form endpoint URL.
2. In `contact.html`, change the `<form id="contact-form" ...>` opening tag to:
   ```html
   <form id="contact-form" action="https://formspree.io/f/XXXXXXXX" method="POST">
   ```
3. Remove (or keep) the demo JavaScript handler in `js/main.js`. With `action`/`method`
   set, the browser will submit straight to Formspree.

**Option B — mailto (simplest):**
Set the form to `action="mailto:info@kpsanghvi.com" method="POST"` — this opens the
visitor's email app. (Least reliable, but zero setup.)

**Option C — Your host's form handler / a serverless function:**
Point the form `action` at your endpoint (e.g. a Hostinger PHP script or a Netlify/
Cloudflare function) and process the POST there.

Other drop-in services that work with a plain static form: **Getform, Basin,
Web3Forms, Netlify Forms**.

---

## 10. Notes

- **Fonts:** the site uses Google Fonts (Bellefair + Jost) loaded from Google's CDN,
  with safe system fallbacks. They load automatically when the visitor is online.
- **Branding:** the KP Sanghvi logos, crest, ethos icons and photographs are the
  authorized brand assets used for this project.
- **Browser support:** all modern browsers (Chrome, Safari, Edge, Firefox) on desktop,
  tablet and mobile. Fully responsive with no horizontal scrolling.
- **Accessibility:** semantic HTML5, keyboard-accessible menu, visible focus states,
  skip-to-content link and descriptive alt text.
