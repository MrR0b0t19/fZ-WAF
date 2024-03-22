# -*- coding: utf-8 -*-
"""
Created 
fuera de la orbita
@author: Fantasma
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Configurar el controlador del navegador
driver = webdriver.Chrome()

# Definir el script para capturar alertas
alert_script = """
window.alert_trigger = false;
window.alert = function() {
    window.alert_trigger = true;
};
window.confirm = window.alert;
window.prompt = window.alert;
"""

# Definir el script para activar eventos en los elementos de la página
event_script = """
var ids = ["list", "of", "element", "IDs"];  // Reemplazar con los IDs reales
for (var i = 0; i < ids.length; i++) {
    var element = document.getElementById(ids[i]);
    if(!element) continue;
    var events = ['click', 'mouseover', 'mousedown', 'mouseup', 'mousemove', 'mouseout', 'mouseenter', 'mouseleave', 'dblclick', 'contextmenu', 'wheel', 'select', 'pointerdown', 'pointerup', 'pointermove', 'pointerover', 'pointerout', 'pointerenter', 'pointerleave', 'gotpointercapture', 'lostpointercapture'];
    try {
        for (var j = 0; j < events.length; j++) {
            var event = new MouseEvent(events[j], {bubbles: true});
            element.dispatchEvent(event);
        }
        element.focus();
        element.blur();
        element.dispatchEvent(new KeyboardEvent('keydown', {ctrlKey: true, altKey: true, key: 'x'}));
    } catch (e) {}
}
"""
##falta el fzzz
# URL de la aplicación web para probar
url = input("Ingrese la URL de la aplicación web para realizar el fuzzing: ")

try:
    # Abrir la URL en el navegador
    driver.get(url)

    # Ejecutar el script para capturar alertas
    driver.execute_script(alert_script)

    # Ejecutar el script para activar eventos en los elementos de la página
    driver.execute_script(event_script)

    

    # Verificar si se desencadenó una alerta
    while not driver.execute_script("return window.alert_trigger"):
        driver.execute_script(event_script)

finally:
    # Cerrar el navegador al finalizar
    driver.quit()
