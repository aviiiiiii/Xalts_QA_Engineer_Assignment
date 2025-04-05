import base64
import os

import pytest
from selenium import webdriver

driver = None


@pytest.fixture(scope="function")
def browserInstance(request):
    global driver
    driver = webdriver.Chrome()
    driver.get("https://xaltsocnportal.web.app/")
    yield driver
    driver.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join(os.path.dirname(__file__), 'reports')
            file_name = os.path.join(reports_dir, report.nodeid.replace("::", "_") + ".png")
            print("file name is " + file_name)
            _capture_screenshot(file_name)


            #
            with open(file_name, "rb") as f:
                image_data = f.read()
            encoded_img = base64.b64encode(image_data).decode('utf-8')
            html_img = (f'<img src="data:image/png;base64,{encoded_img}" alt="screenshot" '
                        f'style="width:300px;height:auto;" />')

            #
            extra.append(pytest_html.extras.html(html_img))
        report.extras = extra


def _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)
