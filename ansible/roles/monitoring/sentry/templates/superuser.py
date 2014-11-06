from sentry.utils.runner import configure
configure()

from django.db import DEFAULT_DB_ALIAS as database
from sentry.models import User

try:
	if User.objects.get(username__exact='{{ superuser_sentry.username }}') is None:
		User.objects.db_manager(database).create_superuser('{{ superuser_sentry.username }}', '{{ superuser_sentry.email }}', '{{ superuser_sentry.password }}')
except:
	User.objects.db_manager(database).create_superuser('{{ superuser_sentry.username }}', '{{ superuser_sentry.email }}', '{{ superuser_sentry.password }}')