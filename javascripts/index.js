/**
 * Clean Productivity Interface - Interactive Enhancements
 * Supports MkDocs instant navigation, sticky active-state observation, and zero CLS.
 */

(function () {
  function initHomePageInteractions() {
    const navPills = document.querySelectorAll('.subnav-pill');
    const sections = document.querySelectorAll('.home-section, .hero-container');

    if (!navPills.length || !sections.length) return;

    // IntersectionObserver for active subnav state
    const observerOptions = {
      root: null,
      rootMargin: '-20% 0px -70% 0px',
      threshold: 0
    };

    const sectionObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const currentId = entry.target.getAttribute('id');
          navPills.forEach((pill) => {
            const href = pill.getAttribute('href');
            if (href === `#${currentId}`) {
              pill.classList.add('active');
            } else {
              pill.classList.remove('active');
            }
          });
        }
      });
    }, observerOptions);

    sections.forEach((sec) => {
      if (sec.id) sectionObserver.observe(sec);
    });
  }

  // Run on initial load
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initHomePageInteractions);
  } else {
    initHomePageInteractions();
  }

  // MkDocs instant navigation integration (observable subscription or DOM subscription)
  if (window.document$) {
    window.document$.subscribe(function () {
      initHomePageInteractions();
    });
  }
})();