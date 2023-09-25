from django.contrib import admin
from .models import Question, Choice

class ChoiceAdmin(admin.ModelAdmin):
    # fields = ('choice_text', 'votes','question')
    # fieldsets = (
    #     ('Choice', {
    #         'fields' : ('choice_text','votes')
    #     }),
    #     ('Question', {
    #         'fields' : ('question',)# 파이썬 튜플은 하나짜리는 무조건 , 를 붙인다.
    #     })
    # )

    fieldsets = (
        ('Choice', {
            'fields' : ['choice_text','votes'], 'classes' : ['collapse']
        }),
        ('Question', {
            'fields' : ['question'], 'classes' : ['collapse'] # classes 숨김기능
        })
    )
    list_filter = ('choice_text', 'question') # 필터

    search_fields = ('choice_text',) # 검색

# admin 사이트에 models 등록
admin.site.register(Question)
admin.site.register(Choice, ChoiceAdmin)

# django-admin startproject vote   // 파일에 들어가기
# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver
# python manage.py createsuperuser 
# python manage.py runserver