from datetime import datetime

from django import forms


def validate_past_date(value):
    if value < datetime.now().date():
        raise forms.ValidationError(
                'วันที่เลือกต้องเป็นวันหลังวันปัจจุบัน'
            )


# Create your forms here
class PollForm(forms.Form):
    title = forms.CharField(max_length=100, label='หัวข้อ')
    start_date = forms.DateField(required=False, label='วันเริ่มเปิดโหวต', validators=[validate_past_date])
    end_date = forms.DateField(required=False, label='วันสิ้นสุดการโหวต', validators=[validate_past_date])

    title.widget.attrs.update({'class': 'form-control'})
    start_date.widget.attrs.update({'class': 'form-control'})
    end_date.widget.attrs.update({'class': 'form-control'})

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