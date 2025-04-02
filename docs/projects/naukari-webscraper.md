---
description: A job listings web scrapper.
date:
  created: Apr 2024
  updated: March 2025
---

# ***Naukari Webscraper***

??? tip "In-Hurry Summary"
    **Naukari Webscraper**  
    A Python-based tool to automate job searches on Naukri.com with skill-based filtering.

    - **Context:** `Personal Project`, `Sep 2023`, `Python`, `Selenium`, `Pandas`
    - **Role:** Sole developer responsible for designing, implementing, testing, and documenting the project
    - **Impact:** Automated job search and filtering, successfully scraped detailed job listings, and exported data to CSV for analysis

## ***Overview***

This project automates job searches on Naukri.com by scraping and filtering listings based on user-specified skills. It extracts detailed job information, including titles, companies, salaries, locations, and required skills, and saves the data in a structured CSV format for further analysis.

## ***Goals***

The primary objective was to simplify the job search process by automating the retrieval and filtering of job listings based on desired skills, solving the problem of manually sifting through numerous postings.

## ***Responsibilities***

As the sole developer, I was responsible for:

- Designing and implementing the web scraping logic using Selenium.
- Developing a skill-based filtering mechanism.
- Handling dynamic content loading challenges.
- Writing unit tests for code correctness.
- Documenting the project for future reference.

## ***Technologies Used***

- **Languages:** Python
- **Frameworks/Libraries:** Selenium, Pandas
- **Tools:** Git, Chrome WebDriver
- **Required Understanding:** HTML, CSS, JavaScript

## ***Process***

1. **Planning:** Identified key elements to scrape from Naukri.com, such as job titles, companies, and skills.
2. **Implementation:** Used Selenium for browser automation and Pandas for data manipulation and CSV export.
3. **Challenges:** Addressed dynamic content loading with explicit waits and implemented robust error handling for missing data.
4. **Testing:** Developed unit tests to ensure functionality and reliability.

## ***:crossed_swords: Challenges & :star2: Solutions***

1. **Dynamic Content Loading**  
    - **:crossed_swords:** Naukri.com relies heavily on JavaScript for rendering job listings.  
    - **:star2:** Used `WebDriverWait` to ensure all elements were fully loaded before extraction.

2. **Data Extraction**  
    - **:crossed_swords:** Extracting text from complex HTML structures.  
    - **:star2:** Created a custom `get_text_or_default` function for reliable text extraction.

3. **Performance Optimization**  
    - **:crossed_swords:** Slow scraping performance due to large datasets.  
    - **:star2:** Employed efficient data structures and parallel processing for faster execution.

## ***Achievements***

- Automated the scraping of detailed job listings from Naukri.com.
- Implemented a user-friendly filtering mechanism based on skills.
- Exported structured data to a CSV file for analysis.
- Developed a comprehensive test suite to ensure code reliability.

## ***Key Learnings***

- Gained expertise in web scraping with Selenium.
- Improved skills in handling dynamic content and data manipulation using Pandas.
- Learned the importance of robust error handling and testing in software development.

## ***Outcomes***

The project successfully automates job searches, allowing users to filter listings based on skills and export the data for analysis. It demonstrates the potential of automation in simplifying repetitive tasks.

## ***Visuals***

### Video Demo

[![Video Demo](https://img.youtube.com/vi/ls_uxjfADN4/maxresdefault.jpg)](https://www.youtube.com/watch?v=ls_uxjfADN4)

## ***Links***

- [GitHub Repository](https://github.com/code50/9698455/tree/main/CS50P/pset/project)

## ***Conclusion***

This project showcases the power of automation in solving real-world problems. By leveraging Selenium and Pandas, I created a tool that simplifies job searches, enhances productivity, and provides valuable insights through structured data.
