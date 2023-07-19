path = 'C:\Thecode\Media\статья.txt'

#Не разобрался c бэкслэшем, умер.
#

def path_spliter (path):
    *_, file = path.split("\\")
    part_of_path = path[:path.rfind("\\") + 1]
    file_name, file_type = file.split('.')
    res = (part_of_path, file_name, file_type)
    return (res)

print(path_spliter(path))
