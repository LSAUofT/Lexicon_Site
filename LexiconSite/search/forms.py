from django import forms


class SearchForm(forms.Form):
    search_query = \
        forms.CharField(label='Search', max_length=150, required=True, widget=forms.TextInput(
            attrs={'placeholder': 'Enter the word you would like to learn about',
                   'class': 'u-border-4 u-border-white u-input u-input-rectangle u-radius-50 u-white',
                   'id': 'email-2555',
                   'name': 'Search'}
        ))
