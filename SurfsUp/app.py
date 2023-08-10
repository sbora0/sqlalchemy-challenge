# Dependencies
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, distinct
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
measurement = Base.classes.measurement
station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def homepage():
    return"""
            <h1> Hawaii Climate API </h1>
            <h2> Available Routes: </h2>
            <ul>
                <li><a href = "/api/v1.0/precipitation">/api/v1.0/precipitation</a></li>
                <li><a href = "/api/v1.0/stations">/api/v1.0/stations</a></li>
                <li><a href = "/api/v1.0/tobs">/api/v1.0/tobs</a></li>
                <li>Use <b>/api/v1.0/start</b> and replace start with start date in "yyyy-mm-dd" format</li>
                <li>Use <b>/api/v1.0/start/end</b> and replace start with start date and end with end date in "yyyy-mm-dd" format</li>
            </ul>
          """

# Define what to do when the user hits the route
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create the session (link) from Python to the DB
    session = Session(engine)
    # Query 
    results = session.query(measurement.date, measurement.prcp).filter(measurement.date >= '2016-08-23').all()
    # Close session
    session.close()
    # Create a dictionary and append to a list
    prcp_list = []
    for dt,prcp in results:
        prcp_dict = {}
        prcp_dict[dt] = prcp
        prcp_list.append(prcp_dict)
    # Jsonify the final list
    return jsonify(prcp_list)

# Define what to do when the user hits the route
@app.route("/api/v1.0/stations")
def stations():
    # Create the session (link) from Python to the DB
    session = Session(engine)
    # Query 
    results = session.query(station.station).all()
    # Close session
    session.close()
    # Convert list of tuples into normal list
    station_list = list(np.ravel(results))
    # Jsonify the final list
    return jsonify(station_list)

# Define what to do when the user hits the route
@app.route("/api/v1.0/tobs")
def tobs():
    # Create the session (link) from Python to the DB
    session = Session(engine)
    # Query 
    results = session.query(measurement.date, measurement.tobs).filter(measurement.station == 'USC00519281').filter(measurement.date >= '2016-08-23').all()
    # Close session
    session.close()
    # Create a dictionary and append to a list
    tobs_list = []
    for dt,tobs in results:
        tobs_dict = {}
        tobs_dict['date'] = dt
        tobs_dict['tobs'] = tobs
        tobs_list.append(tobs_dict)
    # Jsonify the final list
    return jsonify(tobs_list)

# Define what to do when the user hits the route
@app.route("/api/v1.0/<start>")
def get_temp_from(start):
    # Create the session (link) from Python to the DB
    session = Session(engine)
    # Query 
    results = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).filter(measurement.date >= start).all()
    # Close session
    session.close()
    # Convert list of tuples into normal list
    station_list = list(np.ravel(results))
    # Jsonify the final list
    return jsonify(station_list)

# Define what to do when the user hits the route
@app.route("/api/v1.0/<start>/<end>")
def get_temp_from_to(start,end):
    # Create the session (link) from Python to the DB
    session = Session(engine)
    # Query 
    results = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).filter(measurement.date >= start).filter(measurement.date <= end).all()
    # Close session
    session.close()
    # Convert list of tuples into normal list
    station_list = list(np.ravel(results))
    # Jsonify the final list
    return jsonify(station_list)

# Define main branch
if __name__ == '__main__':
    app.run(debug=True)
