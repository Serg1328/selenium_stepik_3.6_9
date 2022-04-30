import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_add_goods_on_basket(browser):
    browser.get(link)
    time.sleep(5)
    button = browser.find_elements_by_css_selector('button[class="btn btn-lg btn-primary btn-add-to-basket"]')
    assert button, 'No button'
