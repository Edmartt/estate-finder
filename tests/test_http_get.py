

from flask import Flask, app, request
import pytest
from src import estate
from src.estate.data_access_layer.data_access_interface import DataAccessInterface

from src.estate.http_estate import EstateFinder


class MockDataAccess(DataAccessInterface):
    
    def read_properties_with_filters(self, *args):
        
        year = args[0] if len(args) > 0 else None
        city = args[1] if len(args) > 1 else None
        status = args[2] if len(args) > 2 else None

        print('args in readP: ', args)
        print(year)
        print(city)
        print(status)
        
        data = [

            {
                'address':'my mock address',
                'city': 'medellin',
                'description': 'my mock description',
                'price': 230000,
                'status': 'en_venta',
                'year': 2022
            },

            {
                'address':'my mock address2',
                'city': 'medellin',
                'description': 'my mock description2',
                'price': 330000,
                'status': 'pre_venta',
                'year': 2020
            },

            {
                'address':'my mock address3',
                'city': 'medellin',
                'description': 'my mock description2',
                'price': 330000,
                'status': 'pre_venta',
                'year': 2018
            },

            {
                'address':'my mock address5',
                'city': 'medellin',
                'description': 'my mock description2',
                'price': 330000,
                'status': 'vendido',
                'year': 2018
            }
            ]

        result = [
                item for item in data
                if (year is None or str(item.get('year')) == str(year)) and
                   (city is None or item.get('city') == city) and
                   (status is None or (str(status).lower() == 'none' and item.get('status') is None) or item.get('status') == status)
            ]
        print(result, "read filter")
        return result

    def read_properties_without_filters(self):
        response = [
            {
                'address':'my mock address',
                'city': 'my mock city',
                'description': 'my mock description',
                'price': 230000,
                'status': 'my mock status'
            },

            {
                'address':'my mock address2',
                'city': 'my mock city2',
                'description': 'my mock description2',
                'price': 330000,
                'status': 'my mock status2'
            }
            ]

        return response

def test_http_estate_get_without_filters():
    
    expected_response = {
            'response':[
                {
                    'address':'my mock address',
                    'city': 'my mock city',
                    'description': 'my mock description',
                    'price': 230000,
                    'status': 'my mock status'
                    },

                {
                    'address':'my mock address2',
                    'city': 'my mock city2',
                    'description': 'my mock description2',
                    'price': 330000,
                    'status': 'my mock status2'
                    }
                ]
            }

    app = Flask(__name__)

    with app.test_request_context():

        mock_data_access = MockDataAccess()

        estate = EstateFinder(mock_data_access)

        response_code = estate.get()[1]
        response_result = estate.get()[0].get_json()

        assert response_code == 200
        assert response_result == expected_response


expected_2022 = {
        'response': [
            {'address':'my mock address',
             'city': 'medellin',
             'description': 'my mock description',
             'price': 230000,
             'status': 'en_venta',
             'year': 2022
             }
            ]
        }


@pytest.mark.parametrize(
        'filter_values, expected',
        [((2022, 'medellin', 'en_venta'), expected_2022)
         ]
        )
def test_http_estate_get_with_one_filters(filter_values, expected):
    app = Flask(__name__)
    year, city, status = filter_values

    with app.test_request_context(f'/api/v1/estates?year={year}&city={city}&status={status}'):
        mock_data_access = MockDataAccess()

        estate = EstateFinder(mock_data_access)
        response = estate.get()
        code = response[1]

        assert response[0].get_json() == expected
        assert code == 200


expected_two_filters = {
        'response': [
            {
                'address':'my mock address',
                'city': 'medellin',
                'description': 'my mock description',
                'price': 230000,
                'status': 'en_venta',
                'year': 2022
            },
            ]
        }
@pytest.mark.parametrize(
        'filter_values, expected',
        [
            (('medellin','en_venta'), expected_two_filters)
        ]
        )
def test_http_estate_get_with_two_filters(filter_values, expected):
    app = Flask(__name__)

    city, status = filter_values

    with app.test_request_context(f'/api/v1/estates?city={city}&status={status}'):
        mock_data_access = MockDataAccess()
        estate = EstateFinder(mock_data_access)

        response = estate.get()
        http_code = response[1]

        assert http_code == 200
        assert response[0].get_json() == expected
