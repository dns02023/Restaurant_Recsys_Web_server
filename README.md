# Restaurant_Recsys_Web_server

고려대학교 커뮤니티 고파스 sofo 서비스 데이터를 활용한 맛집 추천시스템 웹 서비스  

* 웹서비스 & 추천시스템 서빙 파이프라인  

![프로젝트_아키텍처](https://user-images.githubusercontent.com/20104945/91432836-48604680-e89d-11ea-8d94-58834c495d57.png)  




고려대학교 주변 맛집 정보를 조회하고 리뷰를 남길 수 있습니다.   
남긴 리뷰들은 Collaborative Filtering 기반의 추천시스템 학습에 사용됩니다.  


![메인페이지](https://user-images.githubusercontent.com/20104945/92298140-d9f84400-ef80-11ea-81ce-9cf6933b89d3.png)  

로그인을 하면 남겼던 리뷰들을 바탕으로 사용자에게 메인페이지에서 맛집들을 추천해줍니다.  



![상세페이지](https://user-images.githubusercontent.com/20104945/92298143-e1b7e880-ef80-11ea-97ca-3c8079eade3d.png)  

맛집 상세 정보를 조회하면 해당 맛집과 유사한 맛집을 tag 유사도 기반 content-based 기법으로 추천해줍니다.  

추천 결과들을 추천 API 서버에 요청하여 받아온 다음, 사용자에게 서빙합니다.  
추천 API 서버 : https://github.com/dns02023/Restaurant_Recsys_RESTAPI_Server    


해당 웹서비스는 고려대학교 맛집 리뷰 게시판 서비스는 KOREAPAS sofo 의 데이터를 활용하였습니다.   
 


![sofo2](https://user-images.githubusercontent.com/20104945/92298153-090eb580-ef81-11ea-9fe1-97f9dd4ec53e.jpg)
![sofo1](https://user-images.githubusercontent.com/20104945/92298154-09a74c00-ef81-11ea-84bb-23e8b7a99f23.jpg)

