from django.shortcuts import render


# 화면에 글씨를 출력하는 코드
def home(request):
    context= {"name": "오혜빈", "food": "스테이크"}
    # render(html파일을 연결시켜주는 라이브러리)
    return render(request, "first/home.html", context)
