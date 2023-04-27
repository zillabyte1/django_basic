

# Create a django application with a single file. No admin site or database needed
https://blog.ldtalentwork.com/2019/11/19/how-to-start-a-django-project-without-the-default-startproject-command-the-single-file-approach/

# css template
https://wrapbootstrap.com/theme/smarty-website-admin-rtl-WB02DSN1B


# install django
pip install django

# Run application
python single.py runserver

# generate requirements file
python -m pip install -r requirements.txt

# create super user for admin UI
python manage.py createsuperuser
ENTER USER NAME  (admin)
ENTER EMAIL      (zillabyte@gmail.com)
ENTER PASSWORD   (football)