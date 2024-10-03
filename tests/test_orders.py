import allure

import data
from burger_api import UserApi as user_api, OrderApi as order_api
from helper import delete_data_field


class TestOrders:

    @allure.title("Проверка создания заказа")
    def test_create_order(self, generate_registration_data):
        user_data = generate_registration_data
        response = user_api.create_user(user_data)
        json_response = response.json()
        token = json_response['accessToken']
        login_data = delete_data_field(user_data, 'name')
        user_api.login_user(login_data)
        order_response = order_api.create_order(token, data.BurgerIngredientsData.BURGER_DATA)
        assert order_response.status_code == 200
        json_order_response = order_response.json()
        assert json_order_response["success"] is True
        user_api.delete_user(token)

    @allure.title("Проверка создания заказа без логина пользователя")
    def test_create_order_without_login(self):
        order_response = order_api.create_order(ingredients=data.BurgerIngredientsData.BURGER_DATA)
        assert order_response.status_code == 200
        json_order_response = order_response.json()
        assert json_order_response["success"] is True

    @allure.title("Проверка создания заказа без ингредиентов")
    def test_create_order_without_ingredients(self):
        order_response = order_api.create_order("")
        assert order_response.status_code == 400
        json_order_response = order_response.json()
        assert json_order_response["success"] is False

    @allure.title("Проверка создания заказа с неверными хэшами ингредиентов")
    def test_create_order_with_incorrect_ingredients(self):
        order_response = order_api.create_order(ingredients=data.BurgerIngredientsData.BURGER_INCORRECT_DATA)
        assert order_response.status_code == 500

    @allure.title("Проверка получения списка заказа пользователя")
    def test_get_user_orders(self, generate_registration_data):
        user_data = generate_registration_data
        response = user_api.create_user(user_data)
        json_response = response.json()
        token = json_response['accessToken']
        login_data = delete_data_field(user_data, 'name')
        user_api.login_user(login_data)
        order_api.create_order(token, data.BurgerIngredientsData.BURGER_DATA)
        orders_list = order_api.get_orders_list(token).json()

        assert data.BurgerIngredientsData.BURGER_DATA['ingredients'] == orders_list['orders'][0]['ingredients']
        user_api.delete_user(token)

    @allure.title("Проверка получения списка заказа пользователя")
    def test_get_user_orders(self, generate_registration_data):
        user_data = generate_registration_data
        response = user_api.create_user(user_data)
        json_response = response.json()
        token = json_response['accessToken']
        login_data = delete_data_field(user_data, 'name')
        user_api.login_user(login_data)
        order_api.create_order(token, data.BurgerIngredientsData.BURGER_DATA)
        orders_list = order_api.get_orders_list(token).json()

        assert data.BurgerIngredientsData.BURGER_DATA['ingredients'] == orders_list['orders'][0]['ingredients']
        user_api.delete_user(token)

    @allure.title("Проверка получения списка заказа пользователя без авторизации")
    def test_get_user_orders(self, generate_registration_data):
        user_data = generate_registration_data
        response = user_api.create_user(user_data)
        json_response = response.json()
        token = json_response['accessToken']
        login_data = delete_data_field(user_data, 'name')
        user_api.login_user(login_data)
        order_api.create_order(token, data.BurgerIngredientsData.BURGER_DATA)
        orders_list_response = order_api.get_orders_list()
        assert orders_list_response.status_code == 401
        assert orders_list_response.json() == data.BurgerApiData.UNAUTH_ERROR_MSG
        user_api.delete_user(token)
