import requests
import os

token = input("input your API token: ")
dir_path = input("input path to directory: ")


class YaUploader:
    def __init__(self, api_token: str):
        self.token = api_token
        self.headers = {"Authorization": f"OAuth {token}"}

    def upload(self, file_path: str):
        """Метод загруджает файлы из папки на яндекс диск"""
        my_dir = file_path.split('\\')
        dir_name = my_dir[-1]
        contents = []
        for item in os.walk(dir_path):
            contents.append(item)
        if contents:
            requests.put("https://cloud-api.yandex.net/v1/disk/resources",
                         params={"path": f"{dir_name}"},
                         headers=self.headers
                         )
            for path, dirs, files in contents:
                for elem in files:
                    resp = requests.get(
                        "https://cloud-api.yandex.net/v1/disk/resources/upload",
                        params={"path": f"{dir_name}/{elem}"},
                        headers=self.headers
                    )
                    href = resp.json()["href"]
                    with open(f"{dir_path}\\{elem}", "rb") as f:
                        requests.put(href, files={"file": f})
                        print(f'the file {elem} is downloaded')
                complete = '\nDownload is complete'

        if not contents:
            resp = requests.get(
                "https://cloud-api.yandex.net/v1/disk/resources/upload",
                params={"path": f"{dir_name}"},
                headers=self.headers
            )
            href = resp.json()["href"]
            with open(f'{dir_path}', "rb") as f:
                requests.put(href, files={"file": f})
                complete = f"\nDownload file {dir_name} is complete"
        return print(complete)


if __name__ == '__main__':
    uploader = YaUploader(token)
    result = uploader.upload(dir_path)
