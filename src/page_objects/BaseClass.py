from faker import Faker
class BaseClass:
    cookie_selector = "xpath=//button[@id='onetrust-accept-btn-handler']"
    def __init__(self,page):
        self.page = page
        self.faker = Faker()

    def fileupload(self,path:str,label:str):
        with self.page.expect_file_chooser() as fc_info:
            self.page.get_by_label(label).click()
        file_chooser = fc_info.value
        file_chooser.set_files(path)

    def fill_value(self, selector:str, value:str):
        button = self.page.locator(selector)
        button.click()
        button.fill(value)
        self.page.wait_for_timeout(500)

    def handle_cookies(self):
        try:
            self.page.locator(self.cookie_selector).click()
        except:
            print("cookie not found")
            pass

    