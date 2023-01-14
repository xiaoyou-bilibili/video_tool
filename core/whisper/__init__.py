import time

import requests


def _status_callback(status: str):
    print(status)


def whisper(path: str, name: str, host: str, callback: _status_callback):
    callback("文件上传中。。")
    # 先上传文件
    requests.post("{}/whisper/video".format(host), files={
        "video": open(path, "rb"),
    }).json()
    callback("文件上传完成。。")
    status = ""
    # 查询进度
    while True:
        res = requests.get("{}/whisper/process".format(host)).json()
        process = res["process"]
        if process == "finish":
            ass = res["res"]
            ext = name.split(".")[-1]
            with open(path.replace(ext, "ass"), "w", encoding="utf8") as f:
                f.write(ass)
            callback("字幕写入完毕。。")
            return
        elif process != status:
            status = process
            callback(process)
        time.sleep(1)
