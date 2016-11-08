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
import unittest, time, re

class GenomeAsiaFromSelenium(unittest.TestCase):
    def setUp(self):
        """We use Chrome here because Firefox has some issues with hover-selecting"""
        self.driver = webdriver.Chrome("/Users/christopherLee/Downloads/chromedriver")
        self.driver.implicitly_wait(30)
        self.base_url = "http://genome.ucsc.edu/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_genome_asia_from_selenium(self):
        driver = self.driver
        driver.get(self.base_url + "/index.html")
        driver.find_element_by_link_text("Home").click()
        driver.find_element_by_link_text("Genomes").click()
        driver.get("http://genome.ucsc.edu/cgi-bin/cartReset")
        #driver.get("http://genome.ucsc.edu/cgi-bin/hgGateway")
        Select(driver.find_element_by_id("selectAssembly")).select_by_visible_text("Feb. 2009 (GRCh37/hg19)")
        driver.find_element_by_css_selector("div.jwGoButton").click()
        driver.find_element_by_xpath("//td[@id='td_data_knownGene']/div[2]/map/area[5]").click()
        driver.get("http://genome.ucsc.edu/cgi-bin/hgGateway?db=mm10")
        
        self.driver.implicitly_wait(1000)
        # below code taken from: 
        # http://stackoverflow.com/questions/27934945/selenium-move-to-element-does-not-always-mouse-hover
        men_menu = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, "//li[@id='tools1']")))
        ActionChains(driver).move_to_element(men_menu).perform()

        self.driver.implicitly_wait(1000)
        # wait for Mouse/mm10 item to appear, then click it
        mm10= WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//li[@id='tools1']/ul/li[3]")))
        mm10.click()
        driver.find_element_by_xpath("//td[@id='td_data_knownGene']/div[2]/map/area[6]").click()
        
        driver.get("http://genome.ucsc.edu/cgi-bin/hgGateway?db=hg19")
        # the following link does not exist? old gateway relic of problem with selenium export?
        #driver.find_element_by_link_text("Human GRCh37/hg19").click()
        self.driver.implicitly_wait(1000)
        men_menu = WebDriverWait(driver,10).until(EC.visibility_of_element_located((
        By.XPATH, "//li[@id='myData']")))
        ActionChains(driver).move_to_element(men_menu).perform() 
        customTrackLink = WebDriverWait(driver,10).until(EC.visibility_of_element_located((
        By.XPATH, "//li[@id='myData']/ul/li[4]")))
        customTrackLink.click()

        #driver.find_element_by_id("customTracksMenuLink").click()
        driver.find_element_by_name("hgct_customText").clear()
        driver.find_element_by_name("hgct_customText").send_keys("http://hgwdev.cse.ucsc.edu/~brianlee/customTracks/examples.WITHOUT.FTPS.txt")
        driver.find_element_by_name("Submit").click()
        self.driver.implicitly_wait(1000)
        driver.find_element_by_name("submit").click()
        """driver.get("http://genome.ucsc.edu/cgi-bin/cartReset")
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
        driver.find_element_by_id("cartResetMenuLink").click()
        driver.find_element_by_id("blatMenuLink").click()
        Select(driver.find_element_by_css_selector("select[name=\"db\"]")).select_by_visible_text("Feb. 2009 (GRCh37/hg19)")
        driver.find_element_by_name("userSeq").clear()
        driver.find_element_by_name("userSeq").send_keys("AACAAAATCAAACTGTTTTTGTTGGACAATTCTCTGTTAAGCAGCTATAA\\nGCTGAATGACATTAACCGCAAAATGTAACCATAAAGGCCATAAACCCGAC\\nATTGTTAATTAATTAAATGCCTCATTAACTTTTTTAAAAACATGATTTAT\\nTCGATTCATAGAAAACTTAACCATCACTACTAAATGCACACACATGCGGT\\nTCCACATTGGCATCTTAGCCTAAGAACAGACAGGTTCAACTGTAACTGGC\\nCTTTCAGGTGGTCTATTACAGATCTGAAGACAGAGGGTGTTTCTAAACCT\\nCAAGAACCAGATTAACAGAAAACAAAGCTTGAGCAGCCTTTTTATTGCAT\\nGTGGTATCTTTTTAGCTAAGCAGAAGACAATGATAAAGAGGGGTTTTGGG\\nAAACCTCTCCCAAAGCTGTGCATTCATACCGTACCTTATCCTGTTAAGCA\\nAACTGTTCTTTTATTTTAAAGGGTTTACACTGCCACATCTGAATGGACTA")
        driver.find_element_by_name("Submit").click()
        driver.find_element_by_link_text("browser").click()
        driver.find_element_by_id("p_btn_hgUserPsl").click()
        driver.find_element_by_id("cartResetMenuLink").click()
        driver.find_element_by_id("ispMenuLink").click()
        driver.find_element_by_name("wp_f").clear()
        driver.find_element_by_name("wp_f").send_keys("AACAAAATCAAACTGTTTTTGTTGGACAATTCTCTGTTAAGCAGCTATAA")
        driver.find_element_by_name("wp_r").clear()
        driver.find_element_by_name("wp_r").send_keys("AACTGTTCTTTTATTTTAAAGGGTTTACACTGCCACATCTGAATGGACTA")
        driver.find_element_by_name("wp_flipReverse").click()
        driver.find_element_by_name("Submit").click()
        driver.find_element_by_link_text("chrX:40059679+40060178").click()
        driver.find_element_by_link_text("Genome Browser").click()
        driver.find_element_by_id("cartResetMenuLink").click()
        driver.find_element_by_link_text("Genome Browser").click()
        driver.find_element_by_id("convertMenuLink").click()
        driver.find_element_by_name("hglft_doConvert").click()
        driver.find_element_by_link_text("chr9:136127387-136156434").click()
        driver.find_element_by_css_selector("#tools3 > span").click()
        driver.find_element_by_id("liftOverMenuLink").click()
        driver.find_element_by_name("hglft_userData").clear()
        driver.find_element_by_name("hglft_userData").send_keys("chr21:33,031,597-33,041,570")
        driver.find_element_by_name("Submit").click()
        driver.find_element_by_link_text("View Conversions").click()
        """ 
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
    unittest.main()
