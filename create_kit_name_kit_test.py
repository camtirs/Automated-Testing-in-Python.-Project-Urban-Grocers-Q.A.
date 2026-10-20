import sender_stand_request

def get_new_user_token():
    response = sender_stand_request.post_new_user()
    return response.json()["authToken"]

def get_kit_body(name):
    # Crear el diccionario con el cuerpo de la solicitud
    current_body = {"name": name}
    return current_body

def positive_assert(name):
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())

    # Comprueba si el código de estado es 201
    assert response.status_code == 201
    # Comprueba que el campo "name" coincide
    assert response.json()["name"] == kit_body["name"]

def negative_assert(name):
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())

    expected_response = {
       "code": 400,
       "message": "El nombre debe contener sólo letras latino, un espacio y un guión. De 2 a 15 caracteres"
   }

    # Agrega esta línea para ver qué código estás recibiendo
    print(f"Código de estado recibido: {response.status_code}")
    print(f"Respuesta completa: {response.json()}")

    # Comprueba si el código de estado es 201
    assert response.status_code == 400
    # Comprueba que el campo "name" coincide
    assert response.json() == expected_response



# Prueba 1
def test_kit_name_with_1_character():
    positive_assert("a")
try:
    test_kit_name_with_1_character()
    print("✅ Prueba 1 pasó")
except AssertionError:
    print("❌ Prueba 1 falló")

# Prueba 2
def test_kit_name_with_511_characters():
    positive_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcd\
                    abcdabcdabcdabcdabcdabcdabcdabcdabcd\
                    abcdabcdabcdabcdabcdabcdabcdabcdabcd\
                    abcdabcdabcdabcdabcdabcdabcdabcdabcd\
                    abcdabcdabcdabcdabcdabcdabcdabcdabcd\
                    abcdabcdabcdabcdabcdabcdabcdabcdabcda\
                    bcdabcdabcdabcdabcdabcdabcdabcdabcdab\
                    cdAbcdabcdabcdabcdabcdabcdabcdabcdab\
                    cdabcdabcdabcdabcdabcdabcdabcdabcdab\
                    cdabcdabcdabcdabcdabcdabcdabcdabcdabc\
                    dabcdabcdabcdabcdabcdabcdabcdabcdabcd\
                    abcdabcdabcdabcdabcdabcdabcdabcdabcd\
                    abcdabcdabcdabcdabcdabcdabcdabcdabcdab\
                    cdabcdabcdabcdabcdabcdabcdabcdabcdabC")
try:
    test_kit_name_with_511_characters()
    print("✅ Prueba 2 pasó")
except AssertionError:
    print("❌ Prueba 2 falló")

# Prueba 3
def test_kit_name_less_than_1_character():
    negative_assert("")
try:
    test_kit_name_less_than_1_character()
    print("✅ Prueba 3 pasó")
except AssertionError:
    print("❌ Prueba 3 falló")

# Prueba 4
def test_kit_name_with_512_characters():
    negative_assert("Abcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcD")
try:
    test_kit_name_with_512_characters()
    print("✅ Prueba 4 pasó")
except AssertionError:
    print("❌ Prueba 4 falló")

# Prueba 5
def test_kit_name_with_special_characters():
    positive_assert("#%@/\\,""\u2116")

try:
    test_kit_name_with_special_characters()
    print("✅ Prueba 5 pasó")
except AssertionError:
    print("❌ Prueba 5 falló")

# Prueba 6
def test_kit_name_with_spaces():
    positive_assert("A Aaa")

try:
    test_kit_name_with_spaces()
    print("✅ Prueba 6 pasó")
except AssertionError:
    print("❌ Prueba 6 falló")

# Prueba 7
def test_kit_name_with_numbers_as_strings():
    positive_assert("123")

try:
    test_kit_name_with_numbers_as_strings()
    print("✅ Prueba 7 pasó")
except AssertionError:
    print("❌ Prueba 7 falló")

# Prueba 8
def test_kit_without_parameters():
    token = get_new_user_token()
    current_body = {}
    expected_response = {
       "code": 400,
       "message": "No se han aprobado todos los parámetros requeridos"
   }
    response = sender_stand_request.post_new_client_kit(current_body, token)
    # Agrega esta línea para ver qué código estás recibiendo
    print(f"Código de estado recibido: {response.status_code}")
    print(f"Respuesta completa: {response.json()}")

    # Comprueba si el código de estado es 201
    assert response.status_code == 400
    # Comprueba que el campo "name" coincide
    assert response.json() == expected_response

try:
    test_kit_without_parameters()
    print("✅ Prueba 8 pasó")
except AssertionError:
    print("❌ Prueba 8 falló")

# Prueba 9
def test_kit_name_with_numbers_as_a_parameter():
    negative_assert(123)

try:
    test_kit_name_with_numbers_as_a_parameter()
    print("✅ Prueba 9 pasó")
except AssertionError:
    print("❌ Prueba 9 falló")
