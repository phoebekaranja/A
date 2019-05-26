from django import forms
from .models import Project,Profile

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['profile','usability','design','content']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('photo','profile','bio','contact')
        
class VoteForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['link','description','profile','image','title']
# class Comment(forms.modelForm):
#     class Meta:
#         model = Comment
#         exclude = ['comment']
