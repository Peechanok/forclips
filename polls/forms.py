from datetime import datetime

from django import forms

from .models import Poll, Question, Choice


def validate_past_date(value):
    if value < datetime.now().date():
        raise forms.ValidationError(
                'วันที่เลือกต้องเป็นวันหลังวันปัจจุบัน'
            )


# Create your forms here
class PollModelForm(forms.ModelForm):
    start_date = forms.DateField(
        validators=[validate_past_date], 
        widget=forms.DateInput(attrs={ 'class' : 'form-control' })
    )
    end_date = forms.DateField(
        validators=[validate_past_date], 
        widget=forms.DateInput(attrs={ 'class' : 'form-control' })
    )

    class Meta:
        model = Poll
        fields = ('title', 'start_date', 'end_date')
        widgets = {
            'title': forms.TextInput(attrs={ 'class' : 'form-control' })
        }

    # def clean_start_date(self):
    #     data = self.cleaned_data.get('start_date')
        
    #     if data < datetime.now().date():
    #         raise forms.ValidationError(
    #             'วันเริ่มต้นต้องเป็นวันหลังวันปัจจุบัน'
    #         )
    #     return data
    
    # def clean_end_date(self):
    #     data = self.cleaned_data.get('end_date')
        
    #     if data < datetime.now().date():
    #         raise forms.ValidationError(
    #             'วันสิ้นสุดต้องเป็นวันหลังวันปัจจุบัน'
    #         )
    #     return data
    
    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        
        if start_date and end_date:
            if start_date > end_date:
                raise forms.ValidationError(
                    'วันสิ้นสุดจะต้องเป็นวันหลังวันเริ่มต้น'
                )


class PollSearchForm(forms.Form):
    title = forms.CharField(max_length=100, required=False, label='ค้นหาหัวข้อ')
    start_date = forms.DateField(required=False, label='วันเริ่ม')
    end_date = forms.DateField(required=False, label='วันสิ้นสุด')

    title.widget.attrs.update({'class': 'form-control'})
    start_date.widget.attrs.update({'class': 'form-control'})
    end_date.widget.attrs.update({'class': 'form-control'})


class QuestionModelForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('text', 'question_type')
        labels = {
            'text': 'คำถาม',
            'question_type':'ประเภทคำถาม'
        }
        widgets = {
            'text': forms.Textarea(attrs={ 'class' : 'form-control' }),
            'question_type': forms.Select(attrs={ 'class' : 'custom-select' })
        }


class ChoiceModelForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    del_flag = forms.BooleanField(required=False, label='ลบตัวเลือก')

    class Meta:
        model = Choice
        fields = ('id', 'text', 'value', 'del_flag')
        labels = {
            'text': 'ข้อตัวเลือก',
            'value':'ค่า'
        }
        widgets = {
            'text': forms.TextInput(attrs={ 'class' : 'form-control' }),
            'value': forms.TextInput(attrs={ 'class' : 'form-control' })
        }