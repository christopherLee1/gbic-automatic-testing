# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import random, unittest, time, re, sys, os

class GenomeTest(unittest.TestCase):
    def __init__(self, testname, host):
        super(GenomeTest, self).__init__(testname)
        self.base_url = host
        opts = webdriver.ChromeOptions()
        opts.add_argument("--window-size=1280,777")
        opts.add_argument("--disable-device-discovery-notifications")
        self.driver = webdriver.Chrome("/Users/christopherLee/Downloads/chromedriver", chrome_options=opts)
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_genome_test(self):
        driver = self.driver
        driver.get(self.base_url + "/index.html")
        
        driver.find_element_by_link_text("Home").click()
        driver.find_element_by_link_text("Genomes").click()
        try:
            if self.base_url.find("-") != -1: # genome-euro and genome-asia
                driver.find_element_by_xpath("//div[3]/ul/li[3]/a").click()
        except NoSuchElementException:
            pass
        self.cart_reset(driver)
        Select(driver.find_element_by_id("selectAssembly")).select_by_value("hg19")
        driver.find_element_by_css_selector("div.jwGoButton").click()
        driver.find_element_by_xpath("//td[@id='td_data_knownGene']/div[2]/map/area[5]").click()
       
        # check mm10 hgTracks and hgGene 
        self.hover_over_menu(driver, "//li[@id='tools1']", "//li[@id='tools1']/ul/li[3]") # click mm10 from Genomes drop down
        driver.find_element_by_xpath("//td[@id='td_data_knownGene']/div[2]/map/area[6]").click() # clicks into hgGene
        
        # test hgCustom
        driver.get(self.base_url + "/cgi-bin/hgGateway?db=hg19")
        if self.base_url[-4:] == "1234": # gbib
            self.hover_over_menu(driver, "//li[@id='myData']", "//li[@id='myData']/ul/li[5]")
        else: # any other mirror
            self.hover_over_menu(driver, "//li[@id='myData']", "//li[@id='myData']/ul/li[4]")
        driver.find_element_by_name("hgct_customText").clear()
        driver.find_element_by_name("hgct_customText").send_keys("http://hgwdev.cse.ucsc.edu/~chmalee/examples.WITHOUT.FTPS.txt")
        driver.find_element_by_name("Submit").click()
        driver.find_element_by_name("submit").click()
        
        # test hgBlat
        self.cart_reset(driver)
        driver.get(self.base_url + "/cgi-bin/hgGateway?db=hg19")
        self.hover_over_menu(driver, "//li[@id='tools3']", "//li[@id='tools3']/ul/li[1]")
        driver.find_element_by_name("userSeq").clear()
        driver.find_element_by_name("userSeq").send_keys("AACAAAATCAAACTGTTTTTGTTGGACAATTCTCTGTTAAGCAGCTATAA\nGCTGAATGACATTAACCGCAAAATGTAACCATAAAGGCCATAAACCCGAC\nATTGTTAATTAATTAAATGCCTCATTAACTTTTTTAAAAACATGATTTAT\nTCGATTCATAGAAAACTTAACCATCACTACTAAATGCACACACATGCGGT\nTCCACATTGGCATCTTAGCCTAAGAACAGACAGGTTCAACTGTAACTGGC\nCTTTCAGGTGGTCTATTACAGATCTGAAGACAGAGGGTGTTTCTAAACCT\nCAAGAACCAGATTAACAGAAAACAAAGCTTGAGCAGCCTTTTTATTGCAT\nGTGGTATCTTTTTAGCTAAGCAGAAGACAATGATAAAGAGGGGTTTTGGG\nAAACCTCTCCCAAAGCTGTGCATTCATACCGTACCTTATCCTGTTAAGCA\nAACTGTTCTTTTATTTTAAAGGGTTTACACTGCCACATCTGAATGGACTA")
        driver.find_element_by_name("Submit").click()
        driver.find_element_by_link_text("browser").click()
        driver.find_element_by_id("p_btn_hgUserPsl").click()
     
        # test hgPcr
        self.cart_reset(driver)
        if self.base_url[-4:] == "1234":
            self.hover_over_menu(driver, "//li[@id='tools3']", "//li[@id='tools3']/ul/li[7]")
        else:
            self.hover_over_menu(driver, "//li[@id='tools3']", "//li[@id='tools3']/ul/li[8]")
        driver.find_element_by_name("wp_f").clear()
        driver.find_element_by_name("wp_f").send_keys("AACAAAATCAAACTGTTTTTGTTGGACAATTCTCTGTTAAGCAGCTATAA")
        driver.find_element_by_name("wp_r").clear()
        driver.find_element_by_name("wp_r").send_keys("AACTGTTCTTTTATTTTAAAGGGTTTACACTGCCACATCTGAATGGACTA")
        driver.find_element_by_name("wp_flipReverse").click()
        driver.find_element_by_name("Submit").click()
        driver.find_element_by_link_text("chrX:40059679+40060178").click()
  
        # hgConvert
        self.cart_reset(driver)
        driver.find_element_by_link_text("Genome Browser").click()
        self.hover_over_menu(driver, "//li[@id='view']", "//li[@id='view']/ul/li[3]")
        driver.find_element_by_name("hglft_doConvert").click()
        driver.find_element_by_link_text("chr1:11162894-11327804").click()

        # hgLiftOver
        if self.base_url[-4:] == "1234":
            self.hover_over_menu(driver, "//li[@id='tools3']", "//li[@id='tools3']/ul/li[8]")
        else:
            self.hover_over_menu(driver, "//li[@id='tools3']", "//li[@id='tools3']/ul/li[9]")
        driver.find_element_by_name("hglft_userData").clear()
        driver.find_element_by_name("hglft_userData").send_keys("chr21:33,031,597-33,041,570")

        # hgHubConnect
        self.cart_reset(driver)
        self.hover_over_menu(driver, "//li[@id='myData']", "//li[@id='myData']/ul/li[3]")
        #for xpath in ["//table[@class='hubList']/tbody/tr["+str(hubId+1)+"/td/[3]" for hub in random.randint(0,55)]
    
        while True:
            hubId = random.randint(0,55) # random td element, off by one between xpath and connectButton
            xpath = "//table[@class='hubList']/tbody/tr[" + str(hubId+1) + "]"
            print("checking hub: %s" % (driver.find_element_by_xpath(xpath + "/td[2]").text))
            if "hubError" in driver.find_element_by_xpath(xpath + "/td[3]").get_attribute("class"):
                print("hub has some error, trying another")
                continue
            else:
                driver.find_element_by_id("hubConnectButton" + str(hubId)).click()
                break
        driver.find_element_by_css_selector("div.jwGoButton").click()
        try:
            elem = driver.find_element_by_xpath('//select[starts-with(@name, "hub_")]') # hub didn't load
            if elem:
                print("hub loaded correctly")
        except NoSuchElementException:
             print("hub did not load successfully")
             sys.exit()
         
    def test_offline_genome_test(self):
        driver = self.driver
        driver.get(self.base_url + "/index.html")
        driver.get(self.base_url + "/cgi-bin/hgGateway?db=hg19")
        driver.find_element_by_css_selector("div.jwGoButton").click() 

        # hgMirror
        # first make sure no Alt Locations track, should raise an exception
        try:
            elem = driver.find_element_by_name("altLocations")
            if elem:
                print("altLocations track already downloaded. Please delete the table and run again")
                sys.exit(1)
        except NoSuchElementException:
            print("altLocations table does not exist.")
            pass

        # download the altLocations table
        self.hover_over_menu(driver, "//li[@id='tools3']", "//li[@id='tools3']/ul/li[9]")
        group = driver.find_element_by_xpath("//select[@name='clade']/option[@selected='']")
        genome = driver.find_element_by_xpath("//select[@name='org']/option[@selected='']")
        db = driver.find_element_by_xpath("//select[@name='db']/option[@selected='']")
        if db != "Feb. 2009 (GRCh37/hg19)":
            if genome != "Human":
                if group != "Mammal":
                    Select(driver.find_element_by_xpath("//select[@name='clade']")).select_by_value("mammal")
                Select(driver.find_element_by_xpath("//select[@name='org']")).select_by_value("Human")
            Select(driver.find_element_by_xpath("//select[@name='db']")).select_by_value("hg19")
        driver.find_element_by_id("altLocations").click()
        driver.find_element_by_xpath("//input[@value='Download']").click()
        link = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.LINK_TEXT, "Back to Genome Browser")))
        link.click()

        # table should exist now
        try:
            driver.find_element_by_id("map_button").click()
            driver.find_element_by_name("altLocations").click()
            print("altLocations track successfully downloaded.")
        except NoSuchElementException:
            print("altLocations track did not download successfully. Try again.")
            sys.exit(1)

    def wait_for_full_page_load(self, driver, element):
        # wait until a certain element becomes visible before proceeding. 
        # not currently used, needs more work
        elem = None
        if element.startswith('//'):
           print("Wait up to 1 second for custom tracks")
           elem = WebDriverWait(driver, .001).until(EC.visibility_of_element_located((By.XPATH, element)))
        else:
           print("Wait up to 1 second for hgTracks")
           elem = WebDriverWait(driver, .001).until(EC.visibility_of_element_located((By.LINK_TEXT, element)))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        
    def hover_over_menu(self, driver, menu_header, menu_item_xpath):
        """hovers over menubar and clicks an item in a dropdown list"""
        # below code taken from: 
        # http://stackoverflow.com/questions/27934945/selenium-move-to-element-does-not-always-mouse-hover
        men_menu = WebDriverWait(driver,10).until(EC.visibility_of_element_located((
            By.XPATH, menu_header)))
        ActionChains(driver).move_to_element(men_menu).perform() 
        link_to_click = WebDriverWait(driver,10).until(EC.visibility_of_element_located(
            (By.XPATH, menu_item_xpath)))
        link_to_click.click()

    def cart_reset(self, driver):
        # hovers over the Genome Browser menubar item and clicks cart reset
        self.hover_over_menu(driver, "//li[@id='tools2']", "//li[@id='tools2']/ul/li[3]") 

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    if len(sys.argv) > 2 and sys.argv[2] == "offline":
        suite.addTest(GenomeTest("test_offline_genome_test", sys.argv[1]))
    else:
        suite.addTest(GenomeTest("test_genome_test", sys.argv[1]))
    try:
        success = unittest.TextTestRunner().run(suite).wasSuccessful()
    except SystemExit:
        print("not success")
        #os._exit(1)
