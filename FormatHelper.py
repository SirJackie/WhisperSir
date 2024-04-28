from PathHelper import *


def VTT2SRT(vtt_file, srt_file):
    vtt_file = DeQuoteIze(vtt_file)
    srt_file = DeQuoteIze(srt_file)

    with open(vtt_file, 'r', encoding='utf-8') as vtt_file:
        vtt_content = vtt_file.read()

    # Remove WEBVTT header
    vtt_content = vtt_content.replace('WEBVTT\n\n', '')

    # Replace time format from HH:MM:SS.mmm to HH:MM:SS,mmm
    vtt_content = vtt_content.replace('.', ',')

    # Replace '-->' with ' --> '
    vtt_content = vtt_content.replace('-->', ' --> ')

    with open(srt_file, 'w', encoding='utf-8') as srt_file:
        srt_file.write(vtt_content)


def SRT2VTT(srt_file, vtt_file):
    srt_file = DeQuoteIze(srt_file)
    vtt_file = DeQuoteIze(vtt_file)

    with open(srt_file, 'r', encoding='utf-8') as srt_file:
        srt_content = srt_file.read()

    # Add WEBVTT header
    vtt_content = 'WEBVTT\n\n'

    # Replace time format from HH:MM:SS,mmm to HH:MM:SS.mmm
    srt_content = srt_content.replace(',', '.')

    # Replace ' --> ' with '-->'
    srt_content = srt_content.replace(' --> ', '-->')

    vtt_content += srt_content

    with open(vtt_file, 'w', encoding='utf-8') as vtt_file:
        vtt_file.write(vtt_content)


def VTT2TXT(vtt_file, txt_file):
    vtt_file = DeQuoteIze(vtt_file)
    txt_file = DeQuoteIze(txt_file)

    with open(vtt_file, 'r', encoding='utf-8') as vtt_file:
        vtt_content = vtt_file.read()

    # Remove WEBVTT header
    vtt_content = vtt_content.replace('WEBVTT\n\n', '')

    # Split into subtitle blocks
    blocks = vtt_content.strip().split('\n\n')

    # Extract text from each block
    subtitles = []
    for block in blocks:
        lines = block.split('\n')
        if len(lines) > 1:
            timestamp = lines[0]
            text = '，'.join(lines[1:])
            subtitles.append(text)

    # Join subtitles into a single paragraph
    txt_content = '。'.join(subtitles)

    with open(txt_file, 'w', encoding='utf-8') as txt_file:
        txt_file.write(txt_content)
