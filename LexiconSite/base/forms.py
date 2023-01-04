from django import forms


# note: going to Contact page causes "OSError: Bad URL"
class ContactForm(forms.Form):
    user_name = forms.CharField(label='Your name', max_length=100)
    user_address = forms.EmailField(label='Your email', required=True)
    user_message = forms.CharField(label='Your message', widget=forms.Textarea)

    # TODO: add option to cc yourself?
