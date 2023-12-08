from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#----------- prevent chrome from closing-------#
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
#----------------------------------------------#

driver.maximize_window()
driver.get("https://open.spotify.com/track/1ihhh4pUrwstEQnhfCqeZ7") # put the link to the song you like

driver.implicitly_wait(10) # for waiting until the elements are found

#----------------- log in ---------------------------#
def log_in_func():
    log_in = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[3]/header/div[4]/div[2]/button[2]').click()

    mail = driver.find_element(By.XPATH, '//*[@id="login-username"]').send_keys("example@blabla.com") # put your mail

    passw = driver.find_element(By.XPATH, '//*[@id="login-password"]').send_keys("akjshfdakjhd") # put your pass

    log_in2 = driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

log_in_func()

#----------------- click on accept cookies------------#
try:
    accept_cookies = driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()

except:
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'))).click()

#---------------- check if repeat is on ---------------#
def rep():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[2]/button[2]')))
    repeat = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[2]/button[2]')
    if repeat.get_attribute("aria-label") == "Enable repeat":
        repeat.click()
rep()

#------------------------------------------------------#
def play():
    
    play_Song = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[3]/div[4]/div/div/div/div/div/button/span').click()

play()
