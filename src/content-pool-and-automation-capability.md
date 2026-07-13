# Content pool và năng lực tự động hóa


Content pool
Ngoài user pool, thực ra chúng ta còn cần một content pool. Có hai lý do.

Website chính thức: thương hiệu và cửa ngõ
Content pool trước hết dùng để đặt website chính thức — đây là thương hiệu và cửa ngõ của chúng ta.

Thông thường khi làm sản phẩm phần mềm, đa số mọi người sẽ làm một website chính thức cho sản phẩm; nhưng khi làm sản phẩm truyền thông, rất có thể chỉ có đủ loại tài khoản trên các nền tảng mà không có website riêng.

Nhưng thực ra, ý nghĩa của website chính thức rất lớn. Nói rộng ra, nó đại diện cho thương hiệu, IP và cửa ngõ. Nói hẹp lại, nó giải quyết được vấn đề thực tế kiểu "tài khoản bị nền tảng khóa thì làm sao?".

Nếu chúng ta có tài khoản trên mọi nền tảng nhưng không có website độc lập, thì lỡ tài khoản trên nền tảng bị khóa, người dùng dù muốn tìm chúng ta, biết cả tên thương hiệu, họ cũng không có cách nào liên lạc, vì chúng ta chẳng còn kênh nào khác.

Chuyện khóa tài khoản tuy là sự kiện xác suất thấp nhưng rất chí mạng. Hơn nữa, khi ngày càng nhiều nền tảng dùng AI chưa hoàn thiện, kể cả một tài khoản khuôn phép từng li từng tí cũng có thể vô cớ kích hoạt quy tắc kiểm soát rủi ro dẫn đến bị khóa.

Vì vậy chúng ta cần một thứ hoàn toàn nằm trong tay mình. Đảm bảo rằng nếu nền tảng khóa tài khoản, chỉ cần người dùng muốn, họ vẫn tìm được chúng ta. Một thương hiệu dễ nhớ, một tên miền ngắn gọn chính là giải pháp tốt.

Trung tâm nội dung
Content pool ngoài vai trò cửa ngõ còn là trung tâm nội dung của chúng ta — mọi nội dung đều nên đưa lên nền tảng này. Không phải là người dùng chỉ được xem ở đây, mà là nội dung chúng ta đăng trên các nền tảng khác đều nên có một bản ở đây. Có vậy mới ứng phó được với vấn đề "nội dung bị xóa thì làm sao?".

Nội dung bị xóa trên các nền tảng, hoặc không qua kiểm duyệt, hoặc duyệt xong rồi đột nhiên lại không qua — những chuyện này đã quá quen thuộc. Chúng ta cần làm một bản sao lưu trên website của mình. Như vậy, kể cả nội dung đăng trên nền tảng bị xóa, người dùng vào website vẫn xem được.

Có bạn có thể nghĩ nội dung bị xóa chẳng phải chuyện lớn, nhưng nếu là một loạt nội dung mà vài tập trong đó bị xóa, thậm chí một series bài giảng mà mấy bài then chốt nhất bị nền tảng xóa một cách khó hiểu, mình lại không có bản sao lưu, người dùng cũng chẳng còn chỗ nào xem — vậy thì khó chịu vô cùng đúng không?

Chi phí nội dung
Sao lưu toàn bộ nội dung có thể gặp vấn đề chi phí.

Nếu chỉ là nội dung chữ và ảnh thì tổng chi phí khá thấp, chúng ta dùng thẳng lưu trữ cloud, truy cập qua CDN là được. Nhưng nếu nội dung có nhiều video, tự hosting có thể khiến chi phí tăng lên.

Chúng tôi giải quyết vấn đề chi phí video bằng hai phương án.

Phương án đa nguồn video
Nói đơn giản: trên website, ưu tiên hiển thị video của nền tảng khác dưới dạng nhúng (embed); chỉ khi video hỏng, hoặc người dùng chủ động yêu cầu, mới tải nguồn video do chúng tôi tự host.

Về triển khai cụ thể, chúng tôi làm một plugin WordPress. Nó có thể đặt nhiều nguồn video vào cùng một khung phát. Mặc định hiển thị video Bilibili, bấm Tab để chuyển sang YouTube hoặc nguồn của chúng tôi. Nhờ vậy phần lớn lưu lượng video sẽ đổ về Bilibili.

Phương án lưu trữ nước ngoài và CDN
Một cách tiết kiệm khác là với những nghiệp vụ không trọng yếu, có thể cân nhắc dùng dịch vụ nước ngoài.

CDN trong nước (Trung Quốc) vì lý do chi phí đều khá đắt, đại khái mỗi GB cũng mất vài mao tệ. Nhưng giá tài nguyên mạng ở nước ngoài lại khác, hoàn toàn có thể dùng cho nghiệp vụ không trọng yếu hoặc làm phương án dự phòng.


Bảng giá R2
Ví dụ, R2 của Cloudflare không tính phí lưu lượng, chỉ thu phí theo dung lượng lưu trữ và số lần truy cập. Hạn mức miễn phí mặc định cũng rất cao, khi người dùng chưa nhiều thì hoàn toàn có thể dùng miễn phí.

Nhưng vấn đề của nó là khi truy cập từ Trung Quốc, tốc độ không nhanh bằng dịch vụ cùng loại trong nước. Dù sao cũng không có máy chủ trong nước, kể cả đặt ưu tiên khu vực Đông Á, tốc độ truy cập vẫn chậm hơn một chút. Hiện ảnh trên website Fangtang 07 của chúng tôi đang đặt trong R2, mọi người có thể thử tốc độ. Phản hồi của người dùng trước đây là tạm ổn.

Với hai phương án trên, về cơ bản chúng ta có thể sao lưu toàn bộ nội dung với chi phí gần như bằng không.

Nhưng phải hiểu rất rõ một điều: kể cả về dài hạn, lượng người dùng, lưu lượng và sức ảnh hưởng của website chúng ta cũng khó lòng sánh với các nền tảng lớn bên thứ ba. Vì vậy chúng ta vẫn cần phân phối nội dung lên các nền tảng bên thứ ba để tiếp cận những người dùng ở đó.

Không phải người dùng nào trên nền tảng cũng sẵn lòng rời nền tảng để đến website của chúng ta, nên ta cần phân phối nội dung lên các nền tảng đó, để nhóm người dùng không muốn qua vẫn xem được nội dung của chúng ta ngay trên nền tảng bên thứ ba. Chỉ khi chúng ta xây dựng được quan hệ tin cậy lâu dài với họ, họ mới sẵn lòng đến website của chúng ta.

Năng lực phân phối nội dung
Thực tế, phân phối nội dung là một công việc rất cực: nó đơn giản nhưng rất lặp đi lặp lại.

Vì cứ mỗi lần đăng nội dung, chúng ta lại phải làm lại nguyên quy trình đó — đây thực ra là phần lớn khối lượng công việc của vị trí vận hành truyền thông mới.

Hình dưới là một sơ đồ phân phối nội dung khá điển hình, cũng là cách Fangtang đang dùng.


Phương án phân phối nội dung của Fangtang
Nội dung dài
Trước hết chúng tôi dùng WordPress dựng website chính thức (ft07.com) để đặt nội dung chữ-ảnh dài (bài viết). Hiện chủ yếu là nội dung liên quan đến phương pháp doanh nghiệp một người, sau này sẽ chuyển dần các nội dung khác về. Những bài dài này có thể đẩy thẳng qua API vào official account để đăng.

Nội dung ngắn
Mảng nội dung ngắn (kiểu Weibo), chúng tôi tự host một Memos — đây là dự án open source khá giống Weibo, có thể tự dựng. Đăng nội dung lên đó trước, rồi dùng công cụ đồng bộ sang Weibo và Twitter. Cách này tránh được việc nội dung ngắn bị xóa trên nền tảng. Đồng thời, chúng tôi hiển thị nội dung ngắn lên website qua widget, vì website mới là content pool, mọi nội dung đều phải hội tụ về đây.

Nội dung video
Mảng video, vì trước đây chúng tôi làm khóa học online nên có sẵn một sản phẩm khóa học. Chúng tôi đặt video lên nền tảng khóa học đó để host cục bộ. Đồng thời phân phối video lên Bilibili và YouTube, rồi từ hai nền tảng này dẫn ngược lưu lượng về website. Việc tự host video này không bắt buộc, dùng thẳng WordPress cũng làm được.

Có thể thấy, trong khung này, dù là nội dung ngắn, bài chữ-ảnh dài hay video đều được xử lý khá ổn.

Nhưng để vận hành trọn vẹn quy trình này lại không dễ. Nếu nội dung cập nhật hàng ngày, nhất là nội dung ngắn, có khi vài chục lần một ngày, thì bản thân việc phân phối sẽ rất phiền. Không phải nó khó, mà là khối lượng công việc của nó — một việc tay chân thuần túy.

Nhưng may mắn là giờ chúng ta có thể làm việc này bằng tự động hóa, hiệu suất tăng hàng chục lần.

Tất nhiên, không có nghĩa tự động hóa thay thế hoàn toàn được vị trí truyền thông mới — vị trí này còn nhiều chức năng khác như tương tác với người dùng, chăm sóc khách hàng, duy trì quan hệ. Những việc này hiện tự động hóa tạm thời chưa làm được. Nhưng AI có lẽ tương lai sẽ làm được, dù sao bây giờ "bình luận Robert" đã biết cãi nhau với người dùng rồi (đùa thôi).

Tóm lại, hiện chúng ta thực sự có thể dùng năng lực tự động hóa để hoàn thành việc phân phối nội dung. Vì vậy, năng lực phân phối nội dung về bản chất chính là năng lực tự động hóa.

Năng lực tự động hóa
Mảng năng lực tự động hóa, chúng tôi dùng FlowDeer.

FlowDeer
Bạn có thể coi nó là một công cụ quản lý script tự động hóa, đồng thời kèm sẵn rất nhiều script làm sẵn. Có thể đọc bài viết này để tìm hiểu thêm.


Giao diện FlowDeer
Những script chúng tôi dùng nhiều nhất chủ yếu là đăng Weibo, đăng Twitter, giám sát và thu thập nội dung RSS, giám sát kèm dịch nội dung trang web, và giữ tài khoản luôn đăng nhập (keep-alive).


Một số script FlowDeer/FXD thường dùng
Giữ tài khoản luôn đăng nhập nghĩa là, ví dụ khi đăng nội dung Weibo thì tài khoản phải ở trạng thái đăng nhập, đúng không? Keep-alive tức là sau khi đăng nhập một lần, cứ cách một khoảng thời gian nó lại giúp bạn làm mới phiên, đảm bảo tài khoản luôn đăng nhập. Như vậy lúc cần đăng thì không phải đăng nhập lại, đăng thẳng luôn.

Chúng tôi còn làm "trợ lý biên tập bài viết" — một sự kết hợp giữa tự động hóa và tính năng AI.

Như tôi hay chia sẻ các dự án open source trên GitHub, trước đây đều phải tự viết nội dung giới thiệu. Có trợ lý biên tập này rồi, cơ bản tôi chỉ cần ném cho nó một link, nó tự vào chụp màn hình rồi trích xuất nội dung chính, viết một bản tóm tắt, viết xong đưa tôi duyệt, duyệt xong đăng luôn. Cả quy trình rất trơn tru, thường chưa đến một phút.

Vì vậy năng lực tự động hóa thực ra đã là năng lực bắt buộc của content pool. Đặc biệt với doanh nghiệp một người, sức lực của chúng ta cực kỳ hạn chế, nên chỗ nào tự động hóa được thì nhất định phải tự động hóa.

Script trình duyệt lập trình được
Tất nhiên nếu không muốn dùng FlowDeer, thực ra bạn cũng có thể tự viết script Puppeteer. Đây là một headless browser, hoặc chính xác hơn hãy hiểu nó là trình duyệt lập trình được. Chúng ta có thể lập trình điều khiển mọi thứ của trình duyệt: mở một trang web, bấm một nút, kiểm tra đoạn văn bản tương ứng, upload file, đăng video — và tất cả đều tự động.

Vấn đề captcha
Tất nhiên cũng có một số hạn chế, ví dụ captcha và các loại xác minh robot kiểu kéo-thả.

Chúng tôi khuyên mọi người dùng nó để thay thế công việc hàng ngày của chính mình, tức là tự động hóa hoàn toàn trong phạm vi tần suất thao tác mô phỏng người thật. Trong trường hợp đó, thực tế số lần gặp captcha sẽ không nhiều. Còn nếu muốn mở rộng quy mô thì vấn đề này rất lớn — nhưng đó không phải mục tiêu của chúng ta. Mục tiêu của chúng ta là thay thế công việc hàng ngày.

Dùng AI chat điều khiển workflow
Mặt khác, tự động hóa + AI chat có thể làm năng lực tự động hóa trở nên linh hoạt. Đây là một ví dụ: cửa sổ AI chat tích hợp trong FlowDeer.


Workflow chat của FlowDeer Chat
Trong môi trường chat này, bạn có thể dùng tất cả script trong FlowDeer như những công cụ (tool). Ví dụ như trong hình, tôi có thể gọi công cụ tạo ảnh để nó sinh một bức ảnh, đồng thời gọi công cụ đăng Weibo để nó đăng lên Weibo. Và tất cả những việc này chỉ cần hoàn thành bằng cách trò chuyện trong cửa sổ chat — cực kỳ tiện lợi và hiệu quả.

Tất nhiên hiện tại vì giới hạn trí tuệ của AI, nó vẫn chỉ là một thứ mang tính hỗ trợ. Nhưng tôi nghĩ đó chỉ là tạm thời, vì trí tuệ của AI mỗi tháng đều tăng, tôi nghĩ rất nhanh sẽ đạt chuẩn của người bình thường.
