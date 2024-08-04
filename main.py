import time
from selenium import webdriver
from selenium.common import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/")

time.sleep(3)
login_button = driver.find_element(By.XPATH, '//*[@id="o131391810"]/div/div[1]/div/main/div['
                                             '1]/div/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]/div')
login_button.click()

time.sleep(3)
facebook_button = driver.find_element(By.XPATH, '//*[@id="o-1596989266"]/div/div/div/div[1]/div/div/div[2]/div['
                                                '2]/span/div[2]/button/div[2]/div[2]/div[2]/div/div')
facebook_button.click()

time.sleep(3)

# In Selenium, each window has an identification handle, we can get all the window handles with:
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]

# We can switch our Selenium to target the new facebook login window by:
driver.switch_to.window(fb_login_window)
print(driver.title)

email_field = driver.find_element(By.CSS_SELECTOR, '#email')
password_field = driver.find_element(By.CSS_SELECTOR, '#pass')

time.sleep(3)
email_field.send_keys("halidmohamed807@gmail.com")
password_field.send_keys("Haha123@&$", Keys.RETURN)

time.sleep(3)
continue_as = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div/div[1]/div['
                                            '3]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div['
                                            '1]/div/div/div/div/div/div[1]/div/span/span')

continue_as.click()

time.sleep(2)
driver.switch_to.window(base_window)
time.sleep(10)

Allow_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div[3]/button[1]')
time.sleep(1)
Allow_button.click()

time.sleep(1)
notify_me = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div[3]/button[1]')
notify_me.click()

time.sleep(1)
accept_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button')
accept_button.click()

print("Tinder | Match. Chat. Date.")
time.sleep(20)
Like_button = driver.find_element(By.XPATH, '//*[@id="o131391810"]/div/div[1]/div/div/div/main/div/div/div[1]/div/div['
                                            '3]/div/div[4]/button')
for n in range(100):
    time.sleep(3)
    try:
        print("called")
        time.sleep(2)
        Like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, '.itsAMatch a')
            match_popup.click()
        except NoSuchElementException:
            time.sleep(2)

driver.quit()
