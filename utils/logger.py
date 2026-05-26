"""
Logger Utility

This file configures centralized logging
for the automation framework.

Purpose:
- Capture execution flow
- Store logs for debugging
- Improve failure analysis
- Provide execution traceability

Logs are generated in:
logs/execution.log

Logging Types:
- INFO
- WARNING
- ERROR
- DEBUG (future scope)
"""

import logging
import os


# Create logs folder automatically
# if it does not already exist
LOG_FOLDER = "logs"

os.makedirs(LOG_FOLDER, exist_ok=True)


# Define log file path
log_file = os.path.join(
    LOG_FOLDER,
    "execution.log"
)


# Create dedicated framework logger
logger = logging.getLogger(
    "playwright_framework"
)

# Set logging level
logger.setLevel(logging.INFO)


# Define log message format
# Example:
# 2026-05-26 10:30:15 - INFO - Login successful
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)


# File handler
# Stores logs inside execution.log file
file_handler = logging.FileHandler(log_file)

file_handler.setFormatter(formatter)


# Console handler
# Displays logs in terminal during execution
console_handler = logging.StreamHandler()

console_handler.setFormatter(formatter)


# Prevent duplicate handlers
# when framework reloads logger multiple times
if not logger.handlers:

    logger.addHandler(file_handler)

    logger.addHandler(console_handler)