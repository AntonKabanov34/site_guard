# Библиотеки
from os import mkdir, path, listdir

#Модули
from config import project_folder, log_folder_name

class Log:
    def __init__(self, folder_project:str, log_folder_name:str):
        """Конструктор"""
        self.folder = folder_project
        self.log_folder = log_folder_name
        pass

    def create_path_folder(self, users:None):
        """Возвращает путь до конечной папки"""
        pass
        

    def create_folder(self):
        """Создает подпапку с именем log_folder_name"""
        log_folder_path = path.join(self.folder, self.log_folder)
        if path.exists(log_folder_path):
            print(f'Папка "{self.log_folder}" уже существует.')
        else:
            mkdir(log_folder_path)
            print(f'Создана папка "{self.log_folder}" для логов.')

    def create_file(self):
        """Создает файл с текущей датой, если его нет"""
        pass

    def log_add(self):
        """Добавляет запись в лог-файл с именем текущей даты"""

#Путь: Новый пользователь (создать папку с номером его id)! При добвалении сайта, создать файл с логами с текущей датой)

#Объявляем экземпляры:
log_files = Log(project_folder, log_folder_name)
log_files.create_folder()
