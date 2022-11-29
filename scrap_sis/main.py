from connection import conection
from selenium.webdriver.common.by import By

driver = conection()

def ingreso_datos(ap = '', am = '', pn = '', sn = ''):
    driver.find_element(By.NAME, "txtApePaterno").send_keys(ap)
    driver.find_element(By.NAME, "txtApeMaterno").send_keys(am)
    driver.find_element(By.NAME, "txtPriNombre").send_keys(pn)
    driver.find_element(By.NAME, "txtSegNombre").send_keys(sn)
    driver.find_element(By.NAME, "btnConsultar").click()

ingreso_datos('moreno', 'vega')

# nombres = []
# for i in range(1,10):
#     col = driver.find_elements(by = By.XPATH, value = f"//tr[@class='c_texto_02']/td[{i}]")
#     nombres.append(col)
# nombres = driver.find_elements(by = By.XPATH, value = f"//tr[@class='c_texto_02']/td[2]")
# nombres = [i.text for i in nombres]

# print(nombres)

valor = "/html/body/form/div[3]/table/tbody/tr[4]/td/table/tbody/tr[2]/td[2]/table/tbody/tr/td/div[1]/table/tbody/tr[33]/td/table/tbody/tr/td[12]/a"

ultimo = driver.find_elements(By.XPATH, '')
ultimo.click()
