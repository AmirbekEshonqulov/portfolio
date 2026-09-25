/* =========================================================
   Amirbek Eshonqulov — Portfolio
   main.js  — theme, language, canvas bg, interactions
   No dependencies. Vanilla JS only.
========================================================= */

/* =====================================================
   0. Prevent FOUC — theme is applied before first paint
      (also done in <head> inline snippet in base.html,
       this block is a safety net for dynamic changes)
===================================================== */
(function applyThemeEarly() {
  const saved = localStorage.getItem('theme');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const theme = saved || (prefersDark ? 'dark' : 'light');
  document.documentElement.setAttribute('data-theme', theme);
})();

/* =====================================================
   1. Theme Toggle
===================================================== */
const themeBtn = document.getElementById('themeBtn');
function setTheme(t) {
  document.documentElement.setAttribute('data-theme', t);
  localStorage.setItem('theme', t);
}
if (themeBtn) {
  themeBtn.addEventListener('click', () => {
    const current = document.documentElement.getAttribute('data-theme');
    setTheme(current === 'dark' ? 'light' : 'dark');
  });
}

/* =====================================================
   2. Language Switcher
===================================================== */
const langBtn      = document.getElementById('langBtn');
const langDropdown = document.getElementById('langDropdown');

if (langBtn && langDropdown) {
  langBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    const open = langDropdown.classList.toggle('open');
    langBtn.setAttribute('aria-expanded', String(open));
  });

  document.addEventListener('click', (e) => {
    if (!langDropdown.contains(e.target) && !langBtn.contains(e.target)) {
      langDropdown.classList.remove('open');
      langBtn.setAttribute('aria-expanded', 'false');
    }
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      langDropdown.classList.remove('open');
      langBtn.setAttribute('aria-expanded', 'false');
      langBtn.focus();
    }
  });
}

/* =====================================================
   3. Mobile Menu
===================================================== */
const mobileMenuBtn  = document.getElementById('mobileMenuBtn');
const mobileNav      = document.getElementById('mobileNav');
const mobileMenuClose= document.getElementById('mobileMenuClose');

function openMobileMenu() {
  mobileNav.classList.add('open');
  mobileMenuBtn.setAttribute('aria-expanded', 'true');
  document.body.style.overflow = 'hidden';
}
function closeMobileMenu() {
  mobileNav.classList.remove('open');
  mobileMenuBtn.setAttribute('aria-expanded', 'false');
  document.body.style.overflow = '';
}

if (mobileMenuBtn && mobileNav) {
  mobileMenuBtn.addEventListener('click', openMobileMenu);
  if (mobileMenuClose) mobileMenuClose.addEventListener('click', closeMobileMenu);

  mobileNav.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', closeMobileMenu);
  });
}

/* =====================================================
   4. Navbar scroll behaviour
===================================================== */
const navInner = document.querySelector('.nav-inner');
function handleNavScroll() {
  if (window.scrollY > 50) {
    navInner?.classList.add('scrolled');
  } else {
    navInner?.classList.remove('scrolled');
  }
}
window.addEventListener('scroll', handleNavScroll, { passive: true });
handleNavScroll();

/* Active nav link via IntersectionObserver */
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav-link[href^="#"]');

const sectionObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const id = entry.target.id;
      navLinks.forEach(link => {
        link.classList.toggle('active', link.getAttribute('href') === `#${id}`);
      });
    }
  });
}, { rootMargin: '-40% 0px -55% 0px' });

sections.forEach(s => sectionObserver.observe(s));

/* =====================================================
   5. Scroll Reveal
===================================================== */
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });

document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

/* =====================================================
   6. Skill bars — fill on scroll into view
===================================================== */
const skillBarObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const el = entry.target;
      el.style.width = el.dataset.width + '%';
      skillBarObserver.unobserve(el);
    }
  });
}, { threshold: 0.4 });

document.querySelectorAll('.skill-bar-fill').forEach(el => skillBarObserver.observe(el));

/* =====================================================
   7. Glow-card mouse-follow radial gradient
===================================================== */
document.querySelectorAll('.glow-card').forEach(card => {
  card.addEventListener('mousemove', (e) => {
    const rect = card.getBoundingClientRect();
    card.style.setProperty('--mx', (e.clientX - rect.left) + 'px');
    card.style.setProperty('--my', (e.clientY - rect.top) + 'px');
  });
});

/* =====================================================
   8. Certificate Modal
===================================================== */
const certModal      = document.getElementById('certModal');
const certModalClose = document.getElementById('certModalClose');
const certModalImg   = document.getElementById('certModalImg');
const certModalTitle = document.getElementById('certModalTitle');
const certModalMeta  = document.getElementById('certModalMeta');
const certModalLink  = document.getElementById('certModalLink');

function openCertModal(data) {
  if (!certModal) return;
  certModalImg.src   = data.image || '';
  certModalImg.style.display = data.image ? 'block' : 'none';
  certModalTitle.textContent = data.title || '';
  certModalMeta.textContent  = [data.issuer, data.date].filter(Boolean).join(' · ');
  if (data.url) {
    certModalLink.href = data.url;
    certModalLink.style.display = 'inline-flex';
  } else {
    certModalLink.style.display = 'none';
  }
  certModal.classList.add('open');
  document.body.style.overflow = 'hidden';
}
function closeCertModal() {
  if (!certModal) return;
  certModal.classList.remove('open');
  document.body.style.overflow = '';
}

if (certModalClose) certModalClose.addEventListener('click', closeCertModal);
certModal?.addEventListener('click', (e) => {
  if (e.target === certModal) closeCertModal();
});
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') closeCertModal();
});

document.querySelectorAll('.cert-card[data-cert]').forEach(card => {
  card.addEventListener('click', () => {
    const d = card.dataset;
    openCertModal({ title: d.certTitle, issuer: d.certIssuer, date: d.certDate, image: d.certImage, url: d.certUrl });
  });
  card.setAttribute('role', 'button');
  card.setAttribute('tabindex', '0');
  card.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); card.click(); }
  });
});

/* =====================================================
   9. Terminal Typing Effect
===================================================== */
const terminalOutput = document.getElementById('terminalOutput');
const TERMINAL_LINES = window.TERMINAL_LINES || [];

let termTimeout = null;

function startTerminal() {
  if (!terminalOutput || !TERMINAL_LINES.length) return;
  clearTimeout(termTimeout);
  terminalOutput.innerHTML = '';
  let lineIdx = 0, charIdx = 0, html = '';

  function typeNext() {
    if (lineIdx >= TERMINAL_LINES.length) {
      termTimeout = setTimeout(startTerminal, 2800);
      return;
    }

    const raw = TERMINAL_LINES[lineIdx];
    const line = raw.raw || raw;
    const cls  = raw.cls  || detectClass(line);

    if (charIdx < line.length) {
      const partial = escHtml(line.slice(0, charIdx + 1));
      terminalOutput.innerHTML = html + `<span class="${cls}">${partial}</span>`;
      charIdx++;
      termTimeout = setTimeout(typeNext, 18 + Math.random() * 26);
    } else {
      html += `<span class="${cls}">${escHtml(line)}</span>\n`;
      terminalOutput.innerHTML = html;
      lineIdx++; charIdx = 0;
      termTimeout = setTimeout(typeNext, 360);
    }
  }
  typeNext();
}

function detectClass(line) {
  if (line.startsWith('$ '))  return 'cmd';
  if (line.startsWith('> '))  return 'val';
  if (line.startsWith('✓ '))  return 'ok';
  return '';
}

function escHtml(str) {
  return str.replace(/[&<>"']/g, m => ({ '&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;' }[m]));
}

// Start once DOM ready
document.addEventListener('DOMContentLoaded', startTerminal);

/* =====================================================
   10. Background Canvas — Developer Symbols + Particles
===================================================== */
(function initBg() {
  const canvas = document.getElementById('bg-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  const SYMBOLS = ['{ }', '< />', '( )', '#', '$', '=>', '[ ]', '&&', '||', '//', '01', '==', '!=', '++'];
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  let W, H, mouseX = -9999, mouseY = -9999;
  let particles = [], symbols = [];

  function resize() {
    W = canvas.width  = window.innerWidth;
    H = canvas.height = window.innerHeight;
    initParticles();
    initSymbols();
  }

  function rand(min, max) { return min + Math.random() * (max - min); }

  function initParticles() {
    const count = reducedMotion ? 0 : Math.min(80, Math.floor((W * H) / 18000));
    particles = Array.from({ length: count }, () => ({
      x: rand(0, W), y: rand(0, H),
      vx: rand(-0.18, 0.18), vy: rand(-0.18, 0.18),
      r: rand(0.6, 1.8),
    }));
  }

  function initSymbols() {
    const count = reducedMotion ? 0 : Math.min(18, Math.floor((W * H) / 55000));
    symbols = Array.from({ length: count }, () => ({
      x: rand(0, W), y: rand(0, H),
      vx: rand(-0.08, 0.08), vy: rand(-0.06, 0.06),
      text: SYMBOLS[Math.floor(Math.random() * SYMBOLS.length)],
      opacity: rand(0.03, 0.09),
      size: rand(11, 18),
      rotation: rand(-0.3, 0.3),
      rotSpeed: rand(-0.0008, 0.0008),
    }));
  }

  function getAccentColor() {
    const isDark = document.documentElement.getAttribute('data-theme') !== 'light';
    return isDark ? '0,232,122' : '0,153,85';
  }

  function draw() {
    ctx.clearRect(0, 0, W, H);
    const color = getAccentColor();

    /* --- Floating code symbols --- */
    symbols.forEach(s => {
      if (!reducedMotion) {
        s.x = (s.x + s.vx + W) % W;
        s.y = (s.y + s.vy + H) % H;
        s.rotation += s.rotSpeed;
      }
      ctx.save();
      ctx.translate(s.x, s.y);
      ctx.rotate(s.rotation);
      ctx.font = `${s.size}px 'JetBrains Mono', monospace`;
      ctx.fillStyle = `rgba(${color},${s.opacity})`;
      ctx.fillText(s.text, 0, 0);
      ctx.restore();
    });

    /* --- Particles --- */
    particles.forEach(p => {
      if (!reducedMotion) {
        p.x = (p.x + p.vx + W) % W;
        p.y = (p.y + p.vy + H) % H;

        // subtle attraction towards mouse
        const dx = mouseX - p.x, dy = mouseY - p.y;
        const dist = Math.hypot(dx, dy);
        if (dist < 140) {
          p.x -= dx * 0.0015;
          p.y -= dy * 0.0015;
        }
      }
    });

    // connecting lines
    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        const a = particles[i], b = particles[j];
        const d = Math.hypot(a.x - b.x, a.y - b.y);
        if (d < 120) {
          ctx.strokeStyle = `rgba(${color},${(1 - d / 120) * 0.14})`;
          ctx.lineWidth = 0.8;
          ctx.beginPath();
          ctx.moveTo(a.x, a.y);
          ctx.lineTo(b.x, b.y);
          ctx.stroke();
        }
      }
    }

    // dots
    particles.forEach(p => {
      const dx = mouseX - p.x, dy = mouseY - p.y;
      const dist = Math.hypot(dx, dy);
      const boost = dist < 140 ? (1 - dist / 140) : 0;
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r + boost * 1.2, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(${color},${0.3 + boost * 0.5})`;
      ctx.shadowColor = `rgba(${color},0.7)`;
      ctx.shadowBlur  = boost * 10;
      ctx.fill();
    });
    ctx.shadowBlur = 0;

    requestAnimationFrame(draw);
  }

  window.addEventListener('resize', resize, { passive: true });
  window.addEventListener('mousemove', e => { mouseX = e.clientX; mouseY = e.clientY; }, { passive: true });
  window.addEventListener('mouseleave', () => { mouseX = -9999; mouseY = -9999; });
  window.addEventListener('touchmove', e => {
    if (e.touches[0]) { mouseX = e.touches[0].clientX; mouseY = e.touches[0].clientY; }
  }, { passive: true });

  resize();
  draw();
})();

/* =====================================================
   11. Smooth scroll for anchor links
===================================================== */
document.querySelectorAll('a[href^="#"]').forEach(link => {
  link.addEventListener('click', (e) => {
    const target = document.querySelector(link.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});
