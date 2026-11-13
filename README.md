# Calculadora Segura

Actividad 1 de la Unidad 5: manejo de excepciones en Python.

## ¿Qué hace?
- Suma, resta, multiplica y divide.
- Calcula promedios y raíces cuadradas.
- Convierte texto a número mediante la función `convertir_texto`.
- Evita que los errores de entrada cierren el programa.
- Registra resultados y errores en un historial.
- Demuestra cómo un `ValueError` se propaga entre funciones.

## Requisitos
Python 3.9 o superior. No se necesitan librerías externas.

## Cómo ejecutar
```bash
python calculadora_segura.py
```

## Pruebas
- Opción 4: ingresar 10 y 0 para comprobar división por cero.
- Opción 1: ingresar `abc` para comprobar la validación de números.
- Opción 6: ingresar -9 para comprobar raíz negativa.
- Opción 5: presionar Enter sin números para comprobar promedio vacío.
- Opción 7: observar la propagación de `ValueError`.
- Opción 8: consultar el historial de operaciones.

La función `convertir_texto` está disponible para probarse desde Python:
```python
from calculadora_segura import calcular
calcular("convertir_texto", "hola")
```

## Publicación
Subir `calculadora_segura.py` y `README.md` a un repositorio público de GitHub. Después colocar el enlace real en el PDF.
