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
import unittest, time, re, sys

class GenomeTest(unittest.TestCase):
    def __init__(self, testname, host):
        super(GenomeTest, self).__init__(testname)
        self.base_url = host
        self.driver = webdriver.Chrome("/Users/christopherLee/Downloads/chromedriver")
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_genome_test(self):
        #print("url is %s\n" % self.host)
        driver = self.driver
        driver.get(self.base_url + "/index.html")
        driver.find_element_by_link_text("Home").click()
        driver.find_element_by_link_text("Genomes").click()
        self.cart_reset(driver)
        Select(driver.find_element_by_id("selectAssembly")).select_by_visible_text("Feb. 2009 (GRCh37/hg19)")
        driver.find_element_by_css_selector("div.jwGoButton").click()
        self.driver.implicitly_wait(1000)
        driver.find_element_by_xpath("//td[@id='td_data_knownGene']/div[2]/map/area[5]").click()
        driver.get(self.base_url + "/cgi-bin/hgGateway?db=mm10")
       
        # check mm10 hgTracks and hgGene 
        self.driver.implicitly_wait(1000)
        self.hover_over_menu(driver, "//li[@id='tools1']", "//li[@id='tools1']/ul/li[3]") # click mm10 from Genomes drop down
        driver.find_element_by_xpath("//td[@id='td_data_knownGene']/div[2]/map/area[6]").click() # clicks into hgGene
        
        # test custom track
        driver.get(self.base_url + "/cgi-bin/hgGateway?db=hg19")
        self.driver.implicitly_wait(1000)
        if self.base_url[-4:] == "1234": # gbib
            self.hover_over_menu(driver, "//li[@id='myData']", "//li[@id='myData']/ul/li[5]")
        else: # any other mirror
            self.hover_over_menu(driver, "//li[@id='myData']", "//li[@id='myData']/ul/li[4]")
        
        driver.find_element_by_name("hgct_customText").clear()
        driver.find_element_by_name("hgct_customText").send_keys("http://hgwdev.cse.ucsc.edu/~brianlee/customTracks/examples.WITHOUT.FTPS.txt")
        driver.find_element_by_name("Submit").click()
        self.driver.implicitly_wait(1000)
        driver.find_element_by_name("submit").click()
        """
        self.cart_reset(driver)
        driver.find_element_by_link_text("Genome Browser").click()
        driver.find_element_by_id("trackHubsMenuLink").click()
        driver.find_element_by_link_text("My Hubs").click()
        driver.find_element_by_id("hubUrl").clear()
        driver.find_element_by_id("hubUrl").send_keys("http://hgwdev.cse.ucsc.edu/~brianlee/examples/hubExample/hub.txt")
        driver.find_element_by_name("hubAddButton").click()
        driver.get("http://genome.ucsc.edu/cgi-bin/hgGateway")
        driver.find_element_by_css_selector("div.jwGoButton").click()
        driver.get("http://genome.ucsc.edu/cgi-bin/hgTracks")
        driver.find_element_by_id("p_btn_hub_77624_bam1").click()
        Select(driver.find_element_by_name("hub_77624_bam1")).select_by_visible_text("full")
        driver.find_element_by_name("hub_77624_bam1.doWiggle").click()
        driver.find_element_by_name("Submit").click()
        self.cart_reset(driver)
        driver.find_element_by_id("blatMenuLink").click()
        Select(driver.find_element_by_css_selector("select[name=\"db\"]")).select_by_visible_text("Feb. 2009 (GRCh37/hg19)")
        """
        self.cart_reset(driver)
        driver.get(self.base_url + "/cgi-bin/hgGateway?db=hg19")
        self.hover_over_menu(driver, "//li[@id='tools3']", "//li[@id='tools3']/ul/li[1]") # hgBlat
        driver.find_element_by_name("userSeq").clear()
        driver.find_element_by_name("userSeq").send_keys("AACAAAATCAAACTGTTTTTGTTGGACAATTCTCTGTTAAGCAGCTATAA\\nGCTGAATGACATTAACCGCAAAATGTAACCATAAAGGCCATAAACCCGAC\\nATTGTTAATTAATTAAATGCCTCATTAACTTTTTTAAAAACATGATTTAT\\nTCGATTCATAGAAAACTTAACCATCACTACTAAATGCACACACATGCGGT\\nTCCACATTGGCATCTTAGCCTAAGAACAGACAGGTTCAACTGTAACTGGC\\nCTTTCAGGTGGTCTATTACAGATCTGAAGACAGAGGGTGTTTCTAAACCT\\nCAAGAACCAGATTAACAGAAAACAAAGCTTGAGCAGCCTTTTTATTGCAT\\nGTGGTATCTTTTTAGCTAAGCAGAAGACAATGATAAAGAGGGGTTTTGGG\\nAAACCTCTCCCAAAGCTGTGCATTCATACCGTACCTTATCCTGTTAAGCA\\nAACTGTTCTTTTATTTTAAAGGGTTTACACTGCCACATCTGAATGGACTA")
        driver.find_element_by_name("Submit").click()
        self.driver.implicitly_wait(1000)
        driver.find_element_by_link_text("browser").click()
        driver.find_element_by_id("p_btn_hgUserPsl").click()
        self.driver.implicitly_wait(1000)
        self.cart_reset(driver)
        if self.base_url[-4:] == "1234":
            self.hover_over_menu(driver, "//li[@id='tools3']", "//li[@id='tools3']/ul/li[6]") # hgPcr
        else:
            self.hover_over_menu(driver, "//li[@id='tools3']", "//li[@id='tools3']/ul/li[7]") # hgPcr
        driver.find_element_by_name("wp_f").clear()
        driver.find_element_by_name("wp_f").send_keys("AACAAAATCAAACTGTTTTTGTTGGACAATTCTCTGTTAAGCAGCTATAA")
        driver.find_element_by_name("wp_r").clear()
        driver.find_element_by_name("wp_r").send_keys("AACTGTTCTTTTATTTTAAAGGGTTTACACTGCCACATCTGAATGGACTA")
        driver.find_element_by_name("wp_flipReverse").click()
        driver.find_element_by_name("Submit").click()
        self.driver.implicitly_wait(1000)
        driver.find_element_by_link_text("chrX:40059679+40060178").click()
        self.driver.implicitly_wait(1000)
        self.cart_reset(driver)
        driver.find_element_by_link_text("Genome Browser").click()
        self.hover_over_menu(driver, "//li[@id='view']", "//li[@id='view']/ul/li[3]") # hgConvert
        driver.find_element_by_name("hglft_doConvert").click()
        driver.find_element_by_link_text("chr9:136127387-136156434").click()
        driver.find_element_by_css_selector("#tools3 > span").click()
        if self.base_url[-4:] == "1234":
            self.hover_over_menu(driver, "//li[@id='tools3']", "//li[@id='tools3']/ul/li[7]") # hgLiftOver
        else:
            self.hover_over_menu(driver, "//li[@id='tools3']", "//li[@id='tools3']/ul/li[8]") # hgLiftOver
        driver.find_element_by_name("hglft_userData").clear()
        driver.find_element_by_name("hglft_userData").send_keys("chr21:33,031,597-33,041,570")

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
    suite.addTest(GenomeTest("test_genome_test", sys.argv[1]))
    unittest.TextTestRunner().run(suite)
