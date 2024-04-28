import os
import zhconv

def convert_to_simplified_chinese(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    simplified_content = zhconv.convert(content, 'zh-cn')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(simplified_content)

if __name__ == "__main__":
    input_file = 'sound-to-transcript.vtt'
    output_file = 'sound-to-transcript-simplified.vtt'

    if os.path.exists(input_file):
        convert_to_simplified_chinese(input_file, output_file)
        print("Conversion completed.")
    else:
        print("Input file not found.")
