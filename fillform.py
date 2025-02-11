import time
import csv
# import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Auto-install ChromeDriver
# chromedriver_autoinstaller.install()

# Google Form URL
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdQlqBl2-2NYxbSGL5GUaJ022mYixDevciKaHB15WwYfoZUDw/viewform"

# CSV File Path
CSV_FILE_PATH = "users.csv"

def load_csv_data(file_path):
    with open(file_path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            yield row

def fill_google_form(data):
    driver = webdriver.Chrome()
    driver.get(FORM_URL)
    wait = WebDriverWait(driver, 10)

    try:
        text_fields = ["First Name", "Last Name", "Age"]
        
        for index, field_name in enumerate(text_fields):
            field_xpath = f"(//input[@type='text' or @type='email' or @type='url'])[{index + 1}]"
            field = wait.until(EC.element_to_be_clickable((By.XPATH, field_xpath)))
            driver.execute_script("arguments[0].scrollIntoView(true);", field)
            time.sleep(1)  # Short delay
            field.clear()
            field.send_keys(data[field_name])

        # Handle Gender (Radio Button)
        gender_value = data["Gender"].strip().lower()
        radio_buttons = driver.find_elements(By.XPATH, "//div[@role='radiogroup']//span")

        for button in radio_buttons:
            if button.text.strip().lower() == gender_value:
                driver.execute_script("arguments[0].scrollIntoView(true);", button)
                time.sleep(1)  # Short delay
                button.click()
                break

        # Submit
        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Submit')]")))
        driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        time.sleep(1)
        submit_button.click()

        print(f"✅ Form submitted for {data['First Name']} {data['Last Name']}!")

    except Exception as e:
        print("❌ Error:", e)

    finally:
        time.sleep(5)
        driver.quit()

# Process each entry
for row_data in load_csv_data(CSV_FILE_PATH):
    fill_google_form(row_data)
