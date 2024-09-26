from django.contrib import admin
from .models import Issue, Vote

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'creator', 'is_open']
    list_filter = ['is_open']

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['user', 'issue', 'vote_value']
