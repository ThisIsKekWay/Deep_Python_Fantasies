def log (list, data):
    with open('log.txt', 'a') as f:
        f.write(str(list))
        f.write(data + '\n')
