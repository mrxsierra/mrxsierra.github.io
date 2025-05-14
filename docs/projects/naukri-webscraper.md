---
date:
  created: Mar 2024
  updated: Apr 2025
tags:
    - Python
    - Web Scraping
    - Selenium
    - Automation
    - Data Analysis
---

# ***Naukri Webscraper***

??? tip "Quick Summary"
    **Naukri Webscraper**  
    A Python tool that automates job searches on Naukri.com, enabling users to filter listings by skills and export structured data for analysis.

    - **Context:** `Personal Project`, `Mar 2024`, `Python`, `Selenium`, `Pandas`
    - **Role:** Sole developer—designed, implemented, tested, and documented the project
    - **Impact:** Automated skill-based job search and CSV export, validated by automated tests and real-world data extraction

## ***Overview***

Naukri Webscraper is a Python-based automation tool that scrapes job listings from Naukri.com. It extracts job titles, companies, salaries, locations, and required skills, then filters results based on user-specified skills. The project outputs structured data as CSV files for further analysis.  
The project was developed independently as a personal automation and data analysis initiative.

!!! info "**Recent updates:**"
    - Added automated tests for core scraping and filtering logic (`test_project.py`) using `pytest`
    - Improved error handling and robustness in dynamic content extraction
    - Updated documentation and usage instructions in `README.md`

## ***Goals***

- Automate the retrieval and filtering of job listings from Naukri.com based on user-defined skills.
- Simplify and accelerate the job search process by eliminating manual filtering.
- Provide structured, exportable data for further analysis.

## ***Responsibilities***

- Designed and implemented the scraping logic using Selenium WebDriver.
- Developed skill-based filtering and CSV export using Pandas.
- Addressed dynamic content loading and missing data scenarios.
- Authored automated tests with `pytest` to ensure code correctness and reliability.
- Wrote comprehensive documentation and usage instructions.

## ***Technologies Used***

- **Languages:** Python (primary language for all scripts and logic)
- **Frameworks/Libraries:**  
    - Selenium (browser automation and web scraping)  
    - Pandas (data manipulation and CSV export)
- **Testing:**  
    - pytest (for automated tests in `test_project.py`)
- **DevOps/Tools:**  
    - Git (version control)
    - Chrome WebDriver (browser automation)
- **Documentation:**  
    - Markdown (`README.md` for usage and setup)

??? abstract "Tools"
    - Git (version control)
    - Chrome WebDriver (browser automation)
    - Markdown (project documentation)
    - pytest (automated testing)

## ***Process***

1. **Planning:**  
    - Identified key data fields (title, company, salary, location, skills) to extract from Naukri.com.
2. **Implementation:**  
    - Used Selenium to automate browser actions and extract job data.
    - Employed Pandas for data structuring and CSV export.
    - Developed a filtering mechanism for user-specified skills.
3. **Testing:**  
    - Created automated tests (`test_project.py`) using `pytest` to validate scraping and filtering logic.
4. **Documentation:**  
    - Documented setup, usage, and troubleshooting in `README.md`.

## **Recognition**

I am proud to share that I have successfully completed the `CS50P - Introduction to Programming with Python` course.

### Certificate

![CS50P - Introduction to Programming with Python](https://media.licdn.com/dms/image/v2/D562DAQH67rsjAX763w/profile-treasury-image-shrink_1920_1920/profile-treasury-image-shrink_1920_1920/0/1708063772979?e=1747832400&v=beta&t=W0ZkkvY7QYZbOHVDCEfLzxvUo3N0CqLoQV3Y3whZ0YM)

## ***:crossed_swords: Challenges & :star2: Solutions***

1. **Dynamic Content Loading**
    - **:crossed_swords:** Naukri.com uses JavaScript to render job listings, causing timing issues for scraping.
    - **:star2:** Used Selenium's `WebDriverWait` to ensure elements are loaded before extraction.

2. **Complex HTML Structures**
    - **:crossed_swords:** Extracting data from inconsistent or nested HTML elements.
    - **:star2:** Implemented a helper function (`get_text_or_default`) for robust text extraction.

3. **Performance Bottlenecks**
    - **:crossed_swords:** Slow scraping due to large result sets and dynamic content.
    - **:star2:** Optimized data extraction loops and used efficient Pandas operations for filtering/export.

4. **Testing Automation**
    - **:crossed_swords:** Ensuring scraping logic remains reliable as site structure changes.
    - **:star2:** Developed automated tests with `pytest` to validate core logic and catch regressions.

??? warning "***Note :*** On Site Changes and Locators"
    - The HTML structure and element locators (CSS selectors, XPaths) used in `project.py` are based on the current version of Naukri.com.  
    - If the website updates its layout or class names, you may need to update these locators in the code to restore scraping functionality.  
    - Review and adjust selectors in `project.py` if you encounter errors or missing data after a site update.

## ***Achievements***

- Automated the extraction and filtering of job listings from Naukri.com.
- Enabled skill-based filtering and CSV export for downstream analysis.
- Developed a test suite (`test_project.py`) using `pytest` to ensure reliability.
- Improved scraping robustness and error handling based on real-world site changes.

## ***Key Learnings***

- Gained practical experience with Selenium for dynamic web scraping.
- Enhanced skills in data manipulation and export using Pandas.
- Learned to write maintainable, testable code for web automation projects.
- Understood the importance of robust error handling and documentation.
- Applied `pytest` for effective and maintainable automated testing.

## ***Outcomes***

- Successfully automated job search and filtering for Naukri.com.
- Produced structured CSV datasets for analysis.
- Provided a reusable, documented tool for job seekers and data analysts.
- Ensured code reliability through automated testing with `pytest`.

## ***Visuals***

### Video Demo

[![Video Demo](https://img.youtube.com/vi/ls_uxjfADN4/maxresdefault.jpg)](https://www.youtube.com/watch?v=ls_uxjfADN4)

## ***Links***

- [GitHub Repository](https://github.com/mrxsierra/naukari-webscraper)

## ***Conclusion***

Naukri Webscraper demonstrates the power of Python automation for real-world data extraction and analysis. By combining Selenium and Pandas, the project streamlines job searches, enhances productivity, and provides actionable insights through structured data exports. The codebase is robust, tested with `pytest`, and well-documented for future use and extension.

??? summary "**AI Skill Assessment**"
    Prompt[^1] Source [:material-file-eye-outline:{ #source }](https://raw.githubusercontent.com/mrxsierra/mrxsierra.github.io/blob/main/prompts/skill-assesment-prompt.md)
    [^1]:
    This `AI skill assessment` was generated based on the [skill-assessment-prompt.md](https://raw.githubusercontent.com/mrxsierra/mrxsierra.github.io/main/prompts/skill-assesment-prompt.md) and the provided project documentation. It is intended as an illustrative summary and should be interpreted in the context of the available code and documentation in codebase.

    ### **Strengths**

    - **Web Scraping Automation**
        - Demonstrates strong proficiency with Selenium for browser automation, including headless operation, custom user agents, and dynamic navigation (e.g., paginated scraping, handling search forms).
        - Robust handling of web elements using both CSS selectors and XPaths, with fallback/default logic for missing elements.

    - **Data Handling & Export**
        - Uses Pandas effectively for data manipulation and CSV export.
        - Implements structured data extraction with a clear schema (job title, company, salary, skills, etc.).

    - **Testing & Quality Assurance**
        - Provides automated tests using `pytest`, including fixtures, mocking user input, and live web tests (with appropriate skips for anti-bot/site change issues).
        - Tests cover both core scraping logic and utility functions.

    - **Documentation**
        - Comprehensive technical documentation (`doc.md`) and user-facing README.md with clear instructions, schema definitions, troubleshooting, and usage examples.
        - Documents function purposes, parameters, and expected behaviors in code docstrings.

    - **User Interaction & Error Handling**
        - Interactive CLI prompts for user input (search terms, page count, skill filters).
        - Handles invalid input and exceptions gracefully (e.g., `KeyboardInterrupt`, `ValueError`, missing elements).

    - **Project Structure & Packaging**
        - Uses pyproject.toml for dependency management and project metadata.
        - Separates main logic, tests, and documentation cleanly.

    ---

    ### **Areas for Growth**

    - **Security & Anti-Bot Evasion**
        - No evidence of advanced anti-bot evasion techniques (e.g., proxy rotation, CAPTCHA handling, request throttling beyond simple sleep).
        - No explicit handling of robots.txt or ethical scraping considerations in code.

    - **Scalability & Performance**
        - Scraping is single-threaded and synchronous; not optimized for large-scale or parallel scraping.
        - No batching, queuing, or distributed scraping logic.

    - **CI/CD & DevOps**
        - No evidence of CI/CD pipelines, Dockerization, or deployment automation.
        - No Makefile or scripts for environment setup/testing.

    - **Code Modularity & Extensibility**
        - All logic is in a single script (`project.py`); could benefit from modularization (e.g., separating scraping, filtering, and CLI logic).
        - No plugin or configuration system for adapting to site changes.

    - **Error Logging & Monitoring**
        - Uses print statements for errors; lacks structured logging or monitoring for production use.

    - **GUI/UX**
        - No GUI or web interface; CLI-only interaction.

    ---

    ### **Role Suitability**

    #### **Best Fit Roles**

    - **Python Backend Developer**
        - Strong evidence of backend scripting, data processing, and automation skills.
    - **Web Scraping/Data Extraction Engineer**
        - Demonstrated expertise in Selenium, data extraction, and handling dynamic web content.
    - **QA Automation Engineer**
        - Experience with automated testing, mocking, and test-driven development using `pytest`.
    - **Technical Writer/Documentation Specialist**
        - High-quality, thorough documentation and user guides.

    #### **Well-Suited For**

    - **Data Analyst (with Python)**
        - Familiarity with Pandas and CSV data workflows.
    - **SDET (Software Development Engineer in Test)**
        - Automated test coverage and test design.

    #### **Less Suited For**

    - **Frontend Developer**
        - No evidence of frontend/UI development (web or desktop).
    - **DevOps Engineer**
        - Lacks CI/CD, containerization, and deployment automation.
    - **Cloud/Distributed Systems Engineer**
        - No cloud integration, distributed scraping, or scalable architecture.

    ---

    **Summary:**  
    The developer demonstrates strong skills in Python scripting, web scraping automation with Selenium, data processing with Pandas, and automated testing with `pytest`. The codebase is well-documented and user-friendly, with robust error handling and interactive CLI features. Areas for growth include modularization, scalability, advanced anti-bot techniques, and DevOps practices. The developer is best suited for backend, automation, and data extraction roles, and less suited for frontend or DevOps-focused positions based on the current codebase.

    ---
