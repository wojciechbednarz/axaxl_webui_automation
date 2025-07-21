from pages.base_page import BasePage
import pytest

@pytest.mark.smoke
@pytest.mark.base_page
class TestBasePage:
    def test_navigate_to_base_website(self, page):
        """Test that the base website can be navigated to."""
        base_page = BasePage(page)
        base_page.navigate_to_base_website()
        assert page.url == "https://axaxl.com/"

    def test_check_title(self, page):
        """Test that the title of the page can be checked."""
        base_page = BasePage(page)
        base_page.navigate_to_base_website()
        base_page.check_title("Global Commercial Insurance and Reinsurance | AXA XL")

    def test_click_element(self, page):
        """Test that an element can be clicked."""
        base_page = BasePage(page)
        base_page.navigate_to_base_website()
        base_page.click_element("//a[@id='logo-white']//img[@alt='AXA XL Logo']")
        assert page.url == "https://axaxl.com/"

    @pytest.mark.parametrize("value", ["cyber insurance", "property insurance"])
    def test_fill_field(self, page, value):
        """Test that a field can be filled."""
        base_page = BasePage(page)
        base_page.navigate_to_base_website()
        base_page.click_element(".header_search_btn")
        base_page.fill_field("//input[@placeholder='Start Searching...']", value)
        assert page.locator("//input[@placeholder='Start Searching...']").input_value() == value