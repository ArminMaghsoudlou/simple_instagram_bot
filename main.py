from selenium import webdriver
from time import sleep

#make sure chromedriver is in path!

class Instabot:
    def __init__(self, username, pw):
        self.username = username
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[2]/p/a').click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(pw)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()
        sleep(4)
        self.driver.find_element_by_xpath('/ html / body / div[4] / div / div / div[3] / button[2]').click()
        sleep(3)
    def get_ppl_not_following(self):
        self.driver.find_element_by_xpath('/ html / body / div[1] / section / main / section / div[3] / div[1] / div / div[2] / div[1] / a').click()
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
        following = self._get_names()
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a').click()
        followers = self._get_names()
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)


    def _get_names(self):
        sleep(3)
        scroll_box = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')
        last_ht, h = 0, 1
        while last_ht != h:
            last_ht = h
            sleep(3)
            ht = self.driver.execute_script("""arguments[0].scrollTo(0,arguments[0].scrollHeight);
                    return arguments[0].scrollHeight;""", scroll_box)
        sleep(10)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        print(names)
        self.driver.refresh()
        #self.driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button/svg').click()
        return names

# Insert own password/username
bot = Instabot('CHANGE THIS TO USERNAME', 'CHANGE THIS TO PASSWORD')
bot.get_ppl_not_following()
