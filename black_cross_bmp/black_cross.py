WHITE = 1
BLACK = 0
orig_data = []

def color(i ,j):
    if (59 <= i <= 68) or (59 <= j <= 68):
        return WHITE
    else:
        return BLACK

gener_p = open("cross.bmp", 'wb')

with open("black.bmp", 'br') as orig_p:
    data = orig_p.read(10)  #读取源文件中表示偏移量的字节之前的内容
    gener_p.write(data)

    data = orig_p.read(4)   #读取原图片的偏移量信息
    offset = int.from_bytes(data, byteorder = 'little')     #将偏移量转换为整数保存，注意计算机存储器中是小端存储
    gener_p.write(data)
    
    data = orig_p.read(4)
    gener_p.write(data)
    
    width = orig_p.read(4)      #读文件宽度信息（像素），若不是128个像素，则报错
    if width != (128).to_bytes(4, byteorder = 'little'):
        print("BAD WIDTH")
        exit()
    gener_p.write(width)

    height = orig_p.read(4)     #读文件高度信息（像素），若不是128个像素，则报错
    if height != (128).to_bytes(4, byteorder = 'little'):
        print("BAD HEIGHT")
        exit()
    gener_p.write(height)

    data = orig_p.read(offset - 26)                         #将剩余信息读完，其中包括调色板信息
    gener_p.write(data)

for i in range(0, 128):
    for j in range(0, 64):
        if color(i, j * 2) == BLACK and color(i, j * 2 + 1) ==BLACK:
            gener_p.write(b'\x00')
        if color(i, j * 2) == BLACK and color(i, j * 2 + 1) ==WHITE:
            gener_p.write(b'\x0F')
        if color(i, j * 2) == WHITE and color(i, j * 2 + 1) ==BLACK:
            gener_p.write(b'\xF0')
        if color(i, j * 2) == WHITE and color(i, j * 2 + 1) ==WHITE:
            gener_p.write(b'\xFF')

gener_p.close()