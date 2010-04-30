from django import forms
from django.contrib import admin
from fatpages.models import Fatpage
from django.utils.translation import ugettext_lazy as _


class FatpageForm(forms.ModelForm):
    url = forms.RegexField(label=_("URL"), max_length=100, regex=r'^[-\w/]+$',
        help_text = _("Example: '/about/contact/'. Make sure to have leading"
                      " and trailing slashes."),
        error_message = _("This value must contain only letters, numbers,"
                          " underscores, dashes or slashes."))

    class Meta:
        model = Fatpage


class FatpageAdmin(admin.ModelAdmin):
    form = FatpageForm
    fieldsets = (
        (None, {'fields': ('url', 'title', 'headmatter', 'content')}),
        (_('Advanced options'), {'classes': ('collapse',), 'fields': ('enable_comments', 'registration_required', 'template_name')}),
    )
    list_display = ('url', 'title')
    list_filter = ('sites', 'enable_comments', 'registration_required')
    search_fields = ('url', 'title')

admin.site.register(Fatpage, FatpageAdmin)
