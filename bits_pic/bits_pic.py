from PIL import Image
import hashlib


class Pic2Str(object):
    def __init__(self, pic_path: str):
        self.pic_path = pic_path
        self.pic = Image.open(self.pic_path)
        self.rgb2binary = {(255, 255, 255): '0',
                           (0, 0, 0): '1'}

    def pic2binary(self) -> list:
        binary_list = list()
        height = self.pic.height
        width = self.pic.width
        # 像素
        pixels = self.pic.load()

        for h in range(height):
            for w in range(width):
                pixel = pixels[w, h]
                binary_list.append(self.rgb2binary.get(pixel))
        return binary_list

    def pic2str(self) -> str:
        binary_list = self.pic2binary()
        # 按每 8 位分割一个二进制传
        split_binary = [''.join(binary_list[i:i + 8]) for i in range(0, len(binary_list), 8)]
        res_str = bytes([int(x, 2) for x in split_binary]).decode('utf-8')
        return res_str

    @staticmethod
    def md5_from_str(source_str: str) -> str:
        md5_str = hashlib.md5(source_str.encode('utf-8')).hexdigest()
        return md5_str


if __name__ == '__main__':
    path = './quiz5-abc.png'
    pic2str = Pic2Str(path)
    detected_str = pic2str.pic2str()
    print(detected_str)
    # fedeaada897e5b54404e56e5487c49e6
    print(Pic2Str.md5_from_str(detected_str))
