import os
import sys
from django.core.management import execute_from_command_line
from tarot_egipcio_gold.settings import PORT

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tarot_egipcio_gold.settings')
    try:
        execute_from_command_line([sys.argv[0], 'runserver', f'127.0.0.1:{PORT}'])
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
