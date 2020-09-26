def some():
    return 0



print('some module')

if __name__ == '__main__':
    print(__name__)
    print(__file__)

    # file = open('test.txt','w',encoding='UTF-8')
    # ========= ===============================================================
    # Character Meaning
    # --------- ---------------------------------------------------------------
    # 'r'       open for reading (default)
    # 'w'       open for writing, truncating the file first
    # 'x'       create a new file and open it for writing
    # 'a'       open for writing, appending to the end of the file if it exists
    # 'b'       binary mode
    # 't'       text mode (default)
    # '+'       open a disk file for updating (reading and writing)
    # 'U'       universal newline mode (deprecated)
    # ========= ===============================================================

    # file.write('Hello Aleksey!')
    # file.close()
    file = open('test.txt','r',encoding='UTF-8')
    #print(file.readlines())
    # print(file.read(6))
    for line in file:
        print(line)
    file.close()
