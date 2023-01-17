from django import forms


class ContactForm(forms.Form):
    # todo: modify widgets such that they have all the attributes from original .html file
    user_name = forms.CharField(label='Your name', max_length=100,
                                widget=forms.TextInput(
                                        attrs={'placeholder': 'Enter Your Name',
                                               'class': 'u-border-1 u-border-grey-30 u-input u-input-rectangle u-white'}
                                    )
                                )
    user_address = forms.EmailField(label='Your email', required=True)
    user_message = forms.CharField(label='Your message', widget=forms.Textarea)

    # TODO: add option to cc yourself?
