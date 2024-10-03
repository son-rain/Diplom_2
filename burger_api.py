import allure
import requests

from data import BurgerApiData


class UserApi:
    @staticmethod
    @allure.step("Создаём нового пользователя")
    def create_user(register_user_payload):
        reg_response = requests.post(BurgerApiData.CREATE_USER_POST_URL, register_user_payload)
        return reg_response

    @staticmethod
    @allure.step("Логинимся в системе")
    def login_user(login_user_payload):
        login_response = requests.post(BurgerApiData.LOGIN_USER_POST_URL, login_user_payload)
        return login_response

    @staticmethod
    @allure.step("Удаляем пользователя")
    def delete_user(token):
        headers = {'Authorization': token}
        response_delete = requests.delete(BurgerApiData.DELETE_USER_URL, headers=headers)
        return response_delete

    @staticmethod
    @allure.step("Меняем данные пользователя")
    def update_user_data(token, data):
        headers = {'Authorization': token}
        response_patch = requests.patch(BurgerApiData.DELETE_USER_URL, headers=headers, data=data)
        return response_patch


class OrderApi:
    @staticmethod
    def create_order(token="", ingredients=None):
        headers = {'Authorization': token}
        order_response = requests.post(BurgerApiData.ORDERS_URL, headers=headers if token else '', data=ingredients)
        return order_response

    @staticmethod
    def get_orders_list(token=""):
        headers = {'Authorization': token}
        order_list_response = requests.get(BurgerApiData.ORDERS_URL, headers=headers)
        return order_list_response

