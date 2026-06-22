"""
End-to-End Automation Test

This test automates:

1. Login Flow
2. Client Creation Flow
3. Contact Creation Flow
4. Job Creation Flow
5. Logout Flow

Framework Features Used:

- Playwright
- Pytest
- Page Object Model (POM)
- Allure Reporting
- Logging
- Dynamic Test Data
"""

# ---------------------------------------------------
# PAGE IMPORTS
# ---------------------------------------------------

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.sidebar_page import SidebarPage
from pages.clients_page import ClientsPage
from pages.contacts_page import ContactsPage
from pages.jobs_page import JobsPage


# ---------------------------------------------------
# UTILITY IMPORTS
# ---------------------------------------------------

from utils.config_reader import *
from utils.data_generator import *
from utils.logger import logger


def test_login(page):

    """
    End-to-end automation test for:

    - Client Creation
    - Contact Creation
    - Job Creation
    """

    # ---------------------------------------------------
    # TEST EXECUTION START
    # ---------------------------------------------------

    logger.info("Test execution started")

    # ---------------------------------------------------
    # INITIALIZE PAGE OBJECTS
    # ---------------------------------------------------

    login = LoginPage(page)

    dashboard = DashboardPage(page)

    sidebar = SidebarPage(page)

    clients = ClientsPage(page)

    contacts = ContactsPage(page)

    jobs = JobsPage(page)

    # ---------------------------------------------------
    # LOGIN FLOW
    # ---------------------------------------------------

    logger.info("Opening application")

    login.load(BASE_URL)

    logger.info("Logging into application")

    login.login(
        USERNAME_1,
        PASSWORD_1
    )

    logger.info("Selecting India region")

    dashboard.select_region()

    # ---------------------------------------------------
    # CLIENT CREATION FLOW
    # ---------------------------------------------------

    logger.info("Opening Clients module")

    sidebar.open_clients_page()

    logger.info("Clicking New Client")

    clients.click_new_client()

    logger.info("Creating new client")

    clients.create_client(
        COMPANY_NAME,
        COMPANY_NAME
    )

    logger.info("Verifying client creation")

    clients.verify_client_created()

    logger.info("Client created successfully")

    # ---------------------------------------------------
    # CONTACT CREATION FLOW
    # ---------------------------------------------------

    logger.info("Opening Contacts module")

    contacts.open_contacts_module()

    logger.info("Clicking New Contact")

    contacts.click_new_contact()

    logger.info("Creating new contact")

    contacts.create_contact(
        COMPANY_NAME,
        FULL_NAME,
        DISPLAY_NAME,
        EMAIL_ADDRESS,
        PHONE_NUMBER
    )

    logger.info("Verifying contact creation")

    contacts.verify_contact_created()

    logger.info("Contact created successfully")

    # ---------------------------------------------------
    # JOB CREATION FLOW
    # ---------------------------------------------------

    logger.info("Opening Jobs module")

    jobs.open_jobs_module()

    logger.info("Clicking New Job")

    jobs.click_new_job()

    logger.info("Creating new job")

    jobs.create_job(
        JOB_TITLE,
        COMPANY_NAME,
        FULL_NAME,
        JOB_DESCRIPTION
    )

    logger.info("Verifying job creation")

    jobs.verify_job_created()

    logger.info("Job created successfully")

    # ---------------------------------------------------
    # LOGOUT FLOW
    # ---------------------------------------------------

    logger.info("Logging out from application")

    jobs.logout()

    logger.info("Logout successful")

    # ---------------------------------------------------
    # TEST EXECUTION END
    # ---------------------------------------------------

    logger.info("Test execution completed successfully")