# User pool và năng lực tiếp cận

Hạ tầng là gì
-------

Trong phương pháp luận doanh nghiệp một người 2.0, chúng tôi nói về ba mảng.

![](images/image-16-1024x382.png)

Ba nội dung lớn của phương pháp luận doanh nghiệp một người

Thứ nhất, doanh nghiệp một người là gì; thứ hai, hoạch định doanh nghiệp một người như thế nào; thứ ba, xây dựng nghiệp vụ một người ra sao.

Hai phần đầu, chúng tôi đã trình bày khá chi tiết trong các bài trước của chuyên mục — đều là nội dung ở tầng lý thuyết và nhận thức, chưa đi sâu vào thực hành. Đến phần thứ ba, tuy biết là phải xây dựng nghiệp vụ một người, nhưng cụ thể xây thế nào, triển khai ra sao, thao tác thế nào, lại thiếu một ví dụ hay điểm tựa có thể nhìn thấy, sờ thấy được.

Trong các nội dung trước, chúng tôi nhấn mạnh nhiều lần: doanh nghiệp một người không phải là nghiệp vụ một người.

Đây là khác biệt lớn nhất giữa phiên bản 2.0 và 1.0. Doanh nghiệp một người bao gồm rất nhiều nghiệp vụ một người, chỉ cần một trong số đó chạy được, chúng ta đã có thể đạt tự do tài chính.

Theo cách nói này, doanh nghiệp một người giống như trong hình: trong một doanh nghiệp một người có rất nhiều nghiệp vụ một người.

![](images/image-17-1024x503.png)

Mỗi nghiệp vụ tự chiến đấu riêng lẻ

Nhưng thực tế, một khi làm theo cách này, bạn sẽ thấy có rất nhiều nghiệp vụ một người, nhưng mỗi nghiệp vụ tự chiến đấu riêng lẻ, 1+1 có khi không đạt nổi 2, thậm chí nhỏ hơn 2.

Vì sức lực bị phân tán vào từng nghiệp vụ, nên các nghiệp vụ một người bắt buộc phải phối hợp với nhau. Một số tính năng và tài nguyên chung cần được tách ra, đặt vào một chỗ để dùng chung — chúng tôi gọi đó là hạ tầng. Đây chính là nội dung trọng tâm hôm nay.

![](images/image-18-1024x501.png)

Hạ tầng

User pool
---

Trước hết, thứ có thể tách ra từ mỗi nghiệp vụ là user pool. User pool là nơi người dùng đăng ký, đăng nhập và được giữ chân. Tính năng cơ bản của nó dĩ nhiên là đăng ký và đăng nhập.

### Đăng nhập chi phí thấp

Nhưng làm sao để người dùng đăng nhập với chi phí thấp nhất thì thực ra có nhiều điều đáng bàn.

Ví dụ ở Trung Quốc, nếu đăng nhập qua email, tỷ lệ email đến nơi rất kém. Nhiều người dùng không muốn dùng email, nhận email xác thực rất khổ sở. Mặt khác, nếu đăng nhập bằng số điện thoại, tỷ lệ đến nơi tạm ổn, hiện có nền tảng cloud để gửi, nhưng lại có vấn đề chi phí. Ngoài ra, giới kỹ thuật rất ghét đăng nhập bằng số điện thoại, còn người dùng phổ thông thì chấp nhận được — vấn đề chính vẫn là chi phí.

Sau khi thử nghiệm, chúng tôi thấy với doanh nghiệp một người, phương án đăng nhập chi phí thấp nhất là đăng nhập qua bên thứ ba.

![](images/image-19-1024x683.png)

Đăng nhập qua bên thứ ba

Trong tất cả các kiểu đăng nhập bên thứ ba, chúng tôi cho rằng đăng nhập WeChat là tốt nhất. Có hai lý do.

Thứ nhất, bạn có thể phủ được nhóm người dùng chủ lưu nhất với chi phí thấp nhất.

Tôi từng gặp nhiều người không có Alipay, nhưng rất hiếm gặp người không dùng WeChat. Thỉnh thoảng gặp người không dùng WeChat thì đó là người không dùng smartphone. Vì vậy, độ phủ của WeChat cực kỳ cao. Còn một bằng chứng với mẫu lớn hơn: dịch vụ trong nước của Fangtang chúng tôi chỉ hỗ trợ đăng nhập WeChat và thanh toán WeChat, nhiều năm qua số người dùng yêu cầu thanh toán bằng Alipay cực kỳ ít, chưa đến mười người.

Thứ hai, hệ sinh thái WeChat là một vòng khép kín hoàn chỉnh.

Ở Trung Quốc rất khó tìm được sản phẩm thay thế tương đương: Alipay có chức năng thanh toán nhưng không có chức năng mạng xã hội, cũng không có nền tảng phân phối nội dung và official account, không làm vận hành trên đó được; Weibo làm vận hành được nhưng không có chức năng thanh toán, tỷ lệ tin nhắn riêng đến nơi rất kém, không tiếp cận hiệu quả được.

Nhìn từ góc độ hệ sinh thái, chỉ có vòng khép kín của WeChat là rất hoàn chỉnh: có official account, đẩy thông báo, tin nhắn riêng, group và thanh toán.

Vì vậy, nếu chỉ tích hợp một bên thứ ba, chúng tôi khuyên chỉ tích hợp đăng nhập WeChat. Tất nhiên, bạn cũng có thể tích hợp đăng nhập của các nền tảng khác, không ảnh hưởng gì. Nhưng ở giai đoạn khởi đầu của doanh nghiệp một người, chúng tôi khuyên mọi người tập trung vào một nền tảng, đừng phân tán sức lực. Đợi nghiệp vụ chạy ổn rồi hãy quay lại hoàn thiện. Dù sao tích hợp nhiều bên rốt cuộc cũng thêm chi phí phát sinh.

Năng lực tiếp cận
----

Tiếp theo, có user pool rồi mà không tiếp cận được người dùng thì user pool đó thực ra vô nghĩa. Ở chỗ bạn và ở nền tảng khác chẳng khác gì nhau, thậm chí nền tảng khác còn tiếp cận được người dùng.

Vì vậy, làm user pool nhất định phải có năng lực tiếp cận — tức có thể gửi tin nhắn hoặc thông báo cho người dùng bằng cách nào đó — có vậy mới tái sử dụng được lưu lượng và bán sản phẩm lần hai.

![](images/image-20-1024x679.png)

Các cách tiếp cận

Các cách tiếp cận thường gặp gồm:

### Thông báo trong APP

Hiệu quả có lẽ tốt nhất trong mọi kênh đẩy thông báo, độ tự do cũng cao nhất. Nhưng với doanh nghiệp một người thì lại không phù hợp nhất.

Vì tiền đề của thông báo APP là người dùng phải cài APP của bạn, chi phí này giờ đã rất cao; đưa APP lên store cũng rất phiền phức, đặc biệt với cá nhân thì gần như không thể, nên không phù hợp ở giai đoạn khởi đầu.

### SMS

Gửi qua nền tảng cloud, tỷ lệ đến nơi khá ổn, nhưng phải dùng mẫu tin nhắn đăng ký sẵn. Ngoài ra do tin nhắn rác quá nhiều, rất nhiều người dùng không đọc SMS.

### Email

Email có tỷ lệ đến nơi thấp và tính thời gian thực kém. Nhiều người dùng đã bỏ email; kể cả thỉnh thoảng có xem thì cũng có khi một tuần, thậm chí một tháng mới mở một lần.

### Tin nhắn group

Đây là một trong hai kênh hiệu quả nhất theo thử nghiệm của chúng tôi — kênh còn lại là tin nhắn mẫu / tin nhắn đăng ký của WeChat.

Có thể thông báo tin cho tất cả thành viên trong group và tương tác, trao đổi thời gian thực qua mấy cách sau:

1.  Ghim tin trong group: ghim tin quan trọng để mọi thành viên đều thấy. Tin ghim có thể là thông báo quan trọng, lịch hoạt động hoặc ra mắt sản phẩm mới.
2.  Việc cần làm trong group: dùng tính năng nhắc việc của group WeChat để tạo mục cần làm, nhắc thành viên chú ý và tham gia. Mục nhắc việc có thể đặt giờ nhắc, đảm bảo thành viên không bỏ lỡ thông tin quan trọng.
3.  Phát lì xì tương tác: phát lì xì (red packet) để tăng độ sôi nổi trong group. Lì xì không chỉ thu hút sự chú ý của thành viên mà còn tăng mức độ quan tâm và tham gia của họ với thông điệp.
4.  Tương tác thời gian thực: sau khi đăng tin trong group, phản hồi kịp thời ý kiến và câu hỏi của thành viên. Kiểu tương tác thời gian thực này giúp bạn nhanh chóng phát hiện vấn đề trong thông điệp và điều chỉnh, xử lý kịp thời.

### Tin nhắn mẫu hoặc tin nhắn đăng ký của WeChat

Một kênh tin một chiều khá tốt khác là tin nhắn mẫu (template message) hoặc tin nhắn đăng ký (subscription message) của WeChat.

Do quyền gửi tin nhắn đăng ký khá khó xin — tài khoản thường không lấy được quyền "đăng ký một lần, gửi không giới hạn" — nghĩa là người dùng xem xong tin phải đăng ký lại, thao tác bất tiện. Vì vậy chúng tôi thường dùng tin nhắn mẫu. Tin nhắn mẫu tuy bị nhiều hạn chế về hình thức và nội dung đẩy, nhưng không bị bóp lưu lượng, tính thời gian thực cũng rất cao.

Thông qua API đẩy tin của WeChat, bot group (Wechaty) hoặc phương án script trên điện thoại (Auto.js), chúng ta có thể tự động hóa năng lực tiếp cận.
