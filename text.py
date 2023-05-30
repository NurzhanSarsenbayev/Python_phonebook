main_menu = '''\n Главное меню:
1. Открыть файл
2. Записать файл
3. Показать контакт
4. Добавить контакт
5. Найти контакт
6. Изменить контакт
7. Удалить Контакт
8. Выход\n'''

input_choice = 'Выберите пункт меню: '

load_successful = 'Открыто'
save_successful = 'Сохранено'
load_error = 'Ошибка'

input_contact = {'name':'Имя: ',
                 'phone' : 'Телефон: ',
                 'comment' : 'Комментарий: '}

new_contact = 'Введите данные нового контакта ( пусто -> отмена )'
def new_contact_successful(name:str ) -> str:
    return f'Контакт {name} добавлен'

cancel_input = 'Отмена'

index_del_contact = 'Введите индекс контакта для удаления: ' 

find_name_contact = 'Введите имя для поиска контакта: '
find_name_fail = 'Такого контакта нет'

def del_contact (name:str):
    return f'Контакт {name} удалён'