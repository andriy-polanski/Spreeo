from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.views import generic
from django.views.generic.list import ListView
from django.views.generic import DeleteView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from dashboard.forms import ProductForm, ProductImageFormSet, SkuRecordFormSet
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from reflex.models import Product, Merchant, VariantType, ProductVariantType
from django.contrib.auth import login, logout

class DashboardAuthenticationForm(AuthenticationForm):

    def __init__(self, request=None, *args, **kwargs):
        super(DashboardAuthenticationForm, self).__init__(request, *args, **kwargs)
        self.fields['username'].widget.attrs={'class':'form-control', 'placeholder': 'Username'}
        self.fields['password'].widget.attrs={'class':'form-control', 'placeholder': 'Password'}
 
    def clean(self):
        cleaned_data = super(DashboardAuthenticationForm, self).clean()
        user = self.get_user()
        if user and not hasattr(user, "merchant_user"):
            raise ValidationError(
                'This is not a merchant dashboard account', 
                code='non-merchant-account') 
        return cleaned_data


def dashboard_login_page(request):
    d = {} 
    if request.method == "GET":
        d["form"] = DashboardAuthenticationForm()
    elif request.method == "POST":
        d["form"] = form = DashboardAuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return HttpResponseRedirect(reverse("dashboard:index"))
    return render(request, "dashboard/login.html", d)

def dashboard_logout(request):
    logout(request)
    messages.info(request, "You have been logged out")
    return HttpResponseRedirect(reverse("dashboard:dashboard_login"))

class IndexView(generic.TemplateView):
    template_name = "dashboard/home/index.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(IndexView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(IndexView, self).get_context_data(**kwargs)
        ctx['tasks'] = tasks = []

        merchant = self.request.user.merchant_user.merchant

        # Has the merchant profile been filled?
        done = False 
        if (hasattr(merchant, 'merchant_profile') and 
                merchant.merchant_profile.company_name and 
                merchant.merchant_profile.slug):
            done = True
        tasks.append({
            "title": "Set your company name and slug",
            "url": reverse("dashboard:edit_profile"),
            "done": done
        })

        # Any contacts?
        done = False
        if merchant.contacts.all().count() != 0:
            done = True
        tasks.append({
            "title": "Add contact information for you company",
            "url": reverse("dashboard:edit_profile") + "#new_contact",
            "done": done
        })

        # Any store level categories
        done = False
        if merchant.store_level_categories.all().count() != 0:
            done = True
        tasks.append({
            "title": "Add store level categories",
            "url": reverse("dashboard:new_store_category"),
            "done": done
        })

        # Any products?
        done = False
        if merchant.products.all().count() != 0:
            done = True
        tasks.append({
            "title": "Add products and product photos",
            "url": reverse("dashboard:product_new"),
            "done": done
        })

        # Shipping options?
        done = False
        if merchant.shipping_options.all().count() != 0:
            done = True
        tasks.append({
            "title": "Add shipping options",
            "url": reverse("dashboard:new_shipping_option"),
            "done": done
        })
        
        # Payment gateway?
        done = False
        tasks.append({
            "title": "Configure payment gateway",
            "url": None,
            "done": done
        })
        return ctx

class ProductListView(ListView):
    template_name = "dashboard/product/list.html"
    model = Product

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ProductListView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        qs = super(ProductListView, self).get_queryset()
        qs = qs.filter(merchant=self.request.user.merchant_user.merchant)
        return qs


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('dashboard:product_list')
    template_name = "dashboard/product/delete.html"
    context_object_name = 'product'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ProductDeleteView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        qs = super(ProductDeleteView, self).get_queryset()
        qs = qs.filter(merchant=self.request.user.merchant_user.merchant)
        return qs


class ProductUpdateCreateView(generic.UpdateView):
    template_name = "dashboard/product/edit.html"
    model = Product
    context_object_name = 'product'
    form_class = ProductForm
    image_formset = ProductImageFormSet
    skurecord_formset = SkuRecordFormSet

    def __init__(self, *args, **kwargs):
        super(ProductUpdateCreateView, self).__init__(*args, **kwargs)
        self.formsets = {
            'image_formset' :  self.image_formset,
            'skurecord_formset' : self.skurecord_formset
        }

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        resp = super(ProductUpdateCreateView, self).dispatch(
            request, *args, **kwargs)
        return self.check_objects_or_redirect() or resp

    def get_queryset(self):
        qs = super(ProductUpdateCreateView, self).get_queryset()
        qs = qs.filter(merchant=self.request.user.merchant_user.merchant)
        return qs

    def check_objects_or_redirect(self):
        """
        Allows checking the objects fetched by get_object and redirect
        if they don't satisfy our needs.
        """

    def get_context_data(self, **kwargs):
        ctx = super(ProductUpdateCreateView, self).get_context_data(**kwargs)
        ctx['title'] = self.get_page_title()
        for ctx_name, formset_class in self.formsets.items():
            if ctx_name not in ctx:
                ctx[ctx_name] = formset_class(self.request.user,
                                              instance=self.object)

        form = ctx['form']
        if form.is_bound:
            ctx['variant_types'] = self.get_extra_sku_attributes_from_request()
        else:
            ctx['variant_types'] = form.instance.product_variant_types.all().values_list('variant_type__name', flat=True)
        print "Variant types:", ctx['variant_types']
        return ctx

    def get_extra_sku_attributes_from_request(self):
        extra_sku_attributes = self.request.POST.get('extra_sku_attributes', '').strip()
        if extra_sku_attributes:
            return extra_sku_attributes.split(",")
        else:
            return []

    def get_object(self, queryset=None):
        """
        This parts allows generic.UpdateView to handle creating products as
        well. The only distinction between an UpdateView and a CreateView
        is that self.object is None. We emulate this behavior.
        """

        self.creating = 'pk' not in self.kwargs
        if self.creating:
            if self.request.user and hasattr(self.request.user, 'merchant_user'):
                self.product_merchant = self.request.user.merchant_user.merchant
            else:
                # Need to redirect to login page. This is just for testing purpose
                self.product_merchant = get_object_or_404(Merchant, pk=1)

            if self.request.user.is_anonymous:
                # Need to redirect to login page. This is just for testing purpose
                self.created_by = get_object_or_404(User, pk=1)
            else:
                self.created_by = self.request.user

            return None  # success
        else:
            product = super(ProductUpdateCreateView, self).get_object(queryset)
            self.product_merchant = product.merchant
            self.created_by = product.created_by
            return product

    def get_form_kwargs(self):
        kwargs = super(ProductUpdateCreateView, self).get_form_kwargs()
        kwargs['merchant'] = self.product_merchant
        kwargs['created_by'] = self.created_by
        return kwargs

    def get_page_title(self):
        if self.creating:
            return _('Create new product')
        else:
            return _('Edit product : %(product_name)s' % {'product_name' : self.object.name})

    def forms_invalid(self, form, formsets):
        # delete the temporary product again
        if self.creating and self.object and self.object.pk is not None:
            self.object.delete()
            self.object = None

        messages.error(self.request,
                       _("Your submitted data was not valid - please "
                         "correct the errors below"))
        ctx = self.get_context_data(form=form, **formsets)
        ctx['any_errors'] = True
        return self.render_to_response(ctx)

    def forms_valid(self, form, formsets):
        """
        Save all changes and display a success url.
        """
        self.object = form.save()

        # Find the ProductVariantTypes to create/delete 
        maintain_attrs = self.get_extra_sku_attributes_from_request()
        for product_variant_type in self.object.product_variant_types.all():
            if not product_variant_type.variant_type.name in maintain_attrs:
                print "Deleting ProductVariantType:", product_variant_type.variant_type.name
                product_variant_type.delete()

        merchant = self.request.user.merchant_user.merchant
        for attr in maintain_attrs:
            if not self.object.product_variant_types.all().filter(
                    variant_type__name=attr).exists():
                print "Creating ProductVariantType:", attr
                try:
                    variant_type = VariantType.objects.get(merchant=merchant, name=attr)
                except VariantType.DoesNotExist:
                    print "Creating variant type:", attr
                    variant_type = VariantType(merchant=merchant, name=attr)
                    variant_type.save()
                product_variant_type = ProductVariantType(product=self.object, variant_type=variant_type)
                product_variant_type.save()
        
        # Save formsets
        for formset in formsets.values():
            formset.save()

        return HttpResponseRedirect(self.get_success_url())

    def process_all_forms(self, form):
        """
        Short-circuits the regular logic to have one place to have our
        logic to check all forms
        """
        # Need to create the product here because the inline forms need it

        if self.creating and form.is_valid():
            self.object = form.save()
            print self.object.pk

        formsets = {}
        for ctx_name, formset_class in self.formsets.items():
            formsets[ctx_name] = formset_class(self.request.user,
                                               self.request.POST,
                                               self.request.FILES,
                                               instance=self.object)

        is_valid = form.is_valid() and all([formset.is_valid()
                                            for formset in formsets.values()])

        cross_form_validation_result = self.clean(form, formsets)
        if is_valid and cross_form_validation_result:
            return self.forms_valid(form, formsets)
        else:
            return self.forms_invalid(form, formsets)

    form_valid = form_invalid = process_all_forms


    def get_success_url(self):
        """
        Renders a success message and redirects depending on the button:
        """
        messages.success(self.request, _('Product saved successfully.'))
        url = reverse('dashboard:product_edit', kwargs={"pk": self.object.id})
        return self.get_url_with_querystring(url)


    def get_url_with_querystring(self, url):
        url_parts = [url]
        if self.request.GET.urlencode():
            url_parts += [self.request.GET.urlencode()]
        return "?".join(url_parts)

    def clean(self, form, formsets):
        """
        Perform any cross-form/formset validation. If there are errors, attach
        errors to a form or a form field so that they are displayed to the user
        and return False. If everything is valid, return True. This method will
        be called regardless of whether the individual forms are valid.
        """
        return True