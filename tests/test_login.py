"""
Test Case: Client and Contact Creation Flow

This test automates the following workflow:

1. Open Zapp application
2. Login using recruiter credentials
3. Select India region
4. Navigate to Clients module
5. Create new client
6. Verify successful client creation
7. Navigate to Contacts module
8. Create new contact
9. Verify successful contact creation

Framework Features Used:
- Playwright
- Pytest
- Page Object Model (POM)
- Allure Reporting
- Logging
- Dynamic Test Data
- Screenshot on Failure
- Video Recording
"""

# Page imports
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.sidebar_page import SidebarPage
from pages.clients_page import ClientsPage
from pages.contacts_page import ContactsPage

# Utility imports
from utils.config_reader import *
from utils.data_generator import *
from utils.logger import logger


def test_login(page):
    """
    End-to-end automation test for:

    Client Creation Flow
    +
    Contact Creation Flow
    """

    # Log test execution start
    logger.info("Test execution started")

    # Initialize page objects
    login = LoginPage(page)

    dashboard = DashboardPage(page)

    sidebar = SidebarPage(page)

    clients = ClientsPage(page)

    contacts = ContactsPage(page)

    # ---------------------------------------------------
    # LOGIN FLOW
    # ---------------------------------------------------

    # Open application URL
    logger.info("Opening application")

    login.load(BASE_URL)

    # Login using recruiter credentials
    logger.info("Logging into application")

    login.login(USERNAME_1, PASSWORD_1)

    # Select recruiter region
    logger.info("Selecting India region")

    dashboard.select_region()

    # ---------------------------------------------------
    # CLIENT CREATION FLOW
    # ---------------------------------------------------

    # Navigate to Clients module
    logger.info("Opening Clients module")

    sidebar.open_clients_page()

    # Open New Client popup
    logger.info("Clicking New Client")

    clients.click_new_client()

    # Create client using dynamic company name
    logger.info("Creating new client")

    clients.create_client(
        COMPANY_NAME,
        COMPANY_NAME
    )

    # Verify successful client creation
    logger.info("Verifying client creation")

    clients.verify_client_created()

    logger.info("Client created successfully")

    # ---------------------------------------------------
    # CONTACT CREATION FLOW
    # ---------------------------------------------------

    # Navigate to Contacts module
    logger.info("Opening Contacts module")

    contacts.open_contacts_module()

    # Open New Contact popup
    logger.info("Clicking New Contact")

    contacts.click_new_contact()

    # Create new contact using dynamic reusable data
    logger.info("Creating new contact")

    contacts.create_contact(
        COMPANY_NAME,
        FULL_NAME,
        DISPLAY_NAME,
        EMAIL_ADDRESS,
        PHONE_NUMBER
    )

    # Verify successful contact creation
    logger.info("Verifying contact creation")

    contacts.verify_contact_created()

    logger.info("Contact created successfully")

    # Temporary wait added for debugging/demo visibility
    page.wait_for_timeout(5000)