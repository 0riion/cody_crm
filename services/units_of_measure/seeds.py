from django_seed import Seed
from .models import UnitsOfMeasure

seeder = Seed.seeder()

seeder.add_entity(UnitsOfMeasure, 500, {
    'unit_name': lambda x: seeder.faker.word(),
    'case_of_use': lambda x: seeder.faker.sentence(),
    'deleted_at': None,
})

seeder.execute()
