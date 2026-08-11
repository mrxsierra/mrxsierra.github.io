---
description: Personal & Portfolio website of Sunil Sharma - Full-Stack & AI Systems Engineer
hide:
  - tags
  - footer
  - navigation
  - toc
tags:
  - Welcome
---
<!-- markdownlint-disable MD041 -->
<div class="main-body">

<!-- Welcome Banner Quote -->
<blockquote id="wel-quote">
    <h3 id="welcome">
    <i class="fas fa-quote-left"></i>
    Welcome to my Engineering Portfolio &amp; Technical Hub
    <i class="fas fa-quote-right"></i>
    </h3>
</blockquote>

<!-- Hero Section -->
<section>
    <div class="hero-content">
        <h1 id="intro">Hi, I'm <span class="highlight" style="font-size: 2.8em;" id="name">Sunil Sharma</span> 👋</h1>
        <h2>Full-Stack &amp; AI Systems Engineer</h2>
        <p>
            Architecting autonomous agent workflows, high-performance web applications, and scalable developer tools.
        </p>
        
        <!-- Terminal Summary Preview Widget -->
        <div class="terminal-widget">
            <div class="terminal-header">
                <span class="dot red"></span>
                <span class="dot yellow"></span>
                <span class="dot green"></span>
                <span class="terminal-title">mrxsierra ~ bash</span>
            </div>
            <div class="terminal-body">
                <p class="cmd"><span class="prompt">$</span> npx mrxsierra --summary</p>
                <p class="res"><span class="key">&gt; Role   :</span> Full-Stack &amp; AI Systems Specialist</p>
                <p class="res"><span class="key">&gt; Stack  :</span> Python • TypeScript • React • LangGraph • FastAPI • Docker</p>
                <p class="res"><span class="key">&gt; Status :</span> Open for High-Impact Projects &amp; Remote Roles 🚀</p>
            </div>
        </div>

        <div style="margin-top: 25px; display: flex; gap: 15px; flex-wrap: wrap; justify-content: center;">
            <a href="#projects" class="md-button md-button--primary" style="font-weight: 700;">View Proof of Work</a>
            <a href="mailto:9.sunilsharma@gmail.com" class="md-button" style="font-weight: 700;"><i class="fas fa-envelope"></i> Get in Touch</a>
            <a href="resume" class="md-button" style="font-weight: 700;"><i class="fas fa-file-alt"></i> Resume</a>
        </div>
    </div>
</section>

<!-- Navigation Bar Sticky -->
<div class="hero-links-container">
    <div class="hero-links">
        <a class="hero-link" href="#intro">Intro</a>
        <a class="hero-link" href="#projects">Projects</a>
        <a class="hero-link" href="#skills">Skills</a>
        <a class="hero-link" href="#blogs">Blogs</a>
        <a class="hero-link" href="#about">About</a>
        <a class="hero-link" href="#contact">Connect</a>
    </div>
</div>

<!-- Featured Projects Section -->
<section>
    <h2 id="projects"><i class="fas fa-rocket" style="color: var(--primary-color);"></i> Featured Projects</h2>
    <p>Production-grade software, ML pipelines, and cloud automation tools.</p>
    
    <div class="project-cards">
        
        <!-- Project 1: GSTN Hackathon -->
        <div class="project-card">
            <div class="project-content">
                <h3>GSTN Predictive Binary Classification</h3>
                <p>National-level hackathon finalist project — interpretable ML pipeline analyzing 900,000+ GST records.</p>
                <div class="pill-container">
                    <span class="skill-pill">Python</span>
                    <span class="skill-pill">Scikit-Learn</span>
                    <span class="skill-pill">XGBoost</span>
                </div>
                <a class="read-more" href="projects/gstn-pbc/#gstn-predictive-binary-classification">Case Study &rarr;</a>
            </div>
            <a class="project-link" href="projects/gstn-pbc/#gstn-predictive-binary-classification">
                <i class="fas fa-trophy"></i>
            </a>
        </div>

        <!-- Project 2: EMS DB -->
        <div class="project-card">
            <div class="project-content">
                <h3>Examination Management System DB</h3>
                <p>Multi-RDBMS exam management system with Python automation, Dockerized environments &amp; CI support.</p>
                <div class="pill-container">
                    <span class="skill-pill">PostgreSQL</span>
                    <span class="skill-pill">MySQL</span>
                    <span class="skill-pill">Docker</span>
                </div>
                <a class="read-more" href="projects/ems-db/#examination-management-system-database">Case Study &rarr;</a>
            </div>
            <a class="project-link" href="projects/ems-db/#examination-management-system-database">
                <i class="fas fa-database"></i>
            </a>
        </div>

        <!-- Project 3: S3 Faker -->
        <div class="project-card">
            <div class="project-content">
                <h3>S3 Faker Data Generator</h3>
                <p>High-performance mock data generator with direct AWS S3 and LocalStack integration for cloud testing.</p>
                <div class="pill-container">
                    <span class="skill-pill">Python</span>
                    <span class="skill-pill">AWS S3</span>
                    <span class="skill-pill">Boto3</span>
                </div>
                <a class="read-more" href="projects/s3-faker/#s3-faker">Case Study &rarr;</a>
            </div>
            <a class="project-link" href="projects/s3-faker/#s3-faker">
                <i class="fas fa-cloud-upload-alt"></i>
            </a>
        </div>

        <!-- Project 4: Paraxcel -->
        <div class="project-card">
            <div class="project-content">
                <h3>Paraxcel Toolkit</h3>
                <p>Python engine for high-throughput Excel data extraction, complex transformation, and automated reporting.</p>
                <div class="pill-container">
                    <span class="skill-pill">Python</span>
                    <span class="skill-pill">Pandas</span>
                    <span class="skill-pill">OpenPyXL</span>
                </div>
                <a class="read-more" href="projects/paraxcel/#paraxcel">Case Study &rarr;</a>
            </div>
            <a class="project-link" href="projects/paraxcel/#paraxcel">
                <i class="fas fa-file-excel"></i>
            </a>
        </div>

        <!-- Project 5: Naukri Scraper -->
        <div class="project-card">
            <div class="project-content">
                <h3>Naukri Web Scraper</h3>
                <p>Automated Selenium scraper for job market data extraction, telemetry analysis &amp; job aggregation.</p>
                <div class="pill-container">
                    <span class="skill-pill">Python</span>
                    <span class="skill-pill">Selenium</span>
                    <span class="skill-pill">BeautifulSoup</span>
                </div>
                <a class="read-more" href="projects/naukri-webscraper/#naukri-web-scraper">Case Study &rarr;</a>
            </div>
            <a class="project-link" href="projects/naukri-webscraper/#naukri-web-scraper">
                <i class="fas fa-spider"></i>
            </a>
        </div>

        <!-- Project 6: Test Site -->
        <div class="project-card">
            <div class="project-content">
                <h3>Test Management Web Site</h3>
                <p>Responsive web interface for real-time exam management, test scheduling, and student result tracking.</p>
                <div class="pill-container">
                    <span class="skill-pill">JavaScript</span>
                    <span class="skill-pill">HTML5</span>
                    <span class="skill-pill">CSS3</span>
                </div>
                <a class="read-more" href="projects/test-site/#test-management-site">Case Study &rarr;</a>
            </div>
            <a class="project-link" href="projects/test-site/#test-management-site">
                <i class="fas fa-clipboard-list"></i>
            </a>
        </div>

    </div>
    <div class="explore-button">
        <a href="projects/">Explore All Projects &rarr;</a>
    </div>
</section>

<!-- Skills Section -->
<section class="skill-section">
    <h2 id="skills"><i class="fas fa-microchip" style="color: var(--primary-color);"></i> Technical Stack &amp; Capabilities</h2>
    <p>Core engineering competencies across modern full-stack &amp; AI architectures.</p>
    <div class="skills-grid">
        
        <div class="skill-card">
            <div class="content">
                <h3>🤖 AI &amp; Autonomous Systems</h3>
                <p class="skill-list">
                    LLM Orchestration, Autonomous Agents, LangGraph, Scikit-Learn, XGBoost, Machine Learning Pipelines, Kaggle Tabular Modeling
                </p>
            </div>
            <i class="fas fa-robot skill-icon"></i>
        </div>

        <div class="skill-card">
            <div class="content">
                <h3>⚡ Full-Stack &amp; Web Engineering</h3>
                <p class="skill-list">
                    Python (FastAPI, Flask, Django), JavaScript, TypeScript, React, HTML5, CSS3, REST &amp; GraphQL APIs, Microservices
                </p>
            </div>
            <i class="fas fa-code skill-icon"></i>
        </div>

        <div class="skill-card">
            <div class="content">
                <h3>🗄️ Databases &amp; Storage Architecture</h3>
                <p class="skill-list">
                    PostgreSQL, MySQL, SQLite, MongoDB, AWS S3, Relational Schema Design, Query Optimization, Multi-RDBMS Automation
                </p>
            </div>
            <i class="fas fa-database skill-icon"></i>
        </div>

        <div class="skill-card">
            <div class="content">
                <h3>🛠️ DevOps &amp; Container Registries</h3>
                <p class="skill-list">
                    Docker, Git, GitHub Actions, Linux, Cloud Automation, LocalStack, PyPI Package Publishing, DockerHub
                </p>
            </div>
            <i class="fas fa-terminal skill-icon"></i>
        </div>

    </div>
</section>

<!-- Blogs Section -->
<section>
    <h2 id="blogs"><i class="fas fa-book-open" style="color: var(--primary-color);"></i> Featured Technical Writing</h2>
    <p>In-depth engineering post-mortems, database guides, and architectural breakdowns.</p>
    <div class="blog-cards">
        <div class="blog-card">
            <div class="blog-content">
                <h3>Navigating the Nuances: SQL Dialects</h3>
                <p>A Developer's Guide to SQL Dialects (SQLite, MySQL, PostgreSQL) — performance trade-offs, syntax nuances, and schema design.</p>
                <a class="read-more" href="blog/2025/05/07/navigating-the-nuances-a-developers-guide-to-sql-dialects-sqlite-mysql-postgresql/">Read Full Guide &rarr;</a>
            </div>
            <a class="blog-link" href="blog/2025/05/07/navigating-the-nuances-a-developers-guide-to-sql-dialects-sqlite-mysql-postgresql/">
                <i class="fas fa-code-branch"></i>
            </a>
        </div>
        <div class="blog-card">
            <div class="blog-content">
                <h3>Beyond the Schema: Database Querying</h3>
                <p>A Practical Guide to Querying and Interacting with SQLite, MySQL, &amp; PostgreSQL Databases programmatically in Python.</p>
                <a class="read-more" href="blog/2025/05/07/beyond-the-schema-a-practical-guide-to-querying-and-interacting-with-sqlite-mysql--postgresql/">Read Full Guide &rarr;</a>
            </div>
            <a class="blog-link" href="blog/2025/05/07/beyond-the-schema-a-practical-guide-to-querying-and-interacting-with-sqlite-mysql--postgresql/">
                <i class="fas fa-magnifying-glass"></i>
            </a>
        </div>
    </div>
    <div class="explore-button">
        <a href="blog/">Read All Blog Posts &rarr;</a>
    </div>
</section>

<!-- Connect & Social Grid Section -->
<section class="about-connect">
    <div class="about-section">
        <h2 id="about"><i class="fas fa-user-circle"></i> About Sunil Sharma</h2>
        <p>Full-Stack &amp; AI Systems Engineer passionate about high-leverage software, agentic workflows, and open-source development.</p>
        <div class="resume-link">
            <a href="resume">
                <i class="fas fa-file-alt"></i>
                Download Resume (PDF)
            </a>
        </div>
        <div class="explore-button">
            <a href="about">
                <i class="fas fa-id-card"></i>
            Full Story &amp; Bio &rarr;</a>
        </div>
    </div>

    <div class="connect-section">
        <h2 id="contact"><i class="fas fa-paper-plane"></i> Let's Connect</h2>
        <p>Explore my open-source code, developer profiles, and media channels across the web.</p>
        
        <div class="social-links-grid">
            <a href="https://github.com/mrxsierra" target="_blank" class="social-chip">
                <i class="fab fa-github"></i> GitHub
            </a>
            <a href="https://www.linkedin.com/in/sunilsharma97" target="_blank" class="social-chip">
                <i class="fab fa-linkedin"></i> LinkedIn
            </a>
            <a href="https://x.com/mrxsierra" target="_blank" class="social-chip">
                <i class="fab fa-x-twitter"></i> Twitter/X
            </a>
            <a href="https://kaggle.com/mrxsierra" target="_blank" class="social-chip">
                <i class="fab fa-kaggle"></i> Kaggle
            </a>
            <a href="https://dev.to/mrxsierra" target="_blank" class="social-chip">
                <i class="fab fa-dev"></i> Dev.to
            </a>
            <a href="https://medium.com/@mrxsierra" target="_blank" class="social-chip">
                <i class="fab fa-medium"></i> Medium
            </a>
            <a href="https://pypi.org/user/mrxsierra/" target="_blank" class="social-chip">
                <i class="fab fa-python"></i> PyPI
            </a>
            <a href="https://hub.docker.com/u/mrxsierra" target="_blank" class="social-chip">
                <i class="fab fa-docker"></i> DockerHub
            </a>
            <a href="https://www.youtube.com/@mrxsierra" target="_blank" class="social-chip">
                <i class="fab fa-youtube"></i> YouTube
            </a>
            <a href="https://www.reddit.com/user/mrxsierra/" target="_blank" class="social-chip">
                <i class="fab fa-reddit-alien"></i> Reddit
            </a>
            <a href="https://www.instagram.com/mrxsierra/" target="_blank" class="social-chip">
                <i class="fab fa-instagram"></i> Instagram
            </a>
        </div>

        <div class="explore-button" style="margin-top: 15px;">
            <a href="mailto:9.sunilsharma@gmail.com">
                <i class="fas fa-envelope"></i> Send Direct Email &rarr;
            </a>
        </div>
    </div>
</section>

</div>

<script>
window.addEventListener('scroll', function() {
    const nav = document.querySelector('.hero-links-container');
    if (window.scrollY > 100) {
        nav.classList.add('scrolled');
    } else {
        nav.classList.remove('scrolled');
    }
});
</script>
