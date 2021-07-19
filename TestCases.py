import configparser
from selenium import webdriver
import time

from testcases.FA_ApplyLoan import FA_ApplyLoan
applyLoanSite = FA_ApplyLoan()

class TestCases:

    def openBrowser(self):
        driver = webdriver.Chrome('driver/chromedriver')
        driver.maximize_window()
        return  driver

    def siteTest(self, driver):
        config = configparser.RawConfigParser()
        config.read('properties/siteXpaths.properties')
        applyLoanSite.siteValidation(config=config, driver=driver, time=time)