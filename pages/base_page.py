"""
Base Page

This file contains reusable common methods used across
all application pages in the framework.

Purpose:
- Avoid duplicate code
- Improve maintainability
- Centralize common Playwright actions

All page classes inherit from BasePage.
"""

from playwright.sync_api import Page


class BasePage:
    """
    BasePage contains reusable helper methods
    for all page objects.
    """

    def __init__(self, page: Page):
        """
        Constructor to initialize Playwright page object.
        """

        self.page = page

    def navigate(self, url):
        """
        Navigate to the specified application URL.
        """

        self.page.goto(url)

    def click(self, locator):
        """
        Reusable click method.

        Steps performed:
        1. Wait until element becomes visible
        2. Hover on element for realistic interaction
        3. Perform click action
        4. Add small wait for UI stability

        This method is reused across all pages.
        """

        # Wait until element is visible before interaction
        locator.wait_for(
            state="visible",
            timeout=10000
        )

        # Hover before clicking to simulate realistic user behavior
        locator.hover()

        # Small wait for UI stability
        self.page.wait_for_timeout(500)

        # Perform click action
        locator.click()

        # Wait after click to allow page transitions/loaders
        self.page.wait_for_timeout(1000)

    def enter_text(self, locator, text):
        """
        Reusable text input method.

        Uses sequential typing to simulate
        human-like typing behavior.
        """

        # Wait until input field becomes visible
        locator.wait_for(
            state="visible",
            timeout=10000
        )

        # Click on input field
        locator.click()

        self.page.wait_for_timeout(500)

        # Type text character-by-character
        locator.press_sequentially(
            text,
            delay=150
        )

        self.page.wait_for_timeout(500)

    def wait(self, milliseconds):
        """
        Generic reusable wait method.

        Used for temporary debugging or UI stabilization.
        """

        self.page.wait_for_timeout(milliseconds)

    def get_title(self):
        """
        Returns current browser page title.
        """

        return self.page.title()