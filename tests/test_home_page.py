from pages.home_page import HomePage
import pytest

@pytest.mark.smoke
def test_homepage_search(playwright, browser, page):
    """Test the search functionality on the home page."""
    home = HomePage(page)
    home.navigate_to_base_website()
    home.search("cyber insurance")

    cyber_locator = page.locator("//div[@aria-label='Cyber & Technology Insurance']")
    assert cyber_locator.is_visible()
