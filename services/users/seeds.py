from django_seed import Seed
from .models import User

seeder = Seed.seeder()

seeder.add_entity(User, 500, {
    'username': lambda x: seeder.faker.user_name(),
    'email': lambda x: seeder.faker.email(),
    'avatar': lambda x: seeder.faker.image_url(),
    'password': 'user1234',
    'is_staff': False,
    'is_superuser': False,
    'is_active': True,
    'deleted_at': None,
})

seeder.execute()
