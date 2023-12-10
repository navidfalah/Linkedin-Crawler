from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from constants import email, password
import re
from bs4 import BeautifulSoup
import json

name_researcher = "Behnam Yousefi"

# Initialize the WebDriver
driver = webdriver.Chrome()  # Or whichever browser you're using

driver.get("https://www.linkedin.com/login")
username = driver.find_element(By.ID, "username")
username.send_keys(email)
password_input = driver.find_element(By.ID, 'password')
password_input.clear()
password_input.send_keys(password)

sleep(3)

sign_in_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Sign in']"))
)
sign_in_button.click()

# Wait for login to complete
sleep(5)


driver.get(f"https://www.linkedin.com/search/results/people/?keywords={name_researcher}&origin=GLOBAL_SEARCH_HEADER&sid=GGF")

sleep(5)
# Find the first `li` tag
first_li = driver.find_element(By.CSS_SELECTOR, "li.reusable-search__result-container")

# Find the first link within the `li` tag
first_link = first_li.find_element(By.TAG_NAME, "a")

# Click on the link
first_link.click()

sleep(5)


# Use JavaScript to select all content, copy it to a hidden textarea, and return its value
page_source = driver.page_source

soup = BeautifulSoup(page_source, 'html.parser')

# Define the structure to hold extracted data
extracted_data = []

# Find all <li> tags with the specified class
li_tags = soup.find_all('li', class_='artdeco-list__item')

for li in li_tags:
    # Extract the href attribute from <a> tags and the src attribute from <img> tags within the 'ivm-image-view-model' class
    a_tag = li.find('a', {'data-field': 'experience_company_logo'})
    img_tag = li.find('div', class_='ivm-image-view-model').find('img') if li.find('div', class_='ivm-image-view-model') else None

    if img_tag:
        image_alt = img_tag.get('alt', '')

        # Remove 'logo' if it is at the end of the image_alt text
        # image_alt = re.sub(r'\s+logo$', '', image_alt, flags=re.IGNORECASE)
        image_alt = re.sub(r'\s+logo$|\\u[0-9a-fA-F]{4}|[0-9]+', '', image_alt, flags=re.IGNORECASE)

        link = a_tag.get('href', '') if a_tag else ''
        if link:  # Check if link is not empty
            data = {
                'link': link,
                'image_src': img_tag.get('src', ''),
                'image_alt': image_alt,
            }

            extracted_data.append(data)

# Write the extracted content to a new file in JSON format
with open('extracted_content.json', 'w', encoding='utf-8') as file:
    json.dump(extracted_data, file, indent=4)


driver.quit()
