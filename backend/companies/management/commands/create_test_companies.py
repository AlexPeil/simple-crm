from django.core.management.base import BaseCommand
from companies.models import Company


class Command(BaseCommand):
    help = 'Erstellt Testdaten für Companies'

    def handle(self, *args, **options):
        # Lösche existierende Testdaten
        Company.objects.all().delete()
        
        # Erstelle Testunternehmen
        companies_data = [
            {
                'name': 'TechStart GmbH',
                'website': 'https://techstart.de',
                'email': 'info@techstart.de',
                'phone': '+49 30 12345678',
                'street_address': 'Unter den Linden 1',
                'city': 'Berlin',
                'postal_code': '10117',
                'country': 'Deutschland',
                'industry': 'Software',
                'company_size': '11-50',
                'description': 'Innovative Software-Lösungen für Startups'
            },
            {
                'name': 'München Consulting AG',
                'website': 'https://muenchen-consulting.de',
                'email': 'kontakt@muenchen-consulting.de',
                'phone': '+49 89 987654321',
                'street_address': 'Marienplatz 8',
                'city': 'München',
                'postal_code': '80331',
                'country': 'Deutschland',
                'industry': 'Beratung',
                'company_size': '51-200',
                'description': 'Strategische Unternehmensberatung'
            },
            {
                'name': 'Hamburg Logistik Solutions',
                'website': 'https://hh-logistik.de',
                'email': 'info@hh-logistik.de',
                'phone': '+49 40 555666777',
                'street_address': 'Speicherstadt 15',
                'city': 'Hamburg',
                'postal_code': '20457',
                'country': 'Deutschland',
                'industry': 'Logistik',
                'company_size': '201-1000',
                'description': 'Moderne Logistiklösungen für den Welthandel'
            },
            {
                'name': 'Köln Digital Marketing',
                'website': 'https://koeln-digital.de',
                'email': 'hello@koeln-digital.de',
                'phone': '+49 221 111222333',
                'street_address': 'Domkloster 4',
                'city': 'Köln',
                'postal_code': '50667',
                'country': 'Deutschland',
                'industry': 'Marketing',
                'company_size': '1-10',
                'description': 'Digitale Marketing-Strategien für KMU'
            },
            {
                'name': 'Frankfurt Finance Partners',
                'website': 'https://ffp-finance.de',
                'email': 'partners@ffp-finance.de',
                'phone': '+49 69 444555666',
                'street_address': 'Bankenviertel 20',
                'city': 'Frankfurt am Main',
                'postal_code': '60311',
                'country': 'Deutschland',
                'industry': 'Finanzdienstleistungen',
                'company_size': '1000+',
                'description': 'Internationale Finanzdienstleistungen und Investment'
            }
        ]
        
        created_companies = []
        for company_data in companies_data:
            company = Company.objects.create(**company_data)
            created_companies.append(company)
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Erfolgreich {len(created_companies)} Testunternehmen erstellt:'
            )
        )
        
        for company in created_companies:
            self.stdout.write(f'  ✓ {company.name} ({company.city})')
