from pages.about_us_page import AboutUsPage
import pytest

@pytest.mark.smoke
def test_about_us_page_heading_positive(playwright, browser, page):
    """Test the About Us page navigation and content."""
    about_us = AboutUsPage(page)
    about_us.navigate_to_about_us()
    about_us.verify_heading("About AXA XL")


@pytest.mark.negative
def test_about_us_page_heading_negative(playwright, browser, page):
    """Test the About Us page with an incorrect heading."""
    about_us = AboutUsPage(page)
    about_us.navigate_to_about_us()

    # Verify that the heading does not match an incorrect value
    with pytest.raises(AssertionError):
        about_us.verify_heading("Incorrect Heading")
