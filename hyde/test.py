from PIL import Image
from extrahyde import Hyde

a = Hyde()

a.encode("a.jpg",Image.open("testpicture.png")).show()
