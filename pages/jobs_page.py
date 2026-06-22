"""
Jobs Page

This file contains all locators and reusable methods
related to Job creation workflow.
"""

import allure

from playwright.sync_api import Page
from pages.base_page import BasePage


class JobsPage(BasePage):

    def __init__(self, page: Page):

        # Initialize BasePage
        super().__init__(page)

        # ---------------------------------------------------
        # MENU
        # ---------------------------------------------------

        self.jobs_menu = page.get_by_role(
            "listitem"
        ).filter(has_text="Jobs")

        # ---------------------------------------------------
        # BUTTONS
        # ---------------------------------------------------

        self.new_job_button = page.get_by_role(
            "button",
            name="user New Job"
        )

        self.create_job_button = page.get_by_role(
            "button",
            name="Create Job"
        )

        self.ok_button = page.get_by_role(
            "button",
            name="Ok"
        )

        # ---------------------------------------------------
        # JOB DETAILS
        # ---------------------------------------------------

        self.position_name_input = page.get_by_role(
            "combobox",
            name="Position Name"
        )

        self.select_client_dropdown = page.get_by_role(
            "combobox",
            name="Select Client"
        )

        self.location_dropdown = page.get_by_role(
            "combobox",
            name="Location"
        )

        self.bangalore_option = page.get_by_role(
            "option",
            name="Bangalore",
            exact=True
        )

        # ---------------------------------------------------
        # JOB DESCRIPTION
        # ---------------------------------------------------

        self.job_description_editor = page.locator(
            ".ql-editor"
        ).first

        # ---------------------------------------------------
        # COMPENSATION
        # ---------------------------------------------------

        self.total_budget_input = page.get_by_role(
            "textbox",
            name="Total Budget Per Month"
        )

        self.job_close_date = page.get_by_role(
            "textbox",
            name="Job Close Date"
        )

        self.billing_input = page.get_by_role(
            "textbox",
            name="Billing Per Month"
        )

        # ---------------------------------------------------
        # LOGOUT
        # ---------------------------------------------------

        self.profile_icon = page.get_by_role(
            "img",
            name="Profile Picture"
        )

        self.logout_button = page.get_by_role(
            "menuitem",
            name="logout Logout"
        )

        self.confirm_button = page.get_by_role(
            "button",
            name="Confirm"
        )

    # ===================================================
    # OPEN JOBS MODULE
    # ===================================================

    @allure.step("Open Jobs module")
    def open_jobs_module(self):

        self.click(
            self.jobs_menu
        )

    # ===================================================
    # CLICK NEW JOB
    # ===================================================

    @allure.step("Click New Job button")
    def click_new_job(self):

        self.click(
            self.new_job_button
        )

    # ===================================================
    # CREATE NEW JOB
    # ===================================================

    @allure.step("Create new job")
    def create_job(
        self,
        job_title,
        company_name,
        full_name,
        job_description
    ):

        # ---------------------------------------------------
        # POSITION NAME
        # ---------------------------------------------------

        self.enter_text(
            self.position_name_input,
            job_title
        )

        # ---------------------------------------------------
        # SELECT CLIENT
        # ---------------------------------------------------

        self.enter_text(
            self.select_client_dropdown,
            company_name
        )

        self.page.get_by_role(
            "option",
            name=company_name
        ).click()

        # Close overlay
        self.page.keyboard.press("Escape")

        self.page.wait_for_timeout(1000)

        # ---------------------------------------------------
        # SELECT CONTACT
        # ---------------------------------------------------

        self.page.wait_for_timeout(3000)

        self.page.get_by_text(
            "Select Contact"
        ).click()

        self.page.wait_for_timeout(1000)

        self.page.get_by_role(
            "option",
            name=full_name
        ).click()

        # Close overlay
        self.page.keyboard.press("Escape")

        self.page.wait_for_timeout(1000)

        # ---------------------------------------------------
        # WORKING MODEL
        # ---------------------------------------------------

        self.page.get_by_text(
            "Working Model"
        ).click()

        self.page.wait_for_timeout(1000)

        self.page.get_by_role(
            "option",
            name="WFO"
        ).click()

        # Close overlay
        self.page.keyboard.press("Escape")

        self.page.wait_for_timeout(1000)

        # ---------------------------------------------------
        # LOCATION
        # ---------------------------------------------------

        self.click(
            self.location_dropdown
        )

        self.enter_text(
            self.location_dropdown,
            "bang"
        )

        self.click(
            self.bangalore_option
        )

        # Close overlay
        self.page.keyboard.press("Escape")

        self.page.wait_for_timeout(1000)

        # ---------------------------------------------------
        # JOB LEVEL
        # ---------------------------------------------------

        self.page.get_by_text(
            "Job Level"
        ).click()

        self.page.wait_for_timeout(1000)

        self.page.get_by_role(
            "option",
            name="Middle",
            exact=True
        ).click()

        # Close overlay
        self.page.keyboard.press("Escape")

        self.page.wait_for_timeout(1000)

        # ---------------------------------------------------
        # EMPLOYMENT TYPE
        # ---------------------------------------------------

        self.page.mouse.wheel(0, 500)

        self.page.get_by_text(
            "Employment Type"
        ).click()

        self.page.wait_for_timeout(1000)

        self.page.get_by_role(
            "option",
            name="Permanent"
        ).click()

        # Close overlay
        self.page.keyboard.press("Escape")

        self.page.wait_for_timeout(1500)

        # ---------------------------------------------------
        # JOB DESCRIPTION
        # ---------------------------------------------------

        self.job_description_editor.scroll_into_view_if_needed()

        self.page.wait_for_timeout(1000)

        self.job_description_editor.click()

        self.job_description_editor.fill(
            job_description
        )

        self.page.wait_for_timeout(1000)

        # ---------------------------------------------------
        # TOTAL BUDGET
        # ---------------------------------------------------

        self.total_budget_input.scroll_into_view_if_needed()

        self.page.wait_for_timeout(1000)

        self.enter_text(
            self.total_budget_input,
            "30000"
        )

        # ---------------------------------------------------
        # JOB CLOSE DATE
        # ---------------------------------------------------

        self.click(
            self.job_close_date
        )

        self.page.wait_for_timeout(1000)

        # Select current date
        try:
            self.page.get_by_role(
                "button",
                name="Today",
                exact=True
            ).click()
        except Exception:
            # If the Today button is not available, accept the current date via keyboard.
            self.page.keyboard.press("Enter")

        self.page.wait_for_timeout(1000)

        # ---------------------------------------------------
        # LAPTOP OPTION
        # ---------------------------------------------------

        self.page.get_by_text(
            "Select Laptop Options"
        ).click()

        self.page.wait_for_timeout(1000)

        self.page.get_by_role(
            "option",
            name="Provided by Client"
        ).click()

        # Close overlay
        self.page.keyboard.press("Escape")

        self.page.wait_for_timeout(1000)

        # ---------------------------------------------------
        # BILLING AMOUNT
        # ---------------------------------------------------

        self.enter_text(
            self.billing_input,
            "500"
        )

        self.page.wait_for_timeout(1000)

        # ---------------------------------------------------
        # CREATE JOB
        # ---------------------------------------------------

        self.click(
            self.create_job_button
        )

    # ===================================================
    # VERIFY JOB CREATED
    # ===================================================

    @allure.step("Verify job created successfully")
    def verify_job_created(self):

        self.click(
            self.ok_button
        )

    # ===================================================
    # LOGOUT
    # ===================================================

    @allure.step("Logout from application")
    def logout(self):

        self.click(
            self.profile_icon
        )

        self.click(
            self.logout_button
        )

        self.click(
            self.confirm_button
        )