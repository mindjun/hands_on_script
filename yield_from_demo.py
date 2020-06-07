import os


def path_travel(path):
    for item in os.listdir(path):
        temp_path = os.path.join(path, item)
        if os.path.isdir(temp_path):
            yield from path_travel(temp_path)
        else:
            yield item


#for x in path_travel('/root/hujun'):
#    print(x)

res = list(path_travel('/root'))
print(len(res))
