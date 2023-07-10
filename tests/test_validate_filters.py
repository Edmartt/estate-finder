import pytest

from src.estate.utils.filter_validator import validate_http_filters


request_filters1 = {'year': 2022, 'city': 'pereira', 'status': 'pre_venta'}
request_filters2 = {'year': 2018, 'city': 'bogota', 'status': 'en_venta'}
request_filters3 = {'year': 2015, 'city': 'medellin', 'status': 'vendido'}

@pytest.mark.parametrize(
        'good_filters, expected',
        [(request_filters1, (2022, 'pereira', 'pre_venta')),
         (request_filters2, (2018, 'bogota', 'en_venta')),
         (request_filters3, (2015, 'medellin', 'vendido'))
         ]
        )
def test_validate_good_http_filters(good_filters, expected):
    assert validate_http_filters(good_filters) == expected



wrong_filter1 = ({'description': 'a test filter', 'city': 'cali', 'status': 'en_venta'})

wrong_filter2 = ({'year': 2020, 'cities': 'bogota', 'status': 'vendido'})

wrong_filter3 = ({'year': 2018, 'city': 'bogota', 'estatus': 'vendido'})


@pytest.mark.parametrize(
        'wrong_filters, expected',
        [(wrong_filter1, {'not_valid': 'description'}),
         (wrong_filter2, {'not_valid': 'cities'}),
         (wrong_filter3, {'not_valid': 'estatus'})
         ]
        )
def test_validate_wrong_http_filters(wrong_filters, expected):
    assert validate_http_filters(wrong_filters) == expected
