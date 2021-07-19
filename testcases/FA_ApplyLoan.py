from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import logging
logger = logging.getLogger('uploader')


class FA_ApplyLoan:

    def siteValidation(self, config, driver, time):
        print('-----------openSite Method is Started-------------')
        driver.get(config.get('FA_ApplyLoan-FirstSection', 'url'))
        FA_ApplyLoan().siteComponent(config=config, driver=driver, time=time)
        print('-----------openSite Method is completed------------')

    def fieldValidation(self, config, driver, time):
        print('-----------fieldValidation Method is Started-------------')
        driver.find_element_by_xpath(config.get('FA_ApplyLoan-FirstSection', 'continueBtn')).click()
        try:
            driver.find_elements_by_class_name(config.get('FA_ApplyLoan-FirstSection', 'fieldValidationError'))
            print('-----------fieldValidation Method is completed-------------')
            return True
        except Exception as e:
            print('fieldValidation Method----' + str(e))
            logger.error('fieldValidation Method----' + str(e))
            print('-----------fieldValidation Method is completed-------------')
            return False

    def siteComponent(self, config, driver, time):

        # First Section Check
        FA_ApplyLoan().firstSection(config=config, driver=driver, time=time)

        #Second Section Check
        FA_ApplyLoan().secondSection(config=config, driver=driver, time=time)

        #Third Section Check
        FA_ApplyLoan().thirdSection(config=config, driver=driver, time=time)

        print("sample test case successfully completed")

    def firstSection(self, config, driver, time):
        logger.debug('firstSection Method is Started')
        print('-----------firstSection Method is Started-------------')
        # field Validation
        validationCheck = FA_ApplyLoan().fieldValidation(config=config, driver=driver, time=time)

        if validationCheck:
            logger.debug('All Validations are enabled')
            print('All Validations are enabled')
            try:
                element = driver.find_element_by_xpath(config.get('FA_ApplyLoan-FirstSection', 'desiredLoanAmountFieldLabel'))
                assert element.text == 'Desired Loan Amount'
                select = Select(driver.find_element_by_xpath(config.get('FA_ApplyLoan-FirstSection', 'desiredLoanAmountField')))
                select.select_by_value('$3,000 - $25,000')
                print('Desired Loan Amount Field value is Set')

                element = driver.find_element_by_xpath(config.get('FA_ApplyLoan-FirstSection', 'timeInBusinessFieldLabel'))
                assert element.text == 'Time In Business'
                select = Select(driver.find_element_by_xpath(config.get('FA_ApplyLoan-FirstSection', 'timeInBusinessField')))
                select.select_by_value('0-6 Months')
                print('Time In Business Field value is Set')

                element = driver.find_element_by_xpath(config.get('FA_ApplyLoan-FirstSection', 'annualRevenueLabel'))
                assert element.text == 'Annual Revenue'
                select = Select(driver.find_element_by_xpath(config.get('FA_ApplyLoan-FirstSection', 'annualRevenueField')))
                select.select_by_value('<$60,000')
                print('Annual Revenue Field value is Set')

                driver.find_element_by_xpath(config.get('FA_ApplyLoan-FirstSection', 'continueBtn')).click()
                time.sleep(10)
                print('Continue Button is Pressed')

                print('-----------firstSection Method is passed-------------')
                logger.debug('firstSection Method is passed')
            except Exception as e:
                logger.error('firstSection Method----'+str(e))
                print('-----------firstSection Method is failed-------------')

        else:
            print('No Validation Errors are enabled')
            logger.warning('No Validation Errors are enabled')
            print('-----------firstSection Method is passed-------------')


    def secondSection(self, config, driver, time):
        logger.debug('secondSection Method is Started')
        print('-----------secondSection Method is Started-------------')
        # field Validation
        validationCheck = FA_ApplyLoan().fieldValidation(config=config, driver=driver, time=time)

        if validationCheck:
            logger.debug('All Validations are enabled')
            print('All Validations are enabled')
            try:
                element = driver.find_element_by_xpath(config.get('FA_ApplyLoan-SecondSection', 'firstNameFieldLabel'))
                assert element.text == 'First Name'
                driver.find_element_by_xpath(config.get('FA_ApplyLoan-SecondSection', 'firstNameField')).send_keys('Test Data')
                print('First Name Field value is Set')

                element = driver.find_element_by_xpath(config.get('FA_ApplyLoan-SecondSection', 'lastNameFieldLabel'))
                assert element.text == 'Last Name'
                driver.find_element_by_xpath(config.get('FA_ApplyLoan-SecondSection', 'lastNameField')).send_keys('Test Data')
                print('Last Name Field value is Set')

                element = driver.find_element_by_xpath(config.get('FA_ApplyLoan-SecondSection', 'companyNameFieldLabel'))
                assert element.text == 'Company Name'
                driver.find_element_by_xpath(config.get('FA_ApplyLoan-SecondSection', 'companyNameField')).send_keys('Test Data Company')
                print('Company Name Field value is Set')

                element = driver.find_element_by_xpath(config.get('FA_ApplyLoan-SecondSection', 'phoneNumberFieldLabel'))
                assert element.text == 'Phone Number'
                driver.find_element_by_xpath(config.get('FA_ApplyLoan-SecondSection', 'phoneNumberField')).send_keys('7832456789')
                print('Phone Number Field value is Set')

                element = driver.find_element_by_xpath(config.get('FA_ApplyLoan-SecondSection', 'emailFieldLabel'))
                assert element.text == 'Email Address'
                driver.find_element_by_xpath(config.get('FA_ApplyLoan-SecondSection', 'emailField')).send_keys('testatestest@gmail.com')
                print('Email Address Field value is Set')

                driver.find_element_by_xpath(config.get('FA_ApplyLoan-FirstSection', 'continueBtn')).click()
                print('Continue Button is Pressed')

                print('-----------secondSection Method is passed-------------')
                logger.debug('secondSection Method is passed')
                time.sleep(10)

            except Exception as e:
                logger.error('secondSection Method----'+str(e))
                print('-----------secondSection Method is failed-------------')
        else:
            print('No Validation Errors are enabled')
            logger.warning('No Validation Errors are enabled')
            print('-----------secondSection Method is passed-------------')

    def thirdSection(self, config, driver, time):
        logger.debug('thirdSection Method is Started')
        print('-----------thirdSection Method is Started-------------')
        # field Validation
        validationCheck = FA_ApplyLoan().fieldValidation(config=config, driver=driver, time=time)

        if validationCheck:
            logger.debug('All Validations are enabled')
            print('All Validations are enabled')

            try:
                element = driver.find_element_by_xpath(config.get('FA_ApplyLoan-ThirdSection', 'businessAddFieldLabel'))
                assert element.text == 'Business Address'
                driver.find_element_by_xpath(config.get('FA_ApplyLoan-ThirdSection', 'businessAddField')).send_keys('Test Business')
                print('Business Address Field value is Set')

                element = driver.find_element_by_xpath(config.get('FA_ApplyLoan-ThirdSection', 'cityFieldLabel'))
                assert element.text == 'City'
                driver.find_element_by_xpath(config.get('FA_ApplyLoan-ThirdSection', 'cityField')).send_keys('Test Business')
                print('City Field value is Set')

                element = driver.find_element_by_xpath(config.get('FA_ApplyLoan-ThirdSection', 'stateFieldLabel'))
                assert element.text == 'State'
                select = Select(driver.find_element_by_xpath(config.get('FA_ApplyLoan-ThirdSection', 'stateField')))
                select.select_by_value('AK')
                print('State Field value is Set')

                element = driver.find_element_by_xpath(config.get('FA_ApplyLoan-ThirdSection', 'zipCodeFieldLabel'))
                assert element.text == 'Zip Code'
                driver.find_element_by_xpath(config.get('FA_ApplyLoan-ThirdSection', 'zipCodeField')).send_keys('123456')
                print('Zip Code Field value is Set')

                element = driver.find_element_by_xpath(config.get('FA_ApplyLoan-ThirdSection', 'busPhoneFieldLabel'))
                assert element.text == 'Business Phone'
                driver.find_element_by_xpath(config.get('FA_ApplyLoan-ThirdSection', 'busPhoneField')).send_keys('1234567890')
                print('Business Phone Field value is Set')

                element = driver.find_element_by_xpath(config.get('FA_ApplyLoan-ThirdSection', 'busMonthFieldLabel'))
                assert element.text == 'Month'
                select = Select(driver.find_element_by_xpath(config.get('FA_ApplyLoan-ThirdSection', 'busMonthField')))
                select.select_by_value('January')
                print('Business Month Field value is Set')

                element = driver.find_element_by_xpath(config.get('FA_ApplyLoan-ThirdSection', 'busDayFieldLabel'))
                assert element.text == 'Day'
                driver.find_element_by_xpath(config.get('FA_ApplyLoan-ThirdSection', 'busDayField')).send_keys('1')
                print('Business Day Field value is Set')

                element = driver.find_element_by_xpath(config.get('FA_ApplyLoan-ThirdSection', 'busYearFieldLabel'))
                assert element.text == 'Year'
                driver.find_element_by_xpath(config.get('FA_ApplyLoan-ThirdSection', 'busYearField')).send_keys('2020')
                print('Business Year Field value is Set')

                element = driver.find_element_by_xpath(config.get('FA_ApplyLoan-ThirdSection', 'companyTypeFieldLabel'))
                assert element.text == 'Select Company Type'
                select = Select(driver.find_element_by_xpath(config.get('FA_ApplyLoan-ThirdSection', 'companyTypeField')))
                select.select_by_value('Corporation')
                print('Company Type Field value is Set')

                element = driver.find_element_by_xpath(config.get('FA_ApplyLoan-ThirdSection', 'busAnnualRevenueFieldLabel'))
               # assert element.text == 'Annual Revenue'
                driver.find_element_by_xpath(config.get('FA_ApplyLoan-ThirdSection', 'busAnnualRevenueField')).send_keys('78')
                print('Annual Revenue Field value is Set')

                element = driver.find_element_by_xpath(config.get('FA_ApplyLoan-ThirdSection', 'companyTaxIdFieldLabel'))
                assert element.text == 'Company Tax ID'
                driver.find_element_by_xpath(config.get('FA_ApplyLoan-ThirdSection', 'companyTaxIdField')).send_keys('123456777')
                print('Company Tax ID Field value is Set')

                #element = driver.find_element_by_xpath(config.get('FA_ApplyLoan-ThirdSection', 'ownBusinessOptionFieldLabel'))
                #assert element.text == 'Do you own at least 51% of the business?'
                #driver.find_element_by_xpath(config.get('FA_ApplyLoan-ThirdSection', 'ownBusinessYesOptionField')).click()
                print('Do you own at least 51% of the business? Field value is Set')

                element = driver.find_element_by_xpath(config.get('FA_ApplyLoan-ThirdSection', 'ownerFieldLabel'))
                #assert element.text == 'Ownership %'
                driver.find_element_by_xpath(config.get('FA_ApplyLoan-ThirdSection', 'ownerField')).send_keys('89')
                print('Ownership % Field value is Set')

                driver.find_element_by_xpath(config.get('FA_ApplyLoan-FirstSection', 'continueBtn')).click()
                time.sleep(20)
                print('Continue Button is Pressed')

                print('-----------thirdSection Method is passed-------------')
                logger.debug('thirdSection Method is passed')

            except Exception as e:
                time.sleep(20)
                logger.error('thirdSection Method----'+str(e))
                print('-----------thirdSection Method is failed-------------')
        else:
            print('No Validation Errors are enabled')
            logger.warning('No Validation Errors are enabled')
            print('-----------thirdSection Method is passed-------------')