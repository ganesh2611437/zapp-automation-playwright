![Python](https://img.shields.io/badge/Python-3.13-blue)
![Playwright](https://img.shields.io/badge/Playwright-Automation-green)
![Pytest](https://img.shields.io/badge/Pytest-Framework-yellow)
![Allure](https://img.shields.io/badge/Allure-Reporting-orange)
![GitHub](https://img.shields.io/badge/GitHub-VersionControl-black)

# Zapp Automation Playwright Framework

Enterprise-level UI Automation Framework built using Playwright + Python for automating Zapp recruitment workflows.

---

# Project Overview

This framework is designed to automate end-to-end recruitment workflows in the Zapp application using modern automation engineering practices.

The framework follows:

* Page Object Model (POM)
* Reusable utility architecture
* Dynamic test data generation
* Structured logging
* Allure reporting
* Screenshot capture on failures
* Git + GitHub version control

---

# Framework Highlights

* Enterprise-level Playwright Python framework
* Scalable Page Object Model architecture
* Dynamic reusable test data generation
* Integrated Allure reporting
* Screenshot capture on failures
* Logging support for debugging
* Git & GitHub integrated workflow
* Modular reusable framework design
* Stable locator strategies for Angular applications
* Automation flow debugging and synchronization handling

---

# Tech Stack Used

| Technology     | Purpose                   |
| -------------- | ------------------------- |
| Python         | Programming Language      |
| Playwright     | UI Automation             |
| Pytest         | Test Execution Framework  |
| Allure Reports | Advanced Reporting        |
| Logging Module | Execution Logging         |
| Git            | Version Control           |
| GitHub         | Remote Repository Hosting |

---

# Framework Features

## Implemented Features

* Login Automation
* Region Selection
* Client Creation Flow
* Contact Creation Flow
* Job Creation Flow
* Logout Flow
* Dynamic Random Test Data
* Reusable Base Page Methods
* Allure Reporting
* Screenshot Capture on Failure
* Execution Logging
* Page Object Model (POM)
* Git & GitHub Integration

---

# Current End-to-End Scenario

The framework currently automates:

1. Login
2. Region Selection
3. Client Creation
4. Contact Creation
5. Job Creation
6. Logout

This serves as the baseline recruitment workflow automation for the Zapp application.

---

# Automation Workflow

```text
Login
↓
Region Selection
↓
Client Creation
↓
Client Validation
↓
Contact Creation
↓
Contact Validation
↓
Job Creation
↓
Job Validation
↓
Logout
↓
Reporting & Logging
```

---

# Project Structure

```bash
Zapp-playwright-framework/
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── dashboard_page.py
│   ├── sidebar_page.py
│   ├── clients_page.py
│   ├── contacts_page.py
│   └── jobs_page.py
│
├── tests/
│   └── test_login.py
│
├── utils/
│   ├── config_reader.py
│   ├── data_generator.py
│   └── logger.py
│
├── logs/
├── screenshots/
├── videos/
├── allure-results/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Framework Design Pattern

## Page Object Model (POM)

This framework follows the Page Object Model architecture for better scalability and maintainability.

### Advantages

* Better code reusability
* Easier maintenance
* Cleaner test structure
* Centralized locator management
* Improved scalability

---

# Why Playwright?

Playwright was chosen because of:

* Fast execution speed
* Auto-waiting capability
* Modern locator strategies
* Multi-browser support
* Better synchronization handling
* Stable automation execution
* Better reliability compared to traditional Selenium frameworks

---

# Reporting Features

## Allure Reports

Allure Reports are integrated for advanced execution reporting.

### Features

* Step-level execution visibility
* Screenshot attachments
* Failure tracking
* Better debugging support
* Execution history

### Generate Allure Report

```bash
allure serve allure-results
```

---

# Logging

Execution logs are generated using Python logging module.

### Log File Location

```bash
logs/execution.log
```

### Logging Benefits

* Better debugging
* Execution traceability
* Failure analysis
* Real-time execution tracking

---

# Dynamic Test Data

Framework dynamically generates:

* Company Names
* Job Titles
* Full Names
* Display Names
* Email Addresses
* Mobile Numbers

This helps avoid duplicate test data issues during execution.

---

# Latest Playwright Features Used

* get_by_role()
* Accessible locators
* Auto waits
* Locator strategies
* Video recording
* Screenshot capture
* Assertion handling
* Strict mode debugging
* Dynamic element handling

---

# Challenges Solved During Automation

| Challenge                | Solution Implemented                                                                 |
| ------------------------ | ------------------------------------------------------------------------------------ |
| Angular Dynamic Locators | Used stable Playwright locators such as get_by_role(), get_by_label(), get_by_text() |
| Strict Mode Violations   | Used .first(), .nth(), and improved locator uniqueness                               |
| Dropdown Overlay Issues  | Added overlay handling and synchronization                                           |
| Dynamic Test Data        | Implemented reusable data generator utilities                                        |
| Locator Stability        | Followed accessibility-based locator strategy                                        |
| Synchronization Issues   | Used Playwright auto-waits and explicit waits where required                         |
| Framework Scalability    | Implemented reusable Page Object Model architecture                                  |

---

# How To Setup Project

## Clone Repository

```bash
git clone https://github.com/ganesh2611437/zapp-automation-playwright.git
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Playwright Browsers

```bash
playwright install
```

---

# Environment Configuration

Create a `.env` file:

```env
BASE_URL=https://test.zapp.co.id/login

USERNAME_1=your_email
PASSWORD_1=your_password
```

---

# Test Execution Commands

## Run Single Test

```bash
pytest tests/test_login.py -v -s
```

---

## Run With Allure Results

```bash
pytest tests/test_login.py -v -s --alluredir=allure-results
```

---

## Open Allure Report

```bash
allure serve allure-results
```

---

# Current Automated Modules

## Login Module

* Login with Recruiter Credentials
* Region Selection

## Clients Module

* Create New Client
* Validate Client Creation

## Contacts Module

* Create New Contact
* Associate Client
* Validate Contact Creation

## Jobs Module

* Create New Job
* Associate Client
* Associate Contact
* Add Job Description
* Validate Job Creation

## Logout Module

* Logout From Application
* Validate Successful Logout

---

# Failure Handling

On test failure framework automatically:

* Captures screenshots
* Attaches screenshots to Allure report
* Logs execution details

---

# Real Challenges Solved During Automation

The Zapp application is an Angular-based enterprise recruitment platform with dynamic UI behavior. During framework development, several automation challenges were encountered and resolved.

| Challenge                     | Solution Implemented                                                                                                                                 |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Angular Dynamic Locators      | Used stable Playwright locators such as `get_by_role()`, `get_by_text()`, and accessibility-based selectors instead of Angular-generated attributes. |
| Strict Mode Violations        | Resolved multiple matching element issues using `.first()`, `.last()`, and `.nth()` locator strategies.                                              |
| Dynamic Dropdown Overlays     | Implemented overlay closing logic and synchronization handling to avoid blocked actions.                                                             |
| Dynamic Test Data             | Created reusable runtime test data generator to avoid duplicate records.                                                                             |
| Synchronization Issues        | Leveraged Playwright auto-waits and explicit waits where necessary.                                                                                  |
| Dialog Handling               | Added reusable popup and confirmation dialog handling methods.                                                                                       |
| Toast Validation              | Implemented success message validation after Client, Contact, and Job creation.                                                                      |
| Dynamic Record Identification | Used shared runtime variables to identify newly created Clients, Contacts, and Jobs.                                                                 |
| Angular Material Components   | Implemented stable handling for Angular Material dropdowns, menus, and dialogs.                                                                      |
| Form Submission Timing Issues | Added proper wait strategies for Save, Confirm, and Success workflows.                                                                               |
| Reusable Locator Strategy     | Centralized locators within Page Object classes to simplify maintenance.                                                                             |
| Framework Scalability         | Designed framework to support module-wise automation expansion.                                                                                      |

---

# Dynamic Data Management

## Problem Statement

The application generates unique records for every execution.

Examples:

```text
Client:
Wipro_1781105192

Contact:
Ganesh_1781105201

Job:
Python_Automation_1781105215
```

After refreshing the application:

* Record IDs change
* New records move to the top
* Static values become unreliable
* Duplicate data causes failures

---

## Solution Implemented

The framework dynamically generates unique data during runtime.

Generated Data:

* Company Name
* Job Title
* Full Name
* Display Name
* Email Address
* Mobile Number

Example:

```python
COMPANY_NAME = f"Wipro_{timestamp}"

FULL_NAME = f"Ganesh_{timestamp}"

JOB_TITLE = f"Python_Automation_{timestamp}"
```

Benefits:

* Unique execution every run
* No duplicate data issues
* Reliable automation execution
* Improved scalability

---

# Dynamic Data Reusability Strategy

The framework generates data once and reuses it across multiple modules.

Workflow:

```text
Client Created
↓
Contact Uses Same Client
↓
Job Uses Same Client
↓
Job Uses Same Contact
```

Implementation Approach:

```text
Generate Once
↓
Store in Shared Variables
↓
Reuse Across Modules
↓
Maintain Data Consistency
```

Benefits:

* No data mismatch
* No incorrect record association
* Better end-to-end workflow validation

---

# Engineering Practices Followed

## Page Object Model (POM)

Implemented reusable page classes:

* LoginPage
* DashboardPage
* SidebarPage
* ClientsPage
* ContactsPage
* JobsPage

Benefits:

* Better maintainability
* Cleaner test scripts
* Centralized locator management
* Easier framework scaling

---

## Logging Strategy

Implemented Python logging framework.

Execution logs capture:

* Application launch
* Login status
* Module navigation
* Record creation
* Validation results
* Failures and exceptions

Benefits:

* Easier debugging
* Execution traceability
* Faster root cause analysis

---

## Reporting Strategy

Implemented Allure Reporting.

Captured:

* Test Steps
* Execution Status
* Screenshots
* Failure Details

Benefits:

* Better visibility
* Easier reporting
* Professional test evidence

---

# Current Framework Coverage

Completed Modules:

✅ Login

✅ Region Selection

✅ Clients

✅ Contacts

✅ Jobs

✅ Logout

Current Status:

```text
Login
↓
Region Selection
↓
Client Creation
↓
Contact Creation
↓
Job Creation
↓
Logout
```

Framework Status: Stable and Version Controlled.

---

# Roadmap

Upcoming Automation Modules:

* Candidate Creation Workflow
* Candidate Attachment Workflow
* Hiring Workflow
* Support Hub Workflow
* Multi User Workflow
* Employee Portal Automation
* API Automation
* Parallel Execution
* CI/CD Integration
* Jenkins Integration
* Docker Execution
* GitHub Actions Pipeline

---

# Lessons Learned

During framework development, the following automation engineering concepts were applied:

* Playwright Locator Strategies
* Angular Application Automation
* Dynamic Test Data Handling
* Synchronization Techniques
* Popup and Overlay Handling
* Allure Reporting Integration
* Logging Best Practices
* Page Object Model Design
* Git and GitHub Workflow
* Automation Framework Architecture

These practices helped create a scalable and maintainable enterprise automation framework for the Zapp application.


# Future Enhancements

Planned improvements:

* Candidate Creation Workflow
* Candidate Attach Workflow
* Hiring Workflow Automation
* Support Hub Automation
* Multi-User Workflow Automation
* API Testing Integration
* Parallel Execution
* CI/CD Integration
* Docker Support
* Jenkins Integration
* GitHub Actions Pipeline

---

# Author

## Ganesh Kodihalli

Automation Test Engineer

---

# GitHub Repository

https://github.com/ganesh2611437/zapp-automation-playwright
