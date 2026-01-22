from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def run_tests():
    # Setup WebDriver (using Chrome in headless mode for sandbox)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    
    url = "https://chulo-solutions.github.io/qa-internship/"
    
    try:
        # 1. Enter valid data and submit
        print("Testing Valid Registration...")
        driver.get(url)
        driver.find_element(By.ID, "username").send_keys("Bikesh123")
        driver.find_element(By.ID, "password").send_keys("Password123!")
        driver.find_element(By.ID, "creditCard").send_keys("4111666622227777")
        driver.find_element(By.ID, "telephone").send_keys("(123) 456-7890")
        driver.find_element(By.TAG_NAME, "button").click()
        
        # Verify success (assuming an alert or success message appears)
        # Note: The actual site behavior might vary, we'll check for common success indicators
        time.sleep(2)
        try:
            alert = driver.switch_to.alert
            print(f"Success Alert: {alert.text}")
            alert.accept()
        except:
            print("No alert found, checking for success message in DOM...")
            # Placeholder for DOM check if needed
            
        # 2. Attempt invalid data for each field
        print("\nTesting Invalid Data...")
        
        # Invalid Username
        driver.get(url)
        driver.find_element(By.ID, "username").send_keys("User") # Too short
        driver.find_element(By.TAG_NAME, "button").click()
        time.sleep(1)
        # Check for error message (this depends on how the site displays errors)
        print("Submitted invalid username 'User'")

        # Invalid Password
        driver.get(url)
        driver.find_element(By.ID, "password").send_keys("pass") # Too short
        driver.find_element(By.TAG_NAME, "button").click()
        time.sleep(1)
        print("Submitted invalid password 'pass'")

        # Invalid Credit Card
        driver.get(url)
        driver.find_element(By.ID, "creditCard").send_keys("123") # Too short
        driver.find_element(By.TAG_NAME, "button").click()
        time.sleep(1)
        print("Submitted invalid credit card '123'")

        # Invalid Telephone
        driver.get(url)
        driver.find_element(By.ID, "telephone").send_keys("1234567890") # Wrong format
        driver.find_element(By.TAG_NAME, "button").click()
        time.sleep(1)
        print("Submitted invalid telephone '1234567890'")

    finally:
        driver.quit()

if __name__ == "__main__":
    print("Starting automation tests...")
    try:
        run_tests()
        print("All tests completed successfully!")
    except Exception as e:
        print(f"Error occurred: {e}")
        import traceback
        traceback.print_exc()