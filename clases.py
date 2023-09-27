import requests

# Блок для обработки запроса! 
web_sites = [
    'https://demovet.obt-vlg.org/auth/users/login',
    'http://172.25.3.11/auth/users/login',
    'https://demovet2.it-albion.ru/auth/users/login',
    'https://vettest.obt-vlg.ru/',
]

for site in web_sites:
    try:
        response = requests.get(site)
        response.raise_for_status()  # Проверяем успешность запроса

        # Если запрос успешен, выводим статусный код
        print(f'Обратился к хосту {site}: Получил ответ {response.status_code}')
    except requests.exceptions.RequestException as e:
        # Обработка ошибки, когда невозможно достучаться до сайта
        print(f'ВНИМАНИЕ!!!!!!!{site}: Ошибка - {e}!!!!!!!!!!!!!')
