from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

username = ""
password = ""


class Instagram:
    driver_path = "C:\\Users\Talha\Desktop\InstagramApp\chromedriver.exe"

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option(
            'prefs', {'intl.accept_languages': 'en,en_US'})
        self.browser = webdriver.Chrome(
            Instagram.driver_path, options=self.browserProfile)

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        usernameInput = self.browser.find_element(By.NAME, "username")
        passwordInput = self.browser.find_element(By.NAME, "password")

        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(5)

        if self.browser.find_element(By.CLASS_NAME, "_ac8f"):
            el = self.browser.find_element(By.CLASS_NAME, "_ac8f")
            el.find_element(By.TAG_NAME, "button").click()
        time.sleep(4)

        if self.browser.find_element(By.CLASS_NAME, "_a9-z"):
            ele = self.browser.find_element(By.CLASS_NAME, "_a9-z")
            ele = ele.find_elements(By.TAG_NAME, "button")
            ele[1].click()
            time.sleep(3)

    def followUser(self, username):
        self.browser.get("https://www.instagram.com/{}/".format(username))
        time.sleep(3)
        followButton = self.browser.find_element(By.TAG_NAME, "button")
        time.sleep(2)
        if followButton.text == "Follow":
            followButton.click()
            time.sleep(2)
        else:
            print(f"{username} you are already following the page.")

    def FollowUsers(self, users):
        for user in users:
            self.followUser(user)

    def __del__(self):
        time.sleep(10)
        # self.browser.close()


app = Instagram(username, password)

app.signIn()

app.FollowUsers(["yazili_videolar__", "kodevreni"])
