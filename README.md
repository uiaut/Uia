# Facebook Share Tool

✅ Tự động share bài viết Facebook bằng access token từ cookie.  
✅ Chạy 24/7 trên [Render.com](https://render.com) miễn phí.  
✅ Không cần nhập `input()` — dùng `config.json` thay thế.

## Deploy

1. Tạo repo GitHub chứa toàn bộ các file trên.
2. Vào [Render](https://render.com), đăng nhập bằng GitHub.
3. Chọn “New Web Service” → chọn repo.
4. Thiết lập:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python3 main.py`
   - Port: `8080`
   - Plan: **Free**

Bạn có thể sửa `config.json` bất kỳ lúc nào để đổi ID, delay, cookie...
