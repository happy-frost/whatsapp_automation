import os
import shutil
import time

from selenium import webdriver
from selenium_stealth import stealth

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys

import whatsapp_automation.utils as utils
import whatsapp_automation.exceptions as exceptions

class Whatsapp:
    """
    A class to initialize the whatsapp session.
    """
    def __init__(self, user_data_dir:str='', profile_dir:str='Default'):
        """
        Initalization function that starts the driver and save it to the class to be used by other functions.
        After running this funciton, user have to manually scan the qr code to being the session.
        input: None
        output: success (boolean)
        """
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-setuid-sandbox")
        options.add_argument("--remote-debugging-port=9222")
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36')
        if user_data_dir:
            options.add_argument(f"--user-data-dir={user_data_dir}")
            options.add_argument(f"--profile-directory={profile_dir}")

        self.driver = webdriver.Chrome(options=options)
        stealth(self.driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )
        return None
        
    def login(self) -> bool:
        self.driver.get("https://web.whatsapp.com")

        try:
            # Wait for login
            WebDriverWait(self.driver,timeout=300).until(
                EC.presence_of_element_located((By.ID,"expressions-panel-container"))
            )

            # Wait for and press overlay object
            element = WebDriverWait(self.driver,timeout=300).until(
                EC.presence_of_element_located((By.CLASS_NAME,"x889kno"))
            )
            element.click()
            return True
        except: 
            return False
    
    def go_to_chat(self,input: str) -> bool:
        """
        Go to the chat using the phone number or group id
        input: phone number/ group id (string)
        output: success (boolean)
        """
        # Redirect to the correct chat
        if "+" in input or "_" in input:
            try:
                utils.check_number(input)
                self.driver.get("https://web.whatsapp.com/send?phone=" + input)
            except exceptions.InvalidPhoneNumber:
                return False
        else: 
            self.driver.get("https://web.whatsapp.com/accept?code=" + input)
        
        try:
            WebDriverWait(self.driver,timeout=10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,"div.x98rzlu > button > span > svg"))
            )
            return True
        except:
            return False
    
    def send_message(self,message: str) -> bool:
        """
        Send message to chat. To be used after going to a particular chat.
        input: message (string)
        output: success (boolean)
        """
        try:
            textBox = self.driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p')            
            textBox.click()
            lines = message.split('\n')
            for line in lines:
                textBox.send_keys(line)
                textBox.send_keys(Keys.SHIFT + Keys.ENTER)
            textBox.send_keys(Keys.ENTER)
            return True
        except:
            return False
    
    def send_document(self,file_path: str, caption: str = "") -> bool:
        """
        Send document to chat. To be used after going to a particular chat.
        input: file path (string)
        output: success (boolean)
        """
        try:
            addButton = self.driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span/div/div[1]/div/button')
            addButton.click()

            addDocumentInput = self.driver.find_element(By.XPATH,'//*[@id="app"]/div/span[6]/div/ul/div/div/div[1]/li/div/input')
            addDocumentInput.send_keys(file_path)

            captionTextBox = WebDriverWait(self.driver,timeout=10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,"#app > div > div.x78zum5.xdt5ytf.x5yr21d > div > div.x10l6tqk.x13vifvy.x17qophe.x78zum5.xh8yej3.x5yr21d.x6ikm8r.x10wlt62.x47corl > div.x9f619.x1n2onr6.x5yr21d.x6ikm8r.x10wlt62.x17dzmu4.x1i1dayz.x2ipvbc.x1w8yi2h.xyyilfv.x1iyjqo2.xa1v5g2 > span > div > div > div > div.x1n2onr6.xyw6214.x78zum5.x1r8uery.x1iyjqo2.xdt5ytf.x1hc1fzr.x6ikm8r.x10wlt62 > div > div.x1n2onr6.x78zum5.x98rzlu.xdt5ytf.x1qughib.x6ikm8r.x10wlt62 > div.x1n2onr6.x78zum5.x6s0dn4.xl56j7k.xbktkl8.x1y1aw1k.x1pi30zi.xwib8y2.x1swvt13 > div > div > div.x1n2onr6.xh8yej3.x1k70j0n.x11i5rnm.xzueoph.x1mh8g0r.xisnujt.xzwifym.x1vvkbs.x126k92a.x1hx0egp.lexical-rich-text-input > div.x1hx0egp.x6ikm8r.x1odjw0f.x1k6rcq7.x1lkfr7t > p"))
                )
            captionTextBox.send_keys(caption)
            captionTextBox.send_keys(Keys.ENTER)
            return True
        except:
            return False
    
    def send_photo_or_video(self,file_path: str, caption: str = "") -> bool:
        """
        Send photo or video to chat. To be used after going to a particular chat.
        input: file path (string)
        output: success (boolean)
        """
        try:
            addButton = self.driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span/div/div[1]/div/button')
            addButton.click()

            addDocumentInput = self.driver.find_element(By.XPATH,'//*[@id="app"]/div/span[6]/div/ul/div/div/div[2]/li/div/input')
            addDocumentInput.send_keys(file_path)

            captionTextBox = WebDriverWait(self.driver,timeout=10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,"#app > div > div.x78zum5.xdt5ytf.x5yr21d > div > div.x10l6tqk.x13vifvy.x17qophe.x78zum5.xh8yej3.x5yr21d.x6ikm8r.x10wlt62.x47corl > div.x9f619.x1n2onr6.x5yr21d.x6ikm8r.x10wlt62.x17dzmu4.x1i1dayz.x2ipvbc.x1w8yi2h.xyyilfv.x1iyjqo2.xa1v5g2 > span > div > div > div > div.x1n2onr6.xyw6214.x78zum5.x1r8uery.x1iyjqo2.xdt5ytf.x1hc1fzr.x6ikm8r.x10wlt62 > div > div.x78zum5.x1iyjqo2.xs83m0k.x1r8uery.xdt5ytf.x1qughib.x6ikm8r.x10wlt62 > div.x1c4vz4f.xs83m0k.xdl72j9.x1g77sc7.x78zum5.xozqiw3.x1oa3qoh.x12fk4p8.xeuugli.x2lwn1j.xl56j7k.x1q0g3np.x6s0dn4.x1n2onr6.xo8q3i6.x1y1aw1k.xwib8y2.xkhd6sd.x4uap5 > div > div > div.x1c4vz4f.xs83m0k.xdl72j9.x1g77sc7.x78zum5.xozqiw3.x1oa3qoh.x12fk4p8.xeuugli.x2lwn1j.x1nhvcw1.x1q0g3np.x1cy8zhl.x9f619.xh8yej3.x1ba4aug.x1iorvi4.x1pi30zi.xjkvuk6.x1swvt13.x7nbn6e.x1lq5wgf.xgqcy7u.x30kzoy.x9jhf4c > div.x1n2onr6.xh8yej3.x1k70j0n.x11i5rnm.xzueoph.x1mh8g0r.xisnujt.xzwifym.x1vvkbs.x126k92a.x1hx0egp.lexical-rich-text-input > div.x1hx0egp.x6ikm8r.x1odjw0f.x1k6rcq7.x1lkfr7t > p"))
                )
            captionTextBox.send_keys(caption)
            captionTextBox.send_keys(Keys.ENTER)
            return True
        except:
            return False
    
    def find_file(self, target_file_name:str, source_folder:str, destination_folder: str) -> bool:
        chatHistory = self.driver.find_element(By.XPATH,'//*[@id="main"]/div[3]/div/div[2]/div[2]')
        isToday = False     
        target_element = None
        try:
            for chat in chatHistory.find_elements(By.CSS_SELECTOR,'div > div > span'):
                if chat.get_attribute('innerHTML') == "TODAY":
                    isToday = True

                if isToday and chat.get_attribute('innerHTML').__contains__(target_file_name):
                    target_element = chat
                    break

            if not target_element: # if it is none
                return False

            target_element.click()

            time.sleep(10)

            # Create destination folder if it doesn't exist
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            # Move only .xls and .xlsx files
            for file_name in os.listdir(source_folder):
                if file_name == target_file_name:
                    src_file = os.path.join(source_folder, file_name)
                    dest_file = os.path.join(destination_folder, file_name)
                    shutil.move(src_file, dest_file)
                    return True
            
            return False
        except Exception as e:
            return False

    def exit(self):
        self.driver.quit()