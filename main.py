class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать
class YandexDisk:
    def __init__(self,token):
        self.token = token

    def get_files_list(self):
        files_url = HOST + '/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

    def get_headers(self):
        return {'Content-Type' : 'applicaation/json',
            'Authorization' : f'OAuth {self.token}'}

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    # path_to_file = ...
    # token = ...
    # uploader = YaUploader(token)
    # result = uploader.upload(path_to_file)
    import requests
    import pprint
    TOKEN = '...'
    HOST = 'https://cloud-api.yandex.net:443'

    ya = YandexDisk(token=TOKEN)
    pprint.pprint(ya.get_files_list())


