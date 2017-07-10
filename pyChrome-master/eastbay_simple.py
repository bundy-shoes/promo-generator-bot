from pyChrome import PyChrome

browser = PyChrome()
eastbay_url = "http://www.eastbay.com/"
eastbay_product_url = "http://www.eastbay.com/product/"
eastbay_cal_url = "http://www.eastbay.com/ReleaseCalendar/"
account_login_id = "header_account_button"
email_box_id = "login_email"
password_box_id = "login_password"
login_button_id = "login_submit"
select_a_size_id = "pdp_size_select_container"
select_a_size_container = "size_selection_container"
select_a_size_list = "size_selection_list"
add_to_cart_id = "pdp_addtocart_button"
cart_url = "http://www.eastbay.com/shoppingcart/default.cfm?sku="
cart_button_class = "checkout_btn"
shoe_size_prefs = [10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 8.0, 8.5, 9.0, 9.5]


def open_eastbay_homepage():
    browser.open(eastbay_url)
    while browser.getTabLink() != eastbay_url:
        browser.open(eastbay_url)


def open_eastbay_calendar():
    browser.open(eastbay_cal_url)
    while browser.getTabLink() != eastbay_cal_url:
        browser.open(eastbay_cal_url)


def login(username, password):
    # open_eastbay_homepage()
    if not browser.getTabLink().find("eastbay"):
        open_eastbay_homepage()
    print ("Logging in")
    account_button = browser.findElementByID(account_login_id)
    browser.clickElement(account_button)
    email_field = browser.findElementByID(email_box_id)
    browser.sendTextToElement(username, email_field)
    password_field = browser.findElementByID(password_box_id)
    browser.sendTextToElement(password, password_field)
    login_button = browser.findElementByID(login_button_id)
    browser.clickElement(login_button)


def find_shoe_on_release_page(name):
    name = name.upper()
    print (eastbay_cal_url)
    browser.open(eastbay_cal_url)
    while browser.getTabLink() != eastbay_cal_url:
        browser.open(eastbay_cal_url)
    shoe_button = browser.findElementByXPath("//*[(@alt='{}')]".format(name))
    print ("Looking for: {}".format(name))
    browser.clickElement(shoe_button)
    print ("Found: {}".format(name))
    select_a_size(10.0)


def time_until_release_cal(name=None, model=None, sku=None):
    href_str = "/product/model:{}/sku:{}/".format(model, sku)
    container = browser.findElementByXPath("//*[(@href='{}')]".format(href_str))
    browser.scrollToElement(container)
    # time_left = browser.findElementByClass("product_launch_timer", container)
    time_left = browser.findElementByXPath("//*[("
                                           "@class='product_launch_timer')]",
                                           container)
    while time_left.text != "00 HRS. 00 MIN. 01 SEC.":
        print("\rTime til drop: " + time_left.text),
    open_model_sku(model, sku)


def time_until_release_product_page(model, sku):
    open_model_sku(model, sku)
    timer = browser.findElementByID("pdp_timer")
    while timer.text != "00 HRS. 00 MIN. 01 SEC.":
        print("\r" + timer.text.replace("\n", " ")),
    browser.refresh()
    select_a_size(10.0)


def time_until_release_product_page_no_refresh(model, sku):
    open_model_sku(model, sku)
    timer = browser.findElementByID("pdp_timer")
    while timer.text != "00 HRS. 00 MIN. 01 SEC.":
        print("\r" + timer.text.replace("\n", " ")),
    select_a_size(10.0)


def open_model_sku(model, sku):
    shoe_url = eastbay_product_url + "model:" + model + "/sku:" + sku
    print (shoe_url)
    browser.open(shoe_url)
    while browser.getTabLink() != shoe_url:
        browser.open(shoe_url)


# def check_in_stock(model, sku, size=None):
#     shoe_url = eastbay_product_url + "model:" + model + "/sku:" + sku
#     while browser.getTabLink() != shoe_url:
#         browser.open(shoe_url)
#     container = browser.findElementByID(select_a_size_container)
#     size_list = browser.findElementByID(select_a_size_list, container)
#     number_size = browser.findElementByPartialText(str(size), size_list)


def select_a_size(size_index):
    size_button = browser.findElementByID(select_a_size_id)
    browser.clickElement(size_button)
    container = browser.findElementByID(select_a_size_container)
    size_list = browser.findElementByID(select_a_size_list, container)
    size = shoe_size_prefs[size_index]
    number_size = browser.findElementByPartialText(str(size), size_list)
    # print(number_size)
    print ("Looking for size: {}".format(str(size)))
    browser.clickElement(number_size)
    print ("Found size: {}".format(str(size)))
    add_to_cart()
    while check_cart_qty() != 1 and size_index < len(shoe_size_prefs):
        select_a_size(size_index + 1)
    if check_cart_qty() != 1:
        print ("No shoes in stock")
        browser.quit()
    open_cart()


def add_to_cart():
    print ("Adding to cart")
    cart_button = browser.findElementByID(add_to_cart_id)
    browser.clickElement(cart_button)
    # open_cart()


def check_cart_qty():
    cart_qty = browser.findElementByID("cart_quantity")
    return int(cart_qty.text)


def open_cart():
    print ("Opening cart")
    browser.open(cart_url)
    while browser.getTabLink() != cart_url:
        browser.open(cart_url)
    checkout()


def checkout():
    print ("Proceeding to checkout")
    cart_button = browser.findElementByClass(cart_button_class)
    browser.clickElement(cart_button)

# open_model_sku("236830", "BA8927")
# find_shoe_on_release_page("ADIDAS ALPHABOUNCE EM")
# login("l2706689@mvrht.com", "password12")  # extra account for testing login
# login("wiyev@apkmd.com", "ADSFadsf1")
# open_eastbay_calendar()
# time_until_release_cal("ADIDAS ULTRA BOOST", "236754", "BA8143")
# time_until_release_product_page("236754", "BA8143")
# open_model_sku("236754", "BA8143")
open_model_sku("282617", "BW0427")
select_a_size(0)
login("l2706689@mvrht.com", "password12")  # extra account for testing login
# open_model_sku("276453", "36271402")
