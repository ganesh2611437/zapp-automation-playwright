"""
Configuration Reader

This file is responsible for loading
environment variables from the .env file.

Purpose:
- Store sensitive data securely
- Avoid hardcoding credentials
- Support multiple environments easily

Example:
- URLs
- Usernames
- Passwords
- API keys
"""

from dotenv import load_dotenv
import os


# Load all environment variables from .env file
load_dotenv()


# Application URL
BASE_URL = os.getenv("BASE_URL")


# Recruiter Login 1 Credentials
USERNAME_1 = os.getenv("USERNAME_1")
PASSWORD_1 = os.getenv("PASSWORD_1")