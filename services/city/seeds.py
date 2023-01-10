from django_seed import Seed
from .models import City
from services.states.models import State

seeder = Seed.seeder()

seeder.add_entity(City, 500, {
    'city_name': lambda x: seeder.faker.city(),
    'state': lambda x: State.objects.all().order_by('?').first(),
    'is_active': True,
    'deleted_at': None,
})

seeder.execute()
