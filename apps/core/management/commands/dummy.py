from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from django_extensions.management.shells import import_objects

from test.factories import UserFactory

User = get_user_model()


class Command(BaseCommand):
    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            "-u",
            type=str,
            help="Add number of users",
        )

    def handle(self, *args, **kwargs):
        if not kwargs.get("u"):
            users_cnt = 10
        else:
            users_cnt = int(kwargs.get("u"))

        self.stdout.write("Start loading dummy")

        # populates globals() with django models, so no need to worry about importing them
        # https://stackoverflow.com/questions/59267620/how-to-import-all-django-models-and-more-in-a-script
        options = {"quiet_load": True}
        style = BaseCommand().style

        imported_objects = import_objects(options, style)
        globals().update(imported_objects)

        # Make Dummy users(default 10)
        UserFactory.create_batch(size=users_cnt)

        self.stdout.write("Finish load dummy")
