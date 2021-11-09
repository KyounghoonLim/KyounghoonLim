from django import forms
from django.forms import widgets
from django.forms.fields import ChoiceField
from .models import Board

class BoardForm(forms.ModelForm):
    head_form = [
        ('', '말머리를 선택해주세요'),
        ('1', '자유게시판'),
        ('2', '강의 다시보기'),
    ]

    header = forms.ChoiceField(
        required=True,
        label='말머리',
        choices=head_form,
        widget=forms.Select(
        )
    )

    title = forms.CharField(
        required=True,
        label='제목',
        widget=forms.TextInput(
            attrs={
                'max_length': 100,
            }
        )
    )
    
    content = forms.CharField(
        required=True,
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': '',
            }
        )
    )

    image = forms.ImageField(
        required=False,
        label='파일첨부',
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        )
    )

    class Meta:
        model = Board
        fields = '__all__'
        exclude = ['cnt', 'like']