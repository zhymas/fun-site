from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    author_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    main_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
