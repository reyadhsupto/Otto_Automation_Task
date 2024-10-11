import pytest
import os
from slugify import slugify
from playwright.sync_api import sync_playwright
from src.utils.ReadProperties import ReadConfig


headless_status = False

@pytest.fixture( autouse = True,params=['chromium'], scope='class')
def init_page(request):
    with sync_playwright() as playwright:
        if request.param == 'chromium':
            browser = playwright.chromium.launch(
                headless=headless_status, 
                args=["--start-maximized"]
            )
        else:
            raise ValueError(f"Browser Type Unsupported: {request.param}")
        
        context = browser.new_context(no_viewport=True)
        page = context.new_page()

        url = str(ReadConfig.getApplicationURL())
        page.goto(url)


        yield page
        page.close()
        context.close()
        browser.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    pytest_html = item.config.pluginmanager.getplugin("html")

    if report.when == "call" and report.failed:
        page = item.funcargs.get("init_page", None)

        if page:
            scrnsht_path = f"screenshots/{slugify(item.nodeid)}.png"
            page.screenshot(path=scrnsht_path)
            if pytest_html:
                extra = getattr(report, 'extra', [])
                extra.append(pytest_html.extras.image(os.path.normpath(scrnsht_path)))
                report.extras = extra