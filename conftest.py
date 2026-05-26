"""
Pytest Configuration File

This file contains reusable pytest fixtures
used across the automation framework.

Current functionality:
- Browser setup
- Browser teardown
- Playwright initialization
- Video recording
- Screenshot capture on failure

Purpose:
- Centralize browser management
- Improve maintainability
- Support reporting/debugging
"""

import pytest
import allure

from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def page(request):
    """
    Reusable Playwright page fixture.

    Flow:
    1. Launch browser
    2. Create browser context
    3. Open new page/tab
    4. Execute test
    5. Capture screenshot if test fails
    6. Close browser
    """

    # Initialize Playwright
    with sync_playwright() as p:

        # Launch Chromium browser
        browser = p.chromium.launch(

            # Browser visible during execution
            headless=False,

            # Slow down execution for debugging/demo
            slow_mo=100,

            # Open browser in maximized mode
            args=["--start-maximized"]
        )

        # Create browser context
        context = browser.new_context(

            # Disable fixed viewport
            no_viewport=True,

            # Record execution videos
            record_video_dir="videos/"
        )

        # Open new browser page/tab
        page = context.new_page()

        # Provide page object to test
        yield page

        # Capture screenshot if test fails
        if request.node.rep_call.failed:

            screenshot_path = (
                f"screenshots/{request.node.name}.png"
            )

            page.screenshot(
                path=screenshot_path,
                full_page=True
            )

            # Attach screenshot to Allure report
            allure.attach.file(
                screenshot_path,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

        # Close browser context
        context.close()

        # Close browser
        browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Pytest hook used to capture
    test execution result status.

    Required for:
    - Screenshot on failure
    - Custom reporting hooks
    """

    outcome = yield

    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)