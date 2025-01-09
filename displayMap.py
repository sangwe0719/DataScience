import webbrowser
import os

# 지도를 웹 브라우저에 표시
def showMap(map):
    map.save("map.html")  # 지도가 포함된 html 파일 생성
    filepath = os.getcwd()
    file_uri = 'file:///'+filepath + '/map.html'
    webbrowser.open_new_tab(file_uri)  # html 파일 오픈
