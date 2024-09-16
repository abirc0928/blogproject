from django.db import models
from author.models import Author
from categories.models import Category
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def get_truncated_content(self, num_words=15):
        words = self.content.split()  # Split content into words
        if len(words) > num_words:
            return ' '.join(words[:num_words]) + '...'  # Truncate and add '...' if needed
        return self.content  
    
    def __str__(self):
        return self.title