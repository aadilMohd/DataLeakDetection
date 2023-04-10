from django.db import models 
class LoginDetails(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	designation = models.IntegerField(default=1)
	clientid = models.CharField(max_length=17, default="xyz")
	cipher_text = models.CharField(max_length=25, default="xyz")
	hash_text = models.CharField(max_length=65, default="xyz")

	def __str__(self):
		return self.username
class Comment(models.Model):
    name = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)
    website = models.URLField(max_length=200, null=True, blank=True)
    content = models.TextField()
    # post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)