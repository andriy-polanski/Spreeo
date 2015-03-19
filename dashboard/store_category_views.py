from django import forms
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from reflex.models import StoreLevelCategory


class StoreLevelCategoryForm(forms.ModelForm):

    class Meta:
        model = StoreLevelCategory
        fields = ['name', 'path', 'parent']


@login_required
def store_categories(request):
    d = {}
    d["categories"] = request.user.merchant_user.merchant.store_level_categories.all()
    return render(request, "dashboard/store_category/list.html", d)

@login_required
def edit_store_category(request, pk=None):
    d = {}
    merchant = request.user.merchant_user.merchant
    if pk:
        instance = get_object_or_404(StoreLevelCategory, merchant=merchant, id=pk)
    else:
        instance = None

    if request.method == "GET":
        d["form"] = form = StoreLevelCategoryForm(instance=instance)

    elif request.method == "POST":
        d["form"] = form = StoreLevelCategoryForm(request.POST, instance=instance)
        if form.is_valid():
            if form.has_changed():
                instance = form.save(commit=False)
                new = True if not instance.id else False
                instance.merchant = merchant
                instance.save()
                if new:
                    messages.success(request, "'%s' added" % instance.name)
                else:
                    messages.success(request, "'%s' updated" % instance.name)
            else:
                messages.info(request, "'%s' unchanged" % instance.name)
            return HttpResponseRedirect(reverse("dashboard:store_categories"))

    return render(request, "dashboard/store_category/edit.html", d)

@login_required
def delete_store_category(request, pk=None):
    d = {}
    merchant = request.user.merchant_user.merchant
    if pk:
        instance = get_object_or_404(StoreLevelCategory, merchant=merchant, id=pk)
    else:
        instance = None
    d["instance"] = instance

    if request.method == "GET":
        return render(request, "dashboard/store_category/delete.html", d)
    elif request.method == "POST":
        name = instance.name
        instance.delete()
        messages.success(request, "'%s' deleted" % name)
        return HttpResponseRedirect(reverse("dashboard:store_categories"))
