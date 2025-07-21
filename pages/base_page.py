from playwright.sync_api import Page, expect
from utils.logger import get_logger

logger = get_logger(__name__)

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.expect = expect
        self.base_url = "https://axaxl.com/"
        self.logo = "//a[@id='logo-white']//img[@alt='AXA XL Logo']"
        self.base_title = "Global Commercial Insurance and Reinsurance | AXA XL"

    def handle_cookies(self):
        """Handle cookie consent if present."""
        logger.info("Handling cookies consent")
        cookies = self.page.get_by_role("link", name="Accept All")
        if cookies.is_visible():
            logger.info("Accepting cookies")
            cookies.click()
        else:
            logger.info("No cookie consent banner found")

    def navigate_to_base_website(self):
        """Navigate to the base website and verify the title and logo."""
        logger.info("Navigating to base website: %s", self.base_url)
        self.page.goto(self.base_url)
        self.handle_cookies()
        self.check_title(self.base_title)
        self.is_visible(self.logo)

    def check_title(self, title):
        """Check if the current page title matches the expected title."""
        logger.info("Checking page title: %s", title)
        self.expect(self.page).to_have_title(title)

    def click_element(self, selector: str):
        """Click an element specified by the selector."""
        logger.info("Clicking element with selector: %s", selector)
        try:
            element = self.page.locator(selector)
            element.click(timeout=5000)
        except Exception as e:
            logger.error("Failed to click element: %s", e)
            raise

    def fill_field(self, selector: str, value: str):
        """Fill a field specified by the selector with the given value."""
        logger.info("Filling field with selector: %s, value: %s", selector, value)
        try:
            element = self.page.locator(selector)
            element.fill(value, timeout=5000)
        except Exception as e:
            logger.error("Failed to fill field: %s", e)
            raise

    def is_visible(self, selector: str) -> bool:
        """Check if an element specified by the selector is visible."""
        logger.info("Checking visibility of element with selector: %s", selector)
        try:
            self.page.wait_for_selector(selector, state='visible', timeout=5000)
        except Exception as e:
            logger.error("Element not visible: %s", e)
            return False
        return self.page.is_visible(selector)

    def wait_for_element(self, selector: str):
        """Wait for an element specified by the selector to be present in the DOM."""
        logger.info("Waiting for element with selector: %s", selector)
        try:
            self.page.wait_for_selector(selector, timeout=5000)
        except Exception as e:
            logger.error("Element not found: %s", e)
            raise

    def get_by_label_and_link_role(self, label: str, name: str):
        """Get an element by its label and role."""
        logger.info("Getting element by label: %s and link name: %s", label, name)
        try:
            return self.page.get_by_label(label).get_by_role("link", name=name)
        except Exception as e:
            logger.error("Failed to get element by label and role: %s", e)
            raise

    def get_by_textbox_role(self, name: str = None):
        """Get an element by its role and name."""
        logger.info("Getting element by 'textbox' role and name: %s", name)
        try:
            return self.page.get_by_role("textbox", name=name)
        except Exception as e:
            logger.error("Failed to get element by role: %s", e)
            raise

    def get_by_exact_label(self, label: str):
        """Get an element by its label."""
        logger.info("Getting element by label: %s", label)
        try:
            return self.page.get_by_label(label, exact=True)
        except Exception as e:
            logger.error("Failed to get element by label: %s", e)
            raise