import os.path

path = 'C:\Thecode\Media\статья.txt'
print(os.path.split(path))
#Не разобрался c бэкслэшем, умер.
#Воскрес. Стоун - лев.


def path_spliter (path):
    *_, file = path.split("\\")
    part_of_path = path[:path.rfind("\\") + 1]
    file_name, file_type = file.split('.')
    res = (part_of_path, file_name, file_type)
    return (res)

print(path_spliter(path))
