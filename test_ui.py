from appium import webdriver

def test_radio_chat_flow():
    caps = {
        "platformName": "iOS",
        "deviceName": "iPhone 11",
        "automationName": "XCUITest",
        "app": "/path/to/froggytalk.app"
    }

    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

    driver.find_element("accessibility id", "RadioTab").click()
    driver.find_element("accessibility id", "RadioItem_Nigeria").click()

    chat = driver.find_element("accessibility id", "LiveChat")
    assert chat.is_displayed()

    driver.quit()
