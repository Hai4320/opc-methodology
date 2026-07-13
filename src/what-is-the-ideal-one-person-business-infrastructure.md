# Hạ tầng lý tưởng cho doanh nghiệp một người

Sau khi nắm được phương pháp luận, chúng ta thường muốn bắt tay vào thực hành. Nhưng từ đây, độ khó tăng vọt, đặc biệt với những bạn không có nền tảng kỹ thuật, sẽ cảm thấy không biết bắt đầu từ đâu.

Đó là vì chúng ta thiếu một số hạ tầng — những hạ tầng mà bất kỳ doanh nghiệp nào hoạt động trên internet cũng cần, dùng để xử lý các tình huống chung của mọi loại nghiệp vụ. Với một số nghiệp vụ offline, hạ tầng có thể khác, nhưng nghiệp vụ offline một người thường khó mở rộng quy mô, nên ở đây chúng ta chỉ bàn về hạ tầng doanh nghiệp một người lấy internet và kinh tế số làm cốt lõi.

Để đưa ý tưởng và nghiệp vụ của mình vào thực tế, cho người dùng sử dụng được, chúng ta cần xây dựng một số hạ tầng. Hạ tầng không nhất thiết phải tự xây, cũng có thể dùng trực tiếp các nền tảng có sẵn. Ví dụ, WeChat Official Account là một hạ tầng đã rất trưởng thành cho mô hình kinh doanh đọc trả phí hoặc quảng cáo.

Vì sao cần xây hạ tầng của riêng mình
-------------

Vậy khi đã có nền tảng trưởng thành, tại sao chúng ta vẫn cần xây hạ tầng của riêng mình? Trước hết cần làm rõ một điều: không phải là không được dùng hạ tầng của nền tảng, mà là trong khi dùng hạ tầng của nền tảng, cần sở hữu một bộ hạ tầng hoàn toàn do mình kiểm soát, và kết nối liền mạch người dùng giữa hai bên. Biến lựa chọn duy nhất thành nhiều lựa chọn.

### Mô hình kinh doanh

Mô hình kinh doanh cốt lõi của nền tảng là gom người dùng lại để kiếm lợi từ đó. Vì vậy chiến lược của họ với từng loại người dùng, và ở từng giai đoạn vòng đời của nền tảng, là khác nhau — những chiến lược này có thể không phù hợp với giai đoạn cụ thể của chúng ta.

Ví dụ, trên một số nền tảng, nếu một tài khoản có sức ảnh hưởng quá lớn, nền tảng có thể tìm cách làm suy yếu tài khoản đó. Còn với những tài khoản quá nhỏ, nếu không thấy xu hướng tăng trưởng, nền tảng sẽ không phân bổ lưu lượng, thậm chí còn hạn chế cả lưu lượng bạn tự kéo về.

Mặt khác, ở giai đoạn đầu, nền tảng có thể hỗ trợ tài khoản theo một số hướng nhất định, khi đó bạn nhận được khá nhiều lưu lượng, nhưng lưu lượng này là chuyển từ người dùng khác sang.

Nếu không có hạ tầng riêng, bạn chỉ có thể mặc cho nền tảng thao túng. Nhưng nếu có hạ tầng riêng, khi chiến lược của nền tảng không còn phù hợp, bạn có thể dẫn người dùng về nền tảng của mình để tiêu thụ nội dung, mua sản phẩm.

### Rủi ro khóa tài khoản

Nền tảng có lằn ranh đỏ và luật ngầm riêng, thậm chí đôi khi còn xử lý nhầm. Nếu vô tình chạm vào những vấn đề này, tài khoản có thể bị khóa. Với người dùng cá nhân, điều đó có thể không sao, nhưng với người kinh doanh, nó có thể khiến sự nghiệp gây dựng nhiều năm đổ sông đổ biển, mọi nỗ lực tan thành mây khói.

![](images/image-10.png)

### Hình thái sản phẩm và thương hiệu

Dùng hạ tầng của nền tảng còn có thể khiến hình thái sản phẩm trở nên na ná nhau. Nếu sản phẩm theo hướng an toàn thì có thể không sao, nhưng nếu muốn đổi mới về hình thái sản phẩm, ràng buộc của hạ tầng nền tảng sẽ rất lớn.

Ví dụ, khóa học video của chúng tôi trước đây bán trên NetEase Cloud Classroom, nhưng khi muốn cung cấp cho học viên môi trường sandbox để thực hành, nền tảng không hỗ trợ. Kể cả khi chúng tôi tự phát triển sandbox, lúc cần kết nối với người dùng của NetEase Cloud Classroom mới phát hiện nền tảng không cung cấp API.

Để ngăn giảng viên kéo người dùng ra khỏi nền tảng, một số nền tảng thậm chí không cho phép xuất hiện tên miền độc lập trong tài liệu bài giảng. Kiểu quy tắc này ở giai đoạn giữa và cuối của nền tảng sẽ đặc biệt nghiêm ngặt.

### Hệ sinh thái lai

Chúng tôi cho rằng thực hành tốt nhất là trước hết sở hữu một hạ tầng hoàn toàn trong tầm kiểm soát, sau đó tận dụng tối đa tài nguyên và lưu lượng của các nền tảng: phân phối nội dung lên các nền tảng khác, rồi dẫn người dùng quay về hạ tầng của mình, hình thành một hệ sinh thái lai.

Vì sao phải tự xây hạ tầng
------------

Trên thị trường có rất nhiều phần mềm hoặc dịch vụ SaaS để xây hạ tầng, nhưng khi thử dùng, chúng ta sẽ thấy chúng ít nhiều đều có vấn đề.

### Giá cao

Giá cao là một vấn đề điển hình, vì phần lớn SaaS hướng tới doanh nghiệp.

![](images/image-13-1024x759.png)

Bảng giá của một dịch vụ SaaS điển hình

Mức giá có thể là rẻ với doanh nghiệp, nhưng với cá nhân lại đắt. Ở giai đoạn đầu của doanh nghiệp một người, chúng ta chưa kiếm được tiền, cũng không có vốn đầu tư mạo hiểm, nên nguồn lực rất hạn chế. Khoản đầu tư cả chục nghìn tệ mỗi năm với một cá nhân chưa có thu nhập vẫn là quá cao.

### Không mở cho cá nhân

Vấn đề khác là nhiều hạ tầng không mở cho cá nhân, ví dụ như thanh toán.

![](images/image-12-1024x534.png)

Yêu cầu hồ sơ đăng ký WeChat Pay

Một số dịch vụ thanh toán mở cho cá nhân thì lại không tích hợp sẵn với các hạ tầng có sẵn này. Điều đó khiến nhiều hạ tầng có sẵn không dùng trực tiếp được.

### SaaS thay vì tự host

Một rủi ro tiềm ẩn là nếu chúng ta không thể tự dựng hạ tầng mà dùng bản online do nhà cung cấp dịch vụ vận hành, sẽ có hai rủi ro. Một là công ty đột ngột phá sản — kể cả có hoàn tiền, nghiệp vụ của chúng ta cũng sụp đổ đột ngột, không có phương án cứu vãn.

![](images/image-14.png)

InVision đóng cửa

Rủi ro còn lại là nhà cung cấp đột ngột tăng giá. Vì nghiệp vụ đã nằm trên nền tảng của họ, trong thời gian ngắn không chuyển đi được, nên khi họ tăng giá, khả năng mặc cả của ta rất yếu. Nếu chúng ta kiếm được nhiều tiền thì chia phần cho nhà cung cấp cũng không sao, nhưng với doanh nghiệp một người, nếu chi phí quá cao, tổng thể có thể không còn lợi nhuận, thậm chí lỗ.

![](images/image-15.png)

WeChat Work đột ngột thu phí liên hệ bên ngoài

Hạ tầng lý tưởng cho doanh nghiệp một người
-----------

Có thể thấy, các dịch vụ hiện có để dựng hạ tầng ít nhiều đều có vấn đề. Vậy hạ tầng lý tưởng cho doanh nghiệp một người nên trông như thế nào?

### Đủ rẻ

Trước hết, nó phải đủ rẻ — ít nhất khi lượng người dùng còn ít thì phải rất rẻ. Có vậy chúng ta mới duy trì vận hành được trong lúc chưa kiếm ra tiền.

Phần mềm open source tự host là một lựa chọn rất tốt, vì khi lượng người dùng nhỏ, yêu cầu tài nguyên máy chủ rất thấp, chỉ cần thuê một máy ảo cấu hình thấp nhất là vận hành được.

SaaS online có kèm phương án tự host là lựa chọn còn nhàn hơn, vì bạn có thể chuyển sang tự host bất cứ lúc nào, không có rủi ro lock-in.

### Đủ khả năng kiểm soát

Mặt khác, hạ tầng cần đủ khả năng kiểm soát, để nghiệp vụ không bị gián đoạn vì quyết định của người khác. Có thể chịu chút ảnh hưởng, nhưng không thể vì ảnh hưởng đó mà cả nghiệp vụ sụp đổ.

Chẳng hạn, khi nền tảng bóp lưu lượng hoặc khóa tài khoản, ít nhất vẫn có cách khác để tiếp cận người dùng hiện có. Khi nhà cung cấp tăng giá điên cuồng, ít nhất có thể chuyển dữ liệu ra, nhanh chóng dựng lại trong môi trường của mình để người dùng tiếp tục sử dụng, không đến mức chảy sang đối thủ cạnh tranh.

### Cá nhân dùng được

Chúng ta mong hạ tầng này có thể vận hành với tư cách pháp lý cá nhân.

Vì chi phí đăng ký công ty rất cao — tuy phí đăng ký kinh doanh đã đủ rẻ, thậm chí có thành phố còn tặng cả con dấu, nhưng chi phí thực sự nằm ở việc làm sổ sách kế toán hàng tháng. Nếu không có địa điểm phù hợp, còn phải thuê mặt bằng; hai khoản này cộng lại một năm mất vài nghìn đến cả chục nghìn tệ.

Vì vậy chúng ta mong hạ tầng này có một giải pháp trọn vẹn cho người dùng cá nhân: đăng ký, đăng nhập, thanh toán, đẩy thông báo... đều dùng được với tư cách cá nhân.

### Đủ mở

Nếu muốn đổi mới về sản phẩm và mô hình kinh doanh, chắc chắn chúng ta sẽ phải sửa quy trình, giao diện và tính năng thông thường. Vì vậy hạ tầng cần đủ mở, cho phép chúng ta tùy biến và phát triển thêm một cách thuận tiện.

Mặt khác, hạ tầng này tốt nhất nên đủ phổ biến, để dễ tìm được kỹ sư phát triển thêm. Nếu không sẽ như các ngân hàng hiện nay: 43% ngân hàng toàn cầu phụ thuộc vào chương trình COBOL, nhưng đã rất khó tìm kỹ sư tương ứng để bảo trì.

### Hệ sinh thái sôi động

Kể cả tìm được kỹ sư để phát triển, quá trình phát triển luôn tốn thời gian, và do vấn đề về yêu cầu cũng như mức độ hiểu của kỹ sư, phải trải qua thời gian dài lặp đi lặp lại mới ra được sản phẩm tương đối hoàn thiện.

Nếu hạ tầng đang dùng có hệ sinh thái sôi động, nhiều tính năng có thể đã được phát triển sẵn và phát hành dưới dạng plugin miễn phí hoặc trả phí, chúng ta dùng ngay được.

Kể cả plugin có vài chi tiết chưa khớp nhu cầu, việc chỉnh sửa cũng rất nhanh, chi phí giảm đi đáng kể.

### Tương thích với phương pháp luận

Tất nhiên, điều quan trọng nhất là chúng ta mong hạ tầng này tương thích tốt với 《Phương pháp luận doanh nghiệp một người》, hỗ trợ trọn vẹn cho bộ phương pháp luận — có lẽ là duy nhất — dành cho doanh nghiệp một người này, để người dùng theo phương pháp luận có thể dùng ngay khi mở hộp, không phải tốn thêm thời gian vào việc thử nghiệm và phát triển các tính năng cơ bản nữa.
