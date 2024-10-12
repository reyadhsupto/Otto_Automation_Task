from src.page_objects.BaseClass import BaseClass

class HomePage(BaseClass):
    #searching
    searchfield_locator = "xpath=//input[@placeholder='Wonach suchst du?']"
    search_value = "trampolin"
    search_checker_locator = f"xpath=//h1[contains(text(),'„{search_value}')]"

    #sorting
    sorting_locator = "xpath=//select[@id='heureka_desktopSorting--select--cloned']"
    sorting_label = "Preis: höchster zuerst"
    sorted_products_locator = "xpath=//section[@id='reptile-tilelist']/article"

    #filtering
    filter_locator = "xpath=//dt[@class='pl_accordion__header'][normalize-space()='Preis']"
    lowest_price_locator = "xpath=//label[contains(text(),'Von (€)')]/preceding-sibling::input"
    highest_price_locator = "xpath=//label[contains(text(),'Bis (€)')]/preceding-sibling::input"
    filtered_product_locator = "xpath=//ul//header[@class='find_tile__header']/a"
    filter_submit_locator = "xpath=//button[@type='submit'][normalize-space()='Auswahl ansehen']"

    #clicked product
    clicked_product = None
    addtocartbtn_locator = "xpath=//span[contains(text(),'In den Warenkorb')]"
    finaladdtocart_locator = "xpath=//button[contains(text(),'Zum Warenkorb')]"
    cartlisted_product_locator = "xpath=//div[@data-qa='itemgroup']//div[@data-qa='articleName']//following-sibling::a"

    def __init__(self,page):
        self.page = page
        super().__init__(page)
        self.prices = []

    def search_for_trampolin(self):
        super().handle_cookies()
        super().fill_value(self.searchfield_locator,self.search_value)
        self.page.keyboard.press("Enter")
        self.page.wait_for_timeout(500)

        elem = self.page.locator(self.search_checker_locator).count()
        return elem > 0
    
    def sort_by_highest_price(self):
        self.page.locator(self.sorting_locator).select_option(label=self.sorting_label)
        self.page.wait_for_timeout(2000)
        
        try:
            price_articles = self.page.locator(self.sorted_products_locator)
            for i in range(5):
                article = price_articles.nth(i)
                try:
                    price = article.locator("xpath=.//div[@class='find_tile__priceContainer']/span[1]").text_content()
                except Exception:
                    price = article.locator("xpath=.//div[@class='find_tile__priceContainer']/span[2]").text_content()

                if price:
                    price = float(price.replace('€', '').replace(',', '').strip())
                    self.prices.append(price)
            for p in range(len(self.prices) - 1):
                if self.prices[p] < self.prices[p + 1]:
                    return False
            return True
        except Exception:
            return False

    def filtering_by_price_range(self, lowest_range:str , highest_range:str):
        self.page.locator(self.filter_locator).click()
        super().fill_value(self.lowest_price_locator,lowest_range)
        super().fill_value(self.highest_price_locator, highest_range)
        self.page.keyboard.press("Enter")
        self.page.wait_for_timeout(2000)

    def click_product(self,number):
        product = self.page.locator(self.filtered_product_locator).nth(number)
        self.clicked_product = product.get_attribute("title").strip()
        product.click()

    def add_to_cart(self):
        self.page.wait_for_selector(self.addtocartbtn_locator, state="visible", timeout=10000).click()
        self.page.wait_for_load_state('networkidle')

        self.page.wait_for_selector("button:has-text('In den Warenkorb')", state="visible", timeout=10000)
        self.page.get_by_role("button", name="In den Warenkorb").click()
        self.page.wait_for_load_state('networkidle')

    def check_product_addedtocart(self):
        cartproduct = self.page.get_by_text(self.clicked_product)
        return cartproduct.count() > 0
