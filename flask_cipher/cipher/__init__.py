from flask import Flask, render_template, request
##CREATE AN APP AND GIVE IT A NAME
app = Flask('cipher')
## FROM THE CURRENT DIRECTORY, IMPORT VIEWS
from . import secert
## VIEWS IS WEHRE ALL YOUR CODE IS
