from django import forms
from .models import Item, Type


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        type = Type.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in type]

        self.fields['type'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'