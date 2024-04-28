import os
import multiprocessing
import subprocess
import tempfile
import zhconv
from PathHelper import *
from FormatHelper import *

model_files = {
    "tiny": ".\\Models\\whisper-s1-tiny-mem-390MB.bin",
    "base": ".\\Models\\whisper-s2-base-mem-500MB.bin",
    "small": ".\\Models\\whisper-s3-small-mem-1.0GB.bin",
    "medium": ".\\Models\\whisper-s4-medium-mem-2.6GB.bin"
}


def GetCPUNumber():
    return multiprocessing.cpu_count()


def EnableCMDUnicode():
    os.system("chcp 65001")
    os.system("cls")


def RunFFmpegConversion(input_file, output_file):
    Hz = 16000  # 16 kHz, which Whisper requires.
    command = "\".\\Executables\\ffmpeg\\ffmpeg.exe\" -i %s -ac 1 -ar %s %s -y" % \
              (input_file, Hz, output_file)  # -y for "yes" Overwrite.
    print(command)
    # os.system(command)  # os.system() has some bug, don't use it.
    subprocess.run(command)


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


def RunSimplifiedChineseConversion(input_file, output_file):
    input_file = DeQuoteIze(input_file)
    output_file = DeQuoteIze(output_file)

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    simplified_content = zhconv.convert(content, 'zh-cn')
    print("---------- Convert to Simplified Chinese ----------")
    print(simplified_content)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(simplified_content)


if __name__ == "__main__":

    #
    # Info Log
    #

    EnableCMDUnicode()
    print("---------- WhisperSir ----------")
    print("@@@ CPU Cores Detected:", GetCPUNumber())
    print("@@@ Temp Folder:", TempDir().dir_name)

    #
    # Real MEAT :)
    #

    input_string = input("输入要转换的VTT文件的地址（会转换成SRT和TXT，拖动到此窗口即可，可以一次拖动多个文件进来）：")
    input_list = []

    if input_string[0] == "\"":
        # Multiple "path" with quotes
        input_string = input_string.strip("\"")
        input_list = input_string.split('" "')
        pass
    else:
        # Multiple path with no quotes
        input_list = input_string.split(' ')
        pass

    for i in range(0, len(input_list)):
        print("Processing: [", i+1, "/", len(input_list), "] File ...")

        workingDir = WorkingDir(input_list[i])
        tempDir = TempDir()

        VTT2SRT(
            vtt_file=workingDir.At(workingDir.file_name, ".vtt"),
            srt_file=workingDir.At(workingDir.file_name, ".srt")
        )

        VTT2TXT(
            vtt_file=workingDir.At(workingDir.file_name, ".vtt"),
            txt_file=workingDir.At(workingDir.file_name, ".txt")
        )

    print("---------- WhisperSir ----------")
    print("@@@ Completed. Press any key to exit...")