from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
#path
driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe')
#espera
driver.implicitly_wait(0.5)
#maximizar ventana
driver.maximize_window()
#ir a la URL
driver.get("http://sga.unasam.edu.pe/login")
#eliminar elementos con JavaScript
# driver.execute_script("""
#     var list = document.getElementsByName("usuario");
#     for(var i = list.length - 1; 0 <= i; i--)
#     if(list[i] && list[i].parentElement)
#     list[i].parentElement.removeChild(list[i]);
# """)


# element = driver.find_element(By.XPATH, "//select[@name='tipoUsuario']")
# driver.execute_script("arguments[0].click()", element)

# driver.execute_script('window.alert("worked!")')

driver.execute_script('swal("Gotcha!", "Pikachu was caught!", "success");')
sleep(5)
element = driver.find_element(By.XPATH, "//button[@class='confirm']")
driver.execute_script("arguments[0].click()", element)