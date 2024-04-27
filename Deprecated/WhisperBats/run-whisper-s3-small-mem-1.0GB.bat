REM Enable UTF-8 Support for CMD, 65001 for UTF-8, 936 for GBK
chcp 65001

.\whispercpp\main.exe -m .\models\whisper-s3-small-mem-1.0GB.bin -f .\sound-to-transcript-16khz.wav ^
-l auto -t 12 -p 1 -ovtt ture -of .\sound-to-transcript -pp ture
pause
