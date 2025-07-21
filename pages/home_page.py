from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger(__name__)

class HomePage(BasePage):
    SIDE_POPUP = "#hamburger"
    ABOUT_AXA_XL = "//a[@aria-label='Open Menu About AXA XL']"
    SEARCH_BUTTON = "//div[@class='header_search_btn']"
    SEARCH_INPUT = "input[placeholder='Start Searching...']"
    SEARCH_RESULTS = "//h1[normalize-space()='Search Results']"

    def __init__(self, page):
        super().__init__(page)

    def search(self, query: str):
        """Perform a search on the home page."""
        try:
            logger.info("Performing search for query: %s", query)
            self.wait_for_element(self.SEARCH_BUTTON)
            self.click_element(self.SEARCH_BUTTON)
            self.wait_for_element(self.SEARCH_INPUT)
            self.fill_field(self.SEARCH_INPUT, query)
            self.page.keyboard.press("Enter")
            self.wait_for_element(self.SEARCH_RESULTS)
        except Exception as e:
            logger.error("Search failed: %s", e)
            raise

    def navigate_to_about_us(self):
        """Navigate to the About Us page from the home page."""
        self.click_element(self.ABOUT_AXA_XL)
