class YaUploader:
    def __init__(self, token):
        self.token = token

    def upload(self, file_path):
        """Метод загружает файл на яндекс диск"""
        url = self.link_to_load(file_name)
        headers = self.get_headers()
        response = requests.put(url, headers=headers, data=open(file_name, 'rb'))
        print(response.status_code)
        if response.status_code == 201:
            print("Загрузка прошла успешно")

    def get_headers(self):
        """Метод возвращает заголовки для работы с яндекс диском"""
        return {'Content-Type' : 'applicaation/json',
            'Authorization' : f'OAuth {self.token}'}

    def link_to_load(self, file_on_disk):
        """Метод возвращает ссылку для загрузки файла на яндекс диск"""
        url = HOST + '/v1/disk/resources/upload'
        params = {'path' : f'/{file_on_disk}','overwrite' : True }
        headers = self.get_headers()
        response = requests.get(url, headers=headers, params=params)
        return response.json()['href']

if __name__ == '__main__':
    import requests
    file_name = 'filetoload.txt'
    path_to_file = 'filetoload.txt'
    TOKEN = '...'
    HOST = 'https://cloud-api.yandex.net:443'
    uploader = YaUploader(token=TOKEN)
    result = uploader.upload(path_to_file)





