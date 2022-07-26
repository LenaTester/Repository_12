def test_login_to_app(successful_login):
    '''positive test - correct name, correct password - 1'''
    successful_login_page = successful_login
    assert successful_login_page.title == 'LoveRead.ec - Бесплатная Онлайн Библиотека | Читать Книги Онлайн Бесплатно и без регистрации', \
        f'\nUser not logined\nActual title: {successful_login_page.title}, Expected: \'LoveRead.ec - Бесплатная Онлайн Библиотека | Читать Книги Онлайн Бесплатно и без регистрации\''

def test_login_wrong_login_to_app(non_successful_login_wrong_login):
    '''negative test - correct name, wrong password - 2'''
    wrong_creds_page = non_successful_login_wrong_login
    notification = wrong_creds_page.get_notification()
    assert notification == 'Возникла ошибка при вводе Пароля', \
        f'\nUser logined\nActual: {notification}\nExpected: "Возникла ошибка при вводе Пароля"'

def test_login_wrong_passwod_to_app(non_successful_login_wrong_password):
    '''negative test - wrong name, correct password - 3'''
    wrong_creds_page = non_successful_login_wrong_password
    notification = wrong_creds_page.get_notification()
    assert notification == 'Возникла ошибка при вводе Пароля', \
        f'\nUser logined\nActual: {notification}\nExpected: "Возникла ошибка при вводе Пароля"'

def test_click_page_a(get_home_page):
    '''check letter navigation - letter A- 4'''
    home_page = get_home_page
    user_page = home_page.click_page_a_button()
    assert user_page.title == 'Список авторов отсортированные по названию, первая буква - А | LoveRead.ec', \
        f'\nLetter navigation does not work\nActual title: {user_page.title}, Expected: \'Список авторов отсортированные по названию, первая буква - А | LoveRead.ec\''

def test_check_page(get_home_page):
    '''check page navigation - page 50 - 5'''
    home_page = get_home_page
    user_page = home_page.check_page_navigaion('50').click_submit_button()
    assert user_page.title == 'Архив книг | страница 50 | Бесплатная Онлайн Библиотека - LoveRead.ec', \
        f'\nPage navigation does not work\nActual title: {user_page.title}, Expected: \'Архив книг | страница 50 | Бесплатная Онлайн Библиотека - LoveRead.ec\''

def test_check_search(get_home_page):
    '''check search - 6'''
    home_page = get_home_page
    user_page = home_page.check_search('Альтшуллер').click_search_button()
    assert user_page.title == 'Поиск по слову - альтшуллер | LoveRead.ec - Бесплатная Электронная Библиотека', \
        f'\nSearch does not work\nActual title: {user_page.title}, Expected: \'Поиск по слову - альтшуллер | LoveRead.ec - Бесплатная Электронная Библиотека\''

