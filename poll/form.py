from django.forms import ModelForm, DateTimeInput
from .models import Poll

class PollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'expires_at'] 
        widgets = {
            'expires_at': DateTimeInput(attrs={
                'type': 'datetime-local',
            }),
        }

    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control form-control-lg',
                'placeholder': field.label
            })
        