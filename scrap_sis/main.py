from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# def conection():

options = Options()
options.add_argument("--disable-extensions")
options.add_experimental_option("prefs", {"plugins.always_open_pdf_externally": True})
# odriver = webdriver.Chrome(ptions=options)
driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe')

url = "http://sga.unasam.edu.pe/login"
driver.get(url)

# driver.find_element(By.XPATH, "//select[@id='cboTipoBusqueda']/option[2]").click()
# driver.find_element(By.NAME, "txtApePaterno").send_keys("apellido_paterno")
# driver.find_element(By.NAME, "txtApeMaterno").send_keys("apellido_materno")
elemento = driver.find_element(By.NAME, "usuario")
# driver.find_element(By.NAME, "txtPriNombre").send_keys("primer_nombre")
# driver.find_element(By.NAME, "txtSegNombre").send_keys("segundo_nombre")
action = ActionChains(driver)
# elemento = driver.find_element(By.XPATH, "//div[@class='TituloEncabezado2']")
action.context_click(elemento).perform()
action.key_down(2)
# ActionChains(driver).move_to_element(elemento).click(elemento).perform()

# driver.find_element(By.XPATH, "//button").click()
# return driver, url
# return driver

# conection()