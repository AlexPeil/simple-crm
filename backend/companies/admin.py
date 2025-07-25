from django.contrib import admin
from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """
    Admin interface for Company model.
    """
    
    list_display = [
        'name', 
        'city', 
        'industry', 
        'company_size', 
        'is_active',
        'created_at'
    ]
    
    list_filter = [
        'is_active',
        'industry',
        'company_size',
        'country',
        'created_at'
    ]
    
    search_fields = [
        'name',
        'email',
        'city',
        'industry'
    ]
    
    readonly_fields = [
        'created_at',
        'updated_at'
    ]
    
    fieldsets = (
        ('Grundinformationen', {
            'fields': ('name', 'industry', 'company_size', 'description', 'is_active')
        }),
        ('Kontaktinformationen', {
            'fields': ('email', 'phone', 'website')
        }),
        ('Adresse', {
            'fields': ('street_address', 'city', 'postal_code', 'country')
        }),
        ('Metadaten', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )
    
    # Improved list display
    list_per_page = 25
    list_max_show_all = 100
    
    # Enable actions
    actions = ['make_active', 'make_inactive']
    
    def make_active(self, request, queryset):
        """Mark selected companies as active."""
        updated = queryset.update(is_active=True)
        self.message_user(
            request,
            f'{updated} Unternehmen wurden als aktiv markiert.'
        )
    make_active.short_description = "Ausgewählte Unternehmen als aktiv markieren"
    
    def make_inactive(self, request, queryset):
        """Mark selected companies as inactive."""
        updated = queryset.update(is_active=False)
        self.message_user(
            request,
            f'{updated} Unternehmen wurden als inaktiv markiert.'
        )
    make_inactive.short_description = "Ausgewählte Unternehmen als inaktiv markieren"
