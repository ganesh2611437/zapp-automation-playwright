"""
Contacts Page

Handles Contact creation workflow.
"""

import allure

from playwright.sync_api import Page
from pages.base_page import BasePage


class ContactsPage(BasePage):

    def __init__(self, page: Page):

        # Initialize BasePage
        super().__init__(page)

        # Contacts menu
        self.contacts_menu = page.get_by_text(
            "Contacts"
        )

        # New Contact button
        self.new_contact_button = page.get_by_role(
            "button",
            name="user New Contact"
        )

        # Select Client dropdown
        self.select_client_dropdown = page.get_by_role(
            "combobox",
            name="Select Client"
        )

        # Full Name field
        self.full_name_input = page.locator(
            'input[formcontrolname="fullName"]'
        )

        # Display Name field
        self.display_name_input = page.locator(
            'input[formcontrolname="displayName"]'
        )

        # Gender dropdown
        self.gender_dropdown = page.locator(
            ".mat-mdc-select-placeholder"
        ).first

        # Email Address field
        self.email_input = page.get_by_role(
            "textbox",
            name="E-Mail Address"
        ).first

        # Mobile Number field
        self.mobile_input = page.locator(
            'input[type="tel"]'
        ).first

        # Save button
        self.save_button = page.get_by_role(
            "button",
            name="Save"
        )

        # Toast OK button
        self.ok_button = page.get_by_role(
            "button",
            name="Ok"
        )

    @allure.step("Open Contacts module")
    def open_contacts_module(self):

        self.click(self.contacts_menu)

    @allure.step("Click New Contact button")
    def click_new_contact(self):

        self.click(self.new_contact_button)

    @allure.step("Create new contact")
    def create_contact(
        self,
        company_name,
        full_name,
        display_name,
        email,
        mobile
    ):

        # Select newly created client
        self.enter_text(
            self.select_client_dropdown,
            company_name
        )

        # Select matching client from dropdown
        self.page.get_by_role(
            "option",
            name=company_name
        ).click()

        # Close dropdown overlay
        self.page.keyboard.press("Escape")

        # Wait for form rendering
        self.page.wait_for_timeout(2000)

        # Enter Full Name
        self.enter_text(
            self.full_name_input,
            full_name
        )

        # Enter Display Name
        self.enter_text(
            self.display_name_input,
            display_name
        )

        # Select Gender
        self.click(self.gender_dropdown)

        self.page.get_by_role(
            "option",
            name="Male",
            exact=True
        ).click()

        # Wait after gender selection
        self.page.wait_for_timeout(1000)

        # Enter Email Address
        self.enter_text(
            self.email_input,
            email
        )

        # Enter Mobile Number
        self.enter_text(
            self.mobile_input,
            mobile
        )

        # Save Contact
        self.click(self.save_button)

    @allure.step("Verify contact created successfully")
    def verify_contact_created(self):

        self.click(self.ok_button)