import dns.resolver

def check_email_domain(email):
    domain = email.split('@')[-1]
    
    try:
        # Проверяем существование MX записей для домена
        answers = dns.resolver.resolve(domain, 'MX')
        
        if len(answers) > 0:
            return f"{email}: домен валиден"
        else:
            return f"{email}: MX-записи отсутствуют или некорректны"
    except dns.resolver.NXDOMAIN:
        return f"{email}: домен отсутствует"
    except Exception as e:
        return f"{email}: ошибка ({str(e)})"

if __name__ == "__main__":
    emails = input("Введите список email адресов через пробел:\n").split()
    
    for email in emails:
        print(check_email_domain(email))

      
# Инструкция по запуску:
# pip install dnspython
# python check_mx_records.py

# Пример вывода:
# test@example.com: домен валиден
# invalid@nonexistentdomain.ru: домен отсутствует
# info@testserver.io: MX-записи отсутствуют или некорректны
