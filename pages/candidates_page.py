import allure
import os

from playwright.sync_api import Page

from pages.base_page import BasePage


class CandidatesPage(BasePage):

    def __init__(self, page: Page):

        super().__init__(page)

        self.page = page

        # ---------------------------------------------------
        # JOB MENU
        # ---------------------------------------------------

        self.more_options_menu = page.locator(
            ".mat-icon.notranslate.mat-mdc-menu-trigger"
        ).first

        # ---------------------------------------------------
        # ADD CANDIDATE
        # ---------------------------------------------------

        self.add_new_candidate_button = page.get_by_role(
            "button",
            name="user Add New Candidate"
        )

        self.complete_form_button = page.get_by_role(
            "button",
            name="Complete a Form"
        )

        # ---------------------------------------------------
        # RESUME UPLOAD
        # ---------------------------------------------------

        self.resume_upload_input = page.locator(
            "input[type='file']"
        )

        # ---------------------------------------------------
        # CANDIDATE FORM
        # ---------------------------------------------------

        self.first_name_input = page.get_by_role(
            "textbox",
            name="Enter First Name"
        )

        self.last_name_input = page.get_by_role(
            "textbox",
            name="Enter Last Name"
        )

        self.mobile_number_input = page.get_by_role(
            "textbox",
            name="Mobile Number"
        )

        self.email_input = page.get_by_role(
            "textbox",
            name="Email Id"
        )

        # ---------------------------------------------------
        # DATE OF JOINING
        # ---------------------------------------------------

        self.expected_joining_date = page.locator(
            "mat-datepicker-toggle button"
        ).first

        # ---------------------------------------------------
        # NOTICE PERIOD
        # ---------------------------------------------------

        self.notice_period_input = page.get_by_role(
            "spinbutton",
            name="Current Notice Period"
        )

        # ---------------------------------------------------
        # CTC
        # ---------------------------------------------------

        self.current_ctc_input = page.get_by_role(
            "textbox",
            name="Current CTC"
        )

        self.expected_ctc_input = page.get_by_role(
            "textbox",
            name="Expected CTC"
        )

        # ---------------------------------------------------
        # SOURCE
        # ---------------------------------------------------

        self.source_dropdown = page.get_by_text(
            "Select source"
        )

        self.other_source_option = page.get_by_role(
            "option",
            name="Other"
        )

        # ---------------------------------------------------
        # DEPARTMENT
        # ---------------------------------------------------

        self.department_dropdown = page.get_by_text(
            "Department",
            exact=True
        )

        self.department_option = page.get_by_text(
            "Corp"
        )

        # ---------------------------------------------------
        # RESPONSIBILITIES
        # ---------------------------------------------------

        self.responsibilities_input = page.get_by_role(
            "textbox",
            name="Responsibilities"
        )

        self.skills_input = page.get_by_role(
            "textbox",
            name="Candidate Skills"
        )

        # ---------------------------------------------------
        # SUBMIT
        # ---------------------------------------------------

        self.submit_button = page.get_by_role(
            "button",
            name="circleSubmit"
        )

        self.confirm_button = page.get_by_role(
            "button",
            name="Confirm"
        )

        # ---------------------------------------------------
        # SEARCH CANDIDATE
        # ---------------------------------------------------

        self.search_candidate_input = page.get_by_role(
            "textbox",
            name="Search for candidate"
        )

        self.add_candidate_icon = page.locator(
            ".mat-icon.notranslate.add"
        )

        # ---------------------------------------------------
        # CLOSE DIALOG
        # ---------------------------------------------------

        self.close_dialog_button = page.get_by_role(
            "button",
            name="close dialog"
        )

        # ---------------------------------------------------
        # HIRING
        # ---------------------------------------------------

        self.initiate_hiring_option = page.get_by_role(
            "menuitem",
            name="initiate hiring Initiate"
        )

        self.ok_button = page.get_by_role(
            "button",
            name="Ok"
        )

    # ---------------------------------------------------
    # OPEN CREATED JOB
    # ---------------------------------------------------

    @allure.step("Open created job")
    def open_created_job(
        self,
        job_title
    ):

        job_locator = self.page.locator(
            f"text='{job_title}'"
        ).first

        job_locator.scroll_into_view_if_needed()

        self.page.wait_for_timeout(2000)

        job_locator.click()

        self.page.wait_for_load_state(
            "networkidle"
        )

    # ---------------------------------------------------
    # OPEN ADD CANDIDATE MENU
    # ---------------------------------------------------

    @allure.step("Open Add Candidate menu")
    def open_add_candidate_menu(self):

        self.click(
            self.more_options_menu
        )

        self.page.wait_for_timeout(1000)

        self.page.get_by_role(
            "menuitem",
            name="Add Candidate"
        ).click()

        self.page.wait_for_timeout(3000)

    # ---------------------------------------------------
    # CREATE CANDIDATE
    # ---------------------------------------------------

    @allure.step("Create candidate")
    def create_candidate(
        self,
        first_name,
        last_name,
        email,
        mobile
    ):

        self.click(
            self.add_new_candidate_button
        )

        self.page.wait_for_timeout(2000)

        self.click(
            self.complete_form_button
        )

        self.page.wait_for_timeout(5000)

        resume_path = os.path.abspath(
            "test_data/resume.pdf"
        )

        self.resume_upload_input.set_input_files(
            resume_path
        )

        self.page.wait_for_timeout(15000)

        self.first_name_input.wait_for(
            state="visible"
        )

        self.first_name_input.fill(
            first_name
        )

        self.page.wait_for_timeout(1000)

        self.last_name_input.fill(
            last_name
        )

        self.page.wait_for_timeout(1000)

        self.mobile_number_input.fill(
            mobile
        )

        self.page.wait_for_timeout(1000)

        self.email_input.fill(
            email
        )

        self.page.wait_for_timeout(1000)

        self.expected_joining_date.click()

        self.page.wait_for_timeout(2000)

        self.page.keyboard.press(
            "ArrowRight"
        )

        self.page.keyboard.press(
            "Enter"
        )

        self.page.wait_for_timeout(2000)

        self.notice_period_input.fill(
            "0"
        )

        self.page.wait_for_timeout(1000)

        self.current_ctc_input.fill(
            "35000"
        )

        self.page.wait_for_timeout(1000)

        self.expected_ctc_input.fill(
            "45000"
        )

        self.page.wait_for_timeout(1000)

        self.click(
            self.source_dropdown
        )

        self.page.wait_for_timeout(1000)

        self.click(
            self.other_source_option
        )

        self.page.keyboard.press(
            "Escape"
        )

        self.page.wait_for_timeout(2000)

        self.click(
            self.department_dropdown
        )

        self.page.wait_for_timeout(1000)

        self.click(
            self.department_option
        )

        self.page.keyboard.press(
            "Escape"
        )

        self.page.wait_for_timeout(2000)

        self.responsibilities_input.fill(
            "Working on automation framework and agile delivery"
        )

        self.page.wait_for_timeout(1000)

        self.skills_input.fill(
            "Playwright Python Selenium API Testing"
        )

        self.page.wait_for_timeout(3000)

        self.submit_button.wait_for(
            state="visible"
        )

        self.submit_button.click()

        self.page.wait_for_timeout(3000)

        self.confirm_button.wait_for(
            state="visible"
        )

        self.confirm_button.click()

        self.page.wait_for_timeout(5000)

    # ---------------------------------------------------
    # ATTACH CANDIDATE
    # ---------------------------------------------------

    @allure.step("Attach candidate")
    def attach_candidate(
        self,
        first_name
    ):

        # Wait for ok_button with timeout - it may not always appear
        try:
            self.ok_button.wait_for(
                state="visible",
                timeout=5000
            )

            self.ok_button.click(
                force=True
            )

            self.page.wait_for_timeout(2000)

        except:
            # Ok button dialog may not appear in some cases
            self.page.wait_for_timeout(2000)
            pass

        self.search_candidate_input.wait_for(
            state="visible",
            timeout=10000
        )

        self.search_candidate_input.fill(
            first_name
        )

        self.page.wait_for_timeout(2000)

        # Wait for search results to load
        self.page.wait_for_load_state("networkidle")

        self.page.wait_for_timeout(3000)

        try:
            add_button = self.page.locator(
                ".mat-icon.notranslate.add"
            ).last

            add_button.wait_for(
                state="visible",
                timeout=5000
            )

            add_button.click(
                force=True
            )

        except:
            # If the first add button selector fails, try alternative selectors
            try:
                add_buttons = self.page.locator(
                    "button:has-text('add')"
                )
                if add_buttons.count() > 0:
                    add_buttons.last.click(
                        force=True
                    )
            except:
                pass

        self.page.wait_for_timeout(5000)

        # Try to close confirmation dialog if it appears
        try:

            self.ok_button.wait_for(
                state="visible",
                timeout=3000
            )

            self.ok_button.click(
                force=True
            )

        except:

            pass

        self.page.wait_for_timeout(3000)

        overlay = self.page.locator(
            ".cdk-overlay-backdrop"
        )

        if overlay.count() > 0:

            try:

                overlay.last.click(
                    force=True
                )

            except:

                pass

        self.page.wait_for_timeout(2000)

                # ---------------------------------------------------
        # CLOSE ATTACH CANDIDATE DIALOG
        # ---------------------------------------------------

        try:

            self.close_dialog_button.wait_for(
                state="visible",
                timeout=5000
            )

            self.close_dialog_button.click(
                force=True
            )

        except:

            pass

        self.page.wait_for_timeout(3000)

        # ---------------------------------------------------
        # CLOSE ANY REMAINING OVERLAY
        # ---------------------------------------------------

        self.page.keyboard.press(
            "Escape"
        )

        self.page.wait_for_timeout(2000)

        # ---------------------------------------------------
        # DEBUG URL
        # ---------------------------------------------------

        print(
            "Current URL after attach:",
            self.page.url
        )

        # ---------------------------------------------------
        # DEBUG OVERLAYS
        # ---------------------------------------------------

        print(
            "Overlay Count:",
            self.page.locator(
                ".cdk-overlay-backdrop"
            ).count()
        )

        print(
            "Dialog Count:",
            self.page.locator(
                "mat-dialog-container"
            ).count()
        )

        self.page.wait_for_timeout(3000)

    # ---------------------------------------------------
    # MOVE CANDIDATE TO SELECTED STAGE
    # ---------------------------------------------------

    @allure.step("Move candidate to stage by column selector")
    def move_candidate_to_stage(
        self,
        candidate_name,
        source_column_selector=".column-body:first-of-type",
        target_column_id=None,
        target_column_selector=None
    ):
        """
        Move a candidate card between Kanban board stages.
        
        Args:
            candidate_name: Name of the candidate to move
            source_column_selector: CSS selector for source column (default: first column)
            target_column_id: Column ID number (e.g., 7) - uses pattern #column-{id} > .column-kanban-board > .column-body
            target_column_selector: Direct CSS selector for target column (alternative to target_column_id)
        """
        
        # Close any open overlays
        overlay = self.page.locator(".cdk-overlay-backdrop")
        if overlay.count() > 0:
            try:
                overlay.last.click(force=True)
            except:
                pass
        
        self.page.wait_for_timeout(1000)
        
        source_body = self.page.locator(source_column_selector).first
        
        # Determine target column selector
        if target_column_id:
            target_selector = f"#column-{target_column_id} .column-kanban-board .column-body"
        elif target_column_selector:
            target_selector = target_column_selector
        else:
            target_selector = ".column-body:nth-of-type(2)"
        
        target_body = self.page.locator(target_selector).first
        
        candidate_card = source_body.locator(
            ".candidate-info",
            has=self.page.get_by_text(candidate_name)
        ).first
        
        candidate_card.wait_for(state="visible", timeout=30000)
        candidate_card.scroll_into_view_if_needed()
        self.page.wait_for_timeout(500)
        
        target_body.wait_for(state="attached", timeout=15000)
        target_body.scroll_into_view_if_needed()
        self.page.wait_for_timeout(500)
        
        # DEBUG: Log column information
        print(f"\n=== DEBUG: Moving {candidate_name} ===")
        print(f"Source selector: {source_column_selector}")
        print(f"Target ID: {target_column_id}, Selector: {target_selector}")
        print(f"Candidate card found: {candidate_card.count() > 0}")
        print(f"Target body found: {target_body.count() > 0}")
        
        drag_succeeded = False
        
        # Strategy 1: Native drag_and_drop
        try:
            self.page.drag_and_drop(candidate_card, target_body, force=True)
            self.page.wait_for_timeout(1000)
            if target_body.locator('.candidate-info', has=self.page.get_by_text(candidate_name)).count() > 0:
                drag_succeeded = True
        except Exception:
            pass
        
        # Strategy 2: Precise coordinate-based mouse drag
        if not drag_succeeded:
            try:
                candidate_box = candidate_card.bounding_box()
                if not candidate_box:
                    candidate_card.scroll_into_view_if_needed()
                    candidate_box = candidate_card.bounding_box()
                
                target_box = target_body.bounding_box()
                if not target_box:
                    target_body.scroll_into_view_if_needed()
                    target_box = target_body.bounding_box()
                
                if candidate_box and target_box:
                    start_x = candidate_box["x"] + candidate_box["width"] / 2
                    start_y = candidate_box["y"] + candidate_box["height"] / 2
                    
                    # Target upper area of the column to ensure landing
                    end_x = target_box["x"] + 50
                    end_y = target_box["y"] + 50
                    
                    for attempt in range(3):
                        try:
                            self.page.mouse.move(start_x, start_y)
                            self.page.mouse.down()
                            self.page.mouse.move(start_x + 5, start_y + 5, steps=3)
                            self.page.mouse.move(end_x, end_y, steps=25)
                            self.page.mouse.up()
                            self.page.wait_for_timeout(1000)
                            
                            if target_body.locator('.candidate-info', has=self.page.get_by_text(candidate_name)).count() > 0:
                                drag_succeeded = True
                                break
                        except Exception:
                            try:
                                self.page.mouse.up()
                            except:
                                pass
            except Exception:
                pass
        
        # Strategy 3: JS HTML5 drag/drop events
        if not drag_succeeded:
            try:
                source_handle = candidate_card.element_handle()
                target_handle = target_body.element_handle()
                if source_handle and target_handle:
                    self.page.evaluate(
                        "([source, target]) => {\n"
                        "  const dataTransfer = new DataTransfer();\n"
                        "  const dispatch = (node, type) => node.dispatchEvent(new DragEvent(type, {\n"
                        "    dataTransfer, bubbles: true, cancelable: true\n"
                        "  }));\n"
                        "  dispatch(source, 'dragstart');\n"
                        "  dispatch(target, 'dragenter');\n"
                        "  dispatch(target, 'dragover');\n"
                        "  dispatch(target, 'drop');\n"
                        "  dispatch(source, 'dragend');\n"
                        "}",
                        source_handle,
                        target_handle
                    )
                    self.page.wait_for_timeout(1000)
                    if target_body.locator('.candidate-info', has=self.page.get_by_text(candidate_name)).count() > 0:
                        drag_succeeded = True
            except Exception:
                pass
        
        # Strategy 4: Menu-based fallback
        if not drag_succeeded:
            try:
                candidate_card.click(force=True)
                self.page.wait_for_timeout(500)
                
                menu_button = candidate_card.locator(
                    ".mat-icon.notranslate.mat-mdc-menu-trigger.more-vert"
                ).first
                
                menu_button.wait_for(state="visible", timeout=10000)
                menu_button.click(force=True)
                self.page.wait_for_timeout(1000)
            except Exception:
                pass
        
        # Verify candidate is in target column
        target_candidate = target_body.locator(
            ".candidate-info",
            has=self.page.get_by_text(candidate_name)
        )
        
        target_candidate.wait_for(state="visible", timeout=30000)
        self.page.wait_for_timeout(1000)
    
    @allure.step("Move candidate to Selected stage")
    def move_candidate_to_selected_stage(
        self,
        candidate_name
    ):
        """
        Move a candidate from 'New Candidates' to 'Selected' stage.
        """
        self.move_candidate_to_stage(
            candidate_name,
            source_column_selector=".column-body:first-of-type",
            target_column_selector=".column-body:nth-of-type(2)"
        )
    
    @allure.step("Move candidate to Submitted stage")
    def move_candidate_to_submitted_stage(
        self,
        candidate_name,
        column_id=7
    ):
        """
        Move a candidate to the 'Submitted' stage using drag-and-drop.
        Holds the candidate card and drags it to the target column.
        """
        # Close overlays
        overlay = self.page.locator(".cdk-overlay-backdrop")
        if overlay.count() > 0:
            try:
                overlay.last.click(force=True)
            except:
                pass
        
        self.page.wait_for_timeout(1000)
        
        # Find the candidate card in the first column
        new_candidates_body = self.page.locator(".column-body").first
        candidate_card = new_candidates_body.locator(
            ".candidate-info",
            has=self.page.get_by_text(candidate_name)
        ).first
        
        candidate_card.scroll_into_view_if_needed()
        self.page.wait_for_timeout(500)
        
        # Get the target column
        target_column = self.page.locator(f"#column-{column_id}")
        
        # Scroll the target column into view
        self.page.evaluate(
            """
            (columnId) => {
                const column = document.querySelector(`#column-${columnId}`);
                if (column) {
                    column.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
                }
            }
            """,
            column_id
        )
        
        self.page.wait_for_timeout(2000)
        
        # Get the target column body for drag-and-drop
        target_body = self.page.locator(f"#column-{column_id} .column-kanban-board .column-body").first
        
        # DRAG the candidate card to the target column
        self.page.drag_and_drop(candidate_card, target_body, force=True)
        
        self.page.wait_for_timeout(2000)
        
        # Verify candidate is now in the target column
        target_candidate = target_body.locator(
            ".candidate-info",
            has=self.page.get_by_text(candidate_name)
        )
        
        target_candidate.wait_for(state="visible", timeout=30000)
        self.page.wait_for_timeout(1000)

    # ---------------------------------------------------
    # INITIATE HIRING
    # ---------------------------------------------------

    @allure.step("Initiate hiring")
    def initiate_hiring(
        self,
        candidate_name=None
    ):

        self.page.wait_for_timeout(5000)

        overlay = self.page.locator(
            ".cdk-overlay-backdrop"
        )

        if overlay.count() > 0:

            try:

                overlay.last.click(
                    force=True
                )

            except:

                pass

        self.page.wait_for_timeout(2000)

        candidate_card = self.page.locator(
            "div.column",
            has=self.page.get_by_text("Selected")
        ).locator(
            ".candidate-info",
            has=self.page.get_by_text(candidate_name)
        ).first if candidate_name else self.page.locator(
            ".candidate-info"
        ).first

        candidate_card.wait_for(
            state="visible",
            timeout=30000
        )

        candidate_card.click(
            force=True
        )

        self.page.wait_for_timeout(3000)

        email_input = self.page.get_by_role(
            "combobox",
            name="Enter email address"
        )

        if email_input.is_visible():

            email_input.fill(
                "new22@gmail.com"
            )

        self.page.wait_for_timeout(1000)

        subject_input = self.page.get_by_role(
            "textbox",
            name="Subject"
        )

        if subject_input.is_visible():

            subject_input.fill(
                "Congratulations"
            )

        self.page.wait_for_timeout(1000)

        body = self.page.locator(
            ".ql-editor"
        )

        if body.is_visible():

            body.fill(
                "Congratulations"
            )

        self.page.wait_for_timeout(2000)

        menu = self.page.locator(
            ".mat-icon.notranslate.mat-mdc-menu-trigger.more-vert"
        ).first

        menu.wait_for(
            state="visible",
            timeout=30000
        )

        menu.click(
            force=True
        )

        self.page.wait_for_timeout(2000)

        self.initiate_hiring_option.wait_for(
            state="visible"
        )

        self.initiate_hiring_option.click(
            force=True
        )

        self.page.wait_for_timeout(3000)

        self.confirm_button.wait_for(
            state="visible"
        )

        self.confirm_button.click(
            force=True
        )

        self.page.wait_for_timeout(4000)

        try:

            if self.ok_button.is_visible():

                self.ok_button.click(
                    force=True,
                    timeout=5000
                )

        except:

            pass

        self.page.wait_for_timeout(5000)