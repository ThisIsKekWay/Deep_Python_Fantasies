from files_func import homework as hf

if __name__ == '__main__':
    print("Переименование txt файлов в каталоге data_files")
    files_conut = hf.group_rename_files("_ololo_", ".txt", path="./data")
    print(f"Переименовано: {files_conut}")
    files_cnt = hf.group_rename_files("_trololo_", ".csv", path="./data")
    print(f"Переименовано: {files_conut}")