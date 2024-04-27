REM Enable UTF-8 Support for CMD, 65001 for UTF-8, 936 for GBK
chcp 65001

.\whispercpp\main.exe -m .\models\whisper-s4-medium-mem-2.6GB.bin -f .\sound-to-transcript-16khz.wav ^
-l auto -t 12 -p 1 -ovtt ture -of .\sound-to-transcript -pp ture
pause
