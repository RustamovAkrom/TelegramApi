import os
import django
from django.utils.translation import gettext as _
from django.utils.translation import activate

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

activate("ru")
# Now you can use Django's translation functions
print(_("Hello World"))