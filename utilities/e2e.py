import requests, time, sys
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_scores_service(url):    
    req = requests.get(url=url)
    print(req.status_code)
    if req.status_code == 200:
        driver = webdriver.Chrome(executable_path=r"C:\Users\Administrator\DevOps Expert\project\tests\chromedriver.exe")
        driver.get(url)
        time.sleep(3)
        current_score = driver.find_element(By.XPATH, '//*[@id="score"]').text
        if current_score.isdigit() and 0 < int(current_score) < 1001:
            print('Yes, It is a number')
            return True, req.status_code, current_score
    else:
        return False, req.status_code
     
def main_function():
    url = 'http://127.0.0.1:5000'
    res = test_scores_service(url)
    if res[0] == True:
        return sys.exit_code(0)
    elif res[0] == False:
        return sys.exit_code(-1)

main_function()
