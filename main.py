from PIL import Image
import io
image = input()
image2 = input()

result = ""

with open(f"{image}", 'rb') as f:
    result = f.read()

with open(f"{image2}", 'rb') as f:
    result += f.read()

img = Image.open(io.BytesIO(result))
index = result.index(b"\xff\xd9")+2
result = result[index:]
img = Image.open(io.BytesIO(result))
img.show()
