---
date:
    created: Jun 2024
    updated: Mar 2025
tags:
    - Frontend
---

# Test Management Site

??? tip "In-Hurry Summary"
    **Test Management Site**
    A demo vanilla javascripting application for managing tests, enabling test creation, execution, and result tracking. Aims to showcase basic web application functionality using dynamic UI updates and local storage.

    - **Context:** `Personal Project`, `Jun 2024`, `HTML`, `CSS`, `JavaScript`, `Bootstrap`
    - **Role:** Sole Developer - Responsible for designing, developing, and implementing all features.
    - **Impact:** Demonstrated full-stack capabilities by creating a functional test management system, showcasing skills in UI design, dynamic content loading, and local data storage.

## ***Overview***

The Test Management Site is a demo vanilla javascripts application developed in April 2025 to showcase test management capabilities. It allows users to create, manage, take tests, and view results. The application uses HTML, CSS, JavaScript, and Bootstrap for a responsive and dynamic user interface.

## ***Goals***

- Provide a platform to create, update, and delete tests.
- Enable users to take tests with a specified duration.
- Display test results and history.
- Implement user management features like login, logout, and password changes.
- Showcase dynamic UI updates and local data storage.

## ***Responsibilities***

- Designed and developed the entire application from scratch.
- Implemented dynamic UI updates using JavaScript.
- Managed data storage using `localStorage`.
- Created user authentication and session management features.
- Integrated Bootstrap for responsive design and UI components.

## ***Technologies Used***

- **Languages:** JavaScript, HTML, CSS
- **Frameworks/Libraries:** Bootstrap, PapaParse, XLSX.js, Plotly.js
- **Tools:** Visual Studio Code, GitHub Actions (for CI/CD and static site deployment)
- **Browser APIs:** localStorage, sessionStorage, Fetch API
- **Other:** Modular JavaScript (ES6 modules), CSS custom properties, GitHub Pages (hosting)

## ***Process***

The project followed an iterative development approach. Initially, the basic HTML structure and CSS styling were set up. JavaScript was then used to dynamically load content, manage user sessions, and handle data storage. Bootstrap was integrated to ensure a responsive design. Challenges were addressed through continuous debugging and refinement of the code.

## ***:crossed_swords: Challenges & :star2: Solutions***

1. **Dynamic Content Loading**  
    - **:crossed_swords:** Loading and updating content dynamically using JavaScript.  
    - **:star2:** Used `fetch` API to load HTML templates and JavaScript to manipulate the DOM, ensuring smooth transitions and updates.

2. **Data Management with `localStorage`**  
    - **:crossed_swords:** Managing and persisting data using `localStorage`.  
    - **:star2:** Implemented functions to serialize and deserialize data, ensuring data integrity and persistence across sessions.

3. **Responsive Design**  
    - **:crossed_swords:** Ensuring the application is responsive across different devices.  
    - **:star2:** Utilized Bootstrap's grid system and CSS media queries to create a responsive layout.

## ***Achievements***

- Successfully implemented all core features: test management, test taking, results display, and user management.
- Created a dynamic and responsive user interface.
- Demonstrated proficiency in JavaScript, HTML, CSS, and Bootstrap.
- Implemented data persistence using `localStorage`.

## ***Key Learnings***

- Gained a deeper understanding of dynamic content loading and manipulation using JavaScript.
- Learned how to effectively use `localStorage` for data persistence.
- Improved skills in responsive web design using Bootstrap.
- Enhanced problem-solving abilities through debugging and refining the code.

## ***Outcomes***

The project resulted in a functional test management application that showcases dynamic UI updates and local data storage. The application allows users to create, manage, take tests, and view results.

## ***Visuals***

### Screenshot Project Images

Here are some images showcasing the project:

#### Login Page

![Login Page](https://raw.githubusercontent.com/mrxsierra/test-site/main/img/login.jpg)

#### Register Page

![Register Page](https://raw.githubusercontent.com/mrxsierra/test-site/main/img/register.jpg)

#### Test Selection

![Select Test](https://raw.githubusercontent.com/mrxsierra/test-site/main/img/select-test-to-take.jpg)

#### Test Page

![Test Page](https://raw.githubusercontent.com/mrxsierra/test-site/main/img/test-page.png)

#### Test Timeout

![Test Timeout](https://raw.githubusercontent.com/mrxsierra/test-site/main/img/test-time-out.png)

#### Dashboard

![Dashboard](https://raw.githubusercontent.com/mrxsierra/test-site/main/img/anamoly-dash.png)

#### User Management

![Change Password](https://raw.githubusercontent.com/mrxsierra/test-site/main/img/change-pass.png)

#### CRUD Operations

![Create Operation](https://raw.githubusercontent.com/mrxsierra/test-site/main/img/create.png)
![Read Operation](https://raw.githubusercontent.com/mrxsierra/test-site/main/img/Read.png)
![Update Operation](https://raw.githubusercontent.com/mrxsierra/test-site/main/img/update.png)
![Delete Operation](https://raw.githubusercontent.com/mrxsierra/test-site/main/img/delete.png)

#### Test Results

![Individual Test Result](https://raw.githubusercontent.com/mrxsierra/test-site/main/img/individual-test-result.png)
![Multi User Result Track](https://raw.githubusercontent.com/mrxsierra/test-site/main/img/multi-user-result-track.png)

#### Error Handling

![Unsupported Error](https://raw.githubusercontent.com/mrxsierra/test-site/main/img/unsupported-error.png)

## ***Links***

- [Live Project](https://mrxsierra.github.io/test-site/)
- [GitHub Repository](https://github.com/mrxsierra/test-site/)

## ***Conclusion***

The Test Management Site project was a valuable learning experience that allowed me to demonstrate my full-stack capabilities. By creating a functional application with dynamic UI updates and local data storage, I showcased my skills in JavaScript, HTML, CSS, and Bootstrap. Success was measured by the successful implementation of all core features and the creation of a responsive and dynamic user interface.

??? summary "**AI Skill Assessment**"
    Prompt[^1] Source [:material-file-eye-outline:{ #source }](https://raw.githubusercontent.com/mrxsierra/mrxsierra.github.io/blob/main/prompts/skill-assesment-prompt.md)
    [^1]:
    This `AI skill assessment` was generated based on the [skill-assessment-prompt.md](https://raw.githubusercontent.com/mrxsierra/mrxsierra.github.io/main/prompts/skill-assesment-prompt.md) and the provided project documentation. It is intended as an illustrative summary and should be interpreted in the context of the available code and documentation in codebase.

    ---

    ### **Strengths**

    - **Frontend Engineering (HTML/CSS/JS):**
        - Demonstrates strong skills in vanilla JavaScript for DOM manipulation, modular code organization, and dynamic UI updates (e.g., main.js, `js/tests_content.js`).
        - Uses modern CSS with custom properties, responsive design, and theme toggling (see `styles/css/styles.css`).
        - Implements modular HTML with reusable components loaded dynamically (e.g., sidebar, topnav, profile, as seen in sidebar.js and HTML assets).

    - **Data Handling & Storage:**
        - Effectively uses `localStorage` and `sessionStorage` for persistent and session-based data (user profiles, test data, results).
        - Handles file uploads and parsing for CSV and Excel formats using third-party libraries (PapaParse, XLSX.js), with robust error handling and user feedback (`js/utility/file_handle.js`).

    - **Object-Oriented Design:**
        - Defines clear, extensible classes for domain entities (User, Profiles, Test, Question, Result, etc.) with encapsulated logic (`js/utility/temp_data.js`, `js/utility/temp_profile.js`).

    - **User Experience & Usability:**
        - Provides detailed user feedback and error messages throughout the UI (e.g., form validation, alerts for missing data, dynamic content updates).
        - Implements accessibility features such as keyboard navigation and clear visual cues for active elements.

    - **Documentation & Readability:**
        - Includes a comprehensive readme.md with project overview, features, technical details, folder structure, and screenshots.
        - Uses descriptive variable/function names and inline comments for clarity.

    - **Basic DevOps Awareness:**
        - Includes a GitHub Actions workflow for static site deployment to GitHub Pages (`.github/workflows/deploy.yml`).

    ### **Areas for Growth**

    - **Testing:**
        - No evidence of automated unit, integration, or end-to-end tests. All logic appears to be tested manually via the UI.
        - No test framework or test scripts present.

    - **Security:**
        - User authentication is handled entirely client-side with passwords stored in plain text in localStorage/sessionStorage.
        - No input sanitization or protection against XSS/CSRF.
        - No encryption or secure handling of sensitive data.

    - **Scalability & Backend Integration:**
        - The application is entirely client-side; there is no backend API, database, or server-side logic.
        - Not suitable for multi-user or production environments without significant changes.

    - **Accessibility & Internationalization:**
        - While some accessibility is present, there is no evidence of ARIA roles, screen reader support, or internationalization/localization.

    - **Advanced DevOps/CI/CD:**
        - Only basic static site deployment is present; no evidence of automated testing, linting, or code quality checks in CI.

    - **Code Reuse & DRY Principles:**
        - Some repeated logic (e.g., dynamic form handling, error messages) could be further abstracted for maintainability.

    ---

    ### **Role Suitability**

    #### **Best Fit Roles**

    - **Frontend Developer (Vanilla JS/HTML/CSS):**
        - Demonstrated ability to build interactive, modular, and responsive web UIs from scratch without frameworks.

    - **UI/UX Engineer (Prototype/Demo Level):**
        - Strong focus on user flows, feedback, and dynamic content for demo or MVP applications.

    - **Web Application Prototyper:**
        - Skilled at quickly assembling functional prototypes using client-side technologies and third-party libraries.

    #### **Well-Suited For**

    - **Technical Writer/Documenter:**
        - Good documentation practices and clear code organization.

    - **Client-Side Data Engineer:**
        - Experience with data parsing, transformation, and storage in browser environments.

    #### **Less Suited For**

    - **Backend Developer / Full Stack Engineer:**
        - No evidence of backend, API, or database design/implementation.
    - **DevOps Engineer (Advanced):**
        - Only basic CI/CD; lacks advanced automation, monitoring, or infrastructure-as-code.
    - **Security Engineer:**
        - No secure authentication, authorization, or data protection practices.
    - **QA/Test Automation Engineer:**
        - No automated testing or test infrastructure.

    ---

    **Summary:**  
    The developer demonstrates strong skills in vanilla JavaScript, modular frontend architecture, dynamic UI/UX, and client-side data handling. The codebase is well-documented, readable, and suitable for demo or prototype-level applications. However, there is a lack of automated testing, security best practices, backend integration, and advanced DevOps. The developer is best suited for roles focused on frontend development, rapid prototyping, and UI/UX engineering in client-side environments.

    ---
