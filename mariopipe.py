def get_bricks():
    while True:
        try:
            NumBricks = int(input("How high do you want the mountain to be: "))
            if 1 < NumBricks:
                break
        # catch exceptions when user enters either a blank or if it is not an interger like a symbol or alpha char
        except ValueError:
            print ("Enter only digit")
            continue
    return NumBricks
def mario_title():
    from PIL import Image, ImageFont, ImageDraw
    ShowText = 'Mario Bros'
    font = ImageFont.truetype('arialbd.ttf', 15) #load the font
    size = font.getsize(ShowText)  #calc the size of text in pixels
    image = Image.new('1', size, 1)  #create a b/w image
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), ShowText, font=font) #render the text to the bitmap
    for rownum in range(size[1]):
        line = []
        for colnum in range(size[0]):
            if image.getpixel((colnum, rownum)): line.append(' '),
            else: line.append('#'),
        print(''.join(line))
    print()
def print_mountain():
    nb = get_bricks()
    nbstart = 1
    spaceoffset = nb - nbstart
    print()
    while nbstart < nb-1:
        print(' ' * spaceoffset, end="      ")
        for i in range(nbstart):
            print("#", end="")
        print(f"\n", end="")
        spaceoffset -= 1
        nbstart += 1
    print("#### ", end="")
    while nbstart < nb:
        print(' ' * spaceoffset, end=" ")
        for i in range(nbstart):
            print("#", end="")
        print(f"\n", end="")
        spaceoffset -= 1
        nbstart += 1
    print(" ##  ", end="")
    while nbstart < nb+1:
        print(' ' * spaceoffset, end=" ")
        for i in range(nbstart):
            print("#", end="")
        print(f"\n", end="")
        spaceoffset -= 1
        nbstart += 1
def main():
    mario_title()
    print_mountain()
    print()
if __name__ == "__main__":
    main()
