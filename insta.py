from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import sys
import time

systemRandom = random.SystemRandom()

travel_hashtags = [
    'travel', 'travelphotography', 'travelgram', 'wanderlust', 'travelling',
    'travelblogger', 'traveladdict', 'tourism', 'photography', 'naturephotography',
    'travelpic', 'wanderlust'
]
travel_comments = [
    'Your posts are amazing', 'Amazing work. Keep going!', 'Your photos are magnificent',
    'Your work fascinates me!', 'I like how you put your posts together', 'Great job',
    'What a really nice photo!', 'Well done!', 'That is so nice', 'That is so cool', 'This makes me sad :(',
    'One day! xD'
]
coding_hashtags = [
    'coding', 'coder', 'coders', '100daysofcode', 'softwareengineer',
    'programmerlife', 'codingdays', 'codingmeme', 'machinelearning', 'codingpics',
    'html5',
]
coding_comments = [
    'Your posts are amazing', 'Amazing work. Keep going!', 'Your work fascinates me!',
    'I like how you put your posts together', 'Great job', 'Well done!',
    'That is so nice', 'That is so cool', 'This makes me sad :(', 'Cool post', 'One day! xD'
]


class GaryVee:
    username = ''
    password = ''
    hashtags = []
    comments = []
    links = []

    price = 0.0

    def __init__(self, hashtags, comments):
        self.hashtags = hashtags
        self.comments = comments
        self.browser = webdriver.Chrome(executable_path='webdriver/chromedriver.exe')
        self.login()
        self.hustle()

    def login(self):
        self.browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(5)

        self.browser.find_element_by_xpath("//input[@name='username']").send_keys(self.username)
        time.sleep(systemRandom.randint(3, 5))

        self.browser.find_element_by_xpath("//input[@name='password']").send_keys(self.password)
        time.sleep(systemRandom.randint(3, 5))

        login_button = self.browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        time.sleep(systemRandom.randint(3, 5))

    def hustle(self):
        self.getTopPosts()
        self.execute()
        self.finalize()

    def getTopPosts(self):
        for hashtag in self.hashtags:
            self.browser.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
            time.sleep(systemRandom.randint(2, 5))

            links = self.browser.find_elements_by_tag_name('a')
            condition = lambda link: '.com/p/' in link.get_attribute('href')
            valid_links = list(filter(condition, links))

            for i in range(0, 9):
                link = valid_links[i].get_attribute('href')
                if link not in self.links:
                    self.links.append(link)

    def execute(self):
        for link in self.links:
            self.browser.get(link)
            time.sleep(systemRandom.randint(1, 5))

            self.comment()
            time.sleep(systemRandom.randint(1, 5))

            self.like()
            self.price += 0.02

            time.sleep(systemRandom.randint(5, 10))

    def comment(self):
        comment_input = lambda: self.browser.find_element_by_xpath("//textarea[@placeholder='Add a comment…']")
        comment_input().click()
        comment_input().clear()

        comment = systemRandom.choice(self.comments)

        print(comment)
        for letter in comment:
            comment_input().send_keys(letter)
            delay = systemRandom.randint(1, 7) / 30
            time.sleep(delay)

        comment_input().send_keys(Keys.RETURN)

    def like(self):
        like_button = lambda: self.browser.find_element_by_class_name('wpO6b ')
        like_button().click()

    def finalize(self):
        print('You gave $' + str(self.price) + ' back to the community.')
        self.browser.close()
       


garyVee = GaryVee(travel_hashtags, travel_comments)
time.sleep(systemRandom.randint(3, 5))
garyVee = GaryVee(coding_hashtags, coding_comments)
sys.exit()
