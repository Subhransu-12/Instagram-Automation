from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver
driver = webdriver.Chrome()
driver.get("https://www.instagram.com/")

# Wait for the page to load
driver.implicitly_wait(10)

# Find the username field using XPath
username_login_field = driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")
username_login_field.send_keys("_4uemerson_")

# Find the password field using XPath
password_login_field = driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")
password_login_field.send_keys("Emerson@12")

# Find the login button using XPath
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='loginForm']/div/div[3]/button"))
)
login_button.click()

# Wait for the login process to complete
time.sleep(10)

# element = driver.find_element_by_xpath("//*[@id='mount_0_0_HQ']/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/section/div/button")
# element.click()


search_bar = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
search_bar.send_keys("google")

# element = driver.find_element_by_xpath("//*[@id='mount_0_0_gK']/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[2]/div/div[2]/div")
# element.click()

# user_profile = driver.find_element(By.XPATH, "//div[@class='fuqBx']/a[1]")
# user_profile.click()

time.sleep(10)
