from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

# Setup Chrome options
options = Options()
options.add_argument("--headless")  # Run in background
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Set path to your ChromeDriver
service = Service(executable_path=r"C:\Users\happy\Downloads\selenium2\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

# Load the page
url = "https://catalog.pace.edu/graduate/schools/seidenberg-school-computer-science-information-systems/graduate-degree-programs/masters-science-programs/data-science-ms/"
driver.get(url)

time.sleep(3)  # Allow JS to load

# Find all course links (they open popups)
bubbles = driver.find_elements(By.CLASS_NAME, "bubblelink")

# List to collect results
courses = []

for bubble in bubbles:
    try:
        course_code = bubble.text.strip()
        driver.execute_script("arguments[0].click();", bubble)
        time.sleep(0.5)

        # Find the popup
        popup = driver.find_element(By.CLASS_NAME, "lfjsbubblecontent")
        description = popup.text.strip()

        courses.append({
            "Course": course_code,
            "Description": description
        })
    except Exception as e:
        print(f"Failed to extract for {bubble.text.strip()}: {e}")

# Close browser
driver.quit()

# Create DataFrame
df = pd.DataFrame(courses)

# Show it
print(df)



# Optionally save to CSV
#df.to_csv(r"C:\Users\happy\Documents\course_descriptions.csv", index=False)
#try:
 #   df.to_csv(r"C:\Users\happy\Documents\course_descriptions.csv", index=False)
  #  print("CSV file saved successfully.")
#except Exception as e:
 #   print(f"Failed to save CSV: {e}")
#df.to_csv("course_descriptions.csv", index=False)
#df.head()

#df.describe()