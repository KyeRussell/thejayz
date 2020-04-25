import factory


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'users.User'

    username = 'user'
    email = 'me@kye.id.au'
    full_name = 'Kye Russell'
