"""Calculadora segura: práctica de manejo y propagación de excepciones."""
import math

historial = []


def obtener_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada inválida. Escribe un número, por ejemplo 5 o 2.5.")


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero.")
    return a / b


def promedio(numeros):
    if not numeros:
        raise ValueError("No se puede calcular el promedio de una lista vacía.")
    return sum(numeros) / len(numeros)


def raiz_cuadrada(numero):
    if numero < 0:
        raise ValueError("No existe raíz cuadrada real de un número negativo.")
    return math.sqrt(numero)


def convertir_texto(texto):
    return float(texto)


OPERACIONES = {
    "sumar": sumar,
    "restar": restar,
    "multiplicar": multiplicar,
    "dividir": dividir,
    "promedio": promedio,
    "raiz_cuadrada": raiz_cuadrada,
    "convertir_texto": convertir_texto,
}


def calcular(operacion, *args):
    registro = {"operacion": operacion, "argumentos": args, "resultado": None}
    try:
        if operacion not in OPERACIONES:
            raise ValueError("Operación desconocida.")
        resultado = OPERACIONES[operacion](*args)
    except ZeroDivisionError as error:
        registro["resultado"] = f"Error: {error}"
        print(registro["resultado"])
        return None
    except ValueError as error:
        registro["resultado"] = f"Error: {error}"
        print(registro["resultado"])
        return None
    else:
        registro["resultado"] = resultado
        print(f"Resultado: {resultado:g}")
        return resultado
    finally:
        # Se ejecuta incluso si hubo error o se usó return.
        historial.append(registro)


def generar_error():
    print("1. Función interna: voy a lanzar ValueError.")
    raise ValueError("Error intencional para demostrar la propagación.")


def funcion_intermedia():
    print("2. Función intermedia: llamo a la interna sin capturar el error.")
    generar_error()


def propagar_error():
    print("3. Función superior: comienza la demostración.")
    try:
        funcion_intermedia()
    except ValueError as error:
        print(f"4. La función superior capturó el error: {error}")
        historial.append({
            "operacion": "propagación",
            "argumentos": (),
            "resultado": f"Error controlado: {error}",
        })


def leer_lista():
    while True:
        texto = input("Números separados por comas (Enter = lista vacía): ").strip()
        if not texto:
            return []
        try:
            partes = [p.strip() for p in texto.split(",")]
            return [float(p) for p in partes]
        except ValueError:
            print("Lista inválida. Usa números separados por comas, por ejemplo 3, 4, 5.")


def ver_historial():
    print("\n--- HISTORIAL ---")
    if not historial:
        print("Todavía no hay operaciones.")
    for numero, item in enumerate(historial, 1):
        print(f"{numero}. {item['operacion']} {item['argumentos']} -> {item['resultado']}")


def menu():
    opciones = {
        "1": "sumar", "2": "restar", "3": "multiplicar",
        "4": "dividir", "5": "promedio", "6": "raiz_cuadrada",
    }
    while True:
        print("\n" + "=" * 40)
        print("  CALCULADORA SEGURA")
        print("=" * 40)
        print("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir")
        print("5. Calcular promedio\n6. Raíz cuadrada")
        print("7. Probar propagación de excepciones")
        print("8. Ver historial\n9. Salir")
        print("=" * 40)
        opcion = input("Seleccione una opción: ").strip()
        if opcion in ("1", "2", "3", "4"):
            a = obtener_numero("Primer número: ")
            b = obtener_numero("Segundo número: ")
            calcular(opciones[opcion], a, b)
        elif opcion == "5":
            calcular("promedio", leer_lista())
        elif opcion == "6":
            calcular("raiz_cuadrada", obtener_numero("Número: "))
        elif opcion == "7":
            propagar_error()
        elif opcion == "8":
            ver_historial()
        elif opcion == "9":
            print("Gracias por usar la calculadora.")
            break
        else:
            print("Opción no válida. Elige un número del 1 al 9.")


if __name__ == "__main__":
    menu()
