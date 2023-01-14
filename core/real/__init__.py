import base64
import os.path

import cv2
import requests
import numpy as np


def _process_handle(process: int):
    return


def video_real_esr_gan(path: str, name: str, host: str, save_img: bool, process_handle: _process_handle):
    cap = cv2.VideoCapture(path)
    frames_num = cap.get(7)
    fps = cap.get(5)
    width = cap.get(3)
    height = cap.get(4)
    print(frames_num, fps, width, height)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(path.replace(name, "real_{}".format(name)), fourcc, fps, (int(width) * 4, int(height) * 4))
    ext = name.split(".")[-1]
    save_img_path = path.replace(".%s" % ext, "")
    if save_img:
        if not os.path.exists(save_img_path):
            os.mkdir(save_img_path)
    for i in range(0, int(frames_num)):
        try:
            ret, frame = cap.read()
            data = cv2.imencode('.jpg', frame)[1].tobytes()
            res = requests.post("{}/esr/img/row".format(host), {
                "data": base64.encodebytes(data).decode(),
                "face_enhance": "false"
            })
            tmp = cv2.imdecode(np.frombuffer(res.content, np.uint8), cv2.IMREAD_UNCHANGED)
            if save_img:
                cv2.imwrite("{}/{}.jpg".format(save_img_path,i), tmp)
            out.write(tmp)
            process_handle(int(((i+1)/frames_num)*100))
        except Exception as e:
            print("convert {} frame err! info {}".format(i, e))

    cap.release()
    out.release()
