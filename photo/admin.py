from django.contrib import admin
# Photo 모델 등록
from .models import Photo, User

# Register your models here.

# 관리자 페이지 사진목록을 보기 편한 형태로 변경하기 위해 관리자 페이지 커스타마이징
# PhotoAdmin이라는 옵션 클래스 정의
class PhotoAdmin(admin.ModelAdmin): # admin.ModelAdmin 클래스 상속받음
    list_display = ['id', 'author', 'created', 'updated']
    # 목록에 보일  필드 설정, 모델 필드 선택 or 별도 함수 만들어 필드처럼 등록
    raw_id_fields = ['author']
    # ForeignKey 필드 -> 연결된 모델 객체 목록 출력 선택시 목록이 길 경우 불편함
    # 설문조사 앱 -> Choice 값 입력시 팝업 창으로 Question 선택
    # raw_id_fields로 설정시 Id값 입력창으로 형태가 바뀌고 검색 기능 선택 가능
    list_filter = ['created', 'updated', 'author']
    # 필터 기능 사용할 필드 선택, Django가 적절하게 필더 범위 출력
    search_fields = ['text', 'created']
    # 검색 기능 -> 검색할 필드 선택, ForeignKey 필드는 설정불가
    ordering = ['-updated', '-created']
    # 모델의 기본 정렬값x 관리자 사이트에서 기본으로 사용할 정렬값 설정

admin.site.register(Photo, PhotoAdmin)

admin.site.register(User) # User 모델 등록