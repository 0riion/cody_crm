from django_seed import Seed
from .models import Category

seeder = Seed.seeder()

seeder.add_entity(Category, 1000, {
    'description': lambda x: seeder.faker.text(),
    'is_active': True,
    'deleted_at': None,
})

seeder.execute()

# how to run the seed?
# python manage.py shell
# from services.category.seeds import seeder
# seeder.execute()
