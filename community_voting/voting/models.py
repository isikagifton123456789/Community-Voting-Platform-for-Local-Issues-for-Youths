from django.contrib.auth.models import User
from django.db import models

class Issue(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    is_open = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    vote_value = models.BooleanField()  # True for Yes, False for No

    class Meta:
        unique_together = ('user', 'issue')  # Users can vote only once per issue
