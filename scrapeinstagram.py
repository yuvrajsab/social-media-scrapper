import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os

load_dotenv()

driver = webdriver.Chrome(executable_path='./chromdriver')
wait = WebDriverWait(driver, 10)

# Login if required
driver.get('https://instagram.com')

loginForm = wait.until(EC.visibility_of_element_located(
    (By.XPATH, "//*[@id='loginForm']")))
usernameField = loginForm.find_elements(By.XPATH, "//input")[0]
usernameField.send_keys(os.environ.get('INSTAGRAM_ID'))
passwordField = loginForm.find_elements(By.XPATH, "//input")[1]
passwordField.send_keys(os.environ.get('INSTRGRAM_PASSWORD'))
loginButton = loginForm.find_element(By.XPATH, "//button[@type='submit']")
loginForm.click()
time.sleep(5)
driver.get("https://www.instagram.com/samagragovernance/")

postLinks = []
lastSize, newSize = 0, -1
while lastSize != newSize:
    lastSize = newSize
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//a[contains(@href, '/p/')]")))
    driver.find_element(By.XPATH, '//body').send_keys(Keys.END)
    time.sleep(3)
    newSize = len(driver.find_elements(
        By.XPATH, "//a[contains(@href, '/p/')]"))
print("Loaded all posts...")
postLinks = [post.get_attribute('href') for post in driver.find_elements(
    By.XPATH, "//a[contains(@href, '/p/')]")]

data = []
print(len(postLinks))
print(postLinks)
for post in postLinks:
    driver.get(post)
    # Specific post
    likes, comments = 0, 0
    try:
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[contains(text(), 'others')]")))
        likes = driver.find_element(
            By.XPATH, "//span[contains(text(), 'others')]").text.split()[0]
    except:
        print("Could not find element!")
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, "//ul")))
        comments = len(driver.find_elements(By.XPATH, "//ul"))
    except:
        print("Could not find element!")

    data.append({
        "postLink": post,
        "likes": likes,
        "comments": comments
    })

print(data)
