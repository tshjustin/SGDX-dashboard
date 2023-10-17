from flask import Flask 
from query_price import fetch_rates
from utils import * 
from database_handler import * 
import time 

app = Flask() 


