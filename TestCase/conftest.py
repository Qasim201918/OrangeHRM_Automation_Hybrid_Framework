from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


def pytest_configure(config):
    metadata = config.pluginmanager.getplugin("metadata")
    if metadata:
        from pytest_metadata.plugin import metadata_key
        config.stash[metadata_key]['Project Name'] = 'HRM'
        config.stash[metadata_key]['Tester Name'] = 'Muhammad Qasim Khan'
        config.stash[metadata_key]['Testing Scope / Features to be tested'] = 'Complete Application'
        config.stash[metadata_key]['Testing Level'] = 'System testing & Acceptance testing'
        config.stash[metadata_key]['Testing types'] = 'Functional, Smoke/Sanity, Regression testing & Re-Testing'
        config.stash[metadata_key]['Testing  Approaches or Strategies']= 'Automation testing'
        config.stash[metadata_key]['Test Environment']= 'Operating System: Windows 10, Server: QA / Staging, Browser: Chrome, Firefox, Network: WIFI'
        config.stash[metadata_key]['Test Deliverables']= 'Test cases, Bug reports, test summary report'
        config.stash[metadata_key]['Test Case Information']= 'Total test cases= 2,Test Case Coverage: Percentage of requirements covered by test cases= 2, Test Status= Passed: 2, Failed: 0'
        config.stash[metadata_key]['Estimation']= '1 Weeks'
        config.stash[metadata_key]['Defect Tracking Tool'] = 'Jira'
        config.stash[metadata_key]['Reporting Format']= 'HTML'
        config.stash[metadata_key]['Automation Framework'] = 'Selenium webdriver: Hybrid Framework, Pytest'

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)