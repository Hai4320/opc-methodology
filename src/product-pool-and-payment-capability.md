# Product pool và năng lực thanh toán

Product pool
---

Chúng ta đã có user pool và content pool, giờ hãy đưa tầm mắt quay lại phía nghiệp vụ.

Thực tế, giữa nhiều nghiệp vụ tồn tại rất nhiều điểm chung — chẳng hạn vì chúng đều nhằm tạo ra lợi nhuận, nên cần rất nhiều tính năng và năng lực chung liên quan đến thương mại.

Mặt khác, khi đã có user pool và content pool, bản thân nghiệp vụ chuyển thành một module cắm-rút được (pluggable). Nó không cần quan tâm đến các tính năng liên quan đến nội dung và người dùng; chỉ cần nối vào user pool và content pool của chúng ta là bắt đầu vận hành được, không cần phải là một nghiệp vụ độc lập hoàn chỉnh nữa.

Vì vậy, chúng tôi gom các nghiệp vụ này thành một loạt component nghiệp vụ, đồng thời dùng "product pool" để chứa chúng.

![](images/image-26-1024x858.png)

Từ đa nghiệp vụ sang product pool + component nghiệp vụ

Năng lực thanh toán
----

Thứ product pool cần nhất là năng lực thanh toán — điều này dễ hiểu. Vì với doanh nghiệp, mục đích cốt lõi chắc chắn là kiếm tiền, mà không có chức năng thanh toán thì không thể tạo ra doanh thu.

### Nhà cung cấp dịch vụ thanh toán

#### Nhà cung cấp thông dụng

Ở Trung Quốc, thông dụng có WeChat Pay và Alipay, nhưng cả hai đều không mở cho cá nhân, phải đăng ký doanh nghiệp hoặc hộ kinh doanh cá thể.

Chi phí đăng ký doanh nghiệp tập trung ở sổ sách kế toán và mặt bằng. Còn địa chỉ đăng ký hộ kinh doanh cá thể ở một số tỉnh cũng đã có yêu cầu, điều này rõ ràng đẩy chi phí lên, vì địa điểm văn phòng thực chất là chi phí cố định, mà nhà ở tại nhiều thành phố lại không được phép dùng để đăng ký. Yêu cầu cụ thể có thể hỏi cơ quan quản lý công thương địa phương, chính sách mỗi nơi mỗi khác, nhưng nhìn chung, điều này quả thực làm tăng chi phí.

#### Nhà cung cấp mở cho cá nhân

May mắn là, vẫn còn một số nhà cung cấp dịch vụ thanh toán mở cho cá nhân.

Như XorPay — thực chất là một nền tảng thanh toán cho hộ kinh doanh siêu nhỏ, trên nền tảng này bạn có thể tích hợp WeChat và Alipay. Có thể tự đăng ký kích hoạt, địa chỉ cửa hàng dùng được địa chỉ nhà ở, ảnh cửa hàng dùng được ảnh cổng nhà. Ngoài ra tôi nhớ nó có khoản phí kích hoạt một trăm tệ, có thể xác nhận lại với bộ phận hỗ trợ.

![](images/image-27.png)

Giải thích về phí kích hoạt trong FAQ của XorPay

Một số phương án thanh toán của Alipay cũng mở cho cá nhân, ví dụ "Đương diện phó" (thanh toán trực diện), nhưng bối cảnh sử dụng hơi lệch, vì nhìn tên là biết, nó vốn dành cho thanh toán mặt đối mặt.

So sánh lại, tôi cho rằng dùng nền tảng thanh toán hộ kinh doanh siêu nhỏ như XorPay là phương án tốt hơn: hỗ trợ nhiều kênh hơn, tiền người dùng thanh toán cũng vào thẳng tài khoản của chúng ta — khá an toàn.

Tích hợp thanh toán
----

Có năng lực thanh toán rồi, còn phải kết nối nó với các component nghiệp vụ thì mới dùng được.

Nếu chỉ có một nghiệp vụ thì không sao; nhưng khi nghiệp vụ nhiều lên, chúng ta sẽ đối mặt hai vấn đề.

Thứ nhất, mỗi nghiệp vụ đều phải tích hợp riêng, thực sự rất phiền. Vì thứ nhà cung cấp đưa ra thường là tích hợp ở tầng hệ thống chứ không phải tầng ứng dụng, cả quy trình khá rườm rà.

Mặt khác, một số hệ thống về thiết kế không hỗ trợ đa nghiệp vụ. Nếu dùng thanh toán chính thức của WeChat, thư mục thanh toán (payment directory) của nó có giới hạn, tối đa 5. Vậy nghiệp vụ của chúng ta vượt quá năm cái thì sao? Lúc đó phải tự tìm giải pháp.

### Phương án tự xây quầy thanh toán

Giải pháp của chúng tôi là xây một quầy thanh toán (cashier) của riêng mình, cách này giải quyết tốt cả hai vấn đề trên.

Nói đơn giản, nó coi mỗi nghiệp vụ là một ứng dụng, rồi cấp cho ứng dụng đó một tham số. Người dùng mang tham số này chuyển hướng đến trang thanh toán để trả tiền. Thanh toán xong, quầy thanh toán dùng ID đơn hàng này để chuyển hướng tiếp; người dùng mang ID đơn hàng đã thanh toán quay lại nghiệp vụ để xác thực, thế là hoàn tất giao dịch.

![](images/Screen-Shot-2024-07-07-at-12.59.57-PM-1024x669.png)

Sơ đồ quy trình của quầy thanh toán

Ý nghĩa của quầy thanh toán là: nhiều nghiệp vụ của chúng ta có thể dùng chung hệ thống thanh toán và đơn hàng.

Nếu phát triển đủ nhiều nghiệp vụ, bạn sẽ hiểu việc phát triển riêng hệ thống thanh toán và đơn hàng cho từng nghiệp vụ phiền đến mức nào. Tuy code có thể tái sử dụng, nhưng nếu nó rải rác trong từng nghiệp vụ, việc bảo trì sẽ rất mệt. Vì vậy, làm nó thành một component dùng chung, đóng gói thành một năng lực hạ tầng chuẩn là rất cần thiết.

### Cổng thanh toán WooCommerce

Nếu dùng WordPress, có một phương án đơn giản hơn: thêm cổng thanh toán (payment gateway) cho WooCommerce.

Phần lớn plugin WordPress liên quan đến thanh toán đều dùng WooCommerce. Nó vốn là plugin bên thứ ba, sau bị công ty mẹ của WordPress mua lại; tuy vẫn vận hành với thương hiệu độc lập nhưng thực chất là sản phẩm chính thức.

Nó cung cấp đầy đủ các tính năng về thanh toán và sản phẩm, nhưng thiếu một số nhà cung cấp thanh toán thông dụng ở Trung Quốc.

![](images/image-29-1024x644.png)

Giao diện cài đặt cổng thanh toán WooCommerce

Chúng ta chỉ cần thêm vài cổng, ví dụ cổng thanh toán chính thức của WeChat hoặc cổng XorPay, thế là mọi ứng dụng hỗ trợ WooCommerce đều dùng thẳng được năng lực thanh toán của chúng ta.

Năng lực gọi vốn cộng đồng (crowdfunding)
----

### Ý nghĩa của crowdfunding

Trong phương pháp luận doanh nghiệp một người, tôi liên tục nhấn mạnh ý nghĩa quan trọng của crowdfunding. Vì chuyện quan trọng phải nói ít nhất ba lần.

Sức lực của doanh nghiệp một người cực kỳ hạn chế, nên chi phí thử-sai rất cao — không chỉ là tiền, nó còn là chi phí cơ hội, vì số việc chúng ta làm được trong một năm rất giới hạn. Do đó, năng lực dùng crowdfunding để kiểm chứng là cực kỳ quan trọng.

Trong các phương pháp luận khởi nghiệp chủ lưu, thứ cần kiểm chứng cốt lõi là hai điều: một là tuyên bố giá trị (value proposition), tức sản phẩm của chúng ta rốt cuộc có giá trị với người dùng mục tiêu hay không; hai là kênh tiếp cận (channel), tức sản phẩm có giá trị với nhóm người này, nhưng nó có tăng trưởng được không? Có đạt được quy mô ta muốn không?

![](images/image-30-1024x590.png)

Hai giả thuyết quan trọng nhất

### Kiểm chứng đa điểm

Kiểm chứng bằng crowdfunding là một kiểu kiểm chứng đa điểm đơn giản thô bạo: kiểm chứng một lượt cả tuyên bố giá trị lẫn kênh tiếp cận. Chính xác mà nói, nó có thể không kiểm chứng được tăng trưởng giai đoạn sau, nhưng kiểm chứng được kênh giai đoạn đầu.

Mức đạt mục tiêu của crowdfunding, ở mức độ nào đó, chính là cận dưới của quy mô giai đoạn đầu; khi người dùng ít, ta có thể đặt nó ở điểm hòa vốn; khi người dùng đủ nhiều, thậm chí có thể đặt nó ở quy mô ta kỳ vọng — nhiều dự án trên Kickstarter có nguồn thu chính đến từ crowdfunding.

Việc crowdfunding kiểm chứng tuyên bố giá trị là chính xác hơn cả — đó là kiểm chứng thật bằng tiền thật. Nếu ta làm landing page hay phỏng vấn để kiểm chứng tuyên bố giá trị, nhiều người dùng sẽ nói với ta rằng thứ này hay đấy, để về thử xem, rồi chẳng có gì tiếp theo nữa. Nhưng kiểm chứng qua crowdfunding, ai thật lòng thấy hay sẽ móc ví, ai chỉ khen ngoài miệng sẽ không bỏ khoản tiền này — kết quả kiểm chứng cực kỳ chân thực.

### Đưa bán hàng lên trước

Thứ hai, crowdfunding đưa khâu bán hàng lên trước. Kiểm chứng đạt thì việc bán hàng đã hoàn thành; kiểm chứng không đạt thì ta không đi xây những sản phẩm bán không được. Điều này rất quan trọng: với doanh nghiệp một người, trong chi phí nghiệp vụ có lẽ hơn 80% là chi phí xây dựng, mà nếu trước khi xây ta đã biết nó bán không được thì có thể không làm nữa, tiết kiệm được lượng chi phí khổng lồ.

Tất nhiên có bạn sẽ nói: đồ của tôi còn chưa làm ra, sức hút với người dùng rõ ràng chưa đủ, chiến dịch crowdfunding không thể trình diễn tốt sản phẩm, nên người dùng mới không mua — điều này có thể xảy ra.

Nhưng giải pháp không phải là đi phát triển sản phẩm, mà là làm video crowdfunding hoặc bản demo cho mọi người dùng thử lúc crowdfunding thật chỉn chu, để người ủng hộ có thể trải nghiệm được hiệu quả cuối cùng khi ta hoàn thành.

Cũng có bạn cho rằng crowdfunding phụ thuộc quá nhiều vào năng lực bán hàng, nhưng quá trình phát triển sản phẩm không hề nâng cao năng lực bán hàng của bạn — nghĩa là, sản phẩm lúc crowdfunding bán không được thì phát triển xong đem bán, khả năng vẫn bán không được là rất cao.

### Các thành phần cấu thành crowdfunding

Thực tế, các thành phần của một hệ thống crowdfunding rất đơn giản.

-   Thu tiền
-   Thống kê điều kiện đạt mục tiêu
-   Hoàn tiền hàng loạt hoặc giao hàng

#### Crowdfunding bằng group

Chúng ta thậm chí có thể hoàn thành crowdfunding rất tốt chỉ với một group, không cần mua bất kỳ phần mềm nào.

Ví dụ, ta làm hình thức trả phí vào group — thế là giải quyết xong khâu thu tiền; thống kê điều kiện đạt mục tiêu thì làm qua "nối đuôi" (điểm danh theo chuỗi) trong group: ai trả phí rồi thì nối một dòng, là biết ngay phần mềm bán được bao nhiêu bản, khóa học bán được bao nhiêu suất, đạt hay chưa — cả group nhìn là rõ. Hoàn tiền hàng loạt cũng đơn giản: chỉ cần phát một lì xì group định mức, mỗi người nhận đúng một suất cố định, thế là tiền hoàn về.

Về giao hàng, làm sơ sài một chút thì có thể đặt phần mềm hoặc video lên ổ đĩa mạng, cung cấp link qua thông báo group, hoặc đưa thẳng vào mục file của group — tùy tính năng group hỗ trợ.

![](images/image-31.png)

Thực hiện crowdfunding qua group

Bạn thấy đấy, crowdfunding là một cách tư duy chứ không phải một hệ thống cố định — không phải cứ có hệ thống mới làm được crowdfunding; kể cả chỉ có một group, ta vẫn xử lý được rất tốt.

Hơn nữa, như bước hoàn tiền hàng loạt, nếu không hoàn hàng loạt được thì cùng lắm hoàn thủ công, vất vả hơn chút thôi. Chủ yếu là kịch bản phải hoàn tiền thường là lúc không đạt mục tiêu, nên số người dùng lại không quá nhiều — vì người dùng nhiều thì đã đạt mục tiêu rồi.

#### Crowdfunding bằng WooCommerce

Tất nhiên, nếu thường xuyên làm crowdfunding, dùng group sẽ khá phiền. Nếu dùng WordPress, ta cũng có thể làm bằng plugin WordPress. Thực ra WooCommerce đã hoàn chỉnh một quy trình bán hàng chuẩn: mua hàng và giao hàng.

Chỗ cần sửa chỉ có hai. Thứ nhất, có thể cần thêm một shortcode để hiển thị doanh số của sản phẩm và thống kê đạt mục tiêu hay chưa, ví dụ như hình dưới.

![](images/image-32.png)

Hiệu ứng hiển thị của shortcode crowdfunding sản phẩm

Thứ hai, cần một nút hoàn tiền hàng loạt. Nhưng thực ra đều là tùy chọn — không có nút này vẫn hoàn tiền được, chỉ phiền hơn chút.

![](images/image-33.png)

Thêm nút hoàn tiền hàng loạt cho WooCommerce

Cho nên, đừng nghĩ crowdfunding phiền phức, cũng đừng nghĩ nhất định phải có hệ thống mới làm được — nó là một cách tư duy, mong mọi người dùng nó. Với doanh nghiệp một người và các đội nhóm nhỏ thiếu nguồn lực, điều này thật sự vô cùng quan trọng.

![](images/image-34-1024x463.png)

Năng lực crowdfunding về bản chất là năng lực thanh toán

Suy cho cùng, năng lực crowdfunding về bản chất là một dạng năng lực thanh toán — nó thực ra là một sự đổi mới về mô hình kinh doanh. Nếu ta làm việc component hóa và tự động hóa năng lực thanh toán đủ tốt, sẽ thấy những mô hình kinh doanh trông có vẻ sáng tạo như crowdfunding, "học xong miễn phí"... đều rất dễ hiện thực hóa.
