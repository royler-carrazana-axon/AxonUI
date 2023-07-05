import os
import shutil

# Ruta de la carpeta raíz de componentes Svelte
ruta_raiz = "./src/components/ui"

# Ruta de la carpeta "static" en tu proyecto Svelte
ruta_static = "./static"

# Recorrer las carpetas y subcarpetas
for ruta_carpeta, carpetas, archivos in os.walk(ruta_raiz):
    # Recorrer los archivos en cada carpeta
    for archivo in archivos:
        if archivo.endswith(".svelte"):
            # Leer el contenido del componente Svelte
            with open(os.path.join(ruta_carpeta, archivo), "r") as file:
                contenido = file.read()

            # Ruta de la carpeta en "static" donde se copiará el archivo HTML
            ruta_carpeta_static = os.path.relpath(ruta_carpeta, ruta_raiz)
            ruta_carpeta_static = os.path.join(ruta_static, ruta_carpeta_static)

            # Crear la carpeta en "static" si no existe
            os.makedirs(ruta_carpeta_static, exist_ok=True)

            # Crear nuevo archivo HTML en la carpeta "static" con el mismo nombre y extensión ".html"
            nuevo_archivo = os.path.splitext(archivo)[0] + ".html"
            nuevo_path = os.path.join(ruta_carpeta_static, nuevo_archivo)

            # Agregar el código dentro de la etiqueta <pre> en el nuevo archivo
            with open(nuevo_path, "w") as file:
                file.write(f"{contenido}")

 