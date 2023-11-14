from django.contrib.auth.models import User
from blog.models import Post

user = User.objects.all().first()