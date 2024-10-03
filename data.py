class BurgerApiData:
    BURGER_MAIN_URL = "https://stellarburgers.nomoreparties.site/api"
    CREATE_USER_POST_URL = f'{BURGER_MAIN_URL}/auth/register'
    LOGIN_USER_POST_URL = f'{BURGER_MAIN_URL}/auth/login'
    UPDATE_USER_DATA_PATCH_URL = f'{BURGER_MAIN_URL}/auth/user'
    DELETE_USER_URL = f'{BURGER_MAIN_URL}/auth/user'
    ORDERS_URL = f'{BURGER_MAIN_URL}/orders'

    USER_EXIST_DATA_MSG = {
        "success": False,
        "message": "User already exists"
    }

    WRONG_USER_DATA_MSG = {
        "success": False,
        "message": "Email, password and name are required fields"
    }

    WRONG_LOGIN_USER_MSG = {
        "success": False,
        "message": "email or password are incorrect"
    }

    EMPTY_USER_DATA = {
        "email": '',
        "password": '',
        "name": ''
    }

    PATCH_DATA = [{"email": 'rtrtrt@ya.ru'},
                  {"password": 'wefefefefefefe'},
                  {"name": 'sdvfsghgfddfgrd'}]

    UNAUTH_ERROR_MSG = {
        "success": False,
        "message": "You should be authorised"
    }


class BurgerIngredientsData:
    BURGER_DATA = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa72", "61c0c5a71d1f82001bdaaa70",
                            "61c0c5a71d1f82001bdaaa71", "61c0c5a71d1f82001bdaaa6d"]}
    BURGER_INCORRECT_DATA = {"ingredients": ["61c0c5a712001bdaaa6d", "61c0c5a7133332001bdaaa72", "61c0c5a71d1f82001bdaaa70",
                            "61c01bdaaa71", "61c0c5a01bdaaa6d"]}
