from pages.base_page import BasePage

class AboutUsPage(BasePage):
    ABOUT_US_TITLE = "About AXA XL Insurance  | AXA XL"
    ABOUT_US_HEADER = "//h1[normalize-space()='About AXA XL']"
    ABOUT_US_CONTENT = ".typo18.block-with-text"
    ABOUT_AXA_XL = "//a[@class='footer__linkStyle'][normalize-space()='About AXA XL']"

    def __init__(self, page):
        super().__init__(page)

    def navigate_to_about_us(self):
        """Navigate to the About Us page and verify its content."""
        self.navigate_to_base_website()
        self.click_element(self.ABOUT_AXA_XL)
        self.check_title(self.ABOUT_US_TITLE)
        self.is_visible(self.ABOUT_US_CONTENT)

    def verify_heading(self, expected: str):
        """Verify that the About Us page has the expected heading."""
        heading_text = self.page.text_content(self.ABOUT_US_HEADER)
        assert expected in heading_text