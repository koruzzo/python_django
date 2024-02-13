from selenium import webdriver
from selenium.webdriver.common.by import By
import time


drivers = []

for _ in range(1):
    driver = webdriver.Chrome()
    driver.get("http://www.youtube.com/")
    drivers.append(driver)
    time.sleep(0.2)

for index, driver in enumerate(drivers):
    try:
        reject_all_element = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[6]/div[1]/ytd-button-renderer[1]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]')
        reject_all_element.click()
    except Exception as e:
        print("Le bouton Refuser tout pas trouvé :", e)
    time.sleep(2)
    search_box = driver.find_element(By.NAME, "search_query")
    search_box.send_keys("sax guy 10 hours")
    search_box.submit()
    time.sleep(2)
    try:
        first_result = driver.find_element(By.XPATH, '//*[@id="contents"]/ytd-video-renderer[1]')
        first_result.click()
        print(f"Résultat {index+1} trouvé.")
    except Exception as e:
        print(f"Résultat {index+1} pas trouvé :", e)

    for _ in range(150):
        try:
            like_button = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[2]/div/div/ytd-menu-renderer/div[1]/segmented-like-dislike-button-view-model/yt-smartimation/div/div/like-button-view-model/toggle-button-view-model/button-view-model/button/yt-touch-feedback-shape/div/div[2]')
            like_button.click()
            print("Like cliqué.")
        except Exception as e:
            print("L'élément Like n'a pas été trouvé :", e)
        time.sleep(0.1)

time.sleep(30)

driver.quit()
