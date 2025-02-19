from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from .helpers import generate_slug  # Assuming this function is defined in helpers.py


# ------------------------------------------------------------------------------
# 1️⃣ ViewsModel: Track unique visitor views
# ------------------------------------------------------------------------------

class ViewsModel(models.Model):
    # Changed IntegerField to CharField to store IP addresses
    total_visits = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.total_visits  # Now returns IP address string


# ------------------------------------------------------------------------------
# 2️⃣ Profile: Extended user profile model
# ------------------------------------------------------------------------------

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    # Renamed field to follow Python naming conventions (snake_case)
    profile_picture = models.ImageField(
        null=True, blank=True, upload_to='img/blog-assets/profile-pictures/'
    )
    website_url = models.CharField(max_length=255, null=True, blank=True)
    github_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)


# ------------------------------------------------------------------------------
# 3️⃣ Blog: Blog post model with improvements
# ------------------------------------------------------------------------------

class Blog(models.Model):
    title = models.CharField(max_length=1000)
    gist = models.CharField(max_length=1000)
    content = FroalaField()
    slug = models.SlugField(max_length=1000, null=True, blank=True, unique=True)
    image = models.ImageField(null=True, blank=True, upload_to='blogs')
    # Ensuring each blog is associated with a user
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Approval system fields
    is_approved = models.BooleanField(default=False)
    is_ready_for_review = models.BooleanField(default=False)
    # It's more robust to use a DateTimeField for approved_at
    approved_at = models.DateTimeField(null=True, blank=True)
    approved_by = models.CharField(max_length=255, null=True, blank=True)

    # Use a ManyToMany field to track which visitor (or IP) has viewed this blog
    views = models.ManyToManyField(ViewsModel, related_name="post_views", blank=True)
    # Uncomment and update the likes field to allow a like system, e.g., using the User model
    likes = models.ManyToManyField(User, related_name="blog_likes", blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Generate a slug only if it doesn't exist already
        if not self.slug:
            self.slug = generate_slug(self.title)
        super(Blog, self).save(*args, **kwargs)

    def total_views(self):
        return self.views.count()

    def total_likes(self):
        return self.likes.count()


# ------------------------------------------------------------------------------
# 4️⃣ BlogComment: Comments on blogs with optional nesting
# ------------------------------------------------------------------------------

class BlogComment(models.Model):
    # Django automatically adds an "id" primary key, so explicit serial is optional.
    # If you prefer to use your own, you can keep this field.
    serial = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    # Allow null for top-level comments; use related_name for reverse lookups.
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Display the user's first name and a snippet of the comment
        return f"{self.user.first_name}: {self.comment[:20]}"

    def get_replies(self):
        # Helper method to fetch nested replies
        return self.replies.all()


# ------------------------------------------------------------------------------
# 5️⃣ Contact: Contact form submissions
# ------------------------------------------------------------------------------

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    desc = models.TextField()
    contacted_on = models.DateTimeField(auto_now_add=True)
    is_viewed = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# ------------------------------------------------------------------------------
# 6️⃣ Subscription: Newsletter subscriptions
# ------------------------------------------------------------------------------

class Subscription(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email