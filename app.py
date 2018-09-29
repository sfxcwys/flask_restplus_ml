from flask import Flask
from flask_restplus import Resource, Api
from flask_restplus import reqparse
import pickle
import pandas as pd
import traceback
import os
import PipelineHelper


input_parser = reqparse.RequestParser()
input_parser.add_argument('Age', type=int, required=False, help='Age in years')
input_parser.add_argument('Fare', type=float, required=False, help='Passenger fare')
input_parser.add_argument('Pclass', type=int, required=False, choices=[1, 2, 3],
                          help='Ticket class')
input_parser.add_argument('Sex', type=str, required=False, choices=['female', 'male'],
                          help='Sex')

# Create a Flask WSGI application
app = Flask(__name__)
# Create a Flask-RESTPlus API
api = Api(app=app,
          title='Titanic: Machine Learning from Disaster',
          description='Model scoring UI',
          specs=False)


# Create a URL route to this resource
@api.route('/prediction')
# Create a RESTful resource
class Prediction(Resource):
    @api.expect(input_parser)
    def get(self):
        try:
            args = input_parser.parse_args()
            x = pd.DataFrame([args])
            model = pickle.load(open('model_pipeline.pkl', 'rb'))
            prediction = model.predict_proba(x)[0][1]
            return {"prediction": prediction}

        except Exception as e:
            return {'message': str(e), 'error': traceback.print_exc()}, 400

if __name__ == '__main__':
    app.run(debug=False, host=os.environ['MODEL_HOST'])