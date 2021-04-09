from django.db import models


# ポストのモデルを作成
class Post(models.Model):

    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + " - " + self.title


# タスクのモデルを作成
class Task(models.Model):

    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + " - " + self.title
