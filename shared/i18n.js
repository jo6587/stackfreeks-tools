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
    nav_back: '← all tools',
    // Vultr banner
    vultr_label: 'Sponsor',
    vultr_title: 'Get started on Vultr',
    vultr_sub: '$100 free credit for new accounts',
    vultr_cta: 'Try Vultr →',
    // Footer
    footer_copy: '© 2026 StackFreeks',
  },
  ko: {
    // Navbar
    nav_back: '← 전체 툴',
    // Vultr banner
    vultr_label: '스폰서',
    vultr_title: 'Vultr로 시작하세요',
    vultr_sub: '신규 가입 시 $100 크레딧 무료',
    vultr_cta: 'Vultr 시작하기 →',
    // Footer
    footer_copy: '© 2026 StackFreeks',
  }
};

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
    toggle: function () {
      lang = lang === 'en' ? 'ko' : 'en';
      localStorage.setItem('sf-lang', lang);
      applyLang();
      document.dispatchEvent(new CustomEvent('sfLangChanged', { detail: { lang: lang } }));
    }
  };

  document.addEventListener('DOMContentLoaded', applyLang);
})();
