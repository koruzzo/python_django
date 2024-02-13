from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://localhost:8000/")

try:
    div_element = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div')
    
    if div_element:
        div_text = div_element.text
        print("Texte de la div:", div_text)
    else:
        print("L'élément div n'a pas été trouvé.")
    
    driver.quit()
    
except Exception as e:
    print("Une erreur s'est produite :", e)