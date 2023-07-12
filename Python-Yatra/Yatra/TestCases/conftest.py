import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()

    request.cls.driver=driver
    driver.delete_all_cookies()
    yield
    driver.close()




def pytest_configure(config):
    config._metadata['Project Name']='Yatra'
    config._metadata['Tester']='Khushi Nipul Shah'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)

@pytest.mark.optionalhook
def pytest_cmdline_preparse(config, args):
        config.option.htmlpath = "my-report.html"
        config.option.self_contained_html = True