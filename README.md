DartCMS Boilerplate
===================

This repository contains empty DartCMS-based application.
You can clone it, change repository settings in your `.git/config` file and start coding your project.


Features
--------

- Based on Django Framework
- DartCMS (https://github.com/astrikov-d/dartcms) as content-management system
- Bootstrap 3 as CSS framework
- PostgreSQL as database. Why? Because I like it.
- Subdomain based architecture. Your admin app will be on different domain (`admin` by default) that your public application part.


Quickstart
----------

- Edit your hosts file. Add entry for your website: `127.0.0.1 example.dev admin.example.dev`
- Clone repository
- Cd into project root
- Change git repository settings
- Setup database
- Change `conf.def.project_settings` and `conf.prod.project_settings` according to your needs
- Run `virtualenv --no-site-packages --prompt="(your project name)" venv && source venv/bin/activate`
- Run `pip install -r ./requirements/base.txt` to setup all deps.
- Run `python manage.py migrate`
- Create Django's superuser: `python manage.py createsuperuser`
- Run `python manage.py runserver`
- Navigate your browser to `http://admin.example.dev:8000/admin/modules/module/` and setup DartCMS module rights for your superuser


What's next
-----------

- Read DartCMS documentation to write new apps - http://dartcms.readthedocs.io/en/latest/
- If you want to contribute, feel free to fork repo and create pull-request!