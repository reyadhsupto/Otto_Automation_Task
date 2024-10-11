import pytest
import random

from tests.BaseTest import TestBase
from src.page_objects.Homepage import HomePage

class Test_login(TestBase):
    @pytest.mark.run(order = 1)
    def test_search_functionality(self, init_page):
        super().logger.info(" TC_001: Verify that the search functionality works properly and displays accurate results.")
        hp = HomePage(init_page)
        super().logger.info("searching for trampolin")
        val = hp.search_for_trampolin()
        assert val == True, "Search functionality not working"

    @pytest.mark.run(order = 2)
    def test_sorting_functionality(self, init_page):
        super().logger.info(" TC_002: Verify that the first 5 products have been sorted correctly (by price descending).")
        hp1 = HomePage(init_page)
        super().logger.info("Sorting by highest price")
        checker = hp1.sort_by_highest_price()
        assert checker == True, "System not showing correct sorted results upon clicking on sort by highest price"

    @pytest.mark.run(order = 3)
    def test_correct_product_added_to_cart(self, init_page):
        super().logger.info(" TC_003: Verify that the correct product has been successfully added to the shopping cart.")
        hp2 = HomePage(init_page)

        super().logger.info("Filtering products by price range 500 - 1000")
        hp2.filtering_by_price_range("500" , "1000")

        super().logger.info("Clicking one of the first 5 products from the filtered list")
        hp2.click_product(random.randint(0,4))

        super().logger.info("Adding selected product to cart")
        hp2.add_to_cart()

        super().logger.info("Assertion, if the correct product is added to cart")
        listprodname= hp2.check_product_addedtocart()
        assert listprodname == True, "Product not added to cart, or selected product not added to cart"
