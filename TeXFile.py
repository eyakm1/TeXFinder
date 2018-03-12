import chardet


class TeXFile:
    def __init__(self, path):
        file = open(path, 'r')
        detector = chardet.UniversalDetector()
        for line in file.readlines():
            detector.feed(line)
            if detector.done:
                break
        self.encoding = detector.result['encoding']
