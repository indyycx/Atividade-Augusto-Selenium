from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.events import AbstractEventListener, EventFiringWebDriver
import time

class Escuta(AbstractEventListener):
    def before_navigate_to(self, url, driver):
        print(f"[ANTES] Navegando para: {url}")

    def after_navigate_back(self, driver):
        print("[DEPOIS] Voltou para a página anterior")


driver = webdriver.Chrome()
browser = EventFiringWebDriver(driver, Escuta())

browser.get("https://pt.wikipedia.org/wiki/Python")
time.sleep(3)


titulo = browser.find_element(
    By.CSS_SELECTOR,
    "h1#firstHeading"
)

paragrafo = browser.find_element(
    By.CSS_SELECTOR,
    "div.mw-parser-output > p"
)

print("\n--- CONTEÚDO EXTRAÍDO ---")
print("TÍTULO:")
print(titulo.text)

print("\nPARÁGRAFO:")
print(paragrafo.text)


browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.TAB)
time.sleep(1)


actions = ActionChains(browser)

actions.key_down(Keys.CONTROL) \
       .send_keys('a') \
       .send_keys('c') \
       .key_up(Keys.CONTROL) \
       .perform()

time.sleep(2)

browser.quit()
