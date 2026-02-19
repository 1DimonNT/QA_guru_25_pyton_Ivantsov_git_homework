from datetime import datetime

# 1. Создаю словарь email
email = {
    "subject": "Quarterly Report",
    "from": "Alice.Cooper@Company.ru",
    "to": " bob_smith@Gmail.com ",
    "body": "Hello Bob,\n\tHere is the report.\n\tPlease review it.\n\nAlice"
}

# 2. Добавляю дату отправки
email["date"] = datetime.now().strftime("%Y-%m-%d")

# 3. Нормализую e-mail адреса
email["from"] = email["from"].strip().lower()
email["to"] = email["to"].strip().lower()

# 4. Логин и домен
login, domain = email["from"].split("@")

# 5. Сокращенный текст
email["short_body"] = email["body"][:10] + "..."

# 6. Списки доменов
personal_domains = {
            "gmail.com",
            "list.ru",
            "yahoo.com",
            "outlook.com",
            "hotmail.com",
            "icloud.com",
            "yandex.ru",
            "mail.ru",
            "list.ru",
            "bk.ru",
            "inbox.ru"
    }

corporate_domains = {
            "company.ru",
            "corporation.com",
            "university.edu",
            "organization.org",
            "company.ru",
            "business.net"
    }

# 7. Проверка пересечений (не должно быть общих элементов)
assert set(personal_domains).isdisjoint(set(corporate_domains))

# 8. Проверка «корпоративности»
is_corporate = domain in corporate_domains

# 9. Чистый текст
email["clean_body"] = email["body"].replace("\t", " ").replace("\n", " ")

# 10. Формируем текст письма
email["sent_text"] = f"""Кому: {email['to']}, от {email['from']}
Тема: {email['subject'].strip()}, дата {email['date']}
{email['clean_body']}"""


# 11. Количество страниц
pages = (len(email["sent_text"]) + 499) // 500

# 12. Проверка пустоты
is_subject_empty = not email["subject"].strip()
is_body_empty = not email["body"].strip()

# 13. «Маска» email
email["masked_from"] = login[:2] + "***@" + domain

# 14. Удаление из списка личных доменов
if "list.ru" in personal_domains:
    personal_domains.remove("list.ru")
if "bk.ru" in personal_domains:
    personal_domains.remove("bk.ru")

# Вывод результата
print(f"Маскированный адрес: {email['masked_from']}")
print(f"Количество страниц: {pages}")
