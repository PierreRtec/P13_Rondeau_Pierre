import os


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    port = int(os.environ.get("PORT", 8080))
    execute_from_command_line(["manage.py", "runserver", f"0.0.0.0:{port}"])


if __name__ == "__main__":
    main()
