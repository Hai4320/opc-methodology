# Năng lực crowdsourcing

Cuối cùng còn một năng lực rất quan trọng, xây trên nền product pool và user pool — năng lực crowdsourcing.

Vì sao cần crowdsourcing
-------

Với doanh nghiệp một người, năng lực này cực kỳ quan trọng, vì chúng ta cần kiểm soát nghiêm ngặt số nhân sự. Đó là do mô hình kinh doanh và chiến lược cạnh tranh của chúng ta đều được thiết kế dựa trên điều này.

Trong nhiều chiến lược, chúng tôi đã nói: nhờ ít người, ta có thể tập trung vào những thị trường ngách rất hẹp. Kể cả lợi nhuận thu được ít so với công ty lớn, nhưng vì ít người nên bình quân đầu người cao — đây chính là nền tảng của mô hình kinh doanh và chiến lược cạnh tranh của chúng ta. Nếu có nhiều người, lợi thế này không còn nữa.

Hiện chúng ta có thể xử lý rất nhiều việc bằng AI và tự động hóa, nhưng luôn có những vấn đề chúng không giải quyết được, cần con người xử lý. Điều này tạo thành một mâu thuẫn cơ bản. Tuy ở giai đoạn khởi đầu, mâu thuẫn này chưa quá rõ, nhưng khi khối lượng nghiệp vụ tăng, nó sẽ ngày càng lộ rõ.

Để giải quyết mâu thuẫn này, chúng ta cần sở hữu năng lực crowdsourcing. Nói đơn giản, crowdsourcing là chia nhỏ nhiệm vụ giao cho nhiều người — thường là người dùng sản phẩm của chúng ta. Theo cách này, ta không cần thuê nhân viên, nên số nhân viên không tăng, đáp ứng tốt yêu cầu về quy mô của doanh nghiệp một người.

![](images/image-36-1024x468.png)

Vị trí và tầm quan trọng của năng lực crowdsourcing trong hạ tầng

Các thành phần cấu thành năng lực crowdsourcing
---------

Phương án này nghe rất lý tưởng, nhưng khi thao tác thực tế có rất nhiều chi tiết cần lưu ý.

Trước hết, không phải nhiệm vụ nào cũng crowdsourcing được: chúng cần cực kỳ rõ ràng, và người nhận nhiệm vụ cần có đủ năng lực, thời gian và mong muốn tương ứng. Nên nhìn chung, ta cần xử lý hết những gì bản thân, tự động hóa và AI làm được, cuối cùng đem phần không xử lý nổi ra crowdsourcing.

![](images/image-37-1024x491.png)

Các thành phần cấu thành hệ thống crowdsourcing

Các thành phần của hệ thống crowdsourcing gồm mấy khía cạnh.

### Nhiệm vụ chia nhỏ rõ ràng

Trước hết, phải có nhiệm vụ được chia nhỏ và rõ ràng. Không thể ném nguyên một khối việc ra ngoài — rủi ro không hoàn thành rất cao, chi phí trao đổi cũng cao. Nhiệm vụ cần nhiều người phối hợp chặt chẽ cũng không phù hợp để crowdsourcing trực tiếp. Ta cần chia nhiệm vụ thật nhỏ, đến mức không cần trao đổi gì cũng thực hiện được ngay.

Ví dụ, nếu muốn dịch toàn bộ website, ta có thể tách toàn bộ nội dung cần dịch thành từng câu đơn lẻ, rồi gửi cho người dùng. Mỗi người chỉ cần dịch một câu rồi nộp. Ta so sánh kết quả dịch của hai đến ba người, chọn ra bản tốt hơn. Mà việc chọn kết quả lại có thể trở thành một nhiệm vụ độc lập, tiếp tục phân phát qua hệ thống crowdsourcing. Bằng cách chia tách dần như vậy, mỗi nhiệm vụ nhỏ đều đủ rõ ràng.

Ngoài ra, khối lượng công việc của mỗi người nên đủ nhỏ. Vì crowdsourcing khác outsourcing: người thực hiện làm việc này trong thời gian rảnh, nên thời gian và sức lực của họ rất khó kiểm soát và khó đoán. Ta cần làm cho phần việc mỗi người gánh đủ nhỏ, và số người thực hiện đủ đông, như vậy mới kiểm soát chất lượng và rủi ro tốt hơn.

### Điều kiện nghiệm thu rõ ràng

Thứ hai là điều kiện nghiệm thu rõ ràng. Cốt lõi là lượng hóa: nhiệm vụ này xong chưa, làm tốt hay không, phải có tiêu chuẩn định lượng. Tốt nhất là nghiệm thu tự động được.

Ưu điểm lớn nhất của nghiệm thu tự động là: nghiệm thu xong có thể gửi thưởng theo thời gian thực. Như vậy hiệu quả khích lệ với người thực hiện được khuếch đại — không chỉ kích thích họ tiếp tục nhận nhiệm vụ crowdsourcing, thậm chí còn thúc đẩy họ mời bạn bè cùng tham gia.

### Phần thưởng hấp dẫn

Cuối cùng, phần thưởng hấp dẫn cũng rất quan trọng.

Hiện các loại nhiệm vụ mời bạn bè trong đủ thứ APP đã quá nhiều, chiêu trò đã bị dùng nhàm, tạo được "sức hút" rất khó.

Chúng tôi thấy phần thưởng vẫn còn hấp dẫn trước hết là tiền mặt hoặc vật ngang giá, ví dụ thẻ mua sắm JD; sau đó là những vật phẩm liên quan đến nghiệp vụ mà có tiền cũng khó mua, ví dụ như "gói NodeJS phiên bản vật lý" chúng tôi từng thiết kế — giờ đã không mua được nữa. Nếu dùng nó làm phần thưởng, tôi nghĩ với nhóm mục tiêu của chúng tôi vẫn rất hấp dẫn. Nhìn chung, về phần thưởng, hãy chân thành nhiều hơn, bớt chiêu trò đi.

Về thời điểm trao thưởng thì vừa nói rồi: lý tưởng nhất là trao theo thời gian thực, vì nó khởi động được vòng lặp khích lệ ngay trong quá trình thực hiện nhiệm vụ, hiệu quả cuối cùng sẽ tốt hơn nhiều.

Hệ thống crowdsourcing
----

Vậy, để làm crowdsourcing, chúng ta cần hệ thống hỗ trợ như thế nào?

Điều này tùy thuộc ta có muốn tự động phán định điều kiện nghiệm thu hay không, vì điều kiện nghiệm thu của mỗi loại nhiệm vụ hoàn toàn khác nhau.

Nếu muốn phán định tự động, ta cần các hệ thống chuyên dụng theo từng ngách. Ví dụ, cơ chế lan truyền mời bạn (viral referral) và hoàn tiền giới thiệu là kiểu crowdsourcing chuyên ngách rất điển hình. Kịch bản này được tách riêng ra tối ưu vận hành, đến mức giờ mọi người còn chẳng coi nó là crowdsourcing nữa.

Nhưng bản chất nó chính là một dạng crowdsourcing. Ta có thể quay lại soi các thành phần của nó:

1.  Trước hết, nó có nhiệm vụ chia nhỏ rõ ràng: đưa bạn một link, bạn mời người dùng qua link đó.
2.  Sau đó, điều kiện nghiệm thu cũng rất rõ: người dùng mang mã mời đăng ký, hệ thống nhận diện được ngay.
3.  Cuối cùng, phần thưởng cũng trao theo thời gian thực: hễ phát hiện nhiệm vụ hoàn thành, lập tức gửi thưởng — nhiều hệ thống nhận được tiền mặt ngay trên WeChat.

Vì vậy, crowdsourcing không nhất thiết là một hệ thống độc lập, nó cũng có thể là một tính năng chuyên ngách.

Nếu chấp nhận nghiệm thu thủ công, ta có thể có những phương án phổ quát hơn.

Ví dụ forum kết hợp gian hàng đổi điểm. Các bạn có thâm niên trên mạng chắc từng dùng: quy trình cơ bản là bạn đăng nhiệm vụ lên forum, treo thưởng bằng điểm; người khác hoàn thành nhiệm vụ, bạn chốt thớt, điểm sẽ chuyển cho họ. Đồng thời bản thân forum cung cấp gian hàng đổi điểm để quy đổi phần thưởng. Tất nhiên, hình thái sản phẩm forum giờ đã được dùng rất ít, nhưng cơ chế tương tự vẫn vận hành rất tốt.

Nếu dùng WordPress, có sẵn một số plugin thương mại kiểu "chợ việc tự do" (task marketplace). Cài xong, WordPress sẽ có thêm các tính năng tương tự: đăng nhiệm vụ, nhận nhiệm vụ, nghiệm thu, thanh toán bằng điểm/tiền mặt.
