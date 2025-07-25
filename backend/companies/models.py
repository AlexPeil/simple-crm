from django.db import models
from django.urls import reverse


class Company(models.Model):
    """
    Model representing a company in the CRM system.
    """
    
    # Basic Information
    name = models.CharField(
        max_length=200,
        verbose_name="Firmenname",
        help_text="Name des Unternehmens"
    )
    
    # Contact Information
    website = models.URLField(
        blank=True,
        null=True,
        verbose_name="Website",
        help_text="Website URL des Unternehmens"
    )
    
    email = models.EmailField(
        blank=True,
        null=True,
        verbose_name="E-Mail",
        help_text="Hauptkontakt E-Mail"
    )
    
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="Telefon",
        help_text="Haupttelefonnummer"
    )
    
    # Address Information
    street_address = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Straße",
        help_text="Straße und Hausnummer"
    )
    
    city = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Stadt"
    )
    
    postal_code = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        verbose_name="PLZ"
    )
    
    country = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Land",
        default="Deutschland"
    )
    
    # Business Information
    industry = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Branche",
        help_text="Branche/Industriezweig"
    )
    
    company_size = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Unternehmensgröße",
        choices=[
            ('1-10', '1-10 Mitarbeiter'),
            ('11-50', '11-50 Mitarbeiter'),
            ('51-200', '51-200 Mitarbeiter'),
            ('201-1000', '201-1000 Mitarbeiter'),
            ('1000+', '1000+ Mitarbeiter'),
        ]
    )
    
    # Additional Information
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Beschreibung",
        help_text="Zusätzliche Informationen über das Unternehmen"
    )
    
    # Metadata
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Erstellt am"
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Aktualisiert am"
    )
    
    is_active = models.BooleanField(
        default=True,
        verbose_name="Aktiv",
        help_text="Ist das Unternehmen aktiv im System?"
    )

    class Meta:
        verbose_name = "Unternehmen"
        verbose_name_plural = "Unternehmen"
        ordering = ['name']
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('companies:detail', kwargs={'pk': self.pk})
    
    @property
    def full_address(self):
        """Returns the complete address as a formatted string."""
        address_parts = []
        if self.street_address:
            address_parts.append(self.street_address)
        if self.postal_code and self.city:
            address_parts.append(f"{self.postal_code} {self.city}")
        elif self.city:
            address_parts.append(self.city)
        if self.country:
            address_parts.append(self.country)
        return ", ".join(address_parts) if address_parts else ""
