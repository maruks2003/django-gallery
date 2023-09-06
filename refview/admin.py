from django import forms
from django.contrib import admin
from django.forms.widgets import CheckboxSelectMultiple
from .models import ImagePost, Tag
from django.utils.html import format_html

admin.site.register(Tag)

class ImagePostAdminForm(forms.ModelForm):
    class Meta:
        model = ImagePost
        fields = "__all__"
        widgets = {
            "tags": CheckboxSelectMultiple,
        }

@admin.register(ImagePost)
class ImagePostAdmin(admin.ModelAdmin):
    list_display = ("preview_image", "get_tags")
    list_filter = ("tags",)
    form = ImagePostAdminForm

    # Create image preview and scale it accordingly
    @admin.display(description="Image Preview")
    def preview_image(self, obj):
        ImagePost.objects.filter(image=obj)

        try:
            html = format_html(
                "<img style=\"{}\" src=\"{}\" width=\"{}px\" height=\"{}px\">",
                "max-width:33%; height: auto;",
                obj.image.url,
                obj.image.width,
                obj.image.height,
            )
            return html
        except ValueError:
            return obj

    # List individual tags separated by commas
    # TODO: make it pretty
    @admin.display(description="Tags")
    def get_tags(self, obj):
        return ", ".join([str(t) for t in obj.tags.all()])
    pass


