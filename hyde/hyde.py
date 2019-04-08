from PIL import Image
import sys

#improved steganography library 

def from_image_to_binary(img):
    resultlist = list(img.getdata())
    for i in range(len(resultlist)):
        resultlist[i] = list(resultlist[i])
    return resultlist



def from_binary_to_image(binary,size):
    resultimage = Image.new("RGB",(size))
    for i in range(len(binary)):
        binary[i] = tuple(binary[i])
    resultimage.putdata(binary)
    return resultimage




def encode(file,text=""):
    img = file
    if type(img) is str:
        img = Image.open(file)

    imgarr = from_image_to_binary(img)
    txt = text + "^^^^"

    binarytxt = ""
    for i in txt:
        a = bin(ord(i))[2:]
        for _ in range(8-len(a)):
            a = "0"+a
        binarytxt+=a
        
    count = 0
    for i in range(len(imgarr)):
        for j in range(len(imgarr[i])):
            if count < len(binarytxt):
                imgarr[i][j] = int(bin(imgarr[i][j])[2:-1] + binarytxt[count],2)
                count+=1
                
            else:
                
                return from_binary_to_image(imgarr,img.size)
                
    print("file is too big")





def decode(file):
    img = file
    if type(file) is str:
        img = Image.open(file)

    resulttext = ""
    a = ""
    width,height = img.size
    for i in range(height):
        for j in range(width):
            for t in img.getpixel((j,i)):
                if len(a) >= 8:
                    resulttext += chr(int(a,2))
                    if resulttext[-4:] == "^^^^":
                        return resulttext[:-4]
                    a = ""
                a += bin(t)[-1]

    
    return None


def main():
    arr = sys.argv[1:]
    if arr[0] == '-e':
        if len(arr) > 1 and len(arr) <= 3:
            fp = arr[1]
            txt = ""
            if len(arr) > 2:
                txt = arr[2]
            try:
                img = encode(fp,txt)
                img.show()
                img.save("resultpicture.png")
            except Exception as e:
                print(e)
        else:
            print("wrong arguments")
            sys.exit(0)
    elif arr[0] == '-d':
        if len(arr) > 1:
            fp = arr[1]
            try:

                print(decode(fp))
            except Exception as e:
                print(e)
        else:
            print("wrong argmuents")
            sys.exit(0)
    else:
        print("wrong arguments")

        
                    



if __name__ == "__main__":
    main()
