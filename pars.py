from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://www.vesti.ru/"

driver = webdriver.Chrome()
driver.get(url)
time.sleep(1)

cards = driver.find_elements(By.CLASS_NAME, "main-news__item")

print("Количестов новостей:", len(cards))
k = 0
for idx in range(len(cards)):
    i = cards[idx]


    try:
        title = i.find_element(By.CSS_SELECTOR, "h3.main-news__title").text.strip()
    except:
        title = ""
    if not title:
        continue
    try:
        date_text = i.find_element(By.CSS_SELECTOR, ".main-news__info .main-news__time").text.strip()
    except:
        date_text = ""


    try:
        link = i.find_element(By.TAG_NAME, "a").get_attribute("href")
    except:
        link = ""

    print()
    print(f"{k} )  {title}")
    if date_text:
        print(date_text)


    if link:
        main = driver.current_window_handle
        driver.execute_script(f"window.open('{link}','_blank');")
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(1)

        parts = []
        try:
            anons = driver.find_element(By.CSS_SELECTOR, "div.article__anons").text.strip()
            if anons:
                parts.append(anons)
        except:
            pass

        try:
            for el in driver.find_elements(By.CSS_SELECTOR, "div.article__text p, div.article__text blockquote"):
                t = el.text.strip()
                if t:
                    parts.append(t)
        except:
            pass

        if parts:
            print("\n".join(parts))

        driver.close()
        driver.switch_to.window(main)

    k += 1

driver.quit()
