from APIHelper import *
import os


def Mode1():
    #
    # Recognition: MP4 => VTT
    #

    os.system("cls")
    print("已选择模式：[1] 语音识别 (MP4 => VTT)")

    input_list = DropFiles()

    for i in range(0, len(input_list)):
        print("Processing: [", i + 1, "/", len(input_list), "] File ...")

        workingDir = WorkingDir(input_list[i])
        tempDir = TempDir()

        hashCode = GenerateHash(workingDir.file_name)

        RunFFmpegConversion(
            input_file=workingDir.At(workingDir.file_name, workingDir.file_extension),
            output_file=tempDir.At(hashCode, ".wav")
        )

        RunWhisper(
            input_file=tempDir.At(hashCode, ".wav"),
            output_file=workingDir.At(hashCode, "")
        )

        os.rename(
            workingDir.At(hashCode, ".vtt"),
            workingDir.At(workingDir.file_name, ".vtt")
        )

        RunSimplifiedChineseConversion(
            input_file=workingDir.At(workingDir.file_name, ".vtt"),
            output_file=workingDir.At(workingDir.file_name, ".vtt")
        )


def Mode2():
    #
    # Extraction: VTT => TXT
    #

    os.system("cls")
    print("已选择模式：[2] 提取文字稿 (VTT => TXT)")

    input_list = DropFiles()

    for i in range(0, len(input_list)):
        print("Processing: [", i + 1, "/", len(input_list), "] File ...")

        workingDir = WorkingDir(input_list[i])

        VTT2TXT(
            vtt_file=workingDir.At(workingDir.file_name, ".vtt"),
            txt_file=workingDir.At(workingDir.file_name, ".txt")
        )


def Mode3():
    #
    # Conversion: VTT => SRT
    #

    os.system("cls")
    print("已选择模式：[3] 字幕格式转换 (VTT => SRT)")

    input_list = DropFiles()

    for i in range(0, len(input_list)):
        print("Processing: [", i + 1, "/", len(input_list), "] File ...")

        workingDir = WorkingDir(input_list[i])

        VTT2SRT(
            vtt_file=workingDir.At(workingDir.file_name, ".vtt"),
            srt_file=workingDir.At(workingDir.file_name, ".srt")
        )


if __name__ == "__main__":

    # Starter
    EnableCMDUnicode()
    print("---------- WhisperSir ----------")
    print("@@@ CPU Cores Detected:", GetCPUNumber())
    print("@@@ Temp Folder:", TempDir().dir_name)

    # Mode Selection
    mode = int(
        input("[1] 语音识别 (MP4 => VTT)\n"
              "[2] 提取文字稿 (VTT => TXT)\n"
              "[3] 字幕格式转换 (VTT => SRT)\n"
              "输入模式，并按回车：")
    )
    if mode == 1:
        Mode1()
    elif mode == 2:
        Mode2()
    elif mode == 3:
        Mode3()

    # Ender
    print("---------- WhisperSir ----------")
    print("@@@ Completed. Press any key to exit...")
