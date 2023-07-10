

def validate_http_filters(filters: dict) -> dict |  tuple:
    allowed_filters = ['year', 'status', 'city']

    for _, value in enumerate(filters):

        if value not in allowed_filters:
            return {'not_valid': value}

    year = filters.get('year')
    city = filters.get('city')
    status = filters.get('status')

    return (year, city, status)
