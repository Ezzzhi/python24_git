# Задача "Рассылка писем"
def send_mail(message, recipient, *, sender = "university.help@gmail.com"):
    email_ends = ('.com', '.ru', '.net', 'gmail.com')
    if '@' not in (recipient or sender) or not (recipient.lower().endswith(email_ends)
                                                or recipient.lower().endswith(email_ends)):
        print(f'Невозможно отправить письмо с адреса <{sender}> на адрес <{recipient}>')
    # check emails equal
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <{sender}> на адрес <{recipient}>.")
    else:
        print(f"Письмо успешно отправлено с адреса <{sender}> на адрес <{recipient}>.")


send_mail('Congratulations on starting your studies!', 'riuguru.ru')
send_mail('The exams are coming!', 'university.help@gmail.com')
send_mail('Your homework checked', "university.help@gmail.com", sender='homework@tst.net')
send_mail('You have successfully completed the course!', 'riu@guru.com')