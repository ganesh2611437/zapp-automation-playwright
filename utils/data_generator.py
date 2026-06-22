"""
Dynamic Test Data Generator

This file is responsible for generating
dynamic and realistic test data used during execution.

Purpose:
- Avoid duplicate data issues
- Ensure unique test execution every run
- Simulate real-world application usage

Current functionality:
- Dynamic company name generation
- Dynamic person name generation
- Dynamic email generation
- Dynamic mobile number generation

Future scope:
- Job titles
- Candidate data
- Addresses
- Locations
"""

import random
import time


# Generate unique timestamp for every execution
# Helps avoid duplicate data conflicts
timestamp = int(time.time())


# ---------------------------------------------------
# COMPANY DATA
# ---------------------------------------------------

# List of realistic company names
company_names = [

    "Google",
    "Microsoft",
    "Amazon",
    "Infosys",
    "TCS",
    "Wipro",
    "Accenture",
    "IBM",
    "Oracle",
    "Deloitte",
    "Capgemini",
    "Tech Mahindra",
    "Cognizant",
    "Meta",
    "Netflix"
]


# Select random company name
random_company = random.choice(company_names)


# Generate unique company name
# Example:
# Google_174827272
COMPANY_NAME = f"{random_company}_{timestamp}"


# ---------------------------------------------------
# CONTACT DATA
# ---------------------------------------------------

# First names list
first_names = [

    "Rahul",
    "Arjun",
    "David",
    "John",
    "Sam",
    "Kiran",
    "Vijay",
    "Ajay",
    "Rohit",
    "Aman"
]


# Last names list
last_names = [

    "Kumar",
    "Sharma",
    "Reddy",
    "Patel",
    "Singh",
    "Mehta",
    "Verma",
    "Nair",
    "Das",
    "Joseph"
]


# Generate dynamic full name
FIRST_NAME = random.choice(first_names)

LAST_NAME = random.choice(last_names)

FULL_NAME = f"{FIRST_NAME} {LAST_NAME}"


# Display Name should match Full Name
DISPLAY_NAME = FULL_NAME


# ---------------------------------------------------
# EMAIL DATA
# ---------------------------------------------------

# Generate unique email address
# Example:
# rahul174827@gmail.com
EMAIL_ADDRESS = (
    f"{FIRST_NAME.lower()}{timestamp}@gmail.com"
)


# ---------------------------------------------------
# MOBILE NUMBER DATA
# ---------------------------------------------------

# Generate random 10-digit mobile number
PHONE_NUMBER = (
    f"9{random.randint(100000000, 999999999)}"
)


# ---------------------------------------------------
# JOB DATA
# ---------------------------------------------------

job_titles = [
    "Automation Engineer",
    "Software Developer",
    "QA Engineer",
    "Technical Consultant",
    "Business Analyst",
    "Project Coordinator",
    "DevOps Engineer",
    "Product Specialist"
]

JOB_TITLE = f"{random.choice(job_titles)}_{timestamp}"

JOB_DESCRIPTION = (
    "Responsible for supporting the delivery of high-quality software products, "
    "working closely with cross-functional teams to ensure requirements are met."
)
