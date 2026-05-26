"""
Login Page

This file contains all locators and reusable methods
related to Zapp application login functionality.
"""

import allure

from playwright.sync_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    LoginPage handles all actions related
    to user authentication.
    """

    def __init__(self, page: Page):
        """
        Initialize page locators used in login flow.
        """

        # Initialize BasePage constructor
        super().__init__(page)

        # Email address input field
        self.email_input = page.get_by_role(
            "textbox",
            name="Email Address"
        )

        # Password input field
        self.password_input = page.get_by_role(
            "textbox",
            name="Password"
        )

        # Login button
        self.login_button = page.get_by_role(
            "button",
            name="Login"
        )

    @allure.step("Open Zapp application")
    def load(self, url):
        """
        Opens the Zapp application URL.
        """

        self.navigate(url)

    @allure.step("Login into application")
    def login(self, username, password):
        """
        Perform login using provided credentials.

        Steps:
        1. Enter username/email
        2. Enter password
        3. Click login button
        """

        # Enter email address
        self.enter_text(
            self.email_input,
            username
        )

        # Enter password
        self.enter_text(
            self.password_input,
            password
        )

        # Click Login button
        self.click(self.login_button)