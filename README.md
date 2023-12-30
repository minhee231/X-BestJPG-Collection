# What is this
제가 지정한 태그를 검색하여 이미지, 좋아요 데이터들을 저장합니다.
그 중 좋아요 n개  가 넘는 트윗들을 분류하여 웹 페이지에 띄어줍니다.

# Deploy 
* AWS EC2
* Apache Server

# Link
[GoSite]()

### 번외
[GoS3Site](https://goooooo.s3.ap-northeast-2.amazonaws.com/index.html)
S3 웹 정적 배포가 가능해 한 번 올려보았습니다.  
route를 통한 페이지 접근은 가능하지만 이동한 URL에 다시 접근하면 액세스 디나이드가 뜹니다.

###예
https://goooooo.s3.ap-northeast-2.amazonaws.com/index.html 에 접근하여 아무 버튼이나 눌러
https://goooooo.s3.ap-northeast-2.amazonaws.com/project-sekai/100 에 접근하는것은 가능합니다.
하지만 https://goooooo.s3.ap-northeast-2.amazonaws.com/project-sekai/100 이 URL에 다시 요청을 보내면 액세스 디나이드가 뜹니다.