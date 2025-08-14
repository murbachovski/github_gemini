# 프로젝트 제목
```
YoutubeGemini — 유튜브 영상 AI 분석 서비스
```

# 프로젝트 설명
```
YoutubeGemini는 유튜브 영상 URL과 질문을 입력하면,
Google Gemini AI로 영상을 분석해 자연어 답변을 제공하는 웹 서비스
```

# 가상환경 설정
```
conda create -n gem_tube python=3.9
```

# API_KEY 설정
```
export GENAI_API_KEY="AIzaSyDxxxxxxxxxxxxxxxxxxxx"
```

# 라이브러리 설치
```
pip install -r requirements.txt
```

# 앱 실행
```
./run.sh
```

# 웹 구성
<p align="center">
  <img src="https://github.com/user-attachments/assets/fd94db63-3fab-4d28-84a0-cb9bbe6e81da" width="700">
  <img src="https://github.com/user-attachments/assets/0f9d8a61-aaf3-4ff6-a94f-fd6ea061cf35" width="700">
  <img src="https://github.com/user-attachments/assets/4260a276-01ba-4b19-9ce5-4cf7d4300e8a" width="700">
</p>

# Ngrok
(로컬 서버 => 공개 서버로 전환)
```
<Mac M1 설치 기준>
https://ngrok.com/downloads/mac-os
brew install ngrok
ngrok config add-authtoken <token>
ngrok http 80
```

# Ngrok log
<p align="center">
  <img src="https://github.com/user-attachments/assets/5ca755c3-d8f8-4088-b3b4-1b735945d351" width="700">
</p>

# Ngrok(공개 서버 접속)
[Ngrok 공개 서버 접속](https://c83c0967a9dd.ngrok-free.app/)<br>

# Ngrok 참고 문서
[위키독스](https://cordcat.tistory.com/105)<br>

# Make requirements.txt
```
pip install pipreqs
```

# pipreqs 참고 문서
[PyPI pipreqs](https://pypi.org/project/pipreqs/)<br>

# Gemini 참고 문서
[위키독스](https://ai.google.dev/gemini-api/docs)<br>
