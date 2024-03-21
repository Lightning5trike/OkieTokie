from flask_wtf import Form
from wtforms import StringField, PasswordField, IntegerField, TextAreaField,RadioField,SubmitField, SelectField, SelectMultipleField, DateField
from wtforms.validators import ValidationError, DataRequired, Length, Email
import sqlite3



class SignUpForm(Form):
    email = StringField(label="Enter email: ", validators=[DataRequired()])
    customer_password = PasswordField(label="Enter password: ", validators=[DataRequired(), Length(min = 8)])
    submit = SubmitField("submit")


CAKE_EXTRAS = [('Rosettes(all)   ( £20.00)'), ('rosettes(top)'), ('Swirls     ( £5.00)'), ('Sprinkles   ( £2.00)'), ('Toppers   ( £2.00)'), ('Jam       ( £3.00)'), ('Drip     ( £5.00)'), ('Flowers   ( £15.00)')]
class cake_form(Form):
    users_email = StringField(label="Email: ", validators=[DataRequired()])
    extras = SelectMultipleField('Extras: ', choices=CAKE_EXTRAS)
    cake_size = RadioField('Size: ', validators=[DataRequired()], choices=[('4 inch'),('5 inch'),('6 inch'),('7 inch'),('8 inch')])
    collection_date = DateField(label="Collection date: ", validators=[DataRequired()])
    layers = RadioField('Layers : ', validators=[DataRequired()], choices=[('3'),('4'),('5')])
    submit = SubmitField("submit ")
    quantity = StringField(label="Quantity: ", validators=[DataRequired()])
    productName = StringField(label="Which products: ", validators=[DataRequired()])
    extra_info = TextAreaField(label="Extra information: ", validators=[DataRequired()])
    submit = SubmitField("Submit")

class creation_form(Form):
    productName =  StringField(label="Product name:  ", validators=[DataRequired()])
    product_section = StringField(label="Product section:  ", validators=[DataRequired()])
    product_image = StringField(label="Product url:  ", validators=[DataRequired()])
    submit = SubmitField("submit")

