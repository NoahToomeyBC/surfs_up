# Import dependencies

import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Create engine variable

engine = create_engine("sqlite:///hawaii.sqlite")

#Create base format
Base = automap_base()

# Reflect tables

Base.prepare(engine, reflect= True)

# Create/ Access measurement and station classes
Measurement = Base.classes.measurement
Station = Base.classes.station

#create a session


# Define flask app

app=Flask(__name__)

# Setup welcome route
@app.route("/")

# Create welcome route function
def welcome():
    session=Session(engine)
    session.close()
    return(
    '''
    Welcome to the Climate Analysis API!<br/>
    Available Routes:<br/>
    /api/v1.0/precipitation<br/>
    /api/v1.0/stations<br/>
    /api/v1.0/tobs<br/>
    /api/v1.0/temp/start/end
    ''')

# Setup precipitation route
@app.route("/api/v1.0/precipitation")

# Create precipitation route function
def precipitation():
   session=Session(engine) 
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   session.close()
   return jsonify(precip)

# Setup stations route
@app.route("/api/v1.0/stations")

# Create station route function
def stations():
    session=Session(engine)
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    session.close()
    return jsonify(stations)

# Setup temp route
@app.route("/api/v1.0/tobs")

# Create tobs route function
def temp_monthly():
    session=Session(engine)
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    session.close()
    return jsonify(temps=temps)

# Setup start and end date route for temp
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# Create a stats function
def stats(start=None, end=None):
    session=Session(engine)
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    session.close()
    return jsonify(temps)

if __name__ == "__main__":
    app.run(debug=True)