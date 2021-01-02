from django.contrib import admin

from .models import Choice, Question


# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    # admin.TabularInline is the compact version of admin.StackedInline
    # http://127.0.0.1:8000/admin/polls/question/1/change/
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # http://127.0.0.1:8000/admin/polls/question/1/change/
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    # display individual fields
    # http://127.0.0.1:8000/admin/polls/question/
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # adds a “Filter” sidebar that lets people filter the change list by the pub_date field
    list_filter = ['pub_date']
    # adds a search box at the top of the change list
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
