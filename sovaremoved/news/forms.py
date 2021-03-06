from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
	class Meta:
		model = Articles
		fields = ['title', 'anons', 'full_text', 'date']


		widgets = {
			'title': TextInput(attrs={
					'class': 'form-control',
					'placeholder': 'article title'
				}),
			'anons': TextInput(attrs={
					'class': 'form-control',
					'placeholder': 'article anons'
				}),
			'date': DateTimeInput(attrs={
					'class': 'form-control',
					'placeholder': 'publication date'
				}),
			'full_text': Textarea(attrs={
					'class': 'form-control',
					'placeholder': 'article text'
				})
		}