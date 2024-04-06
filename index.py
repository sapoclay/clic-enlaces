import tkinter as tk
from tkinter import simpledialog, messagebox
import re
import time
import random
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    ElementNotInteractableException,
    NoSuchElementException,
    StaleElementReferenceException,
    ElementClickInterceptedException,
    NoSuchWindowException,
    TimeoutException
)

def validar_url(url):
    # Patrón de expresión regular para validar una URL
    patron_url = re.compile(
        r'^(?:http|ftp)s?://'  # http:// o https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # Dominio...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...o dirección IP
        r'(?::\d+)?'  # Opcional: puerto
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(patron_url, url) is not None

def es_enlace_interno(enlace, dominio):
    parsed_enlace = urlparse(enlace)
    return parsed_enlace.netloc == dominio

def navegar_enlaces(url, tiempo_espera_min=3, tiempo_espera_max=5):
    try:
        # Configura el navegador
        driver = webdriver.Firefox()
        driver.get(url)

        # Extraer el dominio de la URL proporcionada por el usuario
        dominio = urlparse(url).netloc

        while True:
            # Esperar a que la página se cargue completamente
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

            while True:
                try:
                    # Obtener todos los enlaces de la página
                    enlaces = driver.find_elements(By.TAG_NAME, 'a')
                    # Saltar al contenido principal
                    enlaces = [enlace for enlace in enlaces if enlace.is_displayed() and "Saltar al contenido principal" not in enlace.text]
                    break
                except NoSuchElementException:
                    print("No se encontraron enlaces en la página.")
                    break
                except StaleElementReferenceException:
                    continue

           # if not enlaces:
            #    print("No se encontraron más enlaces en la página.")
             #   break

            # Filtrar solo los enlaces internos al dominio proporcionado por el usuario
            enlaces = [enlace for enlace in enlaces if es_enlace_interno(enlace.get_attribute('href'), dominio)]

            if not enlaces:
                print("No se encontraron enlaces internos en la página.")
                break

            # Escoger un enlace aleatorio de entre los disponibles para hacer clic
            enlace = random.choice(enlaces)
            print(f"Haciendo clic en el enlace: {enlace.text}")

            # Desplazar el enlace a la vista
            driver.execute_script("arguments[0].scrollIntoView();", enlace)
            # Desplazar un poco más para asegurarse de que el elemento sea completamente visible
            driver.execute_script("window.scrollBy(0, -100);")

            # Esperar un momento para que la página se estabilice
            time.sleep(1)

            try:
                enlace_clickeable = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//a[@href='{enlace.get_attribute('href')}']")))
                if enlace_clickeable.is_displayed():
                    enlace_clickeable.click()
                else:
                    print("El enlace no está visible en este momento.")
            except ElementNotInteractableException:
                print("El enlace no es interactuable en este momento.")
            except TimeoutException:
                print("El enlace no pudo ser encontrado o no es clickeable.")

            # Tiempo de espera aleatorio entre clics, con aviso por terminal
            tiempo_espera = random.randint(tiempo_espera_min, tiempo_espera_max)
            print(f"Esperando {tiempo_espera} segundos antes del próximo clic.")

            # Esperar unos segundos antes de continuar
            time.sleep(tiempo_espera)

    except KeyboardInterrupt:
        print("El script ha sido detenido por el usuario.")

    except NoSuchWindowException:
        print("La ventana del navegador ha sido cerrada. El script ha finalizado.")

    finally:
        driver.quit()  # Cerrar el navegador al finalizar

def obtener_datos():
    root = tk.Tk()
    root.withdraw() # Oculta la ventana principal de tkinter

    while True:
        url = simpledialog.askstring("URL de navegación", "Introduce la URL por la que navegar (http://nombredelaweb.tal):")
        if url is None:
            break
        if validar_url(url):
            break
        else:
            messagebox.showerror("Error", "La URL proporcionada no es válida.")

    if url is not None:
        while True:
            try:
                tiempo_min = int(simpledialog.askstring("Tiempo mínimo para saltar al siguiente enlace", "Introduce el tiempo mínimo de espera para el salto al siguiente enlace (en segundos):"))
                if tiempo_min is None:
                    break
                if tiempo_min >= 0:
                    break
                else:
                    messagebox.showerror("Error", "El tiempo mínimo debe ser un número entero mayor o igual a cero.")
            except ValueError:
                messagebox.showerror("Error", "El tiempo mínimo debe ser un número entero.")

    if url is not None and tiempo_min is not None:
        while True:
            try:
                tiempo_max = int(simpledialog.askstring("Tiempo máximo para saltar al siguiente enlace", "Introduce el tiempo máximo de espera para el salto al siguiente enlace (en segundos):"))
                if tiempo_max is None:
                    break
                if tiempo_max >= tiempo_min:
                    break
                else:
                    messagebox.showerror("Error", "El tiempo máximo debe ser un número entero mayor o igual al tiempo mínimo.")
            except ValueError:
                messagebox.showerror("Error", "El tiempo máximo debe ser un número entero.")

    if url is not None and tiempo_min is not None and tiempo_max is not None:
        navegar_enlaces(url, tiempo_min, tiempo_max)

if __name__ == "__main__":
    obtener_datos()