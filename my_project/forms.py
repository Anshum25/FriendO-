from django import forms
from accounts.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio']
    
    def clean_bio(self):
        return self.cleaned_data.get('bio', '')  # ✅ Default to empty string

