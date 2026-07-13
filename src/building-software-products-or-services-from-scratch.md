# Xây dựng sản phẩm: Xây dựng sản phẩm hoặc dịch vụ phần mềm từ con số 0

Bài viết này cố gắng giới thiệu trọn vẹn toàn bộ quá trình từ hoạch định đến ra mắt của một sản phẩm phần mềm, hy vọng mang lại cho bạn nguồn cảm hứng. Nội dung được trích lược và viết lại từ [《Lean Side Business》](https://github.com/easychen/lean-side-bussiness).

Quy trình sản phẩm
----

![](images/image-106-1024x511.png)

Quy trình sản phẩm phù hợp hơn với doanh nghiệp một người

Trong bài viết này, chúng ta áp dụng quy trình sản phẩm đã được tối ưu hóa, phù hợp hơn với doanh nghiệp một người. Trong đó, bước「Business Model Canvas」nên được thay bằng「[Canvas doanh nghiệp một người](https://ft07.com/opb-canvas-and-opb-report/)」có tính nhắm đích cao hơn.

Quy trình này rất giống với quy trình sản phẩm của nhiều công ty ở Silicon Valley, nhưng đã được điều chỉnh và tối ưu cho doanh nghiệp một người. Sau hơn ba năm sử dụng, bản thân chúng tôi đã dùng rất thuần thục.

1.  Trước tiên định nghĩa tuyên bố giá trị, sau đó thiết kế Business Model Canvas xoay quanh giá trị đó.
2.  Sau khi hoàn thành canvas, chúng ta lấy phần「phân khúc khách hàng」trong canvas ra để xây dựng「chân dung người dùng」. Đây là công cụ giúp cụ thể hóa các phân khúc khách hàng, khiến họ trở nên có da có thịt.
3.  Có chân dung rồi, ta dựa vào đó tái hiện các bối cảnh người dùng sử dụng sản phẩm: họ dùng máy tính hay điện thoại, dùng ở nhà hay trên xe, v.v.
4.  Hình dung xem để truyền tải giá trị đến người dùng trong các bối cảnh nói trên, chúng ta cần những tính năng gì — như vậy sẽ có được một danh sách tính năng.
5.  Danh sách tính năng sẽ rất dài, độ ưu tiên của các tính năng cũng khác nhau. Vì vậy chúng ta sẽ chia tính năng thành các giai đoạn, trong đó giai đoạn quan trọng nhất và đứng đầu tiên chính là giai đoạn dùng để phát triển「sản phẩm khả thi tối thiểu」(MVP).
6.  Khi「sản phẩm khả thi tối thiểu」phát triển xong, tiến hành kiểm chứng「product-market fit」; nếu không đạt mục tiêu kiểm chứng đã đặt ra, cần điều chỉnh tính năng, thậm chí thiết kế lại tuyên bố giá trị.
7.  Khi đã vượt qua「product-market fit」, chúng ta có thể phát triển lặp các tính năng còn lại của sản phẩm theo từng giai đoạn.
8.  Trong quá trình phát triển lặp, chúng ta liên tục tối ưu tăng trưởng cho các tính năng mới ra mắt, đảm bảo mỗi phần tính năng đạt được mục tiêu định trước.

Trên đây là quy trình tinh gọn mà chúng tôi tối ưu cho doanh nghiệp một người; tuy kể ra thì khá dài dòng, nhưng thao tác thực tế lại tương đối đơn giản. Hơn nữa, chúng tôi thực ra đã lược bỏ không ít khâu trong quy trình của các công ty lớn, ví dụ như phỏng vấn người dùng, focus group v.v.

Giới thiệu dự án
----

Trước tiên xin giới thiệu dự án thực chiến của chúng ta ------ Fuli Words (福利单词).

Nó xuất phát từ một nhu cầu tự nhiên của tôi trong quá trình học. Ban đầu tôi dùng phần mềm Anki để học từ vựng; phần mềm rất tốt, nhưng lần nào cũng có cảm giác như đang ép bản thân phải học, học xong thì nhẹ cả người. Để nhắc mình đừng trốn tránh, tôi còn đặt báo thức thúc giục bản thân mỗi ngày.

Một hôm, tôi lại mải xem tranh trên [Pixiv](https://www.pixiv.net/) (một cộng đồng sáng tác nội dung anime/manga) mà quên mất thời gian. Bỗng nhiên tôi nghĩ: liệu có thể gắn hai hành vi học từ vựng và xem tranh lại với nhau không?

Bạn thấy đấy, học từ vựng tuy hữu ích nhưng khiến tôi khổ sở, một ngày dài như một năm; xem tranh thì vui vẻ, mê mải quên lối về, nhưng có vẻ không mấy「hữu ích」. Nếu ta kết hợp cả hai, vừa xem tranh vừa học từ, chẳng phải sẽ khiến việc học từ bớt khó chịu và có thể duy trì liên tục hay sao?

Đó chính là điểm xuất phát của Fuli Words.

Tiếp theo, chúng ta sẽ xem làm thế nào để từ ý tưởng còn mơ hồ này rút ra một tuyên bố giá trị rõ ràng, rồi xoay quanh nó tiến hành hoạch định mô hình kinh doanh, thiết kế tính năng và giao diện, kiểm chứng và phát triển lặp, cuối cùng biến nó thành một sản phẩm thương mại.

![](images/image-107.png)

Ứng dụng Fuli Words

Cần nói rõ rằng quá trình lập trình rất khó trình bày rõ ràng trong khuôn khổ có hạn, và cũng lệch khỏi chủ đề của bài viết, nên chúng tôi chỉ nhắc sơ qua một số điểm cần lưu ý chứ không dạy lập trình.

Bước một: Hoạch định mô hình kinh doanh
----------

Trước tiên, chúng ta dùng Business Model Canvas để hoạch định mô hình kinh doanh của sản phẩm.

### Tuyên bố giá trị

![](images/image-108-1024x373.png)

Tuyên bố giá trị của Fuli Words

Tuyên bố giá trị cốt lõi của Fuli Words là mang đến một cách học nhẹ nhàng, vui vẻ cho những người cảm thấy việc học tiếng Anh đầy thử thách. Mục tiêu là giảm áp lực cho người học bằng cách thêm niềm vui vào quá trình học, khiến hoạt động học vốn ngắn ngủi và khó khăn trở nên bền vững hơn và dễ thành thói quen hơn.

Vì vậy, trong phần「tuyên bố giá trị」, chúng ta đặc biệt nhấn mạnh hai điểm then chốt:「học không đau khổ」và「học liên tục」. Hai điểm này tạo nên giá trị cốt lõi của sản phẩm.

Với những tuyên bố giá trị này, chúng ta có thể giúp khách hàng vượt qua những rào cản từng ngăn họ học tập, từ đó thúc đẩy sự trưởng thành và tiến bộ của cá nhân họ.

### Phân khúc khách hàng

![](images/image-109-1024x463.png)

Phân khúc khách hàng của Fuli Words

Việc cụ thể hóa tuyên bố giá trị đòi hỏi chúng ta cân nhắc kỹ các phân khúc khách hàng. Xét rằng Fuli Words là một phần mềm học tập, nhóm khách hàng mục tiêu của nó đương nhiên gắn chặt với nhu cầu học tiếng Anh. Ta có thể chia khách hàng mục tiêu thành ba nhóm:

1.  Sinh viên cần ôn thi chứng chỉ tiếng Anh đại học CET-4/CET-6.
2.  Người có nhu cầu du học hoặc định cư, cần chuẩn bị cho kỳ thi IELTS, TOEFL.
3.  Người đi làm muốn nâng cao trình độ tiếng Anh chuyên ngành để thể hiện tốt hơn nơi công sở.

Ba nhóm khách hàng này có mục đích học tập với trọng tâm khác nhau, nhưng thông qua tính năng「chuyển đổi kho từ vựng」hoặc「kho từ vựng tùy chỉnh」, phần mềm của chúng ta có thể linh hoạt đáp ứng nhu cầu của họ.

### Cụ thể hóa tuyên bố giá trị

![](images/image-110-1024x527.png)

Tuyên bố giá trị của Fuli Words sau khi cụ thể hóa

Chỉ cung cấp kho từ vựng cho người dùng học thì không thể khiến phần mềm của chúng ta khác biệt. Vì vậy, trong tuyên bố giá trị, chúng ta bổ sung phần khiến họ khó lòng cưỡng lại ------「kẹo ngọt」.

Tuy nhiên, với các nhóm người dùng khác nhau, ý nghĩa của「kẹo ngọt」không giống nhau.

Nếu chỉ đăng vài cô nàng dễ thương phong cách anime, thì chỉ những người thích anime mới thấy đó là「kẹo」của họ, mới bị thu hút mà ngày nào cũng vào xem. Với những người không hứng thú với anime, những bức tranh đó chẳng hấp dẫn chút nào, nên chúng ta cần tăng chủng loại「kẹo」. Ví dụ, có cô nàng thích ngắm trai đẹp, có fan thích ngắm thần tượng, có「con sen」thích ngắm chó mèo, có tín đồ ẩm thực thích ngắm thịt nướng và bánh ngọt. Phần này, ta có thể đáp ứng bằng cách làm nhiều thư viện ảnh.

Dựa vào đó, chúng ta đặt ra tuyên bố giá trị cụ thể hơn cho từng phân khúc khách hàng:

1.  「Mỗi ngày ngắm gái xinh 40 phút, một tháng thuộc hết từ vựng CET-4/6」
2.  「Vừa ngắm trai đẹp, vừa chinh phục từ vựng IELTS/TOEFL」
3.  「Vừa hít mèo online vừa thăng chức tăng lương」

Nghe như vậy chẳng phải hấp dẫn hơn nhiều sao?

### Kênh tiếp cận

![](images/image-111-1024x577.png)

Kênh tiếp cận của Fuli Words

Về「kênh tiếp cận」, chúng ta dự định dẫn người dùng hạt giống về qua Weibo. Thông qua phản hồi thử nghiệm từ người dùng hạt giống, một khi tỷ lệ chuyển đổi của sản phẩm đạt tiêu chuẩn kỳ vọng, chúng ta sẽ triển khai hợp tác rộng hơn và khởi động quảng cáo trên Weibo, qua đó đo lường chi phí quảng cáo so với hiệu quả lưu lượng mang lại.

### Quan hệ khách hàng

![](images/image-112-1024x560.png)

Quan hệ khách hàng của Fuli Words

Để duy trì quan hệ khách hàng tốt, chúng ta sẽ dùng công cụ「TuXiaoChao」(兔小巢) của Tencent để hỗ trợ sau bán hàng. Như vậy, người dùng có thể gửi phản hồi thuận tiện, còn chúng ta có thể phản hồi kịp thời qua nhiều kênh như WeChat hay QQ.

### Hoạt động then chốt

![](images/image-113-1024x537.png)

Hoạt động then chốt của Fuli Words

Về hoạt động then chốt, phiên bản đầu của sản phẩm khả thi tối thiểu (MVP) nên bao gồm tính năng học từ vựng cơ bản, 100 từ cùng hình ảnh tương ứng, và một module học tương tác đơn giản. Ngoài ra, chúng ta còn cần quan tâm dữ liệu học tập của người dùng để kiểm chứng tuyên bố giá trị của mình.

Sau khi MVP kiểm chứng thành công, chúng ta sẽ phát triển ứng dụng bản web, làm bản phát hành sản phẩm của giai đoạn một. Các tính năng then chốt của giai đoạn này gồm giao diện học từ vựng và tính năng chọn kho từ vựng. Để tạo doanh thu, chúng ta còn đưa vào hệ thống thanh toán và đơn hàng, đồng thời phát triển công cụ phân tích để tối ưu quá trình chuyển đổi.

### Nguồn lực then chốt



Nguồn lực then chốt của Fuli Words

Về nguồn lực then chốt, ngoài nhân lực, vốn và thời gian, chúng ta còn phải đặc biệt lưu ý nguồn hình ảnh dùng cho việc học từ vựng. Nhất là ở khâu thu phí, chúng ta phải đảm bảo sử dụng hợp pháp nguồn hình ảnh.

Trong sản phẩm khả thi tối thiểu, vì chưa liên quan đến thu phí, chúng ta có thể dùng rất nhiều hình ảnh. Nhưng một khi bắt đầu thu phí, nếu vẫn tải bừa các hình ảnh không rõ bản quyền trên mạng, đưa vào phần mềm của mình rồi bán dưới hình thức thu phí, rất có thể sẽ vi phạm bản quyền.

Vì vậy, chúng ta cần suy nghĩ về phương án giải quyết nguồn hình ảnh. Sau khi phân tích sơ bộ, có mấy hướng sau:

1.  Xin tác giả cấp quyền
2.  Chuyển sang dùng hình ảnh không bản quyền
3.  Người dùng tự cung cấp hình ảnh

#### Xin tác giả cấp quyền

Trực tiếp tìm tác giả mua lại hình ảnh, rồi bán cho người dùng dưới dạng kho từ vựng trả phí — đây là cách trực tiếp nhất. Nhưng có vấn đề, đó là giá cả: chỉ riêng một kho từ vựng cỡ lớn đã có hơn mười nghìn từ, nghĩa là chúng ta phải mua hơn mười nghìn bức ảnh. Nếu tính 50 tệ một ảnh, cần đầu tư 500 nghìn tệ.

Khi còn chưa kiếm được một xu mà đã bỏ ra khoản đầu tư lớn như vậy thì rủi ro vẫn rất cao. Cách này phù hợp hơn để dùng khi chúng ta đã kiếm được tiền và muốn mở rộng quy mô.

#### Chuyển sang dùng hình ảnh không bản quyền

Tất nhiên, chúng ta cũng có thể tìm hình ảnh không bản quyền để làm thư viện ảnh. Như vậy dù có đóng gói vào phần mềm để bán thương mại cũng không có vấn đề gì. Trên Internet đã có những kho ảnh HD không bản quyền khá đồ sộ, ví dụ [Unsplash](https://unsplash.com/). Có điều các kho ảnh này chủ yếu là phong cảnh và động vật, ảnh người thì rất ít.

#### Người dùng tự cung cấp hình ảnh

Về bản chất, thứ chúng ta bán là công cụ「xem ảnh học từ」chứ không phải bản thân hình ảnh. Sở dĩ hiện có rủi ro về bản quyền là do việc đóng gói gây ra. Vậy nên ta có thể thử tách dịch vụ trả phí và hình ảnh miễn phí ra khỏi nhau.

Ví dụ, chúng ta có thể cung cấp cho người dùng công cụ tạo thư viện ảnh tùy chỉnh, để họ tự nhập các hình ảnh mình sưu tầm vào. Như vậy vừa đạt được mục đích, vừa không có rủi ro bản quyền.

Điều tương tự cần cân nhắc là phần âm thanh dùng khi học từ vựng. Cách đơn giản thô sơ nhất là dùng API TTS (chuyển văn bản thành giọng nói) của các nền tảng cloud để sinh trực tiếp.

### Chi phí và doanh thu

![](images/image-115-1024x413.png)

Chi phí và doanh thu của Fuli Words

Cuối cùng, bằng cách điền nốt các phần liên quan của Business Model Canvas, chúng ta có thể bắt đầu ước tính chi phí và doanh thu để tính ra khoảng lợi nhuận kỳ vọng.

Do dự án chúng ta phát triển tương đối nhỏ, nguồn lực dùng đến cũng không nhiều lắm, nên Business Model Canvas làm chưa thật chi tiết. Nhưng thông thường, canvas mô hình kinh doanh phiên bản đầu tiên vốn cũng không quá chi tiết. Nó sẽ được cụ thể hóa dần theo tiến độ dự án.

Cuối cùng hãy xem Business Model Canvas hoàn chỉnh:

![](images/image-116-1024x659.png)

Business Model Canvas hoàn chỉnh của Fuli Words

Bước hai: Xây dựng chân dung người dùng cho các phân khúc khách hàng
---------------

### Chân dung người dùng là gì

Trong Business Model Canvas, chúng ta đã phân khúc khách hàng, chia khách hàng thành các nhóm khác nhau, mỗi nhóm đại diện cho một nhu cầu độc lập.

Chân dung người dùng (persona) chính là việc tạo cho mỗi nhóm đã phân sẵn đó một nhân vật, dựng một hình tượng ảo, khiến nó trở nên có da có thịt — có tên tuổi, có giới tính, có thân phận riêng, có sở thích riêng, có bối cảnh sử dụng sản phẩm.

Như vậy, khi nhắc đến chân dung người dùng này, ta như đang nói về một người quen thuộc như bạn bè, đồng nghiệp của mình.

Biến nhu cầu trừu tượng thành con người sống động — nhờ vậy khi thiết kế sản phẩm, ta dễ tái hiện bối cảnh hơn, mang theo hình ảnh trong đầu để hình dung nhu cầu và hành động của người đó. Đây chính là ý nghĩa của chân dung người dùng.

### Chân dung người dùng của Fuli Words

Tiếp theo, dựa trên phân khúc khách hàng của Fuli Words, chúng ta xây dựng chân dung người dùng cho từng nhóm khách hàng.

#### Sinh viên ôn thi CET-4/6

Đầu tiên là nhóm khách hàng sinh viên ôn thi CET-4/6. Chúng ta gọi cậu ấy là Wang Xiaokang, đặt là một nam sinh năm ba. Cậu hiện có một nhiệm vụ cấp bách: nhất định phải vượt qua kỳ thi CET-4. Cậu bạn này là một otaku mê anime, loại ảnh cậu thích xem là các cô nàng dễ thương phong cách anime.

#### Đội ngũ dự bị du học, định cư

Tiếp theo, chúng ta xây dựng chân dung người dùng cho nhóm có nhu cầu du học, định cư, cần thi IELTS và TOEFL. Chúng ta gọi cô ấy là Zhang Xiaoliu, một cô gái mới tốt nghiệp đại học được một năm, hiện có ý định du học và đang chuẩn bị cho kỳ thi IELTS. Cô bạn này là fan hâm mộ thần tượng, loại ảnh cô thích xem là trai đẹp Hàn Quốc.

#### Nhân viên văn phòng nâng cao chuyên môn

Chân dung người dùng của nhóm thứ ba, chúng ta gọi cô ấy là Lu Xiaobai, một cô gái tốt nghiệp khoảng hai năm, làm công việc liên quan đến kỹ thuật tại một công ty sinh học. Cô cần nhanh chóng làm quen với lượng lớn từ vựng tiếng Anh chuyên ngành sinh học để hiểu rõ hơn về nghiệp vụ của công ty. Nhà cô nuôi mèo, loại ảnh cô thích xem là thú cưng dễ thương và ẩm thực.

Sau khi xác định thông tin cơ bản của ba chân dung người dùng này, chúng ta sẽ gắn ảnh đại diện cho họ, ghi các từ khóa nhu cầu của họ, rồi sắp xếp tất cả lên một trang giấy A4.

Như vậy ta có thể in ra, dán lên tường, để khi thiết kế sản phẩm có thể nhìn họ bất cứ lúc nào, như nhìn những người quen quanh mình.

### Tạo ảnh đại diện cho chân dung

Nhiều cuốn sách nhấn mạnh rằng ảnh đại diện của chân dung người dùng nên chân thực nhất có thể, tốt nhất là dùng ảnh người thật. Nhưng cần lưu ý rằng tìm bừa ảnh người thật trên mạng dễ dẫn đến vấn đề quyền hình ảnh cá nhân. Ở đây xin giới thiệu với các bạn một trang web tạo ảnh chân dung người thật bằng AI, tên là thispersondoesnotexist.com.

![](images/image-117-1024x861.png)

thispersondoesnotexist.com

Có điều trang này tạo ra chủ yếu là người Âu Mỹ, với sản phẩm trong nước thì lại thấy lệch tông đủ kiểu. Tôi thích dùng các trang web tạo khuôn mặt anime kiểu Nhật hơn, ví dụ trang [charat.me](https://charat.me/).

![](images/image-118-1024x948.png)

charat.me

### Chân dung người dùng hoàn chỉnh

Có ảnh đại diện, thêm phần mô tả nhân vật và từ khóa nhu cầu, chúng ta đã có một chân dung người dùng đơn giản mà hữu dụng. Dưới đây là ba chân dung chúng ta đã làm xong:

![](images/image-119-1024x769.png)

Chân dung người dùng: Wang Xiaokang

![](images/image-120-1024x768.png)

Chân dung người dùng: Zhang Xiaoliu

![](images/image-121-1024x767.png)

Chân dung người dùng: Lu Xiaobai

Bước ba: Chân dung → Bối cảnh → Tính năng và phân kỳ
---------------

### Phân tích bối cảnh sử dụng

Có được chân dung người dùng sống động, chúng ta có thể từ chân dung hình dung ra bối cảnh, rồi từ bối cảnh chắt lọc ra danh sách tính năng và tiến hành phân kỳ. Dưới đây, ta sẽ xem cụ thể cách phân tích bối cảnh sử dụng.

#### Phân tích bối cảnh sử dụng của Wang Xiaokang

Trước tiên là bối cảnh sử dụng của Wang Xiaokang, bao gồm ở ký túc xá, ở thư viện và trên lớp học.

Ở ký túc xá, mỗi tối từ tám đến chín giờ cậu dùng máy tính để bàn. Vì ký túc xá khá ồn, cậu sẽ đeo tai nghe khi học. Lúc này cậu dùng bàn phím rời.

Trước khi ngủ, cậu còn cuộn trong chăn nghịch điện thoại một lúc, khoảng từ mười một giờ rưỡi đến mười hai giờ đêm, tức nửa tiếng trước khi ngủ; bối cảnh sử dụng lúc này là học từ vựng bằng điện thoại.

Thư viện cũng là một bối cảnh điển hình, vì trong môi trường này cần giữ yên tĩnh. Nên bạn hoặc đeo tai nghe, hoặc chuyển thiết bị sang chế độ im lặng. Wang Xiaokang thường tự học ở thư viện từ ba đến năm giờ chiều, lúc này cậu dùng laptop và iPad.

Cần lưu ý rằng khi dùng iPad thì không có bàn phím, nên việc nhập liệu không thuận tiện bằng bàn phím rời, tốc độ nhập tổng thể sẽ giảm đi nhiều.

Thư viện và ký túc xá là hai bối cảnh khá khác nhau. Trong ký túc xá rất có thể có bạn cùng phòng đang chơi game hoặc tán gẫu, rất dễ phân tâm, thậm chí quên luôn cả việc học từ vựng, nên chúng ta cần có tính năng nhắc nhở.

Ngược lại, thư viện là môi trường yên tĩnh, đắm chìm, không ai quấy rầy bạn, mọi người đều đang bận học phần của mình.

#### Phân tích bối cảnh sử dụng của Zhang Xiaoliu

Tiếp theo, ta phân tích bối cảnh của Zhang Xiaoliu.

Cô hiện đã nghỉ việc ở nhà, hoàn toàn trong trạng thái ôn thi. Mỗi sáng cô học khóa học online tại nhà hoặc đến lớp luyện thi offline, buổi chiều học từ vựng ở nhà. Buổi tối thì có thể xem phim Hàn.

Bối cảnh chính là buổi chiều học từ vựng. Vì ở nhà, cô dùng máy tính để bàn, chuột và bàn phím đều là loại rời. Mỗi sáng thức dậy có thể cũng cần ôn lại một chút.

Vậy nên hai bối cảnh sử dụng chính của cô là học bằng máy tính, và ôn tập bằng điện thoại khi mới ngủ dậy buổi sáng.

Thực ra bối cảnh này rất giống bối cảnh Wang Xiaokang ôn bài bằng điện thoại buổi tối; ta cứ ghi cả vào, đến khi gộp tính năng ở bước cuối, các nội dung trùng lặp sẽ được gộp lại.

Đồng thời, vì cả hai người dùng này đều đang ôn thi, họ thực ra còn có một bối cảnh đặc thù là「ôn tập cho kỳ thi」.

Trong bối cảnh này, kho từ vựng có phạm vi nhất định, không nhất thiết là toàn bộ kho từ. Còn khi học từ, cần có một chế độ thi: trả lời trong thời gian giới hạn và cho điểm. Những nhu cầu này không nhất thiết đều phải thỏa mãn qua sản phẩm Fuli Words, nhưng có thể ghi lại trước.

#### Phân tích bối cảnh sử dụng của Lu Xiaobai

Xiaobai là dân văn phòng, nên thời gian học rất hạn hẹp, chủ yếu học trong lúc đi lại giữa nhà và công ty, và có chút thời gian rảnh vào cuối tuần.

Bối cảnh thông thường là trên tàu điện ngầm. May mắn thì có chỗ ngồi, không may thì phải đứng. Lúc này cô dùng điện thoại và tai nghe để học.

Vì việc học từ vựng của cô chủ yếu phục vụ nhu cầu công việc, nên trong lúc làm việc có thể còn phát sinh nhu cầu tra từ — có thể giải quyết bằng phần mềm từ điển, nhưng cô có lẽ sẽ muốn thêm từ mới vào Fuli Words để ghi nhớ.

Phần lớn thời gian tàu điện ngầm rất đông, đôi khi phải một tay bám vào tay vịn phía trên hoặc cột bên cạnh, nên Xiaobai có thể cần thao tác bằng một tay.

Ngoài ra cần ý thức rằng Xiaobai chỉ là một đại diện điển hình: cô cần từ vựng ngành sinh học, nhưng những người đi làm khác có thể cần từ vựng của đủ mọi ngành nghề; phần kho từ này cần giải quyết bằng kho từ vựng tùy chỉnh.

Đồng thời, Xiaobai rất thích thú cưng; khi nhìn thấy một chú mèo đáng yêu, rất có thể cô muốn lưu bức ảnh đó vào album. Ở đây nếu kết hợp thêm với chế độ thi ở trên, thực ra ta có thể làm mang tính trò chơi hơn nữa. Ví dụ, ta có thể thêm một bộ sưu tập minh họa — một cuốn album — trong đó có hình tương ứng với từng từ. Chỉ khi bạn đạt độ thành thạo nhất định với từ đó, bạn mới thấy được hình trong đó. Đại thể đó là bối cảnh sử dụng của Xiaobai.

### Từ bối cảnh đến tính năng

Giờ đây bối cảnh sử dụng của ba chân dung người dùng đã phân tích xong. Tiếp theo, ta có thể dựa vào bối cảnh để xác định tính năng. Tức là, để thỏa mãn nhu cầu trong những bối cảnh này, sản phẩm cần cung cấp những tính năng gì để hỗ trợ.

Khi xác định tính năng, có hai loại cần đặc biệt lưu ý. Một là tính năng cốt lõi: thiếu nó thì mọi chân dung đều không dùng được sản phẩm của chúng ta. Loại kia là tính năng biên: thiếu nó thì một chân dung nào đó không dùng được sản phẩm. Tính năng cốt lõi là phần giao, tính năng biên là phần hợp.

Chúng ta sẽ dựa theo thiết lập của các chân dung mà phân bổ một số tính năng biên cho họ. Ví dụ, tại sao Lu Xiaobai lại muốn lưu ảnh vào album, còn Zhang Xiaoliu thì không? Thực tế Zhang Xiaoliu cũng muốn, nhưng ta không cần phân bổ lặp lại một tính năng biên, vì cuối cùng đều sẽ được bao phủ.

Với chân dung, điều cần chú ý là bối cảnh đặc thù của nó, ví dụ chế độ thi là bối cảnh riêng của người ôn thi. Với người không thi thì có hay không cũng chẳng sao, nhưng với người thi thì rất hữu ích.

Sau khi đánh dấu các tính năng biên, ta có thể khoanh vùng phạm vi tính năng tổng thể.

Ví dụ, Zhang Xiaoliu dùng máy tính để bàn của Apple, điều này đòi hỏi bản PC phải hỗ trợ đồng thời hai hệ điều hành Windows và Mac. Lu Xiaobai thao tác một tay khi đi làm về, nên khi thiết kế bàn phím nổi trên điện thoại, ta phải tính đến vấn đề bàn phím đầy đủ 26 phím trên điện thoại màn hình nhỏ dễ bấm nhầm khi dùng một tay.

Với Lu Xiaobai, thời gian rảnh của cô không nhiều, nên có thể còn tận dụng lúc làm việc nhà và tập thể dục; lúc đó nếu muốn ôn từ vựng, có thể còn có nhu cầu đọc từ bằng giọng nói.

Zhang Xiaoliu là fan thần tượng, nên khi xem phim Hàn trên mạng, cô sẽ tiện tay lưu lại ảnh thần tượng mình thích, làm thành kho từ vựng, thậm chí còn chia sẻ cho những người cùng sở thích.

Đây đều là các tính năng biên. Ở giai đoạn thiết kế ban đầu, ta có thể tạm chưa xét đến những vấn đề thực tế như tiến độ, khối lượng phát triển; cứ đưa chúng vào để suy nghĩ trước, còn có làm hay không, khi nào làm, đó là chuyện về sau.

Thứ chúng ta làm ở giai đoạn đầu nên ít nhất có thể, nhưng phạm vi suy nghĩ lại nên rộng nhất có thể. Chúng ta nghĩ cho thấu đáo rất nhiều thứ rồi mới chọn phần cốt lõi nhất, quan trọng nhất để làm. Chứ không phải rất nhiều thứ ta chẳng buồn nghĩ, chỉ làm chút xíu trước mắt rồi bắt tay vào luôn. Như vậy đến giữa dự án sẽ xuất hiện nhiều điểm mù trong tư duy, những điểm mù này thậm chí có thể khiến dự án phải làm lại, nên cần tránh hết mức.

#### [Chắt lọc tính năng bằng sơ đồ tư duy](http://r.ftqq.com/lean-side-bussiness/040305.html#%E9%80%9A%E8%BF%87%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE%E6%A2%B3%E7%90%86%E5%8A%9F%E8%83%BD)

Chúng ta có thể dùng phần mềm sơ đồ tư duy để chắt lọc tính năng.

Hãy hình dung người dùng mới bắt đầu dùng phần mềm của chúng ta từ đâu, rồi theo luồng sử dụng của họ mà xây dựng tính năng song song.

Ví dụ, trước hết cần có hệ thống người dùng để chúng ta nhận diện người dùng. Tiếp đó chắc chắn cần có kho từ vựng, không thì chẳng có từ nào để học. Đương nhiên cũng cần có phần học từ, quản lý từ; nếu muốn thu phí thì chắc chắn còn cần có thanh toán.

Trong hệ thống người dùng, ta cân nhắc dùng đăng nhập WeChat — đây là cách đơn giản nhất hiện nay, không cần làm hệ thống người dùng, cũng không cần làm khôi phục mật khẩu. Có đăng nhập thì đương nhiên phải có đăng xuất.

Có hệ thống người dùng rồi, ta có thể lưu tiến độ học từ của người dùng. Về phía kho từ vựng, đã muốn làm kho từ có thể chuyển đổi và tùy chỉnh thì chắc chắn phải có một danh sách.

Danh sách này, trước hết sẽ có một danh sách chính thức hay còn gọi là tích hợp sẵn, sau đó ta lập thêm một danh sách cục bộ dành cho kho từ tùy chỉnh.

Về phía kho từ tùy chỉnh, có lẽ ta còn cần cung cấp một công cụ để tạo kho từ. Ta cần có bảng từ vựng, cần sinh audio tương ứng, cần có phần giải nghĩa tương ứng, và những hình ảnh xem khi học từ. Đó là các tính năng tổng thể của kho từ vựng.

Nếu muốn làm bộ sưu tập minh họa, ta cần có dữ liệu mức độ hoàn thành kho từ — tức người dùng đã học bao nhiêu phần trăm từ trong kho, và độ thành thạo với từng từ. Trên cơ sở đó, ta còn cần có một album để thưởng thức ảnh HD.

Kho từ tùy chỉnh sau khi tạo xong còn cần có cách chia sẻ. Ta có thể cho phép người dùng chia sẻ qua mã QR, người dùng khác quét mã QR để nhập vào.

Tiếp theo, ta xem tính năng học từ vựng.

Trước hết cần có chỗ để nhập chữ cái; ta sẽ điều chỉnh lớp che (mask) một cách động theo chữ cái được nhập. Sau đó ta cần thống kê thời gian nhập hoặc số lần sai của người dùng — điều này thể hiện độ thành thạo với từ đó. Ta cũng còn cần vài nút phụ trợ để hiển thị nghĩa của từ, cũng như bỏ qua từ không biết.

Cuối cùng, khi từ được nhập đúng, ta cần hiển thị một bức ảnh HD để người dùng có thể xem trọn vẹn bức ảnh — đó là phần thưởng dành cho họ.

Ngoài ra ta cũng cần ghi lại thành tích học từ của người dùng; để nhìn thành tích rõ hơn, có lẽ còn cần cung cấp thống kê tiến độ, cho người dùng biết đã học bao nhiêu phần trăm kho từ, độ thành thạo từng phần là bao nhiêu.

Còn phần thanh toán đừng quên. Trước tiên phải hiển thị các sản phẩm có thể trả phí; khi bấm nút mua, phải gọi WeChat Pay lên. Sau khi thanh toán WeChat hoàn tất, phải tiến hành xác nhận. Đồng thời ta cũng cần duy trì một danh sách đơn hàng để làm hậu mãi và hoàn tiền.

### Phân kỳ

Xác định xong bảng tính năng, tiếp theo có thể tiến hành phân kỳ.

#### Phân kỳ tính năng

Quy trình phổ biến nhất ở bước này thực ra là thiết kế MVP chứ không phải phiên bản đầu tiên, nhưng cách thiết kế là như nhau, nên chúng ta chọn minh họa trường hợp phức tạp hơn.

Vì các tính năng hiện tại thực sự đã rất nhiều, bắt buộc phải chia thành các giai đoạn khác nhau để làm. Sản phẩm khả thi tối thiểu không mấy điển hình, nên ở đây ta lấy phiên bản đầu tiên sau khi kiểm chứng PMF hoàn tất làm ví dụ để chọn nội dung cho kỳ một. Kỳ hai là các tính năng「để sau hẵng làm」, kỳ ba là các tính năng「không biết bao giờ mới làm」.

Hãy xem danh sách tính năng của chúng ta:

-   Thông báo đẩy nhắc nhở: có thể đưa vào kỳ một. Nhưng để làm push, cần có hệ thống tin nhắn. Nếu muốn nhắc nhở theo lịch, còn phải làm giao diện cài đặt. Vì người dùng sau khi cài nhắc nhở, có thể một ngày nào đó không cần nữa, phải hủy được kịp thời, không thì ngày nào cũng bị đẩy thông báo khá phiền.
-   Chế độ thi: đưa vào kỳ hai. Tuy rất quan trọng với người ôn thi, nhưng vì khối lượng phát triển tổng thể khá lớn, trước khi kiếm được tiền có thể tạm chưa làm.
-   Bàn phím ảo: đưa vào kỳ một. Để hỗ trợ thao tác một tay, ta cần thêm giao diện bàn phím trên thiết bị di động cho màn hình học từ. Bàn phím của các bộ gõ khác nhau có thể gây vấn đề tương thích, nên ta giải quyết trực tiếp bằng một bàn phím ảo.
-   Chia sẻ kho từ tùy chỉnh: đưa vào kỳ hai.
-   Chế độ bộ sưu tập minh họa: đưa vào kỳ hai, cũng có thể là kỳ ba.
-   Phát lại giọng đọc: đưa vào kỳ hai.

![](images/image-123-1024x784.png)

Dùng sơ đồ tư duy xây dựng danh sách tính năng

Khi chốt phân kỳ, cũng phải đồng thời kiểm tra các điểm tính năng đã khớp đủ chưa. Ví dụ trong phần thanh toán, ta cần thêm mục「tích hợp WeChat Pay」.

### Gom tính năng vào giao diện

Sau khi chốt danh sách tính năng của một kỳ nào đó, có thể gom các tính năng vào từng giao diện. Tạo một sơ đồ tư duy mới, ghi ra các giao diện hiển nhiên, rồi đặt các tính năng vào dưới giao diện tương ứng.

![](images/image-122-1024x987.png)

Gom tính năng vào giao diện

Nếu phát hiện có tính năng không có giao diện nào để đặt, xin chúc mừng — bạn đã phát hiện sớm một giao diện bị bỏ sót, hãy mau thêm giao diện đó vào.

Hoàn thành bước này, chúng ta có thể bắt đầu bước vào giai đoạn thiết kế.

Bước bốn: Thiết kế sản phẩm
--------

Khuyến nghị dùng phần mềm prototype vector để thiết kế giao diện; các phần mềm thường dùng gồm Adobe XD, Sketch, Figma và Penpot mã nguồn mở. Bài viết này lấy XD làm ví dụ, nhưng cách dùng các phần mềm nhìn chung tương tự nhau, có thể suy một ra ba.

### Adobe XD là gì

![](images/image-124-1024x757.png)

Adobe XD

Adobe XD là công cụ thiết kế vector do Adobe phát triển; nó tương tự Sketch, vừa có thể dùng để vẽ giao diện vector, vừa bao gồm tính năng thiết kế prototype, lại còn có thể xem trước giao diện đã thiết kế trên điện thoại. XD hỗ trợ Windows và Mac, là một trong số ít phần mềm của Adobe có thể dùng miễn phí (tất nhiên bạn có thể trả phí nâng cấp bản pro).

Adobe từng chuẩn bị mua lại Figma nên đã ngừng cập nhật XD, nhưng sau đó thương vụ lại thất bại. Hiện tại khuyến nghị dùng Figma hoặc Penpot mã nguồn mở.

### Dùng Adobe XD thiết kế giao diện đơn giản

Việc dùng phần mềm chủ yếu vẫn dựa vào chăm học chăm luyện; ở đây chúng tôi minh họa cách dùng nó để thiết kế giao diện học từ vựng.

#### Hiểu về artboard

Trước tiên, ta tạo một artboard (bảng vẽ) mới trong XD.

Artboard là gì? Nó tương đương với trang trong Word. Các công cụ thiết kế thuần túy thường không có khái niệm artboard, nhưng XD còn bao gồm tính năng prototype; đôi khi ta cần chuyển qua lại giữa nhiều giao diện, và một artboard thường tương ứng với một giao diện.

Bấm nút artboard — nút thứ hai từ dưới lên trong menu bên trái,

![](images/image-125.png)

Nút artboard

lúc này ở mép phải màn hình sẽ hiện ra một loạt kích thước artboard định sẵn.

![](images/image-126-313x1024.png)

Các artboard định sẵn

Nó đã chuẩn bị sẵn cho chúng ta các quy cách thường dùng, ví dụ iPhone, iPad của Apple, các dòng máy Android của Google, cùng các kích thước web phổ biến.

Ta chỉ cần chọn kích thước tương ứng từ đó; tất nhiên cũng có thể không chọn cái định sẵn mà trực tiếp kéo tay để vẽ hoặc chỉnh chiều rộng, chiều cao của artboard trong phần thuộc tính. Vậy ta tạo một artboard kích thước iPhone Xs nhé.

Sau đó nhấn CTRL hoặc CMD + D là có thể nhân bản artboard trực tiếp. Ta đặt tên artboard đầu tiên là giao diện học từ vựng, rồi bắt đầu thiết kế.

![](images/image-127-1024x614.png)

Nhân bản artboard

#### Tạo lớp che

Trước tiên, ta tạo hiệu ứng lớp che hiển thị khi chưa nhập xong các chữ cái lúc học từ. Chọn công cụ hình chữ nhật trong thanh công cụ bên trái 

![](images/image-129.png)

Công cụ hình chữ nhật\
, vẽ một hình chữ nhật phủ toàn bộ artboard. Sau đó chỉnh màu tô thành đen, độ trong suốt 30%.

![](images/image-128-1024x527.png)

Tạo lớp che

Rồi ta lên unsplash.com — trang ảnh không bản quyền — tìm một bức ảnh mèo và đưa nó vào.

![](images/image-130-1024x677.png)

Thêm ảnh mèo

Lúc này con mèo nằm phía trên lớp che, nên nó che mất lớp che.

![](images/image-131.png)

Điều chỉnh thứ tự layer

Bấm chuột phải, chọn「Send to back」để đưa nó ra sau lớp che, ta sẽ thấy được chú mèo bị lớp che bán trong suốt phủ lên.

#### Nghĩa của từ và ô nhập liệu

Tiếp theo, phía trên lớp che, ta đặt phần nghĩa của từ và ô nhập liệu. Bấm vào biểu tượng

![](images/image-132.png)

Công cụ văn bản\
trong thanh công cụ ngoài cùng bên trái để chuyển sang công cụ văn bản.

Sau đó nhập phần nghĩa bằng chữ.

![](images/image-133-1024x490.png)

Thêm chữ

Trong bảng thuộc tính bên phải, ta có thể chỉnh font, cỡ chữ, màu sắc và căn lề của chữ.

Rồi ta đặt Logo đã thiết kế từ trước lên, thêm ô nhập từ.

![](images/image-134.png)

Thêm ô nhập từ

Lưu ý ô nhập này không nhất thiết phải là「ô」; ví dụ ở đây ta cũng có thể làm nó thành gạch chân.

#### Bàn phím ảo

![](images/image-135-497x1024.png)

Bàn phím ảo

Tạo bàn phím ảo trong XD cũng rất đơn giản, cứ vẽ trực tiếp bằng công cụ hình chữ nhật là được. Điều cần lưu ý là cách làm bo góc.

![](images/image-136.png)

Thiết lập bo góc

Thực ra rất đơn giản: trong phần cài đặt thuộc tính bên phải, đổi bo góc từ 0 thành 5 là xong. Sau khi làm xong một nút, ta có thể giữ Shift để chọn đồng thời nút và chữ phía trên, rồi trong menu chuột phải gộp chúng thành nhóm (Group); sau đó nhấn CTRL hoặc CMD + D là có thể nhân bản nút.

![](images/image-137-1024x892.png)

Phân bố và căn chỉnh hàng loạt

Khi số nút nhiều lên, căn chỉnh chúng khá mất công. Thực ra sau khi chọn nhiều nút, có thể vào menu Object → Align để căn chỉnh tự động; cũng có thể vào Object → Distribute để chúng tự phân bố đều.

#### Icon vector

Tiếp nữa, ta cần đưa icon vào giao diện. Đã là giao diện vector thì đương nhiên icon vector là tốt nhất. Phía trước chúng tôi đã giới thiệu thenounproject.com; nó còn cung cấp cho người dùng pro một ứng dụng client. Trong client này có thể sao chép icon rất tiện lợi.

![](images/image-138.png)

Icon vector

Khi tìm được icon qua từ khóa, ta có thể tải về rồi kéo thả vào XD; hoặc bấm chuột phải trong client chọn Copy as SVG rồi dán trực tiếp. Vì là định dạng SVG, sau khi chỉnh kích thước có thể đổi màu rất dễ dàng.

Cuối cùng ta tinh chỉnh lại vị trí ô nhập và phần nghĩa của từ một chút, giao diện học từ vựng thế là hoàn thành. Việc tạo các giao diện khác cũng rất tương tự, không nhắc lại dài dòng ở đây nữa.

Các bước tiếp theo: Phát triển sản phẩm, gọi vốn cộng đồng, phát triển lặp
-----------------

Hoàn thành thiết kế sản phẩm (phiên bản đầu thường là thiết kế MVP) xong, chúng ta có thể bước vào giai đoạn phát triển. Lưu ý, với MVP, thiết kế sản phẩm và phát triển sản phẩm không phải là bắt buộc, và nên tránh hết mức miễn là vẫn kiểm chứng được nhu cầu. Chỉ khi không thể thể hiện đặc tính sản phẩm bằng bài viết kèm hình ảnh, video demo v.v., cũng không thể dựng nhanh bằng phần mềm open source, thì mới tiến hành phát triển MVP ở cấp độ sản phẩm.

Chuẩn bị xong MVP, chúng ta có thể kiểm chứng nhu cầu và năng lực marketing cơ bản nhất thông qua gọi vốn cộng đồng (crowdfunding). Khi gọi vốn đạt chỉ tiêu, ta mới bước vào giai đoạn phát triển lặp tiếp theo. Ngược lại, thì quay về phần tuyên bố giá trị để tối ưu lại hoặc chuyển hướng.
