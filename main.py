from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from getData import get_data

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.kannapedia.net/strains")

# Click through cookies button
allow_button = driver.find_element(By.CLASS_NAME, 'CookieConsent--allow')
allow_button.click()


# Function to get hrefs of strain links from the current page
def get_strain_hrefs():
    # Locate all strain links on the page
    strain_link_elements = driver.find_elements(By.CSS_SELECTOR, 'h2.SearchResults--strain')

    # Extract and return hrefs of visible links
    hrefs = [strain_link.find_element(By.TAG_NAME, 'a').get_attribute('href') for strain_link in strain_link_elements if
             strain_link.is_displayed()]
    return hrefs


# Iterate through the pages
page_number = 1
while True:
    print(f"Fetching links from Page {page_number}")

    # Get hrefs of visible strain links on the current page
    strain_hrefs = get_strain_hrefs()

    # Print the hrefs
    print(strain_hrefs)
    for link in strain_hrefs:
        get_data(link)

    # Scroll to the bottom of the page to trigger loading more items (if needed)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Adjust the sleep time if needed

    # Locate the "Next" button and click it
    next_button = driver.find_element(By.CSS_SELECTOR, 'button[class*="Pagination--next"]')
    if next_button and next_button.is_enabled():
        next_button.click()
        time.sleep(2)  # Adjust the sleep time if needed
        page_number += 1
    else:
        print("No more pages. Exiting.")
        break

driver.close()
