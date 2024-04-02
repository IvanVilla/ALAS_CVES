# Vulnerability Checker for Amazon Linux

Este script descarga y filtra las vulnerabilidades de seguridad publicadas para las diferentes versiones de Amazon Linux en los últimos días definidos en la variable days_to_check. Utiliza los feeds RSS proporcionados por Amazon Web Services para obtener la información más reciente sobre las vulnerabilidades.

## Uso

Asegúrate de tener Python instalado en tu sistema. Luego, simplemente ejecuta el script `vulnerability_checker.py`. Asegúrate de tener instalados los módulos requeridos, puedes instalarlos ejecutando:

pip install requests

perl
Copy code

## Ejecución

```bash
python vulnerability_checker.py
```
El script generará un archivo Markdown (vulnerabilities_YYYY_MM_DD.md) con la lista de vulnerabilidades encontradas.

## Funcionamiento

El script realiza las siguientes operaciones:

* Descarga los feeds RSS de las fuentes proporcionadas por Amazon Web Services.
* Filtra las vulnerabilidades publicadas en los últimos 365 días.
* Genera un archivo Markdown con las vulnerabilidades encontradas, organizadas por versión de Amazon Linux.
Estructura del Archivo Markdown
* El archivo Markdown generado contendrá una lista de las vulnerabilidades encontradas para cada versión de Amazon Linux. * Cada sección estará encabezada por el nombre de la versión, seguido de una lista de las vulnerabilidades, incluyendo el título, enlace y fecha de publicación.

## Requisitos

* Python 3.x
* Módulos: requests, xml.etree.ElementTree

## Licencia

           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                   Version 2, December 2004
 
Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>

Everyone is permitted to copy and distribute verbatim or modified
copies of this license document, and changing it is allowed as long
as the name is changed.
 
           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
  TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

 0. You just DO WHAT THE FUCK YOU WANT TO.
 