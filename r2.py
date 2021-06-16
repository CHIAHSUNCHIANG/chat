#讀取檔案，可以使用continue
def read_file(filename):
    lines = [] 
    with open(filename, 'r', encoding='utf-8-sig') as f:  #-sig為了去除uefef
            for line in f:
                lines.append(line.strip())
    return lines

def convert(lines):
    person = None
    allen_word_count = 0
    viki_word_count = 0
    allen_sticker_count = 0
    viki_sticker_count = 0
    allen_img_count = 0
    viki_img_count = 0
    for line in lines:
        s = line.split(' ') #遇到空白鍵就切一刀
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_img_count += 1
            else:
                for m in s[2:]:
                    allen_word_count += len(m)
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_count += 1
            elif s[2] == '圖片':
                viki_img_count += 1
            else:
                for m in s[2:]:
                    viki_word_count += len(m)
    print('allen said', allen_word_count, 'words')
    print('allen sent', allen_sticker_count, 'stickers', )
    print('allen sent', allen_img_count, 'images')

    print('viki saie', viki_word_count, 'words')
    print('viki sent', viki_sticker_count, 'stickers')
    print('viki sent', viki_img_count, 'images')
        # print(s)


def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')


def main():
    lines = read_file('LINE-Viki.txt')
    lines = convert(lines)
    #write_file('output.txt', lines)

main()