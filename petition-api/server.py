from flask import Flask
from flask_cors import CORS

import requests
import pandas as pd

app = Flask(__name__)
CORS(app)

constituencies = pd.read_csv('uk_constituency_data.csv', thousands=',')

@app.route('/')
def hello_world():
    return "Hey! You're hitting the Petition API."


# TODO - Add caching around this function as it's not going to update that often.
@app.route('/petition/<number>')
def get_petition_data(number):

    if number:
        # TODO - Handle archived and missing petitions.
        # Break all of this out into different functions.
        url = "https://petition.parliament.uk/petitions/" + number +".json"

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

        # Drop unwanted columns
        del blend['Electorate 2000']
        del blend['Electorate 2010']
        del blend['ons_code']

        response = blend.to_json(orient='table')

        return response

    else:
        
        # TODO - Add correct HTTP responses here.
        return "You didn't specify a petiton number."

if __name__ == '__main__':
    app.run()