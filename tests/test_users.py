import allure
import pytest

import data
from burger_api import UserApi as user_api
from helper import delete_data_field


class TestCreateUser:
    @allure.title("Проверка регистрации пользователя")
    def test_create_user(self, generate_registration_data):
        user_data = generate_registration_data
        response = user_api.create_user(user_data)
        json_response = response.json()
        token = json_response['accessToken']
        user_data.pop('password')
        assert json_response['user'] == user_data
        assert response.status_code == 200
        assert user_api.delete_user(token).status_code == 202

    @allure.title("Проверка регистрации пользователя с ранее использованными данными")
    def test_create_user_with_existed_data(self, generate_registration_data):
        user_data = generate_registration_data
        response = user_api.create_user(user_data)
        response2 = user_api.create_user(user_data)
        json_response = response.json()
        token = json_response['accessToken']
        assert response2.status_code == 403
        json_response2 = response2.json()
        assert json_response2 == data.BurgerApiData.USER_EXIST_DATA_MSG
        assert user_api.delete_user(token).status_code == 202

    @allure.title("Проверка регистрации пользователя с пустыми данными")
    def test_create_user_with_empty_data(self):
        response = user_api.create_user(data.BurgerApiData.EMPTY_USER_DATA)
        json_response = response.json()
        assert json_response == data.BurgerApiData.WRONG_USER_DATA_MSG
        assert response.status_code == 403


class TestLoginUser:
    @allure.title("Проверка авторизации пользователя")
    def test_login_user_with_correct_data(self, generate_registration_data):
        user_data = generate_registration_data
        response = user_api.create_user(user_data)
        json_response = response.json()
        token = json_response['accessToken']
        login_data = delete_data_field(user_data,'name')
        login_response = user_api.login_user(login_data)
        json_login_response = login_response.json()
        expected_user_data = delete_data_field(user_data,'password')
        assert json_login_response['user'] == expected_user_data
        assert login_response.status_code == 200
        assert user_api.delete_user(token).status_code == 202

    @allure.title("Проверка авторизации пользователя с неверными данными")
    def test_login_user_with_wrong_data(self, generate_registration_data):
        user_data = generate_registration_data
        login_data = delete_data_field(user_data,'name')
        login_response = user_api.login_user(login_data)
        json_login_response = login_response.json()
        assert json_login_response == data.BurgerApiData.WRONG_LOGIN_USER_MSG
        assert login_response.status_code == 401


class TestUpdateUserData:
    @allure.title("Проверка обновления данных пользователя")
    @pytest.mark.parametrize('patch_data', data.BurgerApiData.PATCH_DATA)
    def test_update_user_data_with_auth(self, generate_registration_data, patch_data):
        user_data = generate_registration_data
        response = user_api.create_user(user_data)
        json_response = response.json()
        token = json_response['accessToken']
        patch_response = user_api.update_user_data(token, patch_data)
        assert patch_response.status_code == 200
        assert user_api.delete_user(token).status_code == 202

    @allure.title("Проверка обновления данных пользователя без авторизации")
    @pytest.mark.parametrize('patch_data', data.BurgerApiData.PATCH_DATA)
    def test_update_user_data_without_auth(self, patch_data):
        token = ""
        patch_response = user_api.update_user_data(token, patch_data)
        json_response = patch_response.json()
        assert json_response == data.BurgerApiData.UNAUTH_ERROR_MSG
        assert patch_response.status_code == 401
