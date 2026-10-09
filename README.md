# FOOTBALLVERSE — GitHub Pages Edition

Bản tĩnh được thiết kế để triển khai trực tiếp bằng **GitHub Pages**. Không cần Node.js, backend, PostgreSQL hay bước build.

## Chạy thử trên máy
1. Giải nén ZIP.
2. Mở `index.html` bằng trình duyệt.
3. Chọn mini game, chơi và kiểm tra bảng thành tích.

## Đưa lên GitHub Pages
1. Tạo repository GitHub mới.
2. Upload `index.html`, `README.md` và `.nojekyll` ở thư mục gốc repository (không upload file ZIP như một tệp duy nhất).
3. Mở **Settings → Pages**.
4. Ở **Build and deployment**, chọn **Deploy from a branch**.
5. Chọn branch `main` và folder `/(root)`, rồi bấm **Save**.
6. Chờ GitHub hoàn tất deploy; URL website sẽ xuất hiện tại phần Pages.

## Tính năng
- 15 chế độ mini game bóng đá.
- Chuyển ngôn ngữ Việt / Anh.
- Câu hỏi trắc nghiệm, đúng/sai, đoán cầu thủ, CLB, World Cup, giải đấu, sân vận động, kỷ lục, đội tuyển, penalty, logic, tốc độ, chuyển nhượng và chiến thuật.
- Điểm số, tên người chơi, số lượt chơi và kỷ lục được lưu bằng `localStorage`.
- Responsive cho điện thoại và máy tính.

## Giới hạn cần biết
Đây là **phiên bản frontend tĩnh**:
- Không có đăng nhập/tài khoản bảo mật thật.
- Bảng điểm chỉ tồn tại trong trình duyệt và thiết bị hiện tại; không phải leaderboard chung giữa nhiều người.
- Xóa dữ liệu trình duyệt có thể làm mất điểm đã lưu.
- Không cần đặt secret hay mật khẩu trong source code.

Nếu cần tài khoản thật, lưu điểm trên server và bảng xếp hạng dùng chung, cần triển khai thêm backend + database (ví dụ Supabase/Firebase hoặc API riêng).
