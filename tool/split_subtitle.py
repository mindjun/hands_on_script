from pysubs2 import SSAFile


def split_subtitle():
    path = './CHS_test.srt'

    subs = SSAFile.load(path)
    print(subs[0].plaintext)


split_subtitle()
