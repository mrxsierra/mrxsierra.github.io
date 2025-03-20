--- 
hide:
  - tags
  - footer
  - navigation
  - toc
tags:
  - Welcome
background: none
---

<div class="hero-wrapper">
  <h1 style="font-size:1.5em;" id="welcome">Hey there Hello..! Welcome to my Portfolio</h1>
  <script>
    document.addEventListener('DOMContentLoaded', function() {
      function typeWriter(text, targetId, speed) {
        let index = 0;
        const target = document.getElementById(targetId);

        function type() {
          if (index < text.length) {
            target.innerHTML += text.charAt(index);
            index++;
            setTimeout(type, speed);
          }
        }

        target.innerHTML = '';
        type();
      }

      typeWriter("Hey there Hello..! and Welcome to my Portfolio", 'welcome', 10);
      typeWriter("Sunil Sharma", 'name', 100);
      typeWriter("I'm thrilled to have you here. Explore my projects, read my blogs, and get to know more about me.", 'explore', 10);
    });
  </script>
  <div class="hero-content">
    <h2 style="font-size: 2em;">Hi, I'm <span class="highlight" style="font-size: 3em;" id="name">Sunil Sharma</span></h2>
    <p>
      I’m a passionate <span style="background-color: yellow; color:black;">Python Developer</span> and <span style="background-color: yellow; color:black;">Data Scientist</span> who loves crafting innovative solutions and sharing my journey through engaging stories.
    </p>
  </div>
  <div class="hero-links">
    <a class="hero-link" href="projects/">Projects</a>
    <a class="hero-link" href="blog/">Blogs</a>
    <a class="hero-link" href="about">About Me</a>
    <a class="hero-link" href="contact">Contact</a>
  </div>
<blockquote style="background-color:rgba(0,10,255,0.8);color:black;opacity:0.9">
  <h2 style="font-size:1.5em; text-align:center; color:yellow;" id="explore">>> I'm thrilled to have you here. Explore my projects, read my blogs, and get to know more about me. <<</h2>
</blockquote>
<section class="features">
  <div class="feature-card">
    <h3>Projects</h3>
    <p>Discover innovative projects where technology meets creativity.</p>
    <a href="projects/">Explore Projects</a>
  </div>
  <div class="feature-card">
    <h3>Blogs</h3>
    <p>Read my latest insights on development, data science, and tech trends.</p>
    <a href="blog/">Read Blogs</a>
  </div>
  <div class="feature-card">
    <h3>About Me</h3>
    <p>Learn more about my journey, skills, and experiences in tech.</p>
    <a href="about">Get to Know Me</a>
  </div>
  <div class="feature-card">
    <h3>Contact</h3>
    <p>Have a question or a collaboration idea? Let’s connect!</p>
    <a href="contact/">Reach Out</a>
  </div>
</section>

<!-- filepath: d:\work\project\mrxsierra.github.io\docs\index.md -->
<style>
  :root {
    /* Base colors and gradients */
    --primary-color: #036eda;
    --text-color:rgb(8, 8, 8);
    --hero-bg-light: linear-gradient(135deg, rgba(124, 146, 192, 0.05), rgba(221, 194, 247, 0.01));
    --hero-bg-dark: linear-gradient(135deg, rgba(9, 218, 255, 0.02), rgba(130, 159, 255, 0.01));
    --bg-overlay-light: rgba(189, 174, 248, 0.1);
    --bg-overlay-dark: rgba(137, 8, 250, 0.1);
    /* Highlight gradient for light theme */
    --highlight-gradient-light: linear-gradient(130deg, rgb(71, 7, 247), rgba(149, 0, 248, 0.62));
    /* Highlight gradient for dark theme */
    --highlight-gradient-dark: linear-gradient(90deg, rgb(125, 167, 252), rgb(106, 133, 253));
    /* Default variables (will be overridden by dark mode if needed) */
    --hero-bg: var(--hero-bg-light);
    --bg-overlay: var(--bg-overlay-light);
    --highlight-gradient: var(--highlight-gradient-light);
    
    /* Text sizes */
    --hero-title-size: 2.8em;
    --hero-subtitle-size: 2em;
    --hero-text-size: 1.2em;
    --link-size: 1.1em;
  }
  /* Dark mode overrides */ 
  @media (prefers-color-scheme: dark) {
    :root {
      --hero-bg: var(--hero-bg-dark);
      --bg-overlay: var(--bg-overlay-dark);
      --highlight-gradient: var(--highlight-gradient-dark);
    }
  }

  body {
    font-family: 'Poppins', sans-serif;
    margin: 0;
    padding: 0;
  }
  /* Full-width hero section */
  .hero-wrapper {
    width: 100%;
    background: var(--hero-bg);
    padding: 60px 20px;
    text-align: center;
    border-radius: 10px;
    transition: background 0.3s ease;
    box-sizing: border-box;
  }
  .hero-content {
    max-width: 900px;
    margin: auto;
    padding: 30px;
    background: var(--bg-overlay);
    border-radius: 10px;
  }
  h1 {
    font-size: var(--hero-title-size);
    color: var(--text-color);
    margin-bottom: 0.3em;
  }
  h2 {
    font-size: var(--hero-subtitle-size);
    color: var(--primary-color);
    margin-bottom: 0.5em;
  }
  p {
    font-size: var(--hero-text-size);
    color: var(--md-default-fg-color);
    line-height: 1.5;
  }
  .highlight {
    font-weight: bold;
    background: var(--highlight-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    color: transparent; /* Ensure text color is transparent */
  }
  .hero-links {
    margin-top: 20px;
    display: inline-flex;
    flex-wrap: wrap;
    gap: 15px;
    justify-content: center;
  }
  .hero-link {
    font-size: var(--link-size);
    font-weight: bold;
    color: var(--primary-color);
    text-decoration: underline;
    transition: color 0.3s ease;
  }
  .hero-link:hover {
    color: var(--primary-color);
  }
  /* Responsive features grid */
  .features {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 20px;
    max-width: 1200px;
    margin: 40px auto;
    padding: 0 20px;
    box-sizing: border-box;
  }
  @media (max-width: 1024px) {
    .features {
      grid-template-columns: repeat(2, 1fr);
    }
  }
  @media (max-width: 600px) {
    .features {
      grid-template-columns: 1fr;
    }
  }
  .feature-card {
    background: var(--md-default-bg-color);
    padding: 20px;
    border: 1px solid var(--primary-color);
    border-radius: 8px;
    text-align: center;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }
  .feature-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  }
  .feature-card h3 {
    color: var(--primary-color);
  }
  .feature-card a {
    display: inline-block;
    margin-top: 15px;
    padding: 8px 16px;
    background: var(--primary-color);
    color: #121212;
    text-decoration: none;
    border-radius: 5px;
    font-weight: bold;
    transition: background 0.3s ease;
  }
  .feature-card a:hover {
    background: var(--accent-color);
  }
</style>
