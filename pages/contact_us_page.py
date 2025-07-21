from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger(__name__)

class ContactUsPage(BasePage):
    AXA_CONTACT_US_PLAIN_TEXT = "Contact Us"
    AXA_FOOTER_LABEL = "AXA XL Footer Menu"
    CONTACT_US_LOCATOR = "//a[normalize-space()='Contact Us']"
    CONTACT_US_TITLE = "Contact Us | AXA XL"
    CONTACT_US_FORM = "#form1"
    START_THE_CONVERSATION_BTN = "//span[normalize-space()='Start The Conversation']"
    FIRST_NAME_FIELD = "#firtNameTxt"
    LAST_NAME_FIELD = "#lastNameTxt"
    EMAIL_FIELD = "#emailTxt"
    COUNTRY_DROPDOWN = "#countryDdl"
    WHAT_BEST_DESCRIBES_YOU_DROPDOWN = "#requestTypeDdl"
    STATE_FIELD = "#stateDdl"

    def __init__(self, page):
        super().__init__(page)

    def select_from_dropdown(self, dropdown_locator: str, option_text: str):
        """Select an option from a dropdown."""
        try:
            logger.info("Selecting option '%s' from dropdown '%s'", option_text, dropdown_locator)
            self.wait_for_element(dropdown_locator)
            self.page.select_option(dropdown_locator, option_text)
        except Exception as e:
            logger.error("Failed to select option from dropdown: %s", e)
            raise

    def navigate_to_contact_us(self):
        """Navigate to the Contact Us page and verify its content."""
        try:
            logger.info("Navigating to Contact Us page")
            self.navigate_to_base_website()
            self.get_by_label_and_link_role(self.AXA_FOOTER_LABEL, self.AXA_CONTACT_US_PLAIN_TEXT).click()
            self.check_title(self.CONTACT_US_TITLE)
            self.is_visible(self.CONTACT_US_FORM)
        except Exception as e:
            logger.error("Failed to navigate to Contact Us page: %s", e)
            raise

    def wait_for_state_dropdown(self):
        """Wait for the state dropdown to be present."""
        try:
            logger.info("Waiting for state dropdown to be present")
            return self.page.wait_for_selector(self.STATE_FIELD, timeout=5000)
        except Exception as e:
            logger.error("State dropdown not found: %s", e)
            raise

    def verify_contact_form(
            self, first_name: str, last_name: str, country: str, email: str, describe: str, state: str = ""):
        """Verify contact form fields."""
        try:
            logger.info("Verifying contact form fields")
            self.expect(self.get_by_textbox_role("First Name")).to_have_value(first_name)
            self.expect(self.get_by_textbox_role("Last Name")).to_have_value(last_name)
            self.expect(self.get_by_textbox_role("Email Address")).to_have_value(email)
            self.expect(self.get_by_exact_label("Country").locator("option:checked")).to_contain_text(country)
            if state:
                self.expect(self.get_by_exact_label("State").locator("option:checked")).to_contain_text(state)
            self.expect(
                self.get_by_exact_label("What Best Describes You").locator("option:checked")).to_contain_text(describe)
        except AssertionError as e:
            logger.error("Contact Us form verification failed: %s", e)
            raise

    def submit_contact_form(
            self, first_name: str, last_name: str, country: str, email: str, describe: str, state: str = "California"):
        """Fill and submit the contact form."""
        try:
            self.fill_field(self.FIRST_NAME_FIELD, first_name)
            self.fill_field(self.LAST_NAME_FIELD, last_name)
            self.fill_field(self.EMAIL_FIELD, email)
            self.select_from_dropdown(self.COUNTRY_DROPDOWN, country)
            if self.wait_for_state_dropdown():  # Ensure state dropdown is ready
                self.select_from_dropdown(self.STATE_FIELD, state)
            self.select_from_dropdown(self.WHAT_BEST_DESCRIBES_YOU_DROPDOWN, describe)
            self.verify_contact_form(first_name, last_name, country, email, describe, state)
            self.click_element(self.START_THE_CONVERSATION_BTN)
        except Exception as e:
            logger.error("Failed to submit contact form: %s", e)
            raise
