from flask import request, Flask, render_template # Importing flask
from flask_restful import Resource, Api 
from flask import jsonify
import csv, json
import os
import shutil
from weather import Weather
weather = Weather()


myapp = Flask(__name__)
api = Api(myapp)

@myapp.route('/')
def main():
    return render_template('try.html')

@myapp.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    rsp = jsonify(message)
    rsp.status_code = 404

    return rsp
#GET method is used to read the file and return the data present in it in the form of JSON in the format of YYYYMMDD.
@myapp.route('/historical/', methods=['GET'])
def historical():
    with open('daily.csv') as csvfile:
        rd = csv.Dictrd(csvfile)
        ld = []
        for row in rd:
            ld.append({"DATE":row['DATE']})
    return json.dumps(ld)

#GET method with Input is used to see the weather information of particular given date. 
@myapp.route('/historical/<date>', methods=['GET'])
def historical_date(date):
    #date = request.args.get('date')
    with open('daily.csv') as csvfile:
        rd = csv.Dictrd(csvfile)
        dt ={}
        for row in rd:
            if(row['DATE']==date):
                dt = jsonify({"DATE":row['DATE'],"TMAX":row['TMAX'], "TMIN":row['TMIN']})
                return dt
        return not_found() 
 #POST method is used to add weather information of a particular day by taking inputs of Date, TMax and Tmin.
@myapp.route('/historical/', methods=['POST'])
def historical_post():
    dt = request.get_dt();
    json_dt = json.loads(dt)
    Date = json_dt['DATE']
    Tmax = json_dt['TMAX']
    Tmin = json_dt['TMIN']
    new= [Date, Tmax, Tmin];

    with open('daily.csv', 'a') as csvfile:
        newFileWriter = csv.writer(csvfile)
        jsonify(newFileWriter.writerow(new))
    rsp=jsonify(json_dt)
    rsp.status_code=201
    return rsp
#DELETE method is used to delete weather information for a particular day. 
@myapp.route('/historical/<date_del>', methods=['DELETE'])
def historical_delete(date_del):
    #date_del = request.args.get('date');
    #os.remove("daily.csv")
    #os.rename('daily2.csv','daily.csv')
    fieldnames = ["DATE", "TMAX","TMIN"]
    with open('daily.csv', 'r') as csvfile, open('output.csv', 'w') as outputfile:
        rd = csv.Dictrd(csvfile, fieldnames=fieldnames)
        writer = csv.DictWriter(outputfile, fieldnames=fieldnames)
        for row in rd:
            if not date_del == row['DATE']:
                writer.writerow({'DATE': row['DATE'], 'TMAX': row['TMAX'], 'TMIN': row['TMIN']})
    shutil.move('output.csv','daily.csv')
    return json.dumps(date_del)
#Weather Forecasting for next few days is implemented using the Yahoo weather API.
@myapp.route('/forecast/<date>', methods=['GET'])
def forecast(date):
    lookup = weather.lookup(560743)

    location = weather.lookup_by_location('cincinnati')
    forecast_list=[]
    forecasts = location.forecast()
    i=0
    tmp_date=int(date)
    for forecast in forecasts:
        i=i+1
        if(i>7):
            break
        forecast_list.append({"DATE":str(tmp_date), "TMAX":float(forecast.high()), "TMIN":float(forecast.low())})
        tmp_date=tmp_date+1

    return json.dumps(forecast_list)

