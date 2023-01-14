from dataclasses import dataclass

mp4Encode = ["libx264", "h264_nvenc", "libx265"]
flvEncode = ["flv"]
gifEncode = ["gif"]


def get_ext(encode: str):
    if encode in mp4Encode:
        return "mp4"
    elif encode in flvEncode:
        return "flv"
    elif encode in gifEncode:
        return "gif"
    else:
        return ""


@dataclass
class FfmpegBase:
    hard: str
    thread: int

    def __init__(self, hard: str, thread: int):
        self.hard = hard
        self.thread = thread
