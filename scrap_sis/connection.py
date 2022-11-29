from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def conection():

    options = Options()
    options.add_argument("--disable-extensions")
    options.add_experimental_option("prefs", {"plugins.always_open_pdf_externally": True})
    driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe')

    url = "http://app.sis.gob.pe/SisConsultaEnLinea/Consulta/frmConsultaEnLinea.aspx"
    driver.get(url)

    driver.find_element(By.XPATH, "//select[@id='cboTipoBusqueda']/option[2]").click()
    driver.execute_script("""
        var list = document.getElementsByClassName("TituloEncabezado2");
        for(var i = list.length - 1; 0 <= i; i--)
        if(list[i] && list[i].parentElement)
        list[i].parentElement.removeChild(list[i]);
    """)
    return driver


