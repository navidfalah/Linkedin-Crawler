from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import email, password
import re
from bs4 import BeautifulSoup
import csv
from time import sleep


path_enterance = "input_data.csv"
path_output = "output_data.csv"
path_notfound_output = "notfound_data.csv"


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

def loginner():
    driver.get("https://www.linkedin.com/login")
    username = wait.until(EC.visibility_of_element_located((By.ID, "username")))
    username.send_keys(email)
    
    password_input = wait.until(EC.visibility_of_element_located((By.ID, 'password')))
    password_input.clear()
    password_input.send_keys(password)

    sign_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Sign in']")))
    sign_in_button.click()

def searcher(name_researcher):
    driver.get(f"https://www.linkedin.com/search/results/people/?keywords={name_researcher}&origin=FACETED_SEARCH")
    first_li = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "li.reusable-search__result-container")))
    first_link = first_li.find_element(By.TAG_NAME, "a")
    first_link.click()

    sleep(3)

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    
    position_tag = soup.find('div', class_='text-body-medium break-words')
    current_position = position_tag.text.strip() if position_tag else ''
    
    experiences = []
    li_tags = soup.find_all('li', class_='artdeco-list__item')
    for li in li_tags:
        a_tag = li.find('a', {'data-field': 'experience_company_logo'})
        img_tag = li.find('div', class_='ivm-image-view-model').find('img') if li.find('div', class_='ivm-image-view-model') else None
        if img_tag:
            image_alt = img_tag.get('alt', '')
            image_alt = re.sub(r'\s+logo$|\\u[0-9a-fA-F]{4}|[0-9]+', '', image_alt, flags=re.IGNORECASE)
            link = a_tag.get('href', '') if a_tag else ''
            if link:
                data = {
                    'link': link,
                    'experience': image_alt,
                }
                experiences.append(data)

    return current_position, experiences

data_dict = {}

with open(path_enterance, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    data = list(reader)

for row in data:
    if row:
        # change based on your data 
        latin_name = row[2]
        family_name = row[3]
        key = row[0]
        value = f"{latin_name} {family_name}"
        data_dict[key] = value

loginner()

data = []

with open(path_enterance, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        if row:
            data.append(row)

for row in data:
    id_name = row[0]
    # change based on yout data
    name_value = f"{row[2]} {row[3]}"
    try:
        position, experiences_json = searcher(name_value)
        with open(path_output, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            updated_row = row + [position, str(experiences_json)]
            writer.writerow(updated_row)
    except Exception as e:
        with open(path_notfound_output, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(row)

driver.quit()
