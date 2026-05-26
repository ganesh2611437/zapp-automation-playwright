"""
Sidebar Page

This file contains reusable sidebar navigation methods
used across the Zapp application.

Current functionality:
- Navigate to Clients module

Future scope:
- Contacts
- Jobs
- Candidates
- Reports
- Settings
"""

import allure

from playwright.sync_api import Page
from pages.base_page import BasePage


class SidebarPage(BasePage):
    """
    SidebarPage handles navigation actions
    from the application's left sidebar menu.
    """

    def __init__(self, page: Page):
        """
        Initialize sidebar menu locators.
        """

        # Initialize BasePage constructor
        super().__init__(page)

        # Clients sidebar menu option
        self.clients_menu = page.get_by_text(
            "Clients",
            exact=True
        )

    @allure.step("Open Clients module")
    def open_clients_page(self):
        """
        Navigate to Clients page/module.
        """

        # Click Clients menu from sidebar
        self.click(self.clients_menu)