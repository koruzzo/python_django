import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import base64


with open('../data/sign.png', 'rb') as img_file:
    encoded_img = base64.b64encode(img_file.read()).decode('utf-8')

url = input("Veuillez saisir le lien : ")

driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)

try:
    element_with_name = driver.find_element(By.XPATH, "//span[contains(text(), 'JARREAU Raphaël')]")
    element_with_name.click()

    print("Le bouton a été cliqué avec succès.")

except Exception as e:
    print("Une erreur s'est produite :", e)

time.sleep(2)

try:
    canvas = driver.find_element(By.XPATH, "//canvas")
    ActionChains(driver).move_to_element(canvas).click().perform()

    scale_factor = 0.5

    js_code = f"""
    var canvas = document.querySelector('canvas');
    var ctx = canvas.getContext('2d');
    var image = new Image();
    image.src = 'data:image/png;base64,{encoded_img}';
    image.onload = function() {{
        var scaledWidth = image.width * {scale_factor};
        var scaledHeight = image.height * {scale_factor};
        var x = (canvas.width - scaledWidth) / 2;
        var y = (canvas.height - scaledHeight) / 2;
        ctx.drawImage(image, x, y, scaledWidth, scaledHeight);
    }};
    """
    driver.execute_script(js_code)

    print("L'image de signature a été dessinée avec succès.")

except Exception as e:
    print("Une erreur s'est produite :", e)

time.sleep(15)
