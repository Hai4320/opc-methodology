# Tổng quan phương pháp luận phiên bản mới

「Phương pháp luận doanh nghiệp một người」 phiên bản mới
-----------

Cái tên 「phương pháp luận doanh nghiệp một người」 nghe có thể hơi quen tai, vì trước đây tôi từng chia sẻ trên GitHub một bài viết dài mang tên 《[Phương pháp luận công ty một người](https://github.com/easychen/one-person-businesses-methodology)》. Bài viết đó chủ yếu chia sẻ với các lập trình viên phát triển độc lập (indie dev) một số kinh nghiệm vận hành doanh nghiệp một người.

Sau hai đến ba năm liên tục cải tiến, giờ đây chúng ta đã có 「phương pháp luận doanh nghiệp một người」 phiên bản 2.0. Sở dĩ trong tên gọi, 「công ty」 được đổi thành 「doanh nghiệp」 là vì 「công ty một người」 dễ gây nhầm lẫn với loại hình công ty một thành viên trong luật doanh nghiệp, nên tôi đã đổi sang từ 「doanh nghiệp」.

![](images/image-1024x562.png)

Phương pháp luận phiên bản mới

### Khác biệt thứ nhất - Hệ thống hóa hơn

Điểm khác biệt lớn nhất của phiên bản mới là đưa vào tư duy hệ thống. Hạn chế trong cách nghĩ trước đây là đánh đồng nghiệp vụ một người với doanh nghiệp một người, bỏ qua sự phối hợp và tái sử dụng nguồn lực giữa nhiều nghiệp vụ một người. Phương pháp luận phiên bản mới cho rằng cốt lõi của doanh nghiệp một người là duy trì một bể tài sản có thể liên tục mang lại thu nhập thụ động, cần định kỳ bảo trì và tái phân bổ các tài sản trong đó.

### Khác biệt thứ hai - Hướng tới mọi người khởi nghiệp bằng side project

Một điểm khác biệt nữa là, bài viết dài 《Phương pháp luận công ty một người》 trước đây chủ yếu hướng tới lập trình viên phát triển độc lập. Còn phương pháp luận phiên bản mới của chúng ta hướng tới tất cả những người khởi nghiệp bằng side project — dù biết lập trình hay không, bạn đều có thể học nó.

Bởi vì cùng với sự trưởng thành của phần mềm mã nguồn mở, NoCode và công nghệ trí tuệ nhân tạo, nhiều người không biết lập trình cũng có thể nhờ sự trợ giúp của những công cụ này để dựng nên nền tảng kinh doanh của riêng mình rất nhanh chóng. Nền tảng kinh doanh dựng nhanh kiểu này chưa chắc hoàn hảo, nhưng nó đủ dùng.

Logic đằng sau điều này là: chúng ta cần xây dựng MVP và nguyên mẫu trước để kiểm chứng nhu cầu. Mà sản phẩm dùng để kiểm chứng thì bản thân nó không cần công nghệ quá tinh xảo; khi nguyên mẫu nghiệp vụ đã vận hành, chúng ta có dòng tiền, và cũng có thể thuê người chuyên môn làm những việc này ------ công nghệ khi đó không còn là rào cản nữa. Phần nội dung này chúng ta sẽ bàn riêng sau.

Giới thiệu tác giả
----

Trước tiên, xin tự giới thiệu về bản thân.

### Lập trình viên phát triển độc lập

![](images/Screen-Shot-2024-03-11-at-9.42.20-PM-1024x580.png)

Các dự án độc lập do Easy phát triển

Trước hết, tôi là một lập trình viên phát triển độc lập (indie dev).

Tôi bắt đầu làm phát triển độc lập từ thời đại học, muốn thử kiếm lại tiền học phí của mình. Từ đó tôi rơi vào "hố sâu" phát triển độc lập không dứt ra được; ngay cả khi đi làm ở công ty, tôi vẫn làm một số dự án mã nguồn mở có ích cho công việc chính dưới hình thức side project.

-   Khoảng sáu bảy năm trước, tôi làm một dịch vụ đẩy thông báo tối giản tên là [ServerChan](https://sct.ftqq.com/) (Server酱). Dịch vụ này nhờ làm lâu năm nên có khá nhiều người dùng, hơn 200.000 người.
-   Hai năm trước, tôi lại làm một tiện ích mở rộng trình duyệt để giám sát trang web, [CheckChan](https://github.com/easychen/checkchan-dist) (Check酱). Dự án này kết hợp với ServerChan dùng rất tiện.
-   Tác phẩm mới nhất là một công cụ về quy trình làm việc với AI, tên là FlowDeer. Nó là dạng công cụ tích hợp giữa sơ đồ tư duy, AutoGPT và đa tác tử (multi-agent), có thể xử lý logic phức tạp, cũng có thể dùng để tư duy sâu. Sản phẩm này hiện vẫn đang thử nghiệm nội bộ.

Nhưng điều khá thú vị là, thu nhập từ các dự án phát triển độc lập trước đây của tôi thực ra chưa bao giờ đủ trang trải chi phí sinh hoạt.

### Giảng viên khóa học

Vì vậy, tôi còn một thân phận nữa: giảng viên khóa học.

![](images/image-1-1024x604.png)

Trang chủ Fangtang Skill Stack

Trang web 「[Fangtang Skill Stack](https://stack.ftqq.com/)」 (方糖技能栈) này chủ yếu là các khóa học của tôi. Ban đầu nó vốn là một sản phẩm phụ trong quá trình tôi làm phát triển độc lập. Nhưng về sau, chính sản phẩm phụ này lại giúp tôi đạt được 「lợi nhuận khả thi tối thiểu」.

Cái gọi là lợi nhuận khả thi tối thiểu, nghĩa là số tiền kiếm được đủ để nuôi sống bản thân, nhờ đó không phải vì áp lực cuộc sống mà đi tìm việc làm. Với người khởi nghiệp toàn thời gian, hay nói cách khác là người làm doanh nghiệp một người toàn thời gian, đây thực sự là một cột mốc rất quan trọng. Chúng ta sẽ bàn đến ở phần sau.

### Người khám phá và chia sẻ phương pháp luận

Mặt khác, tôi rất hứng thú với việc làm sao kiếm tiền bằng công nghệ, đặc biệt là kiếm tiền một cách thanh lịch theo phương thức cá nhân. Ban đầu, tôi viết [《Lập trình viên kiếm tiền tiêu vặt một cách thanh lịch như thế nào》](https://github.com/easychen/howto-make-more-money). Vì trước đây đều hướng tới lập trình viên, nên tôi đã đăng những bài viết và sách điện tử này lên GitHub, đến nay chúng tích lũy được khoảng 16K Star (đánh dấu sao).

![](images/image-2-1024x601.png)

Những chia sẻ của Easy về side project và doanh nghiệp một người

Sau đó, tôi viết cuốn sách [《Side project tinh gọn》](https://github.com/easychen/lean-side-bussiness) (精益副业), bao quát một số chi tiết thực hành, ví dụ như cách kiếm tiền bằng việc làm khóa học trực tuyến, cách kiếm tiền bằng phát triển phần mềm; thảo luận về việc khi thực hiện những sáng tạo này, quy trình sản phẩm làm sao tiết kiệm nguồn lực nhất, quy trình thiết kế nên sắp xếp thế nào cho phù hợp nhất với thói quen của lập trình viên, cùng những vấn đề cụ thể cần cân nhắc khi làm side project. Cuốn sách này cũng được phát hành dưới dạng sách điện tử miễn phí trên GitHub, hiện có khoảng 8K Star.

Cuối cùng, chính là bài viết dài 《Phương pháp luận công ty một người》 đã nhắc ở trên. Khi đó, nhận thức của tôi về phương pháp luận này còn khá sơ sài, mới chỉ cảm nhận được một đường nét tổng thể; qua hai ba năm cải tiến gần đây, phương pháp luận này giờ đã được tinh chỉnh hơn rất nhiều. Đây cũng chính là nội dung cuốn sách này muốn chia sẻ với mọi người.

Vậy nên nhìn lại, trong chuyện kiếm tiền, tôi vẫn khá kiên trì, trước sau đã dành nhiều năm trời để nghiền ngẫm những điều này.

Hạn chế của phương pháp luận này
--------

Tuy Slogan của phương pháp luận này là 「Từ con ốc vít đến siêu cá nhân」, nhưng khá đáng tiếc là, hiện tại tôi nhiều nhất chỉ được tính là một KOL hết thời. Trong tất cả các mạng xã hội của tôi, Weibo nơi có nhiều người theo dõi nhất cũng chỉ khoảng 600.000. Vì vậy, tôi không thể chia sẻ kinh nghiệm trọn vẹn về cách từng bước trở thành siêu cá nhân ------ bởi chính tôi cũng chưa trở thành siêu cá nhân. Điều cuốn sách này có thể chia sẻ là kinh nghiệm và bài học tính đến mốc 「cá nhân bình thường」.

Nhìn từ góc độ khác, điều này có lẽ cũng có mặt tốt. Nếu tôi đã trở thành siêu cá nhân, thì rất có thể tôi sẽ không dành nhiều thời gian như vậy để suy ngẫm và tổng kết phương pháp luận, rồi chia sẻ nó ra như một sản phẩm phụ.

![](images/image-3-1024x527.png)

Vài mốc trung gian trên con đường trở thành siêu cá nhân

Trước khi trở thành 「siêu cá nhân」, tôi đánh dấu hai mốc trung gian: mốc 「cá nhân sống sót」 và mốc 「cá nhân bình thường」.

### Mốc 「cá nhân sống sót」

Mốc 「cá nhân sống sót」 chính là trạng thái đạt được 「lợi nhuận khả thi tối thiểu」, tôi gọi nó là 「tự do tài chính giả」.

Sở dĩ thêm chữ 「giả」 là vì nó có thể cần thông qua việc kiểm soát và cắt giảm chi phí sinh hoạt để khiến lợi nhuận từ side project hoặc dự án khởi nghiệp độc lập cân bằng với chi tiêu cuộc sống. Ví dụ, giá nhà đắt đỏ ở Bắc Kinh kéo chi phí sinh hoạt lên rất cao; nếu chúng ta chuyển về làm việc và sinh sống ở những thành phố hạng nhất mới có giá nhà thấp hơn, thì sẽ dễ đạt mốc này hơn.

Tất nhiên, tự do tài chính thực sự thì không cần hạ thấp tiêu chuẩn sống để đạt được, mốc đó nằm ở xa hơn nữa.

### Mốc 「cá nhân bình thường」

Ý nghĩa của mốc 「cá nhân sống sót」 là ở chỗ: một khi đạt mốc này, chỉ cần muốn, chúng ta có thể toàn tâm toàn ý kinh doanh nghiệp vụ của mình năm này qua năm khác. Còn mốc 「cá nhân bình thường」 nghĩa là thu nhập từ side project hoặc dự án khởi nghiệp độc lập của bạn đạt hoặc vượt thu nhập từ công việc chính. Trạng thái này tôi gọi là 「tự do công việc」, nghĩa là dù không đi làm không lao động, bạn vẫn có thu nhập thụ động ngang với hồi còn đi làm.

Với một số người, 「tự do công việc」 có thể đồng nghĩa với 「tự do tài chính」; nhưng với những bạn mà thu nhập từ công việc chính vốn không đủ để chi tiêu thoải mái, thì 「tự do tài chính」 cần mức thu nhập cao hơn nữa. Định nghĩa các mốc này chỉ để tiện dùng trong các phần chia sẻ tiếp theo, không phải cách nói đặc biệt chính thống. Bạn hoàn toàn có thể định nghĩa lại theo ý mình.

Tóm lại, hiện tại tôi cơ bản đang ở mốc 「cá nhân bình thường」 với 「tự do công việc」. Nghĩa là, dù mỗi ngày tôi có rong chơi vô công rồi nghề, thu nhập thụ động hàng tháng vẫn không khác mấy so với hồi còn đi làm.

Tuy nhiên thực tế là, tính bền vững của tài sản đều có hạn, cũng cần bảo trì định kỳ (điều này chúng ta sẽ nói sau); do biến động thị trường và các nguyên nhân khác, có những tài sản có thể đột nhiên biến mất, vì vậy nếu muốn phát triển tốt hơn, còn phải không ngừng tạo ra tài sản mới để giảm rủi ro. Cho nên hiện tại tôi vẫn đang trong trạng thái làm việc hết công suất. Nhưng "có thể không làm việc" và "buộc phải làm việc" là hoàn toàn khác nhau: bạn có thể tự cho mình một kỳ nghỉ dài bất cứ lúc nào.

Ý nghĩa của phương pháp luận
------

Trong cuốn sách này, điều tôi hiện có thể chia sẻ chính là phần 「từ con ốc vít đến cá nhân bình thường (tự do công việc)」. Hy vọng sau này có cơ hội bổ sung trọn vẹn phần 「từ cá nhân bình thường đến siêu cá nhân」.

![](images/image-4-1024x535.png)

Tác dụng và ý nghĩa của việc chia sẻ

Còn một điểm cần nói rõ: những chia sẻ ở đây không thể giúp bạn nhảy cóc qua quá trình trưởng thành, từ con ốc vít một bước thành siêu cá nhân hay cá nhân bình thường. Quá trình trưởng thành này là không thể thiếu; ý nghĩa của việc chia sẻ nằm ở chỗ 「bớt đi đường vòng」 — chúng tôi hy vọng qua chia sẻ có thể giúp mọi người tránh được một số sai lầm mà tôi từng tốn rất nhiều thời gian để mắc phải.

Tất nhiên, nhiều hành vi từng là sai lầm trước đây, thì ở hiện tại chưa chắc đã còn là sai lầm. Vì vậy điều chúng tôi nhấn mạnh là phương pháp luận chứ không phải kết luận. Nhu cầu thị trường và môi trường cạnh tranh luôn thay đổi, những kết luận được chia sẻ có thể không quan trọng đến vậy. Quan trọng nhất là chúng ta cần học cách sử dụng một bộ công cụ tư duy và phân tích, để tự mình độc lập suy nghĩ và rút ra kết luận cho từng tình huống khác nhau.

Nhiều sách về khởi nghiệp và side project, thậm chí không ít khóa học trả phí của những người thành công, thường cũng chỉ chia sẻ kết luận chứ không phải phương pháp luận. Cho cá không bằng cho cần câu. Tin tốt là, những năm gần đây hệ thống lý thuyết khởi nghiệp ở nước ngoài dần trưởng thành, phương pháp luận về khởi nghiệp đang trở nên rõ ràng; tin xấu là, phương pháp luận khởi nghiệp lại không phù hợp với doanh nghiệp một người.

Tuy sự trỗi dậy của cá nhân đã là xu thế lớn, nhưng sách vở về mảng này phần nhiều còn hời hợt. Mấy năm nay tôi đã đọc rất nhiều tài liệu liên quan đến doanh nghiệp một người, thử từng bước dung hợp các quan điểm trong đó với phương pháp luận khởi nghiệp, và dành rất nhiều thời gian kiểm nghiệm trong thực tiễn. Từ đó mới có phương pháp luận phiên bản 2.0 cơ bản thành hình như hiện nay.

Nói không khiêm tốn thì, đây là công cụ tư duy sâu hiếm có trong lĩnh vực doanh nghiệp một người và khởi nghiệp bằng side project. Ai đã thực hành qua đều sẽ cảm nhận được giá trị của nó. Hy vọng nó có thể trở thành trợ lực mạnh mẽ trên con đường thành công của bạn.
