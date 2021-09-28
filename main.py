from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth_data import username, password
import time
import random

def hash_search(username, password, hashtag):
    browser = webdriver.Edge('./chromedriver/msedgedriver')


    try:
        browser.get('https://instagram.com')
        time.sleep(random.randrange(3, 5))

        username_input = browser.find_element_by_name('username')
        username_input.clear()
        username_input.send_keys(username)

        time.sleep(2)

        password_input = browser.find_element_by_name('password')
        password_input.clear()
        password_input.send_keys(password)

        password_input.send_keys(Keys.ENTER)
        time.sleep(5)

        try:
            browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
            time.sleep(3)

            for i in range(1, 4):
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(random.randrange(3, 5))

            hrefs = browser.find_elements_by_tag_name('a')
            posts_urls = [item.get_attribute('href') for item in hrefs if "/p/" in item.get_attribute('href')]

            for url in posts_urls:
                try:
                    browser.get(url)
                    time.sleep(3)
                    # like_button = browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div['
                    #                                             '2]/div/div[2]/section[1]/span[1]/button').click()
                    like_button = browser.find_element_by_css_selector('div.eo2As span.fr66n button.wpO6b').click()
                    time.sleep(random.randrange(80, 100))
                except Exception as ex:
                    print(ex)

            browser.close()
            browser.quit()

        except Exception as ex:
            print(ex)
            browser.close()
            browser.quit()

    except Exception as ex:
        print(ex)
        browser.close()
        browser.quit()

hash_search(username, password, 'frenchbulldog')