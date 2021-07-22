from django import forms


class form_data(forms.Form):

    poll_question=forms.CharField(max_length=50)



class poll_id_form(forms.Form):
    poll_id=forms.CharField(max_length=20)


class input_op_form(forms.Form):
    answer=forms.CharField(max_length=40)
