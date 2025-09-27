from PIL import Image

ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    return image.resize((new_width, new_height))

def grayify(image):
    return image.convert("L")

def pixels_to_ascii(image):
    pixels = image.getdata()
    return "".join([ASCII_CHARS[pixel // 32] for pixel in pixels])

def image_to_ascii(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"❌ 无法打开图片: {e}")
        return

    image = resize_image(image, new_width)
    image = grayify(image)

    ascii_str = pixels_to_ascii(image)
    img_width = image.width
    ascii_str_len = len(ascii_str)
    ascii_img = "\n".join([ascii_str[i:i+img_width] for i in range(0, ascii_str_len, img_width)])

    return ascii_img

if __name__ == "__main__":
    img_name = input("请输入图片文件名（和代码同一文件夹）: ")
    ascii_art = image_to_ascii(img_name)
    if ascii_art:
        print("\n🎨 生成的 ASCII 艺术：\n")
        print(ascii_art)
        with open("output.txt", "w", encoding="utf-8") as f:
            f.write(ascii_art)
        print("\n✅ 同时已保存到 output.txt")