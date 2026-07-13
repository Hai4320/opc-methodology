# Dựng hạ tầng doanh nghiệp một người

Qua thảo luận ở các phần trước, chúng tôi cho rằng hạ tầng của doanh nghiệp một người cần có ba "bể chứa" cốt lõi và bốn năng lực then chốt: user pool, content pool, product pool; năng lực tiếp cận, năng lực thanh toán, năng lực tự động hóa và năng lực crowdsourcing.

![](images/image-39-1024x457.png)

Ba pool bốn năng lực của hạ tầng

Xác định rõ mục tiêu rồi, chúng ta có thể bước vào giai đoạn dựng.

Cách dựng
----

Lựa chọn đầu tiên phải đưa ra là: tự phát triển hoặc thuê người phát triển (outsourcing); hay dựng trên nền dự án open source, ví dụ dựng trên WordPress.

![](images/image-40-1024x641.png)

Lựa chọn cách dựng

Mỗi đội nhóm có lựa chọn riêng; tình cờ chúng tôi đã chọn cả hai, ở đây xin chia sẻ trải nghiệm của chính chúng tôi.

### Tự phát triển

Ban đầu chúng tôi chọn tự phát triển, vì lúc đó thấy WordPress quá cồng kềnh. Nhưng giờ nghĩ lại, phần nhiều là do tự cho rằng năng lực phát triển của mình dư dả, lầm tưởng chi phí thời gian và kỹ năng thấp — điều cuối cùng được chứng minh là một phán đoán sai.

Từ 2019 đến 2022, chúng tôi chủ yếu tự phát triển; trong thời gian đó chúng tôi phát triển chủ yếu nền tảng khóa học online, gồm website khóa học cùng một số sandbox, môi trường chạy trực tuyến — toàn bộ là nền tảng tự phát triển độc lập.

Ưu điểm của tự phát triển là kiểm soát hoàn toàn, tùy biến được đến từng pixel, hiện thực hóa 100% tính năng và chi tiết trong đầu.

Nhưng nhược điểm là khối lượng công việc khổng lồ, đặc biệt khi đã phát triển nhiều hệ thống nghiệp vụ thì chi phí bảo trì cực cao. Chúng tôi đã tách phần dùng chung từ nhiều dự án, hình thành framework full-stack riêng, thống nhất frontend và backend, nhưng chi phí bảo trì framework vẫn rất cao. Ví dụ, framework nâng cấp xong, dự án mới đương nhiên dùng ngay được, nhưng có thể phải quay lại nâng cấp các dự án cũ — điều này rất đau khổ.

### Phối trộn trên nền WordPress

Đến 2023 và 2024, chúng tôi nhận ra lượng lớn thời gian phát triển bị tiêu vào những việc vốn có thể tránh, hơn nữa khối lượng nghiệp vụ tăng lên cuối cùng có thể buộc chúng tôi phát triển một hệ quản trị nội dung (CMS) — thực chất lại tương đương làm một WordPress nữa. Vì vậy, chúng tôi quay lại dùng WordPress.

Dựng trên WordPress, ưu điểm trước hết là các tính năng phổ thông đều có sẵn, một số tính năng hơi đặc thù có thể tích hợp qua plugin. Ví dụ, khi dựng cổng thông tin Fangtang 07, nếu tự phát triển, ít nhất phải mất nửa năm mới lặp xong hết chi tiết. Nhưng nhờ dùng WordPress và mua một theme 600 tệ, chúng tôi dựng xong rất nhanh và đạt trải nghiệm đọc khá tốt.

REST API của WordPress cũng rất hoàn thiện, có thể mở rộng tính năng ở tầng API qua plugin, thậm chí phát triển frontend độc lập, gọi REST API để mở rộng.

Nếu cứ phải tìm nhược điểm, thì độ hoàn thiện tính năng và vấn đề hiệu năng tiềm ẩn là hai vấn đề lớn của WordPress. Vấn đề độ hoàn thiện là: khi có thể "lười" (cài và mua plugin để làm), kết quả cuối cùng có thể lệch 10% so với hiệu quả ta muốn. Tất nhiên đây chắc chắn không phải lỗi của WordPress! 😂

Vấn đề tiềm ẩn còn lại là khi dùng WordPress vận hành website có lượng người dùng hoặc nội dung quy mô lớn, hiệu năng có thể thành vấn đề. Dù phần lớn vấn đề hiệu năng do plugin gây ra, đây vẫn là một thách thức. Có điều số người dùng sản phẩm của chúng tôi còn cách quy mô đó rất xa — vẫn đang nỗ lực để "được" gặp vấn đề này.

![](images/image-41-1024x467.png)

So sánh ưu nhược điểm các cách dựng

### Thực hành tốt nhất

Thực hành tốt nhất theo chúng tôi là: trước hết dựng trên WordPress sản phẩm khả thi tối thiểu (MVP) của nghiệp vụ và làm crowdfunding, đồng thời có thể đặt website chính thức và tài liệu sản phẩm trên nền tảng này. Khi nghiệp vụ tăng trưởng và lượng người dùng tăng lên, ta mới tự phát triển.

![](images/image-42-1024x575.png)

Thực hành tốt nhất

Kể cả khi tự phát triển, chúng ta vẫn có thể phối trộn với WordPress ở ba tầng, lần lượt thoát khỏi ràng buộc về giao diện, backend và cơ sở dữ liệu.

Trước hết, có thể dùng WordPress làm backend thông qua REST API, tiết kiệm lượng lớn công việc.

Sau đó, nếu hệ thống quản trị của WordPress vẫn chưa đủ hiệu quả, ta có thể dùng chung cơ sở dữ liệu: tự phát triển một hệ thống mới, đọc dữ liệu trực tiếp từ database của WordPress. Như vậy hiệu năng hệ thống mới do code của ta bảo đảm, dữ liệu thông suốt, hai bên chạy song song được.

Nếu vậy vẫn chưa đủ, ta còn có thể tiến thêm một bước: xây một hệ thống hoàn toàn độc lập, nhưng liên kết người dùng qua đăng nhập thống nhất. Ta có thể liên kết tài khoản WordPress với WeChat. Hệ thống mới tuy khác cơ sở dữ liệu, nhưng qua đăng nhập WeChat dùng chung Open ID, ta vẫn định vị được thông tin liên quan của người dùng. Nếu cần thêm thông tin người dùng, có thể đọc dữ liệu tương ứng qua REST API.

Qua kiểu phối trộn nhiều tầng như vậy, chúng ta có thể hiện thực hóa lượng phát triển tối thiểu, lại có tự do về giao diện và hiệu năng, đồng thời giảm chi phí bảo trì hết mức có thể.

Phương án tham khảo: Fangtang OPB
----------

Fangtang OPB là bộ plugin WordPress do chúng tôi phát triển; dùng phối hợp với BudCoder và FlowDeer có thể phủ ở mức độ cao "ba pool bốn năng lực".

### Giao diện sản phẩm

Dưới đây là giao diện của nó; gần đây chúng tôi có thể sẽ chỉnh sửa đôi chút, ảnh chụp màn hình dưới đây để mọi người tham khảo.

#### Tích hợp tài khoản WeChat

![](images/image-43-1024x577.png)

1.  Chúng tôi thêm tính năng đăng ký bằng mã mời. Nhờ vậy khi sản phẩm chưa ra mắt, có thể chạy thử nghiệm nội bộ — chỉ ai biết mã mời mới đăng nhập được.
2.  Vì phải hỗ trợ vận hành với tư cách cá nhân, chúng tôi hiện thực hóa đăng nhập cho official account chưa xác thực thông qua cơ chế tin nhắn chiều lên (người dùng nhắn tin đến).
3.  Tính năng chuyển tiếp callback hỗ trợ một official account dùng trên nhiều website. Khi nhận được tin nhắn, nó chuyển tiếp đến địa chỉ đích trước; nếu địa chỉ đích không xử lý, mới xử lý theo cấu hình của website hiện tại.

#### WeChat Pay

![](images/image-44-1024x579.png)

1.  Cấu hình năng lực WeChat Pay tiêu chuẩn.
2.  Tính năng quầy thanh toán, gồm ứng dụng thanh toán và quản lý đơn hàng. Chỉ cần một lần chuyển trang và một request HTTP xác thực là hoàn tất giao dịch.
3.  Hiện thực hóa cổng WeChat cho WooCommerce, gồm WeChat chính thức và XorPay. Mọi plugin hỗ trợ WooCommerce đều dùng thẳng được.

#### Đẩy thông báo

![](images/image-45-1024x577.png)

1.  Hiện thực hóa đăng ký theo dõi theo chuyên mục bài viết. Bạn có thể theo dõi một chuyên mục và các cập nhật của nó; khi đăng bài, có thể bấm nút đẩy để gửi cho những người theo dõi chuyên mục đó.
2.  Người dùng còn có thể quản lý các lượt theo dõi này qua một giao diện quản lý.
3.  Còn hỗ trợ theo dõi bình luận, làm tính thời gian thực cao hơn, có thể tăng mạnh tính tương tác.

#### Crowdfunding sản phẩm

![](images/image-46-1024x577.png)

Bản crowdfunding rút gọn hiện thực hóa trên WooCommerce.

1.  Khi đăng trang sản phẩm, chọn bật crowdfunding, đặt thời hạn và số tiền mục tiêu.
2.  Nhúng một shortcode trạng thái crowdfunding vào trang bài viết, nó sẽ hiển thị tiến độ hiện tại của sản phẩm.
3.  Trang quản trị sản phẩm cung cấp tính năng hoàn tiền hàng loạt.

### Cấu trúc hạ tầng và độ phủ năng lực

Chúng ta cùng nhìn lại và đối chiếu cấu trúc cùng năng lực của hạ tầng doanh nghiệp một người.

![](images/image-47-1024x567.png)

Có thể thấy, độ phủ tổng thể của bộ plugin Fangtang OPB là rất cao, ngoại trừ vài chỗ được khoanh đỏ:

1.  Product pool: chúng ta cần năng lực xây nhanh các nhu cầu đơn giản.
2.  Về năng lực tự động hóa: vì WordPress chỉ là website kiến trúc B/S nên không thật phù hợp.
3.  Mảng năng lực crowdsourcing thì chưa được phủ.

### Dùng phối hợp với BudCoder và FlowDeer

![](images/image-48-1024x365.png)

Khi kết hợp thêm hai công cụ BudCoder và FlowDeer, chúng ta có thể nâng độ phủ lên nữa.

BudCoder có thể dùng AI sinh plugin WordPress; với các nhu cầu tương đối đơn giản, khoảng dưới 300 dòng code, nó xử lý được. Và khi năng lực của các model AI tăng lên, hiệu quả xử lý của nó sẽ ngày càng tốt. Còn workflow FlowDeer trong việc phân phối nội dung hiện đã rất trưởng thành.

Có chúng, ta có thể phủ nốt phần còn thiếu trước đó: sinh và hoàn thành nhu cầu đơn giản của product pool, cùng phân phối nội dung trong năng lực tự động hóa. Cả hệ thống chỉ còn duy nhất năng lực crowdsourcing là chưa phủ.

Kịch bản mà nghiệm thu tự động phải đối mặt quá phức tạp, khó có một plugin phổ quát xử lý được, nhưng có thể xử lý riêng bằng hệ thống điểm + plugin tự phát triển/tự sinh; nếu chấp nhận nghiệm thu thủ công, có thể mua các plugin thương mại trưởng thành tương ứng.
