from django.forms import Form, CharField, EmailField, DateTimeField, SlugField, PasswordInput
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

class SignUpForm(UserCreationForm):
    email = EmailField(
        min_length=2,
        max_length=254, 
        help_text='Required. Inform a valid email address.')
    
    # Profile Model
    current_city = CharField()
    profile_picture = CharField(initial="https://media1.thehungryjpeg.com/thumbs2/ori_3686943_09tpyqe6r67ba765aheypmgvqo0vltfraf4ru77u_plane-icon.jpg")
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


class CreatePostForm(Form):
    title = CharField(
        label="Post Title",
        max_length = 200,
        help_text='Fewer than 200 characters'
    )
    content = CharField(
        label="Post Content",
        max_length = 10000,
        help_text='Fewer than 10k characters'
    )

    # Validation: Clean a specific field
    # SRC: https://docs.djangoproject.com/en/3.2/ref/forms/validation/
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 100:
            raise ValidationError("title is too long")
        # return HttpResponse("Title is too long")

    # Validation: Clean multiple fields
    # SRC: https://docs.djangoproject.com/en/3.2/ref/forms/validation/
    # def clean(self):
    #     cleaned_data = super().clean()
    #     title = cleaned_data.get("title")
    #     content = cleaned_data.get("content")

    #     if len(title) > 100:
    #         raise ValidationError("title is too long")
    #     return title

    # Validation: Print Error on template
    # SRC: https://forum.djangoproject.com/t/forms-validationerror-doesnt-print-any-error-message-to-the-template/1783
    # def clean(self):
    #     cleaned_data = super().clean()
    #     title = cleaned_data.get("title")
    #     if len(title) > 100:
    #         self.add_error('title', "title is too long")
