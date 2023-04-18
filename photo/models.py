from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.
# User모델에 몇가지 필드 추가(성별, 생년월일 등) -> Django에서 기본으로 제공하는 User 모델 확장
# 성별을 선택할 수 있도록
GENDER_C = (
    ('선택안함', '선택안함'),
    ('여성', '여성'),
    ('남성', '남성'),
)

class User(AbstractUser):
    gender = models.CharField(max_length=10, choices=GENDER_C, default='N')
    birthdate = models.DateField(null=True, blank=True)

class Photo(models.Model): # 상속을 받은 클래스, 장고에서 장고뒤에있는 models의 model을 상속받도록 함
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos')
    # 누군가를 참조하는 역할(ForeignKey), User테이블 참조(장고에서 디폴트로 정의되어있는 테이블임)
    # 연결된 모델이 삭제될 경우 어떻게 할지...CASCADE -> 하위 객체 같이 삭제
    # 객체에서 하위 객체의 목록을 부를때 사용할 이름
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no_image.png')
    # 마이그레이트 하면 ImageField Pillow not installed 에러 나므로 pip install pillow 하기
    text = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta :
        ordering = ['updated']

    def __str__(self):
        return self.author.username + " " + self.created.strftime("%Y-%m-%d%H:%M:%S")

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[str(self.id)])

