from django_seed import Seed
from .models import State

seeder = Seed.seeder()

seeder.add_entity(State, 500, {
    'state_name': lambda x: seeder.faker.state(),
    'is_active': True,
    'deleted_at': None,
})

seeder.execute()
