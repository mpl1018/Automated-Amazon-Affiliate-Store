from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options  
import time
import sys
from secrets import username, password
import firebase_admin
from firebase_admin import credentials, firestore


PATH = './chromedriver' 
class amazonBot():
    def __init__(self): 
        chrome_options = Options()  
        chrome_options.add_argument("--headless")  
        self.driver = webdriver.Chrome(executable_path=PATH, options=chrome_options)
        self.cred = credentials.Certificate('./key.json')
        self.default_app = firebase_admin.initialize_app(self.cred)
        self.db = firestore.client()

        self.category = sys.argv[1]
        self.input = ""
        for index, inp in enumerate(sys.argv): 
            if index!=0  and index!=1:
                self.input = self.input + inp + " "
    
    def login(self): 
        self.driver.get("https://www.amazon.es/")
        time.sleep(2)
        logB1 = self.driver.find_element_by_xpath('//*[@id="nav-link-accountList"]/span[1]')
        logB1.click()
        time.sleep(2)

        email_in = self.driver.find_element_by_xpath('//*[@id="ap_email"]')
        email_in.send_keys(username)
        continuarButton = self.driver.find_element_by_xpath('//*[@id="continue"]')
        continuarButton.click()
        time.sleep(2)

        pass_in = self.driver.find_element_by_xpath('//*[@id="ap_password"]')
        pass_in.send_keys(password)
        iniciaSesion = self.driver.find_element_by_xpath('//*[@id="signInSubmit"]')
        iniciaSesion.click()
        time.sleep(2)
        print("loged in")

    def buscar(self):
        #print(self.driver.page_source)
        buscar_in = self.driver.find_element_by_id("twotabsearchtextbox")
        time.sleep(2)
        buscar_in.send_keys(self.input)

        buscarButton = self.driver.find_element_by_xpath('//*[@id="nav-search"]/form/div[2]/div/input')
        time.sleep(2)
        buscarButton.click()

    def procesarResultado(self):
        try: main = self.driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[4]/div[2]')
        except Exception: 
            main = self.driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[4]/div[1]')
        articulos = main.find_elements_by_class_name('s-result-item')
        for articulo in articulos:
            try:
                titulo = articulo.find_element_by_class_name('a-size-mini')
                mitit = titulo.text
                precio = articulo.find_element_by_class_name('a-price')
                miprec = precio.text
                # NEW WINDOW
                time.sleep(3) 
                Blink = titulo.find_element_by_class_name('a-link-normal').get_attribute('href')
                time.sleep(3)
                self.driver.execute_script('window.open("' + Blink+ '","_blank");')
                time.sleep(3)
                #CHANGE WINDOW
                self.driver.switch_to.window(self.driver.window_handles[1])
                time.sleep(3)
                #GET IMAGE
                imagen = self.driver.find_element_by_xpath('//*[@id="landingImage"]').get_attribute('src')
                time.sleep(3)
                #GET AFFILIATE LINK
                btnTexto = self.driver.find_element_by_xpath('//*[@id="amzn-ss-text-link"]/span/span/strong/a')
                time.sleep(3)
                btnTexto.click()
                time.sleep(3)
                Glink = self.driver.find_element_by_xpath('//*[@id="amzn-ss-text-shortlink-textarea"]')
                time.sleep(3)

                time.sleep(5) 
                data = {
                    u'imagen': imagen,
                    u'link': Glink.text,
                    u'precio': miprec,
                    u'titulo': mitit,
                    u'timestamp': str(time.time())
                }

                id = imagen[49:-4]                    
                self.db.collection(self.category).document(id).set(data)
                time.sleep(5)

                #CLOSE WINDOW
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])

                time.sleep(2) 

            except Exception as e:
                print(e)
                pass

        self.driver.quit()

    def borrarAntiguo(self): 
        snapshot = self.db.collection(self.category).stream()
        time.sleep (3)
        for element in snapshot:
            if time.time()-float(element.to_dict()['timestamp'])>18000:
                self.db.collection(self.category).document(element.id).delete()
                time.sleep (3)



bot = amazonBot()
bot.login()
bot.buscar()
bot.procesarResultado()

