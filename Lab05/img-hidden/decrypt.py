import sys
from PIL import Image

def encode_image(image_path, message):
    # Mở ảnh và lấy kích thước
    img = Image.open(image_path)
    width, height = img.size
    
    # Chuyển đổi thông điệp sang chuỗi nhị phân (mỗi ký tự 8 bit)
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    # Thêm ký tự đánh dấu kết thúc thông điệp
    binary_message += '1111111111111110' 
    
    data_index = 0
    for row in range(height):
        for col in range(width):
            # Lấy giá trị màu của pixel (R, G, B)
            pixel = list(img.getpixel((col, row)))
            
            for color_channel in range(3): # Duyệt qua 3 kênh Đỏ, Xanh lá, Xanh dương
                if data_index < len(binary_message):
                    # Thay thế bit cuối cùng (LSB) bằng bit của thông điệp
                    pixel[color_channel] = int(format(pixel[color_channel], '08b')[:-1] + binary_message[data_index], 2)
                    data_index += 1
            
            # Cập nhật pixel lại vào ảnh
            img.putpixel((col, row), tuple(pixel))
            
            if data_index >= len(binary_message):
                break
        if data_index >= len(binary_message):
            break
            
    encoded_image_path = 'encoded_image.png'
    img.save(encoded_image_path)
    print("Steganography complete. Encoded image saved as", encoded_image_path)

def main():
    if len(sys.argv) != 3:
        print("Usage: python encrypt.py <image_path> <message>")
        return
    
    image_path = sys.argv[1]
    message = sys.argv[2]
    encode_image(image_path, message)

if __name__ == "__main__":
    main()