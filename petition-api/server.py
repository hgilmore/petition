from flask import Flask
from flask_cors import CORS

import requests
import pandas as pd

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return "Hey! You're hitting the Petition API."


@app.route('/test')
def get_petition_data():

    url = "https://petition.parliament.uk/petitions/202243.json"

    constituencies = pd.read_csv('uk_constituency_data.csv', thousands=',')

    # TODO - Handle archived petitions
    raw = requests.get(url)
    df = pd.read_json(raw.content)

    sigs = df.data[0]['signatures_by_constituency']
    sigs_sorted = pd.io.json.json_normalize(sigs).sort_values(
        by='signature_count', ascending=False)

    sigs_sorted.columns = ['mp', 'Constituency', 'ons_code', 'signature_count']
    constituencies.columns = ['Constituency', 'Electorate 2000',
                              'Electorate 2010', 'Electorate 2015',
                              'Largest county', 'Country', 'Region']


    blend = constituencies.merge(sigs_sorted)
    blend['Percent Signed'] = (blend['signature_count'] / blend['Electorate 2015']) * 100
    blend.sort_values(by='Percent Signed', ascending=False)

    response = blend.to_json(orient='table')

    return response
