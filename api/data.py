from datetime import datetime, timedelta

class Time:
    currentTimeDate = datetime.now() + timedelta(days=1)
    currentTime = currentTimeDate.strftime('%d')

class Credential:
    email = "khokhlova_14@mail.ru"
    lastName = "Alexov"
    address = "Kanoha, 142 apt."
    metroStation = 1
    phone = "+7 800 355 35 35"
    rentTime = 5
    deliveryDate = Time.currentTime
    comment  = "Saske, come back to Konoha"
    color_black = "BLACK"
    color_grey = "GREY"
    color_black_grey = "BLACK, GREY"
    color_0 = ""

class Response:
    code_400_login_courier = {'code': 400, 'message': 'Недостаточно данных для входа'}
    code_404_login_courier = {'code': 404, 'message': 'Учетная запись не найдена'}
    code_409_new_courier = {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}
    code_400_new_courier = {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}
