from pages.contact_us_page import ContactUsPage
import pytest


@pytest.mark.functional
def test_contact_us_page_navigation_positive(playwright, browser, page):
    """Test the Contact Us page navigation and content."""
    contact_us = ContactUsPage(page)
    contact_us.navigate_to_contact_us()
    contact_us.submit_contact_form("John", "Doe",
                                   "United States", "johndoe@gmail.com",
                                   "Other", state="California")



@pytest.mark.negative
def test_contact_us_page_navigation_incorrect_title(playwright, browser, page):
    """Test the Contact Us page with an incorrect title."""
    contact_us = ContactUsPage(page)
    contact_us.navigate_to_contact_us()

    # Verify that the title does not match an incorrect value
    with pytest.raises(AssertionError):
        contact_us.check_title("Incorrect Title")

@pytest.mark.negative
def test_contact_us_page_submit_form_without_required_fields(playwright, browser, page):
    """Test submitting the contact form without required fields."""
    contact_us = ContactUsPage(page)
    contact_us.navigate_to_contact_us()

    # Attempt to submit the form without filling required fields
    with pytest.raises(Exception):
        contact_us.submit_contact_form("", "", "", "", "")