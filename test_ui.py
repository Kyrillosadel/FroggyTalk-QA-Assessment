from appium import webdriver

def test_mobile_topup_flow():
    caps = {
        "platformName": "iOS",
        "deviceName": "iPhone 11",
        "automationName": "XCUITest",
        "app": "/path/to/froggytalk.app"
    }

    driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

    # Navigate to Services
    driver.find_element("accessibility id", "ServicesTab").click()

    # Open Mobile Top-Up
    driver.find_element("accessibility id", "MobileTopUp").click()

    # Enter phone number
    driver.find_element("accessibility id", "PhoneInput").send_keys("08012345678")

    # Select Airtime
    driver.find_element("accessibility id", "AirtimeOption").click()

    # Verify next screen loads
    assert driver.find_element("accessibility id", "PaymentButton").is_displayed()

    driver.quit()
