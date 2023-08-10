# sqlalchemy-challenge
SQL Alchemy Challenge Assignment 10

For this assignment there were two requirements as given below:

1.	Analyze and Explore Climate Data by using Python and SQL Alchemy to do a basic climate analysis and data exploration of climate database. Use SQL Alchemy ORM queries, Pandas, and Matplotlib to complete the below 
    requirements:

    Precipitation analysis:

        o	Find the most recent date in the dataset.
        o	Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.
        o	Load the query results into a Pandas DataFrame. Explicitly set the column names for date and precipitation.
        o	Sort the DataFrame values by "date".
        o	Plot the results in a line graph by using the DataFrame plot method.
        o	Use Pandas to print summary statistics for the precipitation data.

    Station Analysis:

        o	Design a query to calculate the total number of stations in the dataset.
        o	Design a query to find the most-active stations (that is, the stations that have the most rows). To do so, complete the following steps:
        o	Answer the following question: which station id has the greatest number of observations?
        o	Using the most-active station id, calculate the lowest, highest, and average temperatures.
        o	Design a query to get the previous 12 months of temperature observation (TOBS) data. To do so, complete the following steps:
        o	Filter by the station that has the greatest number of observations.
        o	Query the previous 12 months of TOBS data for that station.
        o	Plot the results as a histogram with 12 bins.
        o	Close your session.
  	
3.	Design Climate App

    Design a Flask API based on the queries that you just developed. To do so, use Flask to create your routes as follows:
  	
    Start at the homepage.
  	
    List all the available routes.
  	
    /api/v1.0/precipitation
  	
        •	Convert the query results to a dictionary by using date as the key and prcp as the value.
        •	Return the JSON representation of your dictionary.

    /api/v1.0/stations

  	    •	Return a JSON list of stations from the dataset.
    /api/v1.0/tobs
  	
        •	Query the dates and temperature observations of the most-active station for the previous year of data.
        •	Return a JSON list of temperature observations for the previous year.
    /api/v1.0/start and /api/v1.0/start/end
    
        •	Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
        •	For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
        •	For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.

Files Information:

    •	The “hawaii.sqlite” file for database is in “SurfsUp\Resources” folder.
    •	The file “climate_starter.ipynb” for precipitation and station analysis is in “SurfsUp” folder.
    •	The file “app.py” used to create the Climate App is in  “SurfsUp” folder.

