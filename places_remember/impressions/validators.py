from django.contrib.gis.geos import Point
from django.core.exceptions import ValidationError


def long_lat_validator(point: Point):
    """
    Check are longitude and latitude values valid
    :param point: instance of Point
    :return: None or raise Exception if one value isn't valid
    """
    if not (180 >= point.x >= -180):  # Longitude
        raise ValidationError(f'Longitude value should be in set of [-180; 180], but given {point.x}')
    if not (90 >= point.y >= -90):  # Latitude
        raise ValidationError(f'Latitude value should be in set of [-180; 180], but given {point.y}')
