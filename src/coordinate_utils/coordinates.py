"""Coordinate conversion helpers built on pyproj."""

from __future__ import annotations

from typing import Iterable

from pyproj import Transformer

COORDINATE_SYSTEMS = {
    "WGS84/GPS": "EPSG:4326",
    "RD": "EPSG:28992",
}


def list_coordinate_systems() -> list[str]:
    """Return the supported coordinate system names."""
    return list(COORDINATE_SYSTEMS.keys())


def resolve_crs(name_or_code: str) -> str:
    """Resolve a CRS code from a known name or return the code as-is."""
    return COORDINATE_SYSTEMS.get(name_or_code, name_or_code)


def _projector(target_crs_code: str) -> Transformer:
    """Build a transformer from WGS84 to the target CRS."""
    return Transformer.from_crs("EPSG:4326", target_crs_code, always_xy=True)


def convert_coordinates(lat: float, lon: float, target_crs_code: str) -> tuple[float, float]:
    """Convert WGS84 coordinates to the target CRS."""
    projector = _projector(resolve_crs(target_crs_code))
    east, north = projector.transform(lon, lat)
    return float(east), float(north)


def convert_many(
    points: Iterable[tuple[float, float]], target_crs_code: str
) -> list[tuple[float, float]]:
    """Convert multiple WGS84 coordinates to the target CRS."""
    projector = _projector(resolve_crs(target_crs_code))
    converted: list[tuple[float, float]] = []
    for lat, lon in points:
        east, north = projector.transform(lon, lat)
        converted.append((float(east), float(north)))
    return converted
