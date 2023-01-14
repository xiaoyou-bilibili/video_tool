import os
from subprocess import Popen, PIPE, STDOUT
from ui import show_main_window

def exe_command(command):
    """
    执行 shell 命令并实时打印输出
    :param command: shell 命令
    :return: process, exitcode
    """
    print(command)
    process = Popen(command, stdout=PIPE, stderr=STDOUT, shell=True)
    with process.stdout:
        for line in iter(process.stdout.readline, b''):
            print(line.decode().strip())
    exitcode = process.wait()
    return process, exitcode


def read_files():
    path = "video"
    for file in os.listdir(path):
        if file.endswith(".mp4") or file.endswith(".mkv") or file.endswith(".rmvb"):
            try:
                name = file.split(".")[0]
                # hwaccel 是硬件加速
                # 加字幕
                cmd = "ffmpeg -hwaccel cuda -threads 2 -i {path}/{origin} -vf subtitles={path}/{sub} {path}/{new}".format(path=path, origin=file, sub=file.replace(".mkv", ".ass").replace(".mp4", ".ass"), new="new_"+file)
                # rmvb转mp4
                # cmd = "ffmpeg -hwaccel cuda -threads 4 -i {path}/{origin} -c:v h264 -c:a aac {path}/{new}".format(path=path, origin=file, new="new_{}.mp4".format(name))
                exe_command(cmd)
                # print(cmd)
            except Exception as e:
                print(e)


if __name__ == '__main__':
    show_main_window()