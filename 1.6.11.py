from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[1]/input['text']['first']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[2]/input['text']['last']")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[3]/input['text']['email']")
    input3.send_keys("1@2.com")
    input4 = browser.find_element_by_xpath("/html/body/div/form/div[2]/div[1]/input['text']['phone']")
    input4.send_keys("911")
    input5 = browser.find_element_by_xpath("/html/body/div/form/div[2]/div[2]/input['text']['address']")
    input5.send_keys("Russia street")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
