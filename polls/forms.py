from django import forms

# Create your forms here
class PollForm(forms.Form):
    title = forms.CharField(max_length=100, label='หัวข้อ')
    start_date = forms.DateField(required=False, label='วันเริ่มเปิดโหวต')
    end_date = forms.DateField(required=False, label='วันสิ้นสุดการโหวต')

    title.widget.attrs.update({'class': 'form-control'})
    start_date.widget.attrs.update({'class': 'form-control'})
    end_date.widget.attrs.update({'class': 'form-control'})

class PollSearchForm(forms.Form):
    title = forms.CharField(max_length=100, required=False, label='ค้นหาหัวข้อ')
    start_date = forms.DateField(required=False, label='วันเริ่ม')
    end_date = forms.DateField(required=False, label='วันสิ้นสุด')

    title.widget.attrs.update({'class': 'form-control'})
    start_date.widget.attrs.update({'class': 'form-control'})
    end_date.widget.attrs.update({'class': 'form-control'})