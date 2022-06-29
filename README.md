# API 초기 세팅
pip install fastapi

pip install uvicorn

pip install pymysql

pip install python-dotenv

.env 파일생성후 db 정보 입력 (host, user, password, db)


# API 실행방법
1. API폴더로 이동 (cd API)
2. 명령어 입력 : uvicorn main:app --reload 
3. 아래와 같이 API띄워놓고 vue 실행
![image](https://user-images.githubusercontent.com/94157053/175268298-097fa20d-d60a-48a0-89a2-9b5cab3c2c04.png)

# vue 실행방법
1. API 실행후 또 하나의 쉘 실행
2. intellisys 폴더로 이동 (cd intellisys)
3. 명령어 입력 : npm run serve
![image](https://user-images.githubusercontent.com/94157053/176387991-a2bb0110-cee2-4b71-9151-ce225a0df629.png)

왼쪽은 aoi실행 화면, 오른쪽은 vue실행 화면
![image](https://user-images.githubusercontent.com/94157053/176388365-33d95694-6fdd-4bb6-88c3-8b8ec5e38fb3.png)
