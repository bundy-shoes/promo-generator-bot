from pyChrome import PyChrome
from datetime import datetime
import time

jumpman_23_link = "https://t.co/uQsQoSDWFt"
ovo_link = "https://t.co/XaTXj4Jug8"
ovo_drop_time = datetime(2017, 2, 17, 11)
nike_homepage = "https://www.nike.com/launch/"
jumpman_price = "185.00"
nike_link = "https://www.nike.com/launch/checkout?item="
jumpman_23_item_num = "905847-004"
ovo_item_num = "873864-032"
email1 = ""
password1 = ""
shoe_size = 11
my_cvv = ""
email2 = ""
password2 = ""
email3 = ""
password3 = ""
email4 = ""
password4 = ""
browser = PyChrome()


def open_site(link):
    browser.open(link)


def login(email, password):
    log_in = browser.findElementByXPath("//*[@aria-label='Join or Log In']")
    browser.clickElement(log_in)
    email_box = browser.findElementByXPath("//*[@type='email']")
    browser.sendTextToElement(email, email_box)
    password_box = browser.findElementByXPath("//*[@type='password']")
    browser.sendTextToElement(password, password_box)
    login_button = browser.findElementByXPath("//*[@value='LOG IN']")
    browser.clickElement(login_button)


def buy_link(item_num, size):
    link = "{}{}&size={}".format(nike_link, item_num, str(size))
    browser.open(link)


def select_a_size(size):
    size_el = browser.findElementByXPath("//*[@data-size='{}']".format(size))
    browser.clickElement(size_el)
    save_button = browser.findElementByClass("save-button")
    browser.clickElement(save_button)


def enter_payment_info(cvv):
    # cc_form = browser.findElementByXPath("//*[@id='creditCardForm']")
    # cv_box = browser.findElementByID("cvNumber", cc_form)
    # browser.sendTextToElement(cvv, cv_box)
    save_button = browser.findElementByClass("save-button")
    browser.clickElement(save_button)


def submit_order():
    order_button = browser.findElementByPartialText("Submit Order")
    browser.clickElement(order_button)


def full_checkout_process(home_link, email, password, drop_time, item_num,
                          size, cvv):
    open_site(home_link)
    login(email, password)
    time_til_drop(drop_time)
    buy_link(item_num, size)
    # select_a_size(size)
    enter_payment_info(cvv)
    # submit_order()


def time_til_drop(drop_time=None):
    if drop_time is None:
        return
    while drop_time > datetime.now():
        print("\rTime til drop: {}".format(drop_time - datetime.now())),
        time.sleep(0.5)


full_checkout_process(nike_homepage, email1, password1, ovo_drop_time,
                      ovo_item_num, shoe_size, my_cvv)
# open_site(jumpman_23_link)
# open_site(ovo_link)
# time_til_drop(ovo_drop_time)
# open_site(nike_homepage)
# login(email1, password1)
# login(email2, password2)
# login(email3, password3)
# login(email4, password4)
# buy_link(ovo_item_num)
# buy(jumpman_price)
# buy_link(jumpman_23_item_num)
