from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        counter = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                counter += 1
        if counter != 1:
            raise ValidationError('Тут всегда ошибка!')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 1
    formset = ScopeInlineFormset



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_view = ['name']