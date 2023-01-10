from django_seed import Seed
from .models import Address
from services.city.models import City

seeder = Seed.seeder()

seeder.add_entity(Address, 500, {
    'address': lambda x: seeder.faker.street_address(),
    'zipcode': lambda x: seeder.faker.postcode(),
    'city': lambda x: City.objects.all().order_by('?').first(),
    'is_active': True,
    'deleted_at': None,
})

seeder.execute()
