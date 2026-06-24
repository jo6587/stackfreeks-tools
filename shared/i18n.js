// /shared/i18n.js — StackFreeks Tools multilingual support (EN / KO)
// Usage:
//   1. Add <script src="/shared/i18n.js"></script> before </body>
//   2. Add data-i18n="key" to text elements you want translated
//   3. Add class="lang-en" or class="lang-ko" to block-level content sections
//   4. Add <button class="lang-toggle" onclick="sfLang.toggle()"> in navbar
//   5. Optionally define window.SF_PAGE_I18N = { en: {...}, ko: {...} } before this script
//      to add page-specific translation keys

const SF_I18N = {
  en: {
    // Navbar
    nav_back: '← All Tools',
    // Vultr banner
    vultr_label: 'Sponsor',
    vultr_title: 'Get started on Vultr',
    vultr_sub: 'Get $300 free credit — valid for 30 days (limited-time offer)',
    vultr_cta: 'Claim your credit →',
    // Footer
    footer_copy: '© 2026 StackFreeks',
  },
  ko: {
    // Navbar
    nav_back: '← 전체 툴',
    // Vultr banner
    vultr_label: '스폰서',
    vultr_title: 'Vultr로 시작하세요',
    vultr_sub: '$300 무료 크레딧 — 가입 후 30일 유효 (한정 기간)',
    vultr_cta: '크레딧 받기 →',
    // Footer
    footer_copy: '© 2026 StackFreeks',
  }
};

// Ensure [hidden] beats any author display: rule (display: grid, block, flex, etc.)
(function () {
  var s = document.createElement('style');
  s.textContent = '[hidden] { display: none !important; }';
  document.head.appendChild(s);
})();

(function () {
  // Detect language: localStorage > browser preference > default EN
  let lang = localStorage.getItem('sf-lang') ||
    (navigator.language.startsWith('ko') ? 'ko' : 'en');

  function applyLang() {
    // Merge shared + page-specific translations
    const t = Object.assign({}, SF_I18N[lang], (window.SF_PAGE_I18N || {})[lang]);

    // Update data-i18n text content
    document.querySelectorAll('[data-i18n]').forEach(function (el) {
      if (t[el.dataset.i18n] != null) el.textContent = t[el.dataset.i18n];
    });

    // Update data-i18n-placeholder
    document.querySelectorAll('[data-i18n-placeholder]').forEach(function (el) {
      if (t[el.dataset.i18nPlaceholder] != null) el.placeholder = t[el.dataset.i18nPlaceholder];
    });

    // Show/hide language blocks
    document.querySelectorAll('.lang-en').forEach(function (el) { el.hidden = lang !== 'en'; });
    document.querySelectorAll('.lang-ko').forEach(function (el) { el.hidden = lang !== 'ko'; });

    // Update toggle button label (shows the OTHER language)
    document.querySelectorAll('.lang-toggle').forEach(function (btn) {
      btn.textContent = lang === 'en' ? '한국어' : 'English';
    });

    // Update html[lang] attribute for accessibility / SEO
    document.documentElement.lang = lang === 'ko' ? 'ko' : 'en';
  }

  window.sfLang = {
    get current() { return lang; },
    apply: applyLang,
    toggle: function () {
      lang = lang === 'en' ? 'ko' : 'en';
      localStorage.setItem('sf-lang', lang);
      applyLang();
      document.dispatchEvent(new CustomEvent('sfLangChanged', { detail: { lang: lang } }));
    }
  };

  document.addEventListener('DOMContentLoaded', applyLang);
})();
