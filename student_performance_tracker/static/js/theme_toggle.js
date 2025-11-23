// Theme toggle (persist with localStorage)
(function () {
  const root = document.documentElement;
  const themeToggle = document.getElementById('themeToggle');
  const themeIcon = document.getElementById('themeIcon');

  function setLightIcon() {
    themeIcon.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1M4.22 4.22l.71.71M18.36 18.36l.71.71M1 12h1m20 0h1M4.22 19.78l.71-.71M18.36 5.64l.71-.71"/>';
  }
  function setDarkIcon() {
    themeIcon.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12.79A9 9 0 1111.21 3 7 7 0 0021 12.79z"/>';
  }

  function applyTheme(t) {
    if (t === 'dark') {
      document.documentElement.classList.add('dark');
      setDarkIcon();
    } else {
      document.documentElement.classList.remove('dark');
      setLightIcon();
    }
  }

  const saved = localStorage.getItem('spt_theme') || (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  applyTheme(saved);

  themeToggle?.addEventListener('click', () => {
    const isDark = document.documentElement.classList.contains('dark');
    const newTheme = isDark ? 'light' : 'dark';
    applyTheme(newTheme);
    localStorage.setItem('spt_theme', newTheme);
  });
})();
