from django import forms


class ContactForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100, required=False)
    email = forms.EmailField(label='Email', required=False)
    mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea)
    quiero_recibir_respuestas = forms.BooleanField(required=False)

    def clean_mensaje(self):
        mensaje = self.cleaned_data.get('mensaje')
        if "forro" in mensaje:
            raise forms.ValidationError("Minga que vas a postear esto")
        return mensaje
