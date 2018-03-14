import chardet
import hashlib


class TeXFile:
    def __init__(self, path):
        self.path = path
        self.encoding = self._guess_encoding()
        self._file_wrapper = open(self.path, 'r', encoding=self.encoding)
        self.all_strings = list(map(lambda x: x.strip(), self._file_wrapper.read().split('\n')))
        self.cur_str = 0

    def __len__(self):
        return len(self.all_strings)

    def __next__(self):
        if self.cur_str > len(self):
            raise StopIteration
        else:
            self.cur_str += 1
            return self.all_strings[self.cur_str - 1]

    def __iter__(self):
        return iter(self.all_strings)

    def _guess_encoding(self):
        file = open(self.path, 'rb')
        detector = chardet.UniversalDetector()
        for line in file.readlines():
            detector.feed(line)
            if detector.done:
                break
        return detector.result['encoding']

    def __hash__(self):
        m = hashlib.md5()
        m.update(self._file_wrapper.read())
        return m.hexdigest()