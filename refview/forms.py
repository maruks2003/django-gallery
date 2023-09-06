from django.forms import CheckboxSelectMultiple, ModelForm
from multiupload.fields import MultiFileField, MultiImageField
from .models import ImagePost,Tag

class UploadForm(ModelForm):
    image = MultiFileField(min_num=1, max_file_size=2048*2048*5)

    class Meta():
        model = ImagePost
        fields = "__all__"
        widgets = {
            "tags": CheckboxSelectMultiple(),
        }

    def save(self, commit=True):
        tags = self.cleaned_data["tags"]
        posts = list()
        for i in self.cleaned_data["image"]:
            post = ImagePost.objects.create(image=i)
            post.tags.set(tags)
            
        return posts


class TagForm(ModelForm):
    class Meta():
        model = Tag
        fields = "__all__"
