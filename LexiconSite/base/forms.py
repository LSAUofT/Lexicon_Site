from django import forms


class ContactForm(forms.Form):
    user_name = forms.CharField(label='Name', max_length=100,
                                widget=forms.TextInput(
                                        attrs={'placeholder': 'Enter your name',
                                               'class': 'u-border-1 u-border-grey-30 u-input u-input-rectangle u-white',
                                               'id': 'name-3b9a'}
                                ))
    user_address = forms.EmailField(label='Email', required=True,
                                    widget=forms.EmailInput(
                                        attrs={'placeholder': 'Enter a valid email address',
                                               'class': 'u-border-1 u-border-grey-30 u-input u-input-rectangle u-white',
                                               'id': 'email-3b9a'
                                               }
                                    ))
    user_message = forms.CharField(label='Message',
                                   widget=forms.Textarea(
                                       attrs={'placeholder': 'Enter your message',
                                              'class': 'u-border-1 u-border-grey-30 u-input u-input-rectangle u-white',
                                              'id': 'message-3b9a'}
                                   ))

    # TODO: add option to cc yourself?
