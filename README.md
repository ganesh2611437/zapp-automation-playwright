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

- Page Object Model (POM)
- Reusable utility architecture
- Dynamic test data generation
- Structured logging
- Allure reporting
- Screenshot capture on failures
- Git + GitHub version control

---

# Framework Highlights

- Enterprise-level Playwright Python framework
- Scalable Page Object Model architecture
- Dynamic reusable test data generation
- Integrated Allure reporting
- Screenshot capture on failures
- Logging support for debugging
- Git & GitHub integrated workflow
- Modular reusable framework design
- Stable locator strategies for Angular applications
- Automation flow debugging and synchronization handling

---

# Tech Stack Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Playwright | UI Automation |
| Pytest | Test execution framework |
| Allure Reports | Advanced reporting |
| Logging Module | Execution logging |
| Git | Version control |
| GitHub | Remote repository hosting |

---

# Framework Features

## Implemented Features

- Login Automation
- Region Selection
- Client Creation Flow
- Contact Creation Flow
- Dynamic Random Test Data
- Reusable Base Page Methods
- Allure Reporting
- Screenshot Capture on Failure
- Execution Logging
- Page Object Model (POM)
- Git & GitHub Integration

---

# Automation Workflow

```text
Login
↓
Region Selection
↓
Client Creation
↓
Toast Validation
↓
Contacts Navigation
↓
Contact Creation
↓
Toast Validation
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
│   └── contacts_page.py
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

- Better code reusability
- Easier maintenance
- Cleaner test structure
- Centralized locator management
- Improved scalability

---

# Why Playwright?

Playwright was chosen because of:

- Fast execution speed
- Auto-waiting capability
- Modern locator strategies
- Multi-browser support
- Better synchronization handling
- Stable automation execution
- Better reliability compared to traditional Selenium frameworks

---

# Reporting Features

## Allure Reports

Allure Reports are integrated for advanced execution reporting.

### Features

- Step-level execution visibility
- Screenshot attachments
- Failure tracking
- Better debugging support
- Execution history

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

- Better debugging
- Execution traceability
- Failure analysis
- Real-time execution tracking

---

# Dynamic Test Data

Framework dynamically generates:

- Company Names
- Full Names
- Display Names
- Email Addresses
- Mobile Numbers

This helps avoid duplicate test data issues during execution.

---

# Latest Playwright Features Used

- get_by_role()
- Accessible locators
- Auto waits
- Locator strategies
- Video recording
- Screenshot capture
- Assertion handling
- Strict mode debugging
- Dynamic element handling

---

# Challenges Solved During Automation

- Handled Angular dynamic locators
- Solved strict mode locator issues
- Stabilized dropdown overlays
- Managed dynamic test data
- Implemented reusable locator strategy
- Avoided flaky synchronization issues
- Improved locator stability using accessible locators

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

Create `.env` file:

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

# Current Automated Workflow

## Client Flow

- Login
- Select Region
- Open Clients Module
- Create New Client
- Validate Toast Message

---

## Contact Flow

- Open Contacts Module
- Create New Contact
- Select Newly Created Client
- Enter Contact Details
- Save Contact
- Validate Success Toast

---

# Failure Handling

On test failure framework automatically:

- Captures screenshots
- Attaches screenshots to Allure report
- Logs execution details

---

# Future Enhancements

Planned improvements:

- Jobs Module Automation
- Candidate Workflow Automation
- Drag & Drop Automation
- API Testing Integration
- Parallel Execution
- CI/CD Integration
- Docker Support
- Jenkins Integration
- GitHub Actions Pipeline

---

# Author

## Ganesh Kodihalli

Automation Test Engineer

---

# GitHub Repository

https://github.com/ganesh2611437/zapp-automation-playwright