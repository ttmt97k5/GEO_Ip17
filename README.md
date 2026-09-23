# iPhone 17 Info — bản giao diện đầu mở rộng nội dung

Website thông tin độc lập về iPhone 17. Không phải website chính thức của Apple.

## Chạy ở máy
Mở `index.html` bằng Live Server trong VS Code (hoặc dùng `python -m http.server 5500`).

## Đưa lên GitHub Pages
1. Tạo repository công khai, ví dụ `GEO_iPhone17`.
2. Nếu username là `abc`, chạy: `python configure_site.py https://abc.github.io/GEO_iPhone17/` (trước khi upload).
3. Upload **các file nằm bên trong thư mục này** sao cho `index.html` nằm ở gốc repo.
4. Settings → Pages → Deploy from a branch → main → / (root) → Save.
5. Sau khi deploy, thử `/`, `/faq.html`, `/robots.txt` và `/sitemap.xml`.
6. Đăng ký Search Console rồi yêu cầu indexing; không bảo đảm Google hay AI sẽ trích dẫn chỉ vì deploy website.

## Nội dung và nguồn
Dữ liệu chính từ Apple Newsroom và thông số chính thức Apple iPhone 17/16. Đừng cập nhật giá theo thời điểm hiện tại nếu chưa kiểm tra lại. Nếu chỉnh sửa FAQ, đồng bộ nội dung JSON-LD trong `faq.html`.

## Tệp hỗ trợ làm slide
`tai_lieu/keyword_research.csv` và `tai_lieu/ai_search_test.csv` để làm báo cáo/chụp bằng chứng *riêng*, không hiển thị trong menu hoặc nội dung web.
