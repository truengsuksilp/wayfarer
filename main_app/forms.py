from django.forms import CharField, EmailField, DateTimeField, SlugField, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    # UserModel
    # password1 = CharField(
    #     min_length=8,
    #     widget=PasswordInput,
    #     help_text='At Least 8 characters.  Cannot be just numbers!'
    # )
    email = EmailField(
        min_length=2,
        max_length=254, 
        help_text='Required. Inform a valid email address.')
    
    # Profile Model
    current_city = CharField()
    profile_picture = CharField()
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )