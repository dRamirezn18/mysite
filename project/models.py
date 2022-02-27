from django.db import models
import uuid

class Project(models.Model):
  id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
  title = models.CharField(max_length=150)
  description = models.TextField(blank=True, null=True)
  demo_link = models.CharField(max_length=2500, blank=True, null=True)
  source_link = models.CharField(max_length=2500, blank=True, null=True)
  tags = models.ManyToManyField("Tag", blank=True)
  vote_total = models.IntegerField(default=0)
  vote_ratio = models.IntegerField(default=0)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title

class Review(models.Model):
  VOTE_TYPE = (
    ("up", "up"),
    ("down", "down"),
  )

  id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
  project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
  body = models.TextField(blank=True, null=True)
  value = models.CharField(max_length=50, choices=VOTE_TYPE)
  update = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.value

class Tag(models.Model):
  name = models.CharField(max_length=200, blank=True)

  def __str__(self):
    return self.name