# chantest
app to test django channels

How to reproduce:
launch project with python manage.py runserver, open index page and console

in console type:
app.socketsend({'x': 'y'})

Then, launch in parallel from console:
python manage.py shell
> group_send('location_update', {'msg': 'connected'})

and nothing happens in browser
