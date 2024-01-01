# What is this
제가 지정한 태그를 검색하여 이미지, 좋아요 데이터들을 저장합니다.
그 중 좋아요 n개  가 넘는 트윗들을 분류하여 웹 페이지에 띄어줍니다.

# Deploy 
* AWS EC2
* Apache Server  
[배포 과정](https://minhee-goo.tistory.com/15)

# Link
http://15.164.158.177/about

# ETC
EC2 요금 때문에 서버를 내릴지도 모릅니다.  
  

[S3-Link](https://goooooo.s3.ap-northeast-2.amazonaws.com/index.html)  
그래서 S3 배포하였습니다. 하지만 S3를 통한 배포는 문제점이 있습니다.  
  
페이지에서 버튼을 눌러 페이지에 접근하면 vue router를 통해 /project-sekai/100 으로 이동합니다.  
하지만 S3에는 /project-sekai/100에 해당하는 파일이 없어 액세스 디나이드를 반환합니다.  
때문에 위 웹사이트에 접근하기 위해서는  
https://goooooo.s3.ap-northeast-2.amazonaws.com/index.html
존재하는 파일인 index.html에 접근해야 합니다.