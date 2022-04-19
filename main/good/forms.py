from django.forms import ModelForm
from .models import Portfolio

class PortfolioForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = '__all__'
