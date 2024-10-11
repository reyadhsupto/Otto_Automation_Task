# Otto Automation

Otto is a German e-commerce platform

## Description

This project automates the testing of essential functionalities (searching, sorting, price range filtering, and adding items to the cart) on Otto.de, a German e-commerce platform. The automation is built using Playwright and Pytest frameworks.

## Features Automated

- **Product Search**: Automates the search functionality for products on Otto.de and verifies if the system shows correct search results.
- **Sorting**: Tests the sorting feature to ensure products are displayed in the desired order.
- **Price Range Filtering**: Automates filtering products within a specified price range.
 - **Add to Cart**: Verifies that the correct product is added to the cart.

## Technology Used

**Automation Tool:** Playwright

**Framework:** Pytest

**Programming Language:** Python

**Report Maker:** pytest-html

**Browser:** Chromium

## Prerequisites
pip, Python:3.10 or Higher


## Installation

Clone the repository:

```bash
git clone https://github.com/reyadhsupto/Otto_Automation_Task.git
cd Otto_Automation_Task
```

Install python dependencies:

```bash
pip install -r requirements.txt
```
## Running Tests

Basic test run:

```bash
pytest -v -s --html=sanity.html
```
Clear Cache and Run Tests with Html report:
```bash
pytest --cache-clear -v -s --html=sanity.html --capture=tee-sys
```

## Test Structure

```bash
├───configurations
├───logs
├───reports
├───screenshots
├───src
│   ├───page_objects
│   └───utils
└───tests
```
## 🔗 Test Cases
1. TC_001: Verify that the search functionality works properly and displays accurate results.
2. TC_002: Verify that the first 5 products have been sorted correctly (by price descending).
3. TC_003: Verify that the correct product has been successfully added to the shopping cart.

**[[Test Cases Link]](https://docs.google.com/spreadsheets/d/12hnMMQ7QgGnYi5IH02trE9dvxzZwbqKh3gnIYYphYKo/edit?usp=sharing)**

## License

This project is licensed under the [MIT License](LICENSE). See the `LICENSE` file for more details on terms and conditions.

Feel free to use and contribute to the project under these terms!