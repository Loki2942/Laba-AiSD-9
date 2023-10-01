import os
from tkinter import *
from tkinter import messagebox


def dismiss(win):
    win.grab_release()
    win.destroy()



def init_file():  # Инициализация файла, если этого не сделать програма вылетит c ошибкой, что файла нет
    """Создает файл пользователей"""
    if not os.path.exists('users.txt'):
        with open('users.txt', 'w'):
            pass


def add_user(login: str, password: str) -> bool:
    with open('users.txt', 'r') as f:
        users = f.read().splitlines()  # Считываем всех пользователей из файла
    for user in users:
        args = user.split(':')
        if login == args[0]:  # Если логин уже есть, парль не проверяем
            return False

    with open('users.txt', 'a') as f:
        f.write(f'{login}:{password}\n')  # Добавляем нового пользователя
    return True


def get_user(login: str, password: str) -> bool:
    with open('users.txt', 'r') as f:
        users = f.read().splitlines()  # Считываем всех пользователей из файла

    for user in users:
        args = user.split(':')
        if login == args[0] and password == args[1]:  # Если пользователь с таким логином и паролем существует
            return True
    return False



def authorization():
    win = Toplevel(window)
    win.title('Авторизация')
    win.geometry('450x230+360+210')
    win.protocol("VM_DELETE_WINDOW", lambda: dismiss(win))
    win.grab_set()

    def clicked():
        # получаем имя пользователя и пароль
        login  = username_entry.get()
        password = password_entry.get()

        if len(login) == 0 or len(password) == 0:
            messagebox.showwarning(title='Ошибка', message='Поле заполнения пусто')
        else:
            result = get_user(login, password)

            if result:
                print('Вы вошли в систему')
                messagebox.showinfo('Авторизация', 'Авторизация прошла успешно.\nВы вошли в систему.')
                win.after(300, lambda: (win.destroy(), win.grab_release()))

                gl_okno = Tk()  # создаём окно
                gl_okno.title('Поле')  # заголовок окна
                doska = Canvas(gl_okno, width=800, height=800, bg='#FFFFFF')
                doska.pack()

                def vivod():  # рисуем игровое поле
                    k = 100
                    x = 0

                    while x < 8 * k:  # рисуем доску
                        y = 1 * k
                        while y < 8 * k:
                            doska.create_rectangle(x, y, x + k, y + k, fill="black")
                            y += 2 * k
                        x += 2 * k
                    x = 1 * k

                    while x < 8 * k:  # рисуем доску
                        y = 0
                        while y < 8 * k:
                            doska.create_rectangle(x, y, x + k, y + k, fill="black")
                            y += 2 * k
                        x += 2 * k

                vivod()
                window.after(1, lambda: window.destroy())
                mainloop()

            else:
                print('Неверный логин или пароль')
                messagebox.showwarning(title='Ошибка', message='Неверный логин или пароль')


    main_label = Label(win, text='Авторизация', font=font_header, justify=CENTER, **header_padding)
    main_label.pack()

    # метка для поля ввода имени
    username_label = Label(win, text='Имя пользователя', font=label_font, **base_padding)
    username_label.pack()

    username_entry = Entry(win, bg='#fff', fg='#444', font=font_entry)
    username_entry.pack()

    password_label = Label(win, text='Пароль', font=label_font, **base_padding)
    password_label.pack()

    password_entry = Entry(win, bg='#fff', fg='#444', font=font_entry)
    password_entry.pack()

    send_btn = Button(win, text='Войти', command=clicked)
    send_btn.pack(**base_padding)

def regist():
    win = Toplevel(window)
    win.title('Регистрация')
    win.geometry('450x230+360+210')
    win.protocol("VM_DELETE_WINDOW", lambda: dismiss(win))
    win.grab_set()

    def clicked():
        # получаем имя пользователя и пароль
        login = username_entry.get()
        password = password_entry.get()

        if len(login) == 0 or len(password) == 0:
            messagebox.showwarning(title='Ошибка', message='Поле заполнения пусто')
        else:
            result = add_user(login, password)  # Вызываем функцию добавления пользователя.

            if not result:
                print('Пользователь с таким логином уже существует')
                messagebox.showwarning(title='Ошибка', message='Пользователь с таким логином уже существует')
            else:
                print('Регистрация прошла успешно!')
                messagebox.showinfo('Регистрация', 'Регистрация прошла успешно!\nДля входа в систему авторизуйтесь.')
                win.after(300, lambda: (win.destroy(), win.grab_release()))

    main_label = Label(win, text='Регистрация', font=font_header, justify=CENTER, **header_padding)
    main_label.pack()

    # метка для поля ввода имени
    username_label = Label(win, text='Имя пользователя', font=label_font, **base_padding)
    username_label.pack()

    username_entry = Entry(win, bg='#fff', fg='#444', font=font_entry)
    username_entry.pack()

    password_label = Label(win, text='Пароль', font=label_font, **base_padding)
    password_label.pack()

    password_entry = Entry(win, bg='#fff', fg='#444', font=font_entry)
    password_entry.pack()

    send_btn = Button(win, text='Зарегистрироваться', command=clicked)
    send_btn.pack(**base_padding)

def exit():
    window.destroy()


# кортежи и словари, содержащие настройки шрифтов и отступов
font_header = ('Arial', 15)
font_entry = ('Arial', 12)
label_font = ('Arial', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}

init_file()

window = Tk()
window.title('Вход')
window.geometry('450x230+350+200')
window.resizable(False, False)


main_label = Label(window, text='Выберите необходимый вариант', font=font_header, justify=CENTER, **header_padding)
main_label.pack()

authorization_btn = Button(window, text='Авторизация', command=authorization)
authorization_btn.pack(**base_padding)

regist_btn = Button(window, text='Регистрация', command=regist)
regist_btn.pack(**base_padding)

exit_btn = Button(window, text='Выход', command=exit)
exit_btn.pack(**base_padding)

window.mainloop()