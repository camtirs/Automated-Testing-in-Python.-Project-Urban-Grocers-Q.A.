# Sprint 8 — Introducción a las pruebas automatizadas de Urban Grocers

## Descripción del proyecto

Este proyecto tiene como objetivo desarrollar y ejecutar pruebas automatizadas para validar el funcionamiento de la API de Urban Grocers, específicamente el proceso de creación de kits de productos y las reglas de validación del campo `name`.

La automatización se basa en una lista de comprobación que contempla nueve escenarios de prueba, diseñados para verificar el comportamiento del sistema ante entradas válidas e inválidas. Se evalúan los límites de longitud del nombre, los campos vacíos, los caracteres especiales, los espacios, los valores numéricos representados como texto, la ausencia del parámetro obligatorio y el envío de tipos de datos incorrectos.

## Objetivos

- Automatizar los nueve casos de prueba definidos en los requisitos del proyecto.
- Validar los códigos de respuesta HTTP y la correspondencia entre los datos enviados y los recibidos.
- Verificar los límites de aceptación del campo `name`.
- Implementar funciones reutilizables para el envío de solicitudes HTTP y la gestión de la autenticación.
- Organizar el código en módulos independientes para facilitar su mantenimiento, lectura y reutilización.
- Utilizar Pytest para ejecutar las pruebas y analizar los resultados.
- Gestionar el código fuente mediante Git y GitHub, siguiendo un flujo de trabajo ordenado y documentado.

## Tecnologías y herramientas

- **Python:** lenguaje utilizado para desarrollar las pruebas automatizadas.
- **Pytest:** framework para organizar y ejecutar los casos de prueba.
- **Requests:** biblioteca para enviar solicitudes HTTP a la API.
- **Git:** sistema de control de versiones.
- **GitHub:** plataforma para alojar y entregar el repositorio.
- **Urban Grocers API:** servicio sometido a pruebas.

## Estructura del proyecto

- `configuration.py`: centraliza la URL del servidor y las rutas de los endpoints.
- `data.py`: contiene los datos de prueba y los cuerpos de las solicitudes.
- `sender_stand_request.py`: implementa las funciones para crear usuarios, obtener el token de autenticación y enviar solicitudes de creación de kits.
- `create_kit_name_kit_test.py`: contiene los nueve casos de prueba automatizados para el campo `name`.
- `README.md`: documenta el propósito del proyecto, sus requisitos y los pasos para ejecutar las pruebas.
- `.gitignore`: excluye archivos temporales, cachés y otros elementos que no deben incluirse en el control de versiones.

## Criterios de validación

Las pruebas positivas verifican que la API responda con el código HTTP `201` y que el nombre devuelto coincida con el enviado en la solicitud. Las pruebas negativas comprueban que las entradas no válidas generen el código HTTP `400`, de acuerdo con los requisitos establecidos.

## Ejecución

Una vez configurada la URL vigente del servidor de Urban Grocers e instaladas las dependencias necesarias, las pruebas se ejecutan mediante:

`pytest -v create_kit_name_kit_test.py`

Los resultados permiten identificar comportamientos conformes y posibles discrepancias entre la respuesta de la API y los resultados esperados.

## Resultado esperado

Disponer de una suite de pruebas automatizadas organizada, reutilizable y documentada que permita evaluar las reglas de validación del campo `name` durante la creación de kits de productos, facilitando la detección de errores y contribuyendo a la calidad y confiabilidad del servicio.

**Nota:** la finalización y aprobación del proyecto dependen de la ejecución satisfactoria de las pruebas contra el servidor asignado y de la entrega del repositorio conforme a los requisitos de TripleTen.
