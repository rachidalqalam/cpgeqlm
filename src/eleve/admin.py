from django.contrib import admin
from .models import Annee, Filiere, Module, Eleve
from .forms import ItemForm



admin.site.register(Annee)
class ModuleInline(admin.TabularInline):
    model = Module
    extra = 5
class CampaignAdmin(admin.ModelAdmin):
    search_fields = ['filiere']
    inlines = [ModuleInline, ]
admin.site.register(Filiere, CampaignAdmin)


class ItemAdmin(admin.ModelAdmin):
    form = ItemForm
admin.site.register(Eleve, ItemAdmin)