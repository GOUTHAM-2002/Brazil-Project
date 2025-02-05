from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255, unique=True)
    tagline = models.CharField(max_length=255, blank=True, null=True)
    cuisine = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    atmosphere = models.CharField(max_length=255, choices=[
        ('Fine Dining', 'Fine Dining'),
        ('Casual', 'Casual'),
        ('Family-Friendly', 'Family-Friendly'),
        ('Cafe', 'Cafe'),
    ])
    hours_of_operation = models.TextField()  # e.g., "Mon-Fri: 9 AM - 10 PM"
    delivery_options = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class TargetAudience(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='target_audience')
    age_group = models.CharField(max_length=255, choices=[
        ('Teens', 'Teens'),
        ('Young Adults', 'Young Adults'),
        ('Families', 'Families'),
        ('Seniors', 'Seniors'),
    ])
    income_level = models.CharField(max_length=255, choices=[
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ])
    preferences = models.TextField(help_text="Dietary preferences or dining habits.")
    engagement_platforms = models.TextField(help_text="Preferred social media platforms (e.g., Instagram, LinkedIn).")

    def __str__(self):
        return f"{self.restaurant.name} - {self.age_group}"
