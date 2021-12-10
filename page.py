
from selenium.webdriver.common.by import By

class Page:
    def __init__(self, browser, url):
        browser.get(url)
        self.browser = browser

    def getLang(self, lang):
        return self.browser.find_element(By.CSS_SELECTOR, 'span[data-language='+lang+']')

    def getSearchBox(self):
        return self.browser.find_element(By.ID, "searchbox")

    def getHeadline(self):
        return self.browser.find_element(By.CSS_SELECTOR, "h1.cell-md").text.lower()

    def getMenuElements(self):
        return [elem.text.lower() for elem in self.browser.find_elements(By.CLASS_NAME, "name")]