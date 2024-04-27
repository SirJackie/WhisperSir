import os
import multiprocessing
import subprocess
import tempfile
from PathHelper import *

model_files = {
    "tiny": ".\\Models\\whisper-s1-tiny-mem-390MB.bin",
    "base": ".\\Models\\whisper-s2-base-mem-500MB.bin",
    "small": ".\\Models\\whisper-s3-small-mem-1.0GB.bin",
    "medium": ".\\Models\\whisper-s4-medium-mem-2.6GB.bin"
}


def GetCPUNumber():
    return multiprocessing.cpu_count()


def GetTempDir():
    return tempfile.gettempdir()


def EnableCMDUnicode():
    os.system("chcp 65001")


def RunWhisper(input_file, output_file, model_size="small", language="auto"):
    # Get Model File's Path
    model_file = "\"" + model_files[model_size] + "\""

    # Create Maximum Amount of Threads to Utilize the Resource of PC.
    process_num = 1
    thread_num = GetCPUNumber()

    # Print Progress.
    print_progress = "true"

    command = "\".\\Executables\\whispercpp\\main.exe\" -m %s -f %s -l %s -t %s -p %s -ovtt true -of %s -pp %s" % \
              (model_file, input_file, language, thread_num, process_num, output_file, print_progress)
    print(command)
    # os.system(command)  # os.system() has some bug, don't use it.
    subprocess.run(command)


if __name__ == "__main__":

    #
    # Info Log
    #

    EnableCMDUnicode()
    print("CPU Cores:", GetCPUNumber())
    print("Temp Dir:", GetTempDir())

    #
    # Real MEAT :)
    #

    input_file = input("输入要转换文件的地址（必须是16kHz WAV格式的音频）：")

    workingDir = WorkingDir(input_file)
    output_file = workingDir.At(workingDir.file_name, "")  # Whisper requires no extension.

    RunWhisper(input_file, output_file)
