"""
yesterday.txt 파일 읽어서
yesterday 단어가 몇번 나오는지 카운트 해보장

file open mode
- r : read (open mode default값)
- w : write (overwrite)
- rb : read binary
- wb : write binary
- a : append


"""

def file_read(file_name):
    with open(file_name,"r",encoding='utf-8') as file :
        lyric = file.read()
        return lyric


read = file_read("yesterday.txt")
print(read)
n_of_YESTERDAY = read.upper().count('YESTERDAY')
print(f'Number of a word YESTERDAY {n_of_YESTERDAY}')
n_of_Yesterday = read.count('Yesterday')
print(f'Number of a word Yesterdat {n_of_Yesterday}')
n_of_yesterday = read.lower().count('yesterday')
print(f'Number of a word yesterday {n_of_yesterday}')