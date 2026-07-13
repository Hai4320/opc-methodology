Doanh nghiệp một người ≠ nghiệp vụ một người
=========

Cấu trúc của cuốn sách này gồm ba mô-đun lớn: định nghĩa doanh nghiệp một người, hoạch định doanh nghiệp một người, xây dựng nghiệp vụ một người. Bạn đọc tinh ý có lẽ đã nhận ra, so với hai phần đầu, tiêu đề của phần thứ ba có chút khác biệt------đây không phải là ngẫu nhiên.

![](images/image-72-1024x240.png)

Thực ra trong phiên bản đầu tiên của phương pháp luận, mô-đun thứ ba vốn là "xây dựng doanh nghiệp một người". Nhưng qua hai năm thực hành và lặp lại gần đây, chúng tôi phát hiện rằng nếu đánh đồng doanh nghiệp một người với nghiệp vụ, ta rất dễ rơi vào ngộ nhận trong tư duy.

Doanh nghiệp một người không đồng nghĩa với nghiệp vụ một người
-----------

Nếu chúng ta đánh đồng doanh nghiệp một người với một nghiệp vụ duy nhất, thì một khi nghiệp vụ đó thất bại, ta chỉ còn cách vứt bỏ cả doanh nghiệp và làm lại từ đầu. Cách làm này đặc biệt phổ biến ở các công ty khởi nghiệp, và trước đây chúng tôi cũng đã áp dụng mô hình này mà không suy nghĩ kỹ.

Tuy nhiên, khi suy ngẫm sâu hơn sẽ thấy, việc dự án và công ty gắn chặt với nhau ở các công ty khởi nghiệp phần lớn là do cấu trúc cổ phần và phương thức thanh lý tài sản gây ra. Với doanh nghiệp một người, toàn bộ tài sản thường do một người nắm giữ, nên không tồn tại những lo ngại kiểu này.

Đứng trên vai những nghiệp vụ thất bại
---------

Mặt khác, với doanh nghiệp một người, nghiệp vụ thất bại là chuyện thường tình, vài tháng lại gặp một lần. Nếu ta vứt bỏ mọi thứ của dự án thất bại rồi bắt đầu lại, thì thường sẽ giậm chân tại chỗ. Ngược lại, nếu ta biết tận dụng triệt để các thành quả trung gian của dự án thất bại, thì lần sau có thể đứng trên vai chúng mà tiến lên. Cứ thế thua rồi lại chiến, cuối cùng sẽ thành công.

![](images/image-73-1024x456.png)

Một doanh nghiệp một người có thể có nhiều nghiệp vụ một người

Sự khác biệt nhỏ trong nhận thức này có thể bị phóng đại khi thực thi, dẫn đến những kết quả hoàn toàn khác nhau. Chẳng hạn, trước đây tôi thường đăng ký một tên miền riêng cho mỗi dự án, dùng một hệ thống người dùng độc lập. Như vậy các thương hiệu hoàn toàn tách biệt, không ảnh hưởng lẫn nhau. Nhưng điều đó cũng khiến một khi dự án đóng cửa, người dùng bị mất hoàn toàn.

Cách làm hiện tại của tôi là đưa tất cả dự án vào dưới thương hiệu Fangtang, dùng tên miền cấp hai của Fangtang, dùng hệ thống người dùng thống nhất của Fangtang. Như vậy, người dùng được chia sẻ giữa nhiều nghiệp vụ, và với người dùng cũng tiện lợi hơn, không phải đăng ký đi đăng ký lại.

Về mặt triển khai kỹ thuật, chúng tôi tách rời front-end và back-end, tách hoàn toàn website, client và API back-end, đồng thời cải tạo API back-end thành một nền tảng mở nội bộ. Như vậy khi ra dự án mới, chỉ cần bổ sung các API còn thiếu vào nền tảng mở, rồi dùng trang front-end độc lập để gọi API là xong.

![](images/image-1-414x1024.jpg)

Phương án API back-end lớn thống nhất

Nghiệp vụ một người không vì lợi nhuận
---------

Mở rộng thêm lối tư duy này: nếu chúng ta nhận thấy nghiệp vụ một người quá khó sinh lời (điều này thường xảy ra ở giai đoạn đầu của doanh nghiệp một người, do thiếu nguồn lực và kinh nghiệm), thì ta có thể hoạch định vài nghiệp vụ một người chuyên để thu thập nguồn lực, giảm độ khó cho việc kiếm tiền về sau.

![](images/image-71-1024x456.png)

Xây dựng nghiệp vụ một người

Trước đây, tôi luôn không hiểu nổi cách làm phát triển ứng dụng "ăn theo trend". Ví dụ, cái gì đang thịnh hành thì họ phát triển cái đó. Ta sẽ thấy, một khi những trend này hết hot, các ứng dụng đó nhanh chóng biến mất tăm.

Tuy nhiên, nếu ta xem xét vấn đề này từ góc độ hệ thống hóa, sẽ thấy cách làm này thực ra khá thú vị. Dù nghiệp vụ ăn theo trend dường như không trực tiếp đóng góp doanh thu, nhưng nó có thể thu hút người dùng. Những người dùng này sau khi tải ứng dụng, đăng ký kênh công khai WeChat, hoặc tham gia nhóm WeChat, đã được đưa vào user pool của chúng ta. Khi ta xây dựng nghiệp vụ tiếp theo có nhóm người dùng mục tiêu trùng khớp cao với nhóm này, ta có thể giảm đáng kể chi phí thu hút khách hàng.

Vì vậy, nhìn từ tư duy hệ thống hóa, ăn theo trend không hề vô giá trị. Ngược lại, nó cung cấp cho ta một phương pháp hiệu quả để xây dựng và mở rộng nền tảng người dùng.

Báo cáo tháng doanh nghiệp một người
------

Để suy nghĩ tốt hơn về cách phối hợp tối ưu giữa nghiệp vụ một người và doanh nghiệp một người, chúng tôi đã thiết kế «Báo cáo tháng doanh nghiệp một người». Báo cáo tháng chia làm hai phần, dùng cho đầu tháng và cuối tháng.

![](images/image-81-1024x586.png)

Báo cáo tháng doanh nghiệp một người - phiên bản đầu tháng

### Mục tiêu thu nhập

Đầu tháng, chúng ta đặt ra mục tiêu thu nhập, đồng thời đối chiếu thu nhập định kỳ hàng tháng (MRR) của tài sản hiện tại, mức lợi nhuận khả thi tối thiểu (MVPr) mà ta kỳ vọng đạt được, và mức MRR cần thiết để đạt tự do công việc. Qua so sánh, ta có thể thấy rất rõ vị trí của mình và khoảng cách đến mục tiêu. Hãy tưởng tượng khi đạt cột mốc tiếp theo, ta sẽ có được trạng thái làm việc và cuộc sống thoải mái hơn — điều này sẽ thúc đẩy ta tiến lên.

Tiếp theo là phần biến động tài sản, tức các tài sản mà ta dự định bổ sung, tối ưu và xử lý, cùng mô tả ngắn gọn về những tài sản này.

Ngoài ra, còn có ba mô-đun trạng thái, lần lượt mô tả trạng thái hiện tại của nghiệp vụ — tôi xem chúng như «độ khỏe mạnh» của nghiệp vụ.

### User pool

Trong đó, user pool là nhóm người dùng mà ta có thể tiếp cận. Cách tiếp cận có thể là các phương thức trực tiếp như đẩy thông báo WeChat, email hoặc tin nhắn SMS.

Chúng tôi chia người dùng thành «người dùng gốc» và «người dùng nền tảng bên thứ ba». Người dùng gốc là những người đăng ký trên nền tảng do ta hoàn toàn kiểm soát, ví dụ người dùng sở hữu App của ta; còn người dùng nền tảng bên thứ ba là những người theo dõi tài khoản của ta trên các nền tảng như Weibo hay Bilibili. Điểm khác biệt cốt lõi nằm ở chỗ: khi ta đẩy thông báo, có bị hạn chế hay có phải trả thêm phí hay không.

Ngoài ra, ta còn cần xem xét số lượng người dùng tham gia lan truyền thứ cấp và trả phí — đây đều là các chỉ số then chốt của tầng người dùng.

### Content pool và hạ tầng

Content pool là những nội dung có thể mang lại doanh thu hoặc lưu lượng truy cập. Trong đó, nội dung mang lại doanh thu về bản chất đã trở thành tài sản; đặt ở đây là để suy nghĩ về nó từ góc nhìn thống nhất theo đặc tính nội dung.

Tầng hạ tầng liên quan đến các hạ tầng cần thiết khi xây dựng logic sản phẩm dùng chung.

Rất nhiều sản phẩm đang xây dựng user pool và content pool trên nền tảng kênh công khai WeChat làm hạ tầng. Nhưng nền tảng kênh công khai WeChat đã qua thời kỳ phát triển, giờ bắt đầu kiểm soát lưu lượng và tập trung kiếm tiền, đặt ra không ít hạn chế cho việc lan truyền. Ví dụ, họ yêu cầu các quảng bá thương mại không thuộc chủ đề của kênh phải đi qua chương trình quảng cáo của họ.

So với đó, hạ tầng hoàn toàn tự chủ mới là giải pháp tốt nhất.

APP là phương án tốt nhất về tính tự chủ và tỷ lệ tiếp cận. Nhưng phát triển APP với doanh nghiệp một người là chi phí rất cao. Việc bảo trì cũng cần đầu tư liên tục, chỉ riêng việc cập nhật trên các chợ ứng dụng đã tốn khá nhiều công sức. Mặt khác, phát hành phiên bản APP cần nền tảng phê duyệt, ảnh hưởng lớn đến tính kịp thời của cập nhật.

Mini program là một phương án dung hòa, nhưng từ năm 2024 cũng phải đăng ký hồ sơ như APP. Ngoài ra, thanh toán trên iOS cũng thường xuyên bị cấm.

So sánh lại, chúng tôi cho rằng với các dự án doanh nghiệp một người giai đoạn đầu, dùng website độc lập có hiệu quả chi phí cao nhất. Tuy nhiên cần tích hợp hệ thống người dùng với WeChat, và tận dụng tin nhắn mẫu, tin nhắn chăm sóc khách hàng, tin nhắn đăng ký của WeChat để tiếp cận người dùng.

Nếu phát triển website độc lập từ đầu, chi phí không hề thấp. Nhưng nếu dựng bằng WordPress, thì chỉ cần trả phí máy chủ — một cloud instance nhỏ nhất là đủ, chi tiêu mỗi tháng dưới 50 tệ. Chúng tôi đang phát triển một plugin WordPress hỗ trợ phương pháp luận doanh nghiệp một người, có thể tích hợp WordPress với người dùng WeChat, hỗ trợ đẩy bài viết cho người dùng đăng ký, hỗ trợ thanh toán WeChat và giao diện XorPay, đồng thời có thể thực hiện crowdfunding sản phẩm. Khi hoàn thiện sẽ công bố trên trang này, mời các bạn đón chờ.

Có website độc lập của riêng mình, nội dung và người dùng đều có thể xây dựng xoay quanh nó. Nội dung trước tiên đưa lên trang chủ của mình, rồi mới đồng bộ sang các nền tảng bên thứ ba. Trong nội dung đồng bộ, ta có thể cung cấp nội dung bổ sung trên nền tảng của mình, dẫn dắt người dùng quay về trang chủ xem, từ đó đảm bảo tài sản cốt lõi và hạ tầng đều nằm trong tầm kiểm soát của mình.

### Tổng kết cuối tháng

![](images/opb-month-end-1024x583.png)

Báo cáo tháng doanh nghiệp một người - phiên bản cuối tháng

Cuối tháng, chúng ta có một biểu đồ tương ứng để nhìn lại công việc trong tháng, bao gồm hiện trạng và tình hình xử lý tài sản, cũng như có đạt được mục tiêu đã đặt ra hay không. Phần thay đổi chính là cấu thành tài sản và phần mục tiêu thu nhập.

Mục đích chính của «Báo cáo tháng doanh nghiệp một người» là buộc chúng ta phải suy nghĩ về nghiệp vụ từ góc nhìn toàn diện, và thực hiện định kỳ. Đảm bảo ta không bỏ sót những phần quan trọng.
