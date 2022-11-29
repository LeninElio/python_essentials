from selenium import webdriver
#path
driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe')
#espera
driver.implicitly_wait(0.5)
#maximizar ventana
driver.maximize_window()
#ir a la URL
driver.get("http://sga.unasam.edu.pe/login")
#eliminar elementos con JavaScript
driver.execute_script("""
    var list = document.getElementsByName("usuario");
    for(var i = list.length - 1; 0 <= i; i--)
    if(list[i] && list[i].parentElement)
    list[i].parentElement.removeChild(list[i]);
""")