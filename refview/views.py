from django.db.models.query_utils import Q
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, View
from .models import ImagePost, Tag
from .forms import UploadForm, TagForm

class Index(ListView):
    model = ImagePost
    template_name = "refview/index.html"

class ImageDetailView(DetailView):
    model = ImagePost
    template_name = "refview/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = Q(imagepost=self.object)
        context["tags"] = Tag.objects.filter(query) 
        context["suggestions"] = Tag.objects.filter(~query)
        return context

    def post(self, request, *args, **kwargs):
        imagepost = self.get_object()
        if ("delete" in request.POST):
            delete_pk = int(request.POST["delete"])
            post = ImagePost.objects.get(id=imagepost.id)
            post.tags.through.objects.filter(imagepost_id=imagepost.id, tag_id=delete_pk).first().delete()

        return HttpResponseRedirect(reverse("detail", args=[imagepost.pk]))


class RandomImageView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        random = ImagePost.objects.order_by("?").first()
        if random != None:
            url = reverse("detail",args=[random.pk])
        else:
            url = reverse("index")
        return url


class UploadView(View):
    template_name="refview/upload.html"
    success_url="/upload/"
    form_classes = {
        "post_form": UploadForm,
        "tag_form": TagForm,
    }

    def get(self, request, *args, **kwargs):
        print(request)
        return render(
            request,
            self.template_name,
            {"post_form": self.form_classes["post_form"],
             "tag_form": self.form_classes["tag_form"],
             }
        )

    def post(self, request, *args, **kwargs):
        if "image" in request.POST:
            post_form = UploadForm(request.POST, request.FILES)
            tag_form = TagForm()

            if post_form.is_valid():
                post_form.save()
                return HttpResponseRedirect(reverse("upload"))
        elif "tag" in request.POST:
            tag_form = TagForm(request.POST)
            post_form = UploadForm()

            if tag_form.is_valid():
                tag_form.save()
                return HttpResponseRedirect(reverse("upload"))
        else:
            post_form = UploadForm()
            tag_form = TagForm()

