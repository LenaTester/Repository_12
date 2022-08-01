def test_password_change(new_pass):
    '''check change of password - 7'''
    user_page = new_pass
    notification = user_page.get_notification()
    assert notification == 'Смена пароля прошла успешно. Напоминаем, что пароль должен оставаться секретным.', \
        f'\nPassword was not changed\nActual: {notification}\nExpected: "Смена пароля прошла успешно. Напоминаем, что пароль должен оставаться секретным."'

def test_email_change(new_email):
    '''check change of email - new correct email- 8'''
    user_page = new_email
    notification = user_page.get_notification()
    assert notification == 'На новый e-mail адрес было отправлено письмо. Зайдите в свою электронную ' \
                           'почту. Откройте полученное письмо и для полной смены e-mail адреса перейдите ' \
                           'по ссылке.', \
        f'\nEmail was not changed\nActual: {notification}\nExpected: "На новый e-mail адрес было отправлено письмо. Зайдите в свою электронную ' \
        'почту. Откройте полученное письмо и для полной смены e-mail адреса перейдите ' \
        'по ссылке.'""

def test_user_group(successful_login_go_to_profile):
    '''check, that user group is 'Пользователь' - 9'''
    profile_page = successful_login_go_to_profile
    notification = profile_page.get_notification_group()
    assert notification == 'Пользователь', \
        f'\nUser group is not Пользоватль\nActual: {notification}\nExpected: "Пользователь"'

def test_user_comments(successful_login_go_to_profile):
    '''check, that user does not have comments - 10'''
    profile_page = successful_login_go_to_profile
    notification = profile_page.get_notification_comments()
    print(notification)
    assert notification == '0', \
        f'\nUser have comments\nActual: {notification}\nExpected: ""'


