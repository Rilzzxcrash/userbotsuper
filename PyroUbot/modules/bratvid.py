import requests
import os
from PyroUbot import *

async def BratVideo(text):
    if not text:
        return "textnya mana?"
    if len(text) > 250:
        return " "

    words = text.split(" ")
    temp_dir = os.path.join(os.getcwd(), "lib")
    os.makedirs(temp_dir, exist_ok=True)
    frame_paths = []

    try:
        for i in range(len(words)):
            current_text = " ".join(words[:i + 1])

            res = requests.get(
                f"https://brat.caliphdev.com/api/brat?text={requests.utils.quote(current_text)}",
                stream=True
            )

            if res.status_code != 200:
                raise Exception("Gagal mengambil frame dari API")

            frame_path = os.path.join(temp_dir, f"frame{i}.mp4")
            with open(frame_path, "wb") as f:
                f.write(res.content)
            frame_paths.append(frame_path)

        file_list_path = os.path.join(temp_dir, "filelist.txt")
        with open(file_list_path, "w") as f:
            for frame in frame_paths:
                f.write(f"file '{frame}'\n")
                f.write("duration 0.7\n")
            f.write(f"file '{frame_paths[-1]}'\n")
            f.write("duration 2\n")

        output_video_path = os.path.join(temp_dir, "output.mp4")
        os.system(
            f"ffmpeg -y -f concat -safe 0 -i {file_list_path} -vf 'fps=30' -c:v libx264 -preset ultrafast -pix_fmt yuv420p {output_video_path}"
        )

        for frame in frame_paths:
            if os.path.exists(frame):
                os.remove(frame)
        if os.path.exists(file_list_path):
            os.remove(file_list_path)

        return output_video_path

    except Exception as e:
        print(e)
        return "Terjadi kesalahan"


@PY.UBOT("bratvideo")
@PY.TOP_CMD
async def brat_handler(client, message):
    text = message.text.split(maxsplit=1)[-1] if len(message.text.split()) > 1 else None
    if not text:
        await message.reply_text("textnya mana?")
        return

    processing_msg = await message.reply_text("proses...")
    video_path = await BratVideo(text)

    if isinstance(video_path, str) and video_path.startswith("Terjadi kesalahan"):
        await processing_msg.delete()
        await message.reply_text(video_path)
    else:
        await processing_msg.delete()
        await message.reply_video(video=video_path, caption="```\ndone```")

        if os.path.exists(video_path):
            os.remove(video_path)
