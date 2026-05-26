"""
Dashboard Page

This file contains locators and reusable methods
related to dashboard functionalities after login.

Current functionality:
- Region selection
"""

import allure

from playwright.sync_api import Page
from pages.base_page import BasePage


class DashboardPage(BasePage):
    """
    DashboardPage handles actions performed
    on the dashboard/home screen.
    """

    def __init__(self, page: Page):
        """
        Initialize dashboard page locators.
        """

        # Initialize BasePage constructor
        super().__init__(page)

        # Profile icon used to open region selection menu
        self.profile_icon = page.get_by_role(
            "img",
            name="Profile Picture"
        )

        # India region option from dropdown menu
        self.india_option = page.locator(
            "#mat-menu-panel-0"
        ).get_by_text("India")

    @allure.step("Select India region")
    def select_region(self):
        """
        Select India region after successful login.

        Steps:
        1. Click profile icon
        2. Wait for region dropdown visibility
        3. Select India option
        """

        # Open region dropdown menu
        self.click(self.profile_icon)

        # Wait until India option becomes visible
        # because Angular Material menu renders dynamically
        self.india_option.wait_for(
            state="visible",
            timeout=10000
        )

        # Select India region
        self.click(self.india_option)