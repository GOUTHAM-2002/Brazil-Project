from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.core.cache import cache
from .models import Restaurant, TargetAudience

# Unregister default models
admin.site.unregister(User)
admin.site.unregister(Group)

# Customize admin site
admin.site.site_header = 'Restaurant Dashboard'
admin.site.site_title = 'Restaurant Management'
admin.site.index_title = 'Welcome to Your Dashboard'

# Customize Restaurant model admin
@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    # Simplified list display with most important fields
    list_display = ('name', 'cuisine', 'location', 'atmosphere')
    
    # Add search functionality
    search_fields = ('name', 'location')
    
    # Simplified filters
    list_filter = ('atmosphere', 'delivery_options')
    
    # Group fields logically
    fieldsets = (
        ('📍 Basic Information', {
            'fields': ('name', 'tagline', 'cuisine'),
            'classes': ('wide',)
        }),
        ('📍 Location & Atmosphere', {
            'fields': ('location', 'atmosphere'),
            'classes': ('wide',)
        }),
        ('⏰ Operations', {
            'fields': ('hours_of_operation', 'delivery_options'),
            'classes': ('wide',)
        }),
    )
    
    # Make timestamps read-only
    readonly_fields = ('created_at', 'updated_at')
    
    # Add help text
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['name'].help_text = 'Enter the full name of your restaurant'
        form.base_fields['hours_of_operation'].help_text = 'Example: Mon-Fri: 9 AM - 10 PM'
        return form

# Customize TargetAudience model admin
@admin.register(TargetAudience)
class TargetAudienceAdmin(admin.ModelAdmin):
    # Simplified list display
    list_display = ('restaurant', 'age_group', 'income_level')
    
    # Add search
    search_fields = ('restaurant__name',)
    
    # Simple filters
    list_filter = ('age_group', 'income_level')
    
    # Group fields logically
    fieldsets = (
        ('🏪 Restaurant', {
            'fields': ('restaurant',),
            'classes': ('wide',)
        }),
        ('👥 Audience Details', {
            'fields': ('age_group', 'income_level'),
            'classes': ('wide',)
        }),
        ('🎯 Preferences', {
            'fields': ('preferences', 'engagement_platforms'),
            'classes': ('wide',)
        }),
    )

# Add context to admin index
def get_admin_stats(request):
    return {
        'restaurants_count': Restaurant.objects.count(),
        'audience_count': TargetAudience.objects.count(),
    }

admin.site.index_context = get_admin_stats

