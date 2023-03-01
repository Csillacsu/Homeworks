import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Test_Trial_Of_The_Stones(object):
    def setup_method(self):
        service = Service(executable_path=r'/home/user/Asztal/chromedriver_linux64/chromedriver')
        options = Options()
        options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(service=service, options=options)
        URL = "https://techstepacademy.com/trial-of-the-stones"
        self.browser.get(URL)

    def teardown_method(self):
        self.browser.quit()

    def test_trial(self):
        first_answer_input = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.ID, 'r1Input')))
        first_answer_button = self.browser.find_element(By.ID, "r1Btn")
        first_answer_input.send_keys("rock")
        first_answer_button.click()

        second_word = self.browser.find_element(By.XPATH, '//div[@id="passwordBanner"]/h4')
        second_answer_input = self.browser.find_element(By. ID,"r2Input")
        second_answer_button = self.browser.find_element(By.ID, "r2Butn")
        second_answer_input.send_keys(second_word.text)
        second_answer_button.click()

        first_success_msg = self.browser.find_element(By.ID, 'successBanner1')
        assert first_success_msg.text == "Success!"

        first_name = self.browser.find_elements(By.XPATH, '//b')[0]
        first_wealth = self.browser.find_elements(By.XPATH, '//b/../../p')[0]
        second_name = self.browser.find_elements(By.XPATH, '//b')[1]
        second_wealth = self.browser.find_elements(By.XPATH, '//b/../../p')[1]
        third_answer_input = self.browser.find_element(By.ID, "r3Input")
        third_answer_button = self.browser.find_element(By.ID, "r3Butn")

        if int(first_wealth.text) < int(second_wealth.text):
            third_answer_input.send_keys(second_name.text)
        else:
            third_answer_input.send_keys(first_name.text)

        third_answer_button.click()

        second_success_msg = self.browser.find_element(By.ID, 'successBanner2')
        assert second_success_msg.text == "Success!"

        final_button = self.browser.find_element(By.ID, "checkButn")
        final_button.click()

        complete_message = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@id="trialCompleteBanner"]/h4')))
        assert complete_message.text == "Trial Complete"
