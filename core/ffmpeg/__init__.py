import json
import subprocess as sp
import shlex
import time
from threading import Thread
from core.ffmpeg.model import *

_process_pipe = "-progress pipe:1"


# 进度等信息的回调函数
def _process_callback(process: int, frame: int, fps: int, speed: str):
    pass


# 获取总帧数
def get_total_frame(name: str) -> float:
    # 直接使用ffprobe来对视频进行分析
    data = sp.run(
        shlex.split('ffprobe -v error -select_streams v:0 -count_packets -show_entries stream=nb_read_packets '
                    '-of csv=p=0 -of json {}'.format(name)), stdout=sp.PIPE).stdout
    data = json.loads(data)
    if "streams" in data and len(data["streams"]) > 0 and "nb_read_packets" in data['streams'][0]:
        return float(data['streams'][0]['nb_read_packets'])  # Get the total number of frames.
    else:
        return 0


# 读取命令执行结果
def progress_reader(procs, q):
    while True:
        if procs.poll() is not None:
            break  # Break if FFmpeg sun-process is closed

        progress_text = procs.stdout.readline()  # Read line from the pipe

        # Break the loop if progress_text is None (when pipe is closed).
        if progress_text is None:
            break

        progress_text = progress_text.decode("utf-8")  # Convert bytes array to strings
        # 寻找 "frame=xx"的字样，如果存在就提取其中的字段
        # 获取转换帧数
        if progress_text.startswith("frame="):
            q[0] = int(progress_text.partition('=')[-1])
        # 获取转换的fps
        if progress_text.startswith("fps="):
            q[1] = float(str(progress_text.partition('=')[-1]).strip())
        # 获取转换速度
        if progress_text.startswith("speed="):
            q[2] = str(progress_text.partition('=')[-1]).strip()


# 执行ffmpeg命令
def execute_ffmpeg_cmd(hwaccel: str, threads: int, input: str, out: str, cmd: str, callback: _process_callback):
    if hwaccel != "":
        hwaccel = "-hwaccel {}".format(hwaccel)
    cmd = "ffmpeg {} -threads {} -i {} {} -progress pipe:1 {}".format(hwaccel, threads, input, cmd, out)
    print("cmd is {}".format(cmd))
    process = sp.Popen(cmd, stdout=sp.PIPE)
    # 创建一个数组来保存参数
    q = [0, 0, '']
    progress_reader_thread = Thread(target=progress_reader, args=(process, q))  # Initialize progress reader thread
    progress_reader_thread.start()
    # 读取总帧数
    tot_n_frames = get_total_frame(input)
    while True:
        if process.poll() is not None:
            break  # Break if FFmpeg sun-process is closed
        # 等待1s后再读取，
        time.sleep(1)
        n_frame = q[0]
        progress_percent = int((n_frame / tot_n_frames) * 100)
        callback(progress_percent, q[0], q[1], q[2])

    process.stdout.close()  # 关闭标准输出
    progress_reader_thread.join()  # 等待线程结束
    process.wait()  # 等待ffmpeg结束
