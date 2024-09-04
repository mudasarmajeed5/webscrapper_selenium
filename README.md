
# Web Scraper for Daraz Using Selenium

Welcome to the Daraz Web Scraper project! This tool will help you gather data from Daraz's search results and save it for further analysis.

## 📁 Setup Instructions

1. **Create a Folder**:
   - Create a folder named `data` in the root directory of the project.

2. **Install Dependencies**:
   - Ensure you have Selenium installed. If not, you can install it using the following command:
     ```bash
     pip install selenium
     ```

3. **Run the Scraper**:
   - Open your root directory and run `project.py`. You’ll be prompted to enter a search query and the number of pages to scrape.
   - The script will generate multiple HTML files inside the `data` folder.

4. **Generate CSV File**:
   - After scraping, run `collect.py` to consolidate the data.
   - A `data.csv` file will be created, containing the following fields for each product:
     - **Title**
     - **Price**
     - **Link**

## 🚀 How to Use

1. **Prepare Your Environment**:
   - Make sure you have the necessary packages installed and the `data` folder created.

2. **Start Scraping**:
   - Execute `project.py` and provide the search query and number of pages when prompted.

3. **Collect Data**:
   - Run `collect.py` to aggregate and save the data into a CSV file.

## Example Usage

1. **Running `project.py`**:
   ```bash
   python project.py
   ```
   - Input: `Smartphones` and `5` (for 5 pages of results).

2. **Running `collect.py`**:
   ```bash
   python collect.py
   ```

## ⚠️ Notes

- Ensure that you have a stable internet connection while running the scripts.
- Be mindful of Daraz's scraping policies to avoid potential issues.

## 🎨 Customization

Feel free to customize the script to fit your specific needs. For any enhancements or bug fixes, please contribute or reach out!

---

Hope this helps! Let me know if you need any more tweaks or details.
