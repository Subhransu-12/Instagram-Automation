from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver
driver = webdriver.Chrome()
driver.get("https://www.instagram.com/")

# Wait for the page to load

time.sleep(5)

# Click on the "Sign Up" link
sign_up_link = driver.find_element(By.LINK_TEXT, "Sign up")
sign_up_link.click()

# Wait for the sign-up page to load

time.sleep(5)

# Fill in the sign-up form

email_field = driver.find_element(By.NAME, "emailOrPhone")
email_field.send_keys("fabek10506@iliken.com")

full_name_field = driver.find_element(By.NAME, "fullName")
full_name_field.send_keys("nonamesubhhhh")

username_field = driver.find_element(By.NAME, "username")
username_field.send_keys("nosubh1212")

password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("Pekka@12")

# Click on the "Sign Up" button
sign_up_button = driver.find_element(By.XPATH, "//button[@type='submit' and text()='Sign Up']")
sign_up_button.click()


time.sleep(10)

driver.quit()
