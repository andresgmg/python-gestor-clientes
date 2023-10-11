# gestor clientes
 gestor de clientes el cual guarda toda la dat en un archivo llamado clientes.csv

### NOTA: ESTE GESTOR NO VALIDA AL 100% EL RUT CHILENO, PAA ELLO HABRIA QUE OCUPAR EL SIGUIENTE CODIGO:
```python
def validar_rut(rut):
    # Elimina puntos y guiones del RUT
    rut = rut.replace('.', '').replace('-', '')

    # Obtiene el número y el dígito verificador
    rut_numero = rut[:-1]
    digito_verificador = rut[-1].upper()

    # Verifica que el número tenga al menos un dígito
    if not rut_numero.isdigit():
        return False

    # Calcula el dígito verificador esperado
    suma = 0
    multiplicador = 2
    for d in reversed(rut_numero):
        suma += int(d) * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2

    resto = suma % 11
    digito_esperado = 11 - resto if resto != 1 else 0

    # Compara el dígito verificador ingresado con el esperado
    return digito_verificador == str(digito_esperado)

# Ejemplo de uso
rut = "12.345.678-9"
if validar_rut(rut):
    print(f"El RUT {rut} es válido.")
else:
    print(f"El RUT {rut} no es válido.")
```