"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""

import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename
from app.models import Properties
from app.forms import NewProperyForm
from datetime import datetime


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/properties/create', methods=['POST', 'GET'])
def property_new():
    form = NewProperyForm()

    if form.validate_on_submit():
        print(form.location.data)
        title = form.title.data
        description = form.description.data
        no_rooms = form.no_rooms.data
        no_bathrooms = form.no_bathrooms.data
        price = form.price.data
        property_type = form.property_type.data
        location = form.location.data


        property_new = Properties(title=title, description=description, no_rooms=no_rooms, no_bathrooms=no_bathrooms, price=price, property_type=property_type, location=location)
        db.session.add(property_new)
        db.session.commit()

        path=os.getcwd() + '\\app\\static\\uploads\\' + str(property_new.id)
        

        if os.path.exists(path)==False:
            os.mkdir(path)

        filename  = secure_filename(form.photo.data.filename)
        form.photo.data.save('app/static/uploads/'+ str(property_new.id) + '/' + filename)
        property_new.photo = '/uploads/'+ str(property_new.id) + '/' + filename
        db.session.commit()
        return redirect(url_for('properties'))

    return render_template('new_property.html', form=form)

@app.route('/properties')
def properties():
    properties = Properties.query.all()
    return render_template('properties.html', properties=properties)

@app.route('/properties/<propertyid>', methods=['POST', 'GET'])
def property_view(propertyid):
    print(propertyid);
    property = Properties.query.get(propertyid)
    return render_template('property.html', property=property)


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

def get_upload_images():
    rootdir = os.getcwd()
    filenames = [];
    for subdir, dirs, files in os.walk(rootdir + '\\uploads'):
        for file in files:
            if file.endswith(('.jpg','.png', '.JPG', '.PNG')):
                print ('/uploads/' + file)
                filenames+=['/uploads/' + file]
    return filenames

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)

@app.template_filter()
def currencyFormat(value):
    value = float(value)
    return "${:,.2f}".format(value)

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
