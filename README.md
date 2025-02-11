# Google Form Automation with Selenium

This project automates the process of filling out a Google Form using data from a CSV file. It utilizes Selenium WebDriver to interact with the form elements and submit responses programmatically.

## 📌 Features
- Automatically opens a Google Form.
- Reads data from a CSV file.
- Fills out text fields, selects radio buttons, and submits the form.
- Handles multiple form submissions if multiple rows are present in the CSV file.

## 🛠 Requirements
### Install dependencies:
Ensure you have Python installed (>=3.8) and install required libraries using:
```sh
pip install selenium
```
### Setup ChromeDriver:
1. **Download ChromeDriver**: Ensure you have the correct version matching your Chrome browser from [ChromeDriver download](https://sites.google.com/chromium.org/driver/).
2. **Set the path in your script**:
   ```python
   CHROME_DRIVER_PATH = "path/to/chromedriver"
   ```

## 🚀 Usage
### 1️⃣ Prepare the CSV file
Create a `users.csv` file with the following structure:
```csv
First Name,Last Name,Gender,Age
John,Doe,Male,25
Jane,Smith,Female,22
```

### 2️⃣ Configure the script
Update the script with the Google Form URL:
```python
FORM_URL = "your_google_form_url"
```

### 3️⃣ Run the script
Execute the script:
```sh
python fillform.py
```
The script will open the form, fill out the fields using CSV data, and submit the form.

## 🔍 Handling Errors
### Invalid Element State Error
If you encounter:
```
invalid element state: Element is not currently interactable
```
- Ensure the form fields are visible before interacting.
- Modify the script to wait until elements are ready using `WebDriverWait`.

### ChromeDriver Compatibility Issue
If you see:
```
This version of ChromeDriver only supports Chrome version X
```
- Download the correct ChromeDriver matching your **Chrome version**.
- Update the `CHROME_DRIVER_PATH` in the script.

## 🏗 Future Improvements
- Add support for dropdowns and checkboxes.
- Implement logging for better debugging.
- Improve error handling and exception management.

## 📝 License
This project is open-source and available under the [MIT License](LICENSE).

