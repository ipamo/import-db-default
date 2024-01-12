Import field with Django 5.0 db_default date
============================================

See the [reported issue](https://github.com/django-import-export/django-import-export/issues/1736).

## How to reproduce

Create Python environment:

    python -m venv .venv
    .\.venv\Scripts\activate
    pip install -r requirements.txt

Create and deploy PostgreSql database:

    createdb -U postgres bugs
    python manage.py migrate

Create super user:

    $env:DJANGO_SUPERUSER_PASSWORD = "admin"
    python manage.py createsuperuser --noinput --username admin --email admin@example.org

Run server:

    python manage.py runserver

Go to [http://localhost:8000/admin/import_db_default/item/](http://localhost:8000/admin/import_db_default/item/),
click `Import` and select `sample.csv`.

## Error

**AttributeError: 'DatabaseDefault' object has no attribute 'utcoffset'**

My environment:

- Windows 10 22H2 (build 19045.3930)
- Python 3.11.5
- PostgreSQL 15.4
- Django 5.0.1
- Psycopg 3.1.17
- Django-import-export 3.3.6

Error traceback:

    Traceback (most recent call last):
    File "…\import-db-default\.venv\Lib\site-packages\import_export\resources.py", line 785, in import_row
    diff = self.get_diff_class()(self, original, new)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "…\import-db-default\.venv\Lib\site-packages\import_export\resources.py", line 259, in __init__
    self.left = self._export_resource_fields(resource, instance)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "…\import-db-default\.venv\Lib\site-packages\import_export\resources.py", line 280, in _export_resource_fields
    return [
    ^
    File "…\import-db-default\.venv\Lib\site-packages\import_export\resources.py", line 281, in <listcomp>
    resource.export_field(f, instance) if instance else ""
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "…\import-db-default\.venv\Lib\site-packages\import_export\resources.py", line 1066, in export_field
    return field.export(obj)
    ^^^^^^^^^^^^^^^^^
    File "…\import-db-default\.venv\Lib\site-packages\import_export\fields.py", line 148, in export
    return self.widget.render(value, obj)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "…\import-db-default\.venv\Lib\site-packages\import_export\widgets.py", line 266, in render
    value = timezone.localtime(value)
    ^^^^^^^^^^^^^^^^^^^^^^^^^
    File "…\import-db-default\.venv\Lib\site-packages\django\utils\timezone.py", line 182, in localtime
    if is_naive(value):
    ^^^^^^^^^^^^^^^
    File "…\import-db-default\.venv\Lib\site-packages\django\utils\timezone.py", line 234, in is_naive
    return value.utcoffset() is None
    ^^^^^^^^^^^^^^^
    AttributeError: 'DatabaseDefault' object has no attribute 'utcoffset'
