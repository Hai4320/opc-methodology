import os
import cv2
import easyocr
import numpy as np
from deep_translator import GoogleTranslator
from PIL import Image, ImageDraw, ImageFont

# 1. Cấu hình đường dẫn
INPUT_DIR = '../src/images'   # Thư mục chứa ảnh gốc (tiếng Trung)
OUTPUT_DIR = '../src/images_vi'    # Thư mục lưu ảnh sau khi dịch
FONT_PATH = './ARIAL.TTF'       # Đường dẫn tới file font hỗ trợ tiếng Việt

# Tạo thư mục đầu ra nếu chưa có
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# Khởi tạo công cụ đọc chữ (Hỗ trợ tiếng Trung giản thể và tiếng Anh)
print("Đang tải model AI nhận diện chữ...")
reader = easyocr.Reader(['ch_sim', 'en'])
translator = GoogleTranslator(source='zh-CN', target='vi')

def process_image(image_path, output_path):
    print(f"Đang xử lý: {image_path}")
    
    # Đọc ảnh bằng OpenCV
    img = cv2.imread(image_path)
    if img is None:
        return
    
    # Nhận diện chữ
    results = reader.readtext(img)
    
    # Tạo một bức ảnh đen (mask) cùng kích thước để đánh dấu vùng cần xóa chữ cũ
    mask = np.zeros(img.shape[:2], dtype="uint8")
    
    text_data = [] # Lưu trữ tọa độ và text đã dịch
    
    for (bbox, text, prob) in results:
        # Lấy tọa độ 4 góc của đoạn text
        (tl, tr, br, bl) = bbox
        tl = (int(tl[0]), int(tl[1]))
        tr = (int(tr[0]), int(tr[1]))
        br = (int(br[0]), int(br[1]))
        bl = (int(bl[0]), int(bl[1]))
        
        # --- Tính toán kích thước ô chữ gốc ---
        bb_width = tr[0] - tl[0] # Chiều rộng ô chữ gốc
        bb_height = bl[1] - tl[1] # Chiều cao ô chữ gốc
        # -------------------------------------

        # Vẽ một hình đa giác trắng lên mask tại vị trí có chữ
        pts = np.array([tl, tr, br, bl], np.int32)
        cv2.fillPoly(mask, [pts], 255)
        
        # Dịch đoạn text
        try:
            translated_text = translator.translate(text)
        except Exception:
            translated_text = text # Nếu lỗi dịch thì giữ nguyên
            
        # Lưu trữ dữ liệu: góc trên bên trái, text đã dịch, chiều rộng và chiều cao box gốc
        text_data.append((tl, translated_text, bb_width, bb_height))

    # Xóa chữ tiếng Trung cũ trên ảnh gốc bằng kỹ thuật Inpainting
    img_inpainted = cv2.inpaint(img, mask, 7, cv2.INPAINT_NS)
    
    # Chuyển ảnh từ OpenCV (BGR) sang Pillow (RGB) để vẽ chữ tiếng Việt
    img_pil = Image.fromarray(cv2.cvtColor(img_inpainted, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img_pil)
    
    # Vẽ chữ tiếng Việt lên ảnh mới với logic giảm cỡ chữ
    for (top_left, text, bb_width, bb_height) in text_data:
        try:
            # --- START OF DYNAMIC FONT SIZE LOGIC ---
            # Cấu hình cỡ chữ ban đầu và cỡ chữ nhỏ nhất chấp nhận được
            initial_font_size = max(12, int(bb_height * 0.9)) # Bắt đầu gần với chiều cao box
            current_font_size = initial_font_size
            min_font_size = 12 # Cỡ chữ tối thiểu để còn đọc được
            
            font_fitted = False
            font = None
            text_width = 0
            text_height = 0

            while current_font_size >= min_font_size:
                try:
                    font = ImageFont.truetype(FONT_PATH, current_font_size)
                    # Kiểm tra kích thước text render với cỡ chữ hiện tại
                    text_bbox = draw.textbbox((0, 0), text, font=font)
                    text_width = text_bbox[2] - text_bbox[0]
                    text_height = text_bbox[3] - text_bbox[1]

                    # Nếu text vừa khít chiều rộng (cho phép tràn 5%) và không cao hơn nhiều
                    if text_width <= bb_width * 1.05 and text_height <= bb_height * 1.1:
                        font_fitted = True
                        break # Tìm thấy cỡ chữ phù hợp
                    else:
                        current_font_size -= 1 # Thử cỡ chữ nhỏ hơn

                except IOError:
                    raise # File font lỗi

            # Nếu không tìm được cỡ chữ phù hợp ở min_font_size, 
            # In ra cảnh báo và dùng cỡ chữ nhỏ nhất.
            if not font_fitted:
                print(f"  [CẢNH BÁO] Text không vừa box: '{text[:20]}...' quá dài. Dùng cỡ chữ nhỏ nhất.")
                font = ImageFont.truetype(FONT_PATH, min_font_size)
                # Tính toán lại kích thước để căn giữa
                final_text_bbox = draw.textbbox((0, 0), text, font=font)
                final_text_height = final_text_bbox[3] - final_text_bbox[1]
            else:
                final_text_height = text_height # Sử dụng text_height đã tính được

            # --- END OF DYNAMIC FONT SIZE LOGIC ---

            # --- Căn giữa text theo chiều dọc trong box cũ ---
            x, y = top_left
            centered_y = y + (bb_height - final_text_height) // 2
            
            # Vẽ chữ màu đen
            draw.text((x, centered_y), text, font=font, fill=(0, 0, 0))

        except IOError:
            print("Lỗi: Không tìm thấy file font chữ!")
            break

    # Lưu ảnh đã dịch
    img_pil.save(output_path)
    print(f"Đã lưu thành công: {output_path}")

# Lặp qua toàn bộ file trong thư mục đầu vào
for filename in os.listdir(INPUT_DIR):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        in_path = os.path.join(INPUT_DIR, filename)
        out_path = os.path.join(OUTPUT_DIR, filename)
        process_image(in_path, out_path)

print("Hoàn tất dịch toàn bộ ảnh trong Repo!")