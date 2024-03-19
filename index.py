import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException

def navegar_enlaces(url, tiempo_espera_min=3, tiempo_espera_max=5):
    try:
        # Configura el navegador
        driver = webdriver.Firefox()
        driver.get(url)

        while True:
            # Esperar a que la página se cargue completamente
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

            # Obtener todos los enlaces de la página
            enlaces = driver.find_elements(By.TAG_NAME, 'a')
            # No toma como enlace el que dice "Salta al contenido principal"
            enlaces = [enlace for enlace in enlaces if enlace.is_displayed() and "Salta al contenido principal" not in enlace.text]

            if not enlaces:
                print("No se encontraron más enlaces en la página.")
                break

            # Escoger un enlace aleatorio de entre los disponibles para hacer clic
            enlace = random.choice(enlaces)
            print(f"Haciendo clic en el enlace: {enlace.text}")

            # Desplazar el enlace a la vista
            driver.execute_script("arguments[0].scrollIntoView();", enlace)

            # Esperar un momento para que la página se estabilice
            time.sleep(1)

            try:
                # Hacer clic en el enlace
                enlace.click()
            except ElementNotInteractableException:
                print("El enlace no es interactuable, pasando al siguiente.")

            # Tiempo de espera aleatorio entre clics, con aviso por terminal
            tiempo_espera = random.randint(tiempo_espera_min, tiempo_espera_max)
            print(f"Esperando {tiempo_espera} segundos antes del próximo clic.")

            # Esperar unos segundos antes de continuar
            time.sleep(tiempo_espera)

    except KeyboardInterrupt:
        print("El script ha sido detenido por el usuario.")

    finally:
        driver.quit()  # Cerrar el navegador al finalizar

if __name__ == "__main__":
    url = "" # Aquí va la URL a la que quieres acceder. Pon la del temario (la que tiene la ventana que se abre al hacer clic sobre el temario)
    tiempo_espera_min = 10  # Tiempo mínimo de espera en segundos entre clics
    tiempo_espera_max = 25  # Tiempo máximo de espera en segundos entre clics
    navegar_enlaces(url, tiempo_espera_min, tiempo_espera_max)