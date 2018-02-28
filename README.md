The following process is implemented to create a Restful WebService to host weather information.
# GET method
GET method is used to read the file and return the data present in it in the form of JSON in the format of YYYYMMDD.
Link to view GET method:  http://ec2-18-219-161-204.us-east-2.compute.amazonaws.com:5000/historical  
# GET method with input
GET method with Input is used to see the weather information of particular given date.
Link to view GET method with Input: http://ec2-18-219-161-204.us-east-2.compute.amazonaws.com:5000historical/YYYYMMDD
# POST method 
POST method is used to add weather information of a particular day by taking inputs of Date, TMax and Tmin.
In order to run the POST method, we used the Rest client(POSTMAN)
Link to request post:   http://ec2-18-219-161-204.us-east-2.compute.amazonaws.com:5000/historical/
In body,Example: Date : 20170101
         Tmax : 28
         Tmin : 13
# DELETE METHOD
DELETE method is used to delete weather information for a particular day.
To delete a particular date: http://ec2-18-219-161-204.us-east-2.compute.amazonaws.com:5000historical/YYYYMMDD
In body,Example: Date : 20170101

# Weather Forecast for next 7 days
Weather Forecasting for next few days is implemented using the Yahoo weather API.
GET method inputs the date and forecast the weather of that particular date.
To Forecast weather data : http://ec2-18-219-161-204.us-east-2.compute.amazonaws.com:5000historical/YYYYMMDD
