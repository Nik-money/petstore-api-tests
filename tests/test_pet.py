import requests

BASE_URL = 'https://petstore.swagger.io/v2'

def test_find_pet_by_id():
    # Подготовка
    pet_id = 1
    expected_name = 'doggie'
    expected_status = 'available'
    required_fields = ['id', 'name', 'status', 'category']

    # Действие
    url = f'{BASE_URL}/pet/{pet_id}'
    print(f"Запрашиваю URL: {url}")

    response = requests.get(url)
    assert response.status_code == 200, f'Ожидался 200, получен: {response.status_code}'

    pet_data = response.json()

    # Проверки
    # 1. Наличие всех обязательных полей
    missing_fields = set(required_fields) - set(pet_data.keys())
    assert not missing_fields, f"Отсутствуют поля: {missing_fields}"

    # 2. Проверка значений
    assert pet_data ['id'] == pet_id
    assert pet_data['name'] == expected_name
    assert pet_data['status'] == expected_status

    # Отчет
    print(f'Найден питомец: {pet_data["name"]} ID: {pet_data["id"]} Status: {pet_data["status"]}')
    print((f'Все обязательные поля присутствуют: {required_fields}'))
