# Linkedin Experience Crawler

## Overview
This Python-based tool crawls LinkedIn to gather experience details of various profiles using Selenium WebDriver. It's designed for individuals and organizations needing to automate the collection of professional experience data from LinkedIn profiles.

## Prerequisites
- Python 3.x
- Selenium WebDriver
- A LinkedIn account

## Setup
1. **Clone the Repository**: Clone this repository to your local machine or download the source code.

2. **Install Dependencies**: Run `pip install -r requirements.txt` to install the required Python libraries, including Selenium.

3. **Set Up Credentials**:
   - Create a file named `constants.py` in the project directory.
   - In `constants.py`, enter your LinkedIn credentials:
     ```python
     email = "your_email_here"
     password = "your_password_here"
     ```

## Usage
1. **Configure Settings**: 
   - Open `crawler.py`.
   - Modify the `sleep_time` variable to adjust the delay between requests (to prevent being rate-limited or blocked by LinkedIn).
   - Set `headless_mode` to `True` or `False` depending on whether you want the Selenium WebDriver to run the browser in the background.

2. **Run the Crawler**: Execute `python crawler.py` in your terminal. Ensure you're in the project's root directory.

3. **View Results**: 
   - The crawled data will be saved in a JSON file within the project directory.
   - Check the output JSON file for the crawled experience data.

## Important Notes
- This tool is for educational purposes. Be aware of LinkedIn's terms of service regarding automated data collection.
- Using this script might lead to your LinkedIn account being temporarily or permanently blocked due to suspicious activity.
- Always use a delay between requests to be respectful to LinkedIn's servers and to minimize the risk of your account being flagged.

## Contributions
Contributions, issues, and feature requests are welcome. Feel free to check [issues page](your-repository-link) if you want to contribute.

## License
This project is [MIT licensed](your-license-link).
