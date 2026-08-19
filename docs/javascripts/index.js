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

  /**
   * Social Sharing Interactive Module
   * Generates dynamic sharing links, handles native Web Share API, and provides 1-click clipboard copy.
   */
  function initSocialSharing() {
    const shareWidget = document.getElementById('social-share-widget');
    if (!shareWidget) return;

    const currentUrl = window.location.href;
    const pageTitle = document.title || 'Sunil Sharma (mrxsierra)';
    const encodedUrl = encodeURIComponent(currentUrl);
    const encodedTitle = encodeURIComponent(pageTitle);

    // Native Web Share API
    const btnNative = document.getElementById('btn-share-native');
    if (btnNative) {
      if (navigator.share) {
        btnNative.style.display = 'inline-flex';
        btnNative.onclick = async (e) => {
          e.preventDefault();
          try {
            await navigator.share({
              title: pageTitle,
              text: document.querySelector('meta[name="description"]')?.content || pageTitle,
              url: currentUrl
            });
          } catch (err) {
            // User cancelled or share failed silently
          }
        };
      } else {
        btnNative.style.display = 'none';
      }
    }

    // Direct Intent Mapping
    const shareLinks = {
      'btn-share-x': `https://x.com/intent/post?text=${encodedTitle}&url=${encodedUrl}&via=mrxsierra`,
      'btn-share-linkedin': `https://www.linkedin.com/sharing/share-offsite/?url=${encodedUrl}`,
      'btn-share-reddit': `https://www.reddit.com/submit?url=${encodedUrl}&title=${encodedTitle}`,
      'btn-share-pinterest': `https://pinterest.com/pin/create/button/?url=${encodedUrl}&description=${encodedTitle}`,
      'btn-share-hn': `https://news.ycombinator.com/submitlink?u=${encodedUrl}&t=${encodedTitle}`,
      'btn-share-whatsapp': `https://api.whatsapp.com/send?text=${encodedTitle}%20${encodedUrl}`,
      'btn-share-telegram': `https://t.me/share/url?url=${encodedUrl}&text=${encodedTitle}`
    };

    Object.entries(shareLinks).forEach(([id, targetUrl]) => {
      const btn = document.getElementById(id);
      if (btn) {
        btn.setAttribute('href', targetUrl);
        btn.onclick = (e) => {
          e.preventDefault();
          const width = 600;
          const height = 520;
          const left = Math.max(0, (window.innerWidth - width) / 2 + window.screenX);
          const top = Math.max(0, (window.innerHeight - height) / 2 + window.screenY);
          window.open(
            targetUrl,
            '_blank',
            `toolbar=no,location=no,status=no,menubar=no,scrollbars=yes,resizable=yes,width=${width},height=${height},top=${top},left=${left}`
          );
        };
      }
    });

    // RSS Feed Button
    const btnRss = document.getElementById('btn-share-rss');
    if (btnRss) {
      let rssUrl = 'https://mrxsierra.github.io/feed_rss_created.xml';
      if (window.location.pathname.includes('/blog/')) {
        rssUrl = 'https://mrxsierra.github.io/feed_blog.xml';
      } else if (window.location.pathname.includes('/projects/')) {
        rssUrl = 'https://mrxsierra.github.io/feed_projects.xml';
      }
      btnRss.setAttribute('href', rssUrl);
    }

    // 1-Click Clipboard Copy Button
    const btnCopy = document.getElementById('btn-share-copy');
    const toast = document.getElementById('share-copy-toast');
    const btnCopyText = document.getElementById('copy-btn-text');

    if (btnCopy) {
      btnCopy.onclick = async (e) => {
        e.preventDefault();
        try {
          if (navigator.clipboard && navigator.clipboard.writeText) {
            await navigator.clipboard.writeText(currentUrl);
          } else {
            // Fallback for older environments
            const tempInput = document.createElement('input');
            tempInput.value = currentUrl;
            document.body.appendChild(tempInput);
            tempInput.select();
            document.execCommand('copy');
            document.body.removeChild(tempInput);
          }

          // Visual Button State
          if (btnCopyText) {
            const originalText = btnCopyText.textContent;
            btnCopyText.textContent = 'Copied!';
            btnCopy.classList.add('copied');
            setTimeout(() => {
              btnCopyText.textContent = originalText;
              btnCopy.classList.remove('copied');
            }, 2000);
          }

          // Toast notification
          if (toast) {
            toast.removeAttribute('hidden');
            toast.classList.add('show');
            setTimeout(() => {
              toast.classList.remove('show');
              setTimeout(() => {
                toast.setAttribute('hidden', '');
              }, 300);
            }, 2500);
          }
        } catch (err) {
          console.error('Failed to copy URL:', err);
        }
      };
    }
  }

  /**
   * Accessible Names & ARIA State Enhancer
   * Fulfills WCAG 2.1 AA requirements by ensuring search dialogs and progress bars have accessible labels.
   */
  function initA11yAttributes() {
    // Accessible names for role="dialog" search interfaces
    const searchDialogs = document.querySelectorAll('.md-search[role="dialog"]');
    searchDialogs.forEach((el) => {
      if (!el.getAttribute('aria-label') && !el.getAttribute('aria-labelledby')) {
        el.setAttribute('aria-label', 'Site Search');
      }
    });

    // Accessible names for role="progressbar" elements
    const progressBars = document.querySelectorAll('.md-progress[role="progressbar"]');
    progressBars.forEach((el) => {
      if (!el.getAttribute('aria-label') && !el.getAttribute('aria-labelledby')) {
        el.setAttribute('aria-label', 'Page loading progress');
      }
    });
  }

  function initAll() {
    initHomePageInteractions();
    initSocialSharing();
    initA11yAttributes();
  }

  // Run on initial load
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAll);
  } else {
    initAll();
  }

  // MkDocs instant navigation integration
  if (window.document$) {
    window.document$.subscribe(function () {
      initAll();
    });
  }
})();