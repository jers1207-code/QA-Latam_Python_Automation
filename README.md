# QA-Latam_Python_Automation
Proyecto: Prueba de la interfaz de usuario con Selenium WebDriver — Parte 1 (solo Python)
Estilo de código

El código sigue las siguientes convenciones de estilo:

Los nombres de las variables se escriben en snake_case y son descriptivos de su propósito.

Se utilizan comentarios para explicar los bloques de código importantes.

El código está organizado de forma modular, reutilizando bloques o importando funciones cuando sea necesario.

Se sigue una convención de nombres para los títulos de prueba que comienzan con test_ y describen claramente el escenario que se está verificando.

Se agregan comentarios a los bloques relevantes de código para mejorar la comprensión y el mantenimiento.

Se usa UPPER_CASE para variables y constantes globales.

Extras (opcional)

Aplica el principio DRY (“Don’t Repeat Yourself” o “No te repitas”) reutilizando variables y funciones en diferentes partes del código.

Evita imprimir logs innecesarios en la consola.

No utilices funciones de espera innecesarias que hagan que la prueba tarde más de lo necesario.

-------------------------------------------------------------------

Pasos a considerar:

Preparar el repositorio: 

1) El primer paso es enlazar tu cuenta de GitHub a TripleTen. Para ello, haz clic en el botón "Enlazar la cuenta de GitHub" en el widget en la parte superior de esta página. Esto te llevará a una nueva pestaña del navegador donde se te pedirá que confirmes que deseas enlazar tu cuenta de GitHub. Si aún no has iniciado sesión en GitHub, se te pedirá que introduzcas tu nombre de usuario y contraseña. Al confirmarlo, tu perfil de TripleTen se conectará a tu perfil de GitHub a través de la API segura de GitHub. Esto te permitirá enviar tus proyectos automáticamente con tan solo hacer clic en un botón, directamente dentro de la plataforma de TripleTen.
Una vez que vincules tu cuenta de TripleTen con GitHub, se creará automáticamente un repositorio llamado:

	https://github.com/tripleten-latam/QA-Latam_Python_Automation

2) Actualiza pip e instala las dependencias:

Windows

python -m pip install --upgrade pip
pip install -r requirements.txt

MacOS

python3 -m pip install --upgrade pip
pip install -r requirements.txt


3) No olvidar comprobar que todo está bien con el siguiente comando: 

pytest main.py -s
