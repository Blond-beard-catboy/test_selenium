from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import json

def test_api():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Для запуска без GUI
    driver = webdriver.Remote(
        command_executor='http://selenium:4444/wd/hub',
        options=chrome_options
    )
    
    try:
        # Тест 1: Проверка /api/data
        driver.get("http://api:5000/api/data")
        time.sleep(1)
        
        # Получаем текст из <pre> (где браузер отображает JSON)
        pre_element = driver.find_element(By.TAG_NAME, "pre")
        data = json.loads(pre_element.text)
        
        assert data["status"] == "success"
        assert "Hello from API!" in data["message"]
        
        # Тест 2: Проверка /api/check/10
        driver.get("http://api:5000/api/check/10")
        pre_element = driver.find_element(By.TAG_NAME, "pre")
        data = json.loads(pre_element.text)
        
        assert data["is_even"] is True
        
        print("All tests passed!")
    
    finally:
        driver.quit()

if __name__ == "__main__":
    test_api()