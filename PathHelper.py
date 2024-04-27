import os


def DeQuoteIze(path):
    if path.startswith("\""):
        return path[1:-1]
    else:
        return path


def QuoteIze(path):
    if path.startswith("\""):
        return path
    else:
        return "\"" + path + "\""


class WorkingDir:
    def __init__(self, original_file_path):
        original_file_path = DeQuoteIze(original_file_path)
        self.dir_name, file_full_name = os.path.split(original_file_path)
        self.file_name, self.file_extension = os.path.splitext(file_full_name)

    def At(self, file, extension):
        return QuoteIze(
            os.path.join(self.dir_name, file + extension)
        )
