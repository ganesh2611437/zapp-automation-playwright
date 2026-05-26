"""
Clients Page

This file contains all locators and reusable methods
related to Client management functionality.

Current functionality:
- Open New Client popup
- Create new client
- Validate client creation success message
"""

import allure

from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class ClientsPage(BasePage):
    """
    ClientsPage handles all actions related
    to Client creation and validation.
    """

    def __init__(self, page: Page):
        """
        Initialize all Client page locators.
        """

        # Initialize BasePage constructor
        super().__init__(page)

        # New Client button used to open client creation popup
        self.new_client_button = page.get_by_role(
            "button",
            name="user New Client"
        )

        # Display Name input field
        self.display_name_input = page.get_by_role(
            "textbox",
            name="Display Name"
        )

        # Client Name input field
        self.client_name_input = page.get_by_role(
            "combobox",
            name="Client Name"
        )

        # Save button used to create client
        self.save_button = page.get_by_role(
            "button",
            name="Save"
        )

        # Success toast message displayed after client creation
        self.client_created_toast = page.get_by_text(
            "Client Created",
            exact=True
        )

        # OK button displayed in success popup/toast dialog
        self.ok_button = page.get_by_role(
            "button",
            name="Ok"
        )

    @allure.step("Click New Client button")
    def click_new_client(self):
        """
        Opens the New Client creation popup.
        """

        # Click New Client button
        self.click(self.new_client_button)

    @allure.step("Create new client")
    def create_client(self, display_name, client_name):
        """
        Creates a new client using provided details.

        Steps:
        1. Enter Display Name
        2. Enter Client Name
        3. Click Save button
        """

        # Enter Display Name
        self.enter_text(
            self.display_name_input,
            display_name
        )

        # Enter Client Name
        self.enter_text(
            self.client_name_input,
            client_name
        )

        # Click Save button
        self.click(self.save_button)

    @allure.step("Verify client created successfully")
    def verify_client_created(self):
        """
        Validates successful client creation.

        Verification:
        - 'Client Created' toast message should appear
        - Click OK button to close success popup
        """

        # Verify success toast visibility
        expect(
            self.client_created_toast
        ).to_be_visible()

        # Close success popup
        self.click(self.ok_button)