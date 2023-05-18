from coordinate_utils import (
    COORDINATE_SYSTEMS,
    convert_coordinates,
    convert_many,
    list_coordinate_systems,
    resolve_crs,
)


def test_list_coordinate_systems():
    names = list_coordinate_systems()
    assert "WGS84/GPS" in names
    assert names == list(COORDINATE_SYSTEMS.keys())


def test_convert_coordinates_identity():
    lat, lon = 52.37, 4.90
    x, y = convert_coordinates(lat, lon, "EPSG:4326")
    assert round(x, 6) == round(lon, 6)
    assert round(y, 6) == round(lat, 6)


def test_convert_many_and_resolve():
    points = [(52.37, 4.90), (40.71, -74.0)]
    crs = resolve_crs("WGS84/GPS")
    converted = convert_many(points, crs)
    assert len(converted) == 2
