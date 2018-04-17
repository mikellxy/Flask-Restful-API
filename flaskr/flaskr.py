import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from yourapplication.simple_page import simple_page
from yourapplication.admin.admin import admin

app = Flask(__name__) # create the application instance :)

# begin of examples
from flask_restfull_api.generics import ListView, RetrieveView
from flask_restfull_api import serializers


# the class used for serialization
class MySerializer(serializers.Serializer):
    k1 = serializers.CharField()
    k2 = serializers.CharField()


# objects of class: 'Foo' are used to represent the instance of db Model
class Foo:
    pass


foo = Foo()
foo1 = Foo()
foo.k1 = 'v1'
foo.k2 = 'v2'
foo1.k1 = 'v1'
foo1.k2 = 'v2'


# class: 'ListView' is the view to display a list of data
class GetList(ListView):
    queryset = [foo, foo1]
    serializer = MySerializer


app.add_url_rule('/get_list',view_func=GetList.as_view('get_list'))


# class: 'RetrieveView' is the view to display one item of data
class GetOne(RetrieveView):
    queryset = [foo, foo1]
    serializer = MySerializer


app.add_url_rule('/get_one/<pk>',view_func=GetOne.as_view('get_one'))
