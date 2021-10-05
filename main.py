from selenium import webdriver
import csv
import time
import os

print("Started")

PATH = r'C:\Programação\Python\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://www.amazon.com.br/ap/signin?_encoding=UTF8&openid.assoc_handle=brflex&openid.claimed_id=http%3A%2F'
           '%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%'
           '2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&o'
           'penid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.re'
           'turn_to=https%3A%2F%2Fwww.amazon.com.br%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26ref_%3Dgno_signin')

print("Running")

time.sleep(0.5)


# email
driver.find_element_by_id('ap_email').send_keys('#')
driver.find_element_by_id('continue').click()
time.sleep(0.5)


# password
driver.find_element_by_id('ap_password').send_keys('#')
driver.find_element_by_id('signInSubmit').click()
try:
    driver.find_element_by_id('ap-account-fixup-phone-skip-link').click()
except:
    pass
time.sleep(0.7)


# catalog
driver.find_element_by_id('nav-hamburger-menu').click()
time.sleep(0.5)

driver.find_element_by_xpath('//*[@id="hmenu-content"]/ul[1]/li[3]/a').click()
time.sleep(1)

driver.find_element_by_link_text('Computadores e Informática').click()
time.sleep(0.2)

catalog = driver.find_elements_by_css_selector('div.p13n-sc-truncated')

assert os.path.isfile('products.csv')
n = 1
with open('products.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["row", "product"])
    for item in catalog[0:11]:
        writer.writerow([n, item.text])
        n += 1
        if n == 11:
            break

print("Finished")

driver.close()
