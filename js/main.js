/* =====================================================================
   KP SANGHVI GROUP — main.js
   Vanilla JS: sticky header, mobile menu, hero slider, scroll reveals,
   back-to-top, contact form (front-end only). No dependencies.
   ===================================================================== */
(function () {
  "use strict";
  var doc = document;

  /* ---------- sticky header ---------- */
  var header = doc.querySelector(".site-header");
  function onScroll() {
    if (header) header.classList.toggle("scrolled", window.scrollY > 40);
    var top = doc.querySelector(".to-top");
    if (top) top.classList.toggle("show", window.scrollY > 500);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* ---------- mobile menu ---------- */
  var toggle = doc.querySelector(".nav-toggle");
  var body = doc.body;
  function closeMenu() { body.classList.remove("nav-open"); if (toggle) toggle.setAttribute("aria-expanded", "false"); }
  if (toggle) {
    toggle.addEventListener("click", function () {
      var open = body.classList.toggle("nav-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }
  var backdrop = doc.querySelector(".nav-backdrop");
  if (backdrop) backdrop.addEventListener("click", closeMenu);
  doc.addEventListener("keydown", function (e) { if (e.key === "Escape") closeMenu(); });

  /* mobile dropdown accordions */
  doc.querySelectorAll(".has-dropdown").forEach(function (li) {
    var link = li.querySelector("a");
    if (!link) return;
    link.addEventListener("click", function (e) {
      // only intercept when in mobile (hamburger) mode
      if (window.matchMedia("(max-width:900px)").matches) {
        e.preventDefault();
        var wasOpen = li.classList.contains("open");
        li.parentElement.querySelectorAll(".has-dropdown.open").forEach(function (o) { o.classList.remove("open"); });
        if (!wasOpen) li.classList.add("open");
      }
    });
  });

  /* close menu when a real sub-link is tapped */
  doc.querySelectorAll(".primary-nav .dropdown a").forEach(function (a) {
    a.addEventListener("click", closeMenu);
  });

  /* ---------- hero slider ---------- */
  var slides = Array.prototype.slice.call(doc.querySelectorAll(".hero-slide"));
  if (slides.length > 1) {
    var dotsWrap = doc.querySelector(".hero-dots");
    var idx = 0, timer;
    slides.forEach(function (s, i) {
      if (dotsWrap) {
        var b = doc.createElement("button");
        b.setAttribute("aria-label", "Go to slide " + (i + 1));
        b.addEventListener("click", function () { go(i); reset(); });
        dotsWrap.appendChild(b);
      }
    });
    var dots = dotsWrap ? Array.prototype.slice.call(dotsWrap.children) : [];
    function go(n) {
      slides[idx].classList.remove("active");
      if (dots[idx]) dots[idx].classList.remove("active");
      idx = (n + slides.length) % slides.length;
      slides[idx].classList.add("active");
      if (dots[idx]) dots[idx].classList.add("active");
    }
    function next() { go(idx + 1); }
    function reset() { clearInterval(timer); timer = setInterval(next, 6000); }
    go(0); reset();
  }

  /* ---------- scroll reveal ---------- */
  var revealEls = doc.querySelectorAll(".reveal,.reveal-left,.reveal-right,.reveal-scale,.stat");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { threshold: 0.15, rootMargin: "0px 0px -8% 0px" });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add("in"); });
  }

  /* ---------- count-up for stats ---------- */
  doc.querySelectorAll(".stat .num[data-count]").forEach(function (el) {
    var target = parseFloat(el.getAttribute("data-count"));
    var suffix = el.getAttribute("data-suffix") || "";
    var prefix = el.getAttribute("data-prefix") || "";
    var done = false;
    function run() {
      if (done) return; done = true;
      var start = 0, dur = 1600, t0 = null;
      function step(ts) {
        if (!t0) t0 = ts;
        var p = Math.min((ts - t0) / dur, 1);
        var val = Math.floor((0.5 - Math.cos(p * Math.PI) / 2) * target);
        el.textContent = prefix + val.toLocaleString() + suffix;
        if (p < 1) requestAnimationFrame(step);
      }
      requestAnimationFrame(step);
    }
    if ("IntersectionObserver" in window) {
      var o2 = new IntersectionObserver(function (e) { e.forEach(function (x) { if (x.isIntersecting) { run(); o2.disconnect(); } }); }, { threshold: 0.4 });
      o2.observe(el);
    } else { el.textContent = prefix + target.toLocaleString() + suffix; }
  });

  /* ---------- back to top ---------- */
  var toTop = doc.querySelector(".to-top");
  if (toTop) toTop.addEventListener("click", function () { window.scrollTo({ top: 0, behavior: "smooth" }); });

  /* ---------- contact form (front-end only, no backend) ---------- */
  var form = doc.querySelector("#contact-form");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var status = doc.querySelector("#form-status");
      if (!form.checkValidity()) { form.reportValidity(); return; }
      /* NOTE: static site — no server. See README.md to connect a form service. */
      if (status) {
        status.hidden = false;
        status.textContent = "Thank you. This is a demo form — connect a form service (see README) to receive messages.";
        status.focus();
      }
      form.reset();
    });
  }

  /* ---------- footer year ---------- */
  var y = doc.querySelector("[data-year]");
  if (y) y.textContent = new Date().getFullYear();
})();
