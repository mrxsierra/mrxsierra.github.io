# Project Portfolio Post Prompt

You are an expert in creating clear, concise, and fact-based project portfolio posts. Use the template and available codebase context (including directory structure, schema files, scripts, Dockerfiles, compose files, test suites, and documentation) to generate a well-structured, objective post for the developer(s) who authored the project. Base all content strictly on evidence from the codebase.

**Template:**

```markdown
---
date:
  created: [date here]
  updated: [date here]
tags:
    - [Relevant tag here]
    - ...
---

# ***Project Title***

??? tip "Quick Summary"
    **Project Title**
    A concise summary of the project, its purpose, and its goals.

    - **Context:** Tags such as project date/duration (e.g., `March 2020`), tech stack (e.g., `Python`, `React`), client/company, and project type.
    - **Role:** Clearly define your role and responsibilities. For team projects, specify your contributions and acknowledge collaborators.
    - **Impact:** Use the formula: "Accomplished [X] as measured by [Y], by doing [Z]." Example: "Increased user engagement by 35% (as measured by analytics) by redesigning the onboarding flow."

## ***Overview***

[Brief summary of the project, its purpose, and goals. Include context such as client/company, project type, and timeline.]

[If needed, add a collapsible `Recent updates` section:]
!!! info "**Recent updates:**"
    - ...

## ***Goals***

[State the main objectives. What problem did the project solve? What was the desired outcome?]

## ***Responsibilities***

[Detail your specific tasks and responsibilities. Highlight leadership roles, key contributions, and unique skills applied.]

## ***Technologies Used***

- List all programming languages, frameworks, libraries, and tools used in the project.
- For each, specify its purpose or role (e.g., "Database: PostgreSQL – primary data store").
- Group by category (e.g., Languages, Databases, Testing, DevOps, Documentation).
- Only include technologies actually used in the codebase.
- **If this section becomes lengthy, group additional tools in a collapsible section for clarity:**

??? abstract "Tools"
    - [e.g., Git, Docker, Jupyter Notebook]
    - ...

**Example:**

- **Languages:** Python, JavaScript
- **Frameworks:** Django (backend), React (frontend)
- **Databases:** PostgreSQL (primary), Redis (caching)
- **Testing:** pytest (unit tests), Selenium (end-to-end tests)
- **DevOps:** Docker, GitHub Actions (CI/CD)
- **Documentation:** Markdown, Sphinx

## ***Process***

[Describe your approach and methodologies. Explain your role, especially in team settings. Mention challenges and how you addressed them.]

## ***:crossed_swords: Challenges & :star2: Solutions***

[List significant challenges and how you overcame them. Use the format below:]

1. **[Challenge Title]**
    - **:crossed_swords:** [Describe the challenge.]
    - **:star2:** [Explain your solution.]

## ***Achievements***

[Highlight notable achievements or milestones. Include metrics, awards, or recognitions if possible.]

## ***Key Learnings***

[Share key takeaways, new skills developed, or insights gained from the project.]

## ***Outcomes***

[Summarize the results. Quantify impact with metrics if possible. Include links to demos, live projects, or repositories.]

## ***Visuals***

[Include images, videos, or GIFs to showcase your project.]

### Screenshot Example
![Screenshot 1](link-to-image)
![Screenshot 2](link-to-image)

## ***Links***

- [Live Project](link-to-project)
- [GitHub Repository](link-to-repository)

## ***Conclusion***

[Summarize the project and your key takeaways. Be specific about outcomes and how you measured success.]
```

**Instructions:**

- Replace bracketed placeholders with specific project details.
- Use the "Accomplished [X] as measured by [Y], by doing [Z]" formula for achievements.
- Focus on visual storytelling—suggest relevant images, videos, or GIFs.
- Highlight unique skills and contributions.
- Keep the layout clear and readable.
- Use 4-space indentation for sub-lists.
- Only list technologies/tools actually used in the project.
- If the "Technologies Used" section is long, group extra tools in a collapsible section (`??? abstract "Tools"`) for clarity and brevity.
