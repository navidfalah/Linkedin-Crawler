# LinkedIn Profile Crawler

This project contains a set of Python scripts that automate the process of searching for LinkedIn profiles based on the names provided in an input CSV file, extracting specific information from the profiles, and storing the results in an output CSV file.

### Project Structure 📂

The project consists of the following files and directories:

```
linkedin-profile-crawler/
├── constants.py                 # Contains credentials and constants
├── crawler.py                   # Main script for crawling LinkedIn profiles
├── input_data.csv               # CSV file containing names to search for
├── notfound_data.csv            # CSV file for profiles that couldn't be found
├── output_data.csv              # CSV file containing the crawled data
├── README.md                    # This README file
├── requirements.txt             # List of Python package dependencies
└── utils/
    ├── department_separator.py  # Utility script for department separation
    ├── extracted_content.json   # JSON file with extracted content
    ├── __init__.py              # Makes utils a Python package
    ├── students_separator.py    # Utility script for student separation
    └── teacher_separator.py     # Utility script for teacher separation
```

### Setup Instructions 🛠️

1. Create a LinkedIn account if you do not already have one.
2. Clone this repository to your local machine.
3. Create a `constants.py` file with your LinkedIn credentials and other constants.
   
   Example `constants.py`:
   ```python
   email = 'your_email@example.com'
   password = 'your_password'
   ```
4. Install the required Python packages using the `requirements.txt` file:
   ```
   pip install -r requirements.txt
   ```
   The most important packages are `selenium` and `beautifulsoup4`.

### Running the Crawler 🚀

1. Ensure you have a `input_data.csv` file in the root directory with the names you wish to search on LinkedIn.
2. Run the `crawler.py` script:
   ```
   python crawler.py
   ```
3. After the script finishes, check the `output_data.csv` for successfully found profiles and `notfound_data.csv` for profiles that could not be found on LinkedIn.

### Emojis Key 🗝️

- 📂: Indicates a directory or file
- 🛠️: Represents the setup process
- 🚀: Denotes the action of running the script

### Support 👋

If you encounter any problems or have questions, feel free to contact me by email at navid.falah7@gmail.com or reach out on Telegram at `navid_falah`.
