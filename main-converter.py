# if __name__ == "__main__":
#
#     #
#     # Info Log
#     #
#
#     EnableCMDUnicode()
#     print("---------- WhisperSir ----------")
#     print("@@@ CPU Cores Detected:", GetCPUNumber())
#     print("@@@ Temp Folder:", TempDir().dir_name)
#
#     #
#     # Real MEAT :)
#     #
#
#     input_string = input("输入要转换的VTT文件的地址（会转换成SRT和TXT，拖动到此窗口即可，可以一次拖动多个文件进来）：")
#     input_list = []
#
#     if input_string[0] == "\"":
#         # Multiple "path" with quotes
#         input_string = input_string.strip("\"")
#         input_list = input_string.split('" "')
#         pass
#     else:
#         # Multiple path with no quotes
#         input_list = input_string.split(' ')
#         pass
#
#     for i in range(0, len(input_list)):
#         print("Processing: [", i+1, "/", len(input_list), "] File ...")
#
#         workingDir = WorkingDir(input_list[i])
#         tempDir = TempDir()
#
#         VTT2SRT(
#             vtt_file=workingDir.At(workingDir.file_name, ".vtt"),
#             srt_file=workingDir.At(workingDir.file_name, ".srt")
#         )
#
#         VTT2TXT(
#             vtt_file=workingDir.At(workingDir.file_name, ".vtt"),
#             txt_file=workingDir.At(workingDir.file_name, ".txt")
#         )
#
#     print("---------- WhisperSir ----------")
#     print("@@@ Completed. Press any key to exit...")
