from django import forms

class JobSearchForm(forms.Form):
    job_title = forms.CharField(label='Job Title', max_length=100, required=True)
    job_location = forms.CharField(label='Location', max_length=100, required=True)


class NewsletterForm(forms.Form):
    newsletter_name = forms.EmailField(label='Your Email')