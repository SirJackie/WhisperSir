import os
import multiprocessing
import subprocess
import tempfile
import zhconv
from PathHelper import *
from FormatHelper import *
import hashlib

model_files = {
    "tiny": ".\\Models\\whisper-s1-tiny-mem-390MB.bin",
    "base": ".\\Models\\whisper-s2-base-mem-500MB.bin",
    "small": ".\\Models\\whisper-s3-small-mem-1.0GB.bin",
    "medium": ".\\Models\\whisper-s4-medium-mem-2.6GB.bin"
}


def GenerateHash(text):
    hash_obj = hashlib.sha256()
    hash_obj.update(text.encode('utf-8'))
    return hash_obj.hexdigest()


def GetCPUNumber():
    return multiprocessing.cpu_count()


def EnableCMDUnicode():
    os.system("chcp 65001")
    os.system("cls")


def RunFFmpegConversion(input_file, output_file):
    Hz = 16000  # 16 kHz, which Whisper requires.
    command = "\".\\Executables\\ffmpeg\\ffmpeg.exe\" -i %s -ac 1 -ar %s %s -y" % \
              (
                  QuoteIze(input_file),
                  Hz,
                  QuoteIze(output_file)
              )  # -y for "yes" Overwrite.

    subprocess.run(command)


def RunWhisper(input_file, output_file, model_size="small", language="auto"):
    # Get Model File's Path
    model_file = model_files[model_size]

    # Create Maximum Amount of Threads to Utilize the Resource of PC.
    process_num = 1
    thread_num = GetCPUNumber()

    # Print Progress.
    print_progress = "true"

    command = "\".\\Executables\\whispercpp\\main.exe\" -m %s -f %s -l %s -t %s -p %s -ovtt true -of %s -pp %s" % \
              (
                  QuoteIze(model_file),
                  QuoteIze(input_file),
                  language,
                  thread_num,
                  process_num,
                  QuoteIze(output_file),
                  print_progress
              )

    subprocess.run(command)


def RunSimplifiedChineseConversion(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    simplified_content = zhconv.convert(content, 'zh-cn')
    print("---------- Convert to Simplified Chinese ----------")
    print(simplified_content)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(simplified_content)
