import requests
import os
import sys
import time

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
                count = 1
                part_way = len(files) / 10
                percent = round(100 / len(files))
                ost = 100 - (len(files) * percent)
                for elem in files:
                    try:
                        resp = requests.get(
                            "https://cloud-api.yandex.net/v1/disk/resources/upload",
                            params={"path": f"{dir_name}/{elem}"},
                            headers=self.headers
                        )
                        href = resp.json()["href"]
                    except KeyError:
                        resp = requests.get(
                            "https://cloud-api.yandex.net/v1/disk/resources/upload",
                            params={"path": f"{dir_name}/{elem+'copy'}"},
                            headers=self.headers
                        )
                        href = resp.json()["href"]
                    with open(f"{dir_path}\\{elem}", "rb") as f:
                        requests.put(href, files={"file": f})
                        part = int(count / part_way)
                        status = round(count * percent + ost)
                        print(f"[{count} / {len(files)}] {'##' * part + '--' * (10 - part)} {status} % || {elem}\r")
                        time.sleep(.1)
                        count += 1
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
