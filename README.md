# coordinate-utils

Coordinate conversion helpers built on pyproj.

## Install

Install from source:

```bash
git clone https://github.com/larsderidder/coordinate-utils.git
cd coordinate-utils
python -m venv .venv
. .venv/bin/activate
python -m pip install -U pip
python -m pip install .
```

## Usage

```python
from coordinate_utils import convert_coordinates, convert_many, resolve_crs

x, y = convert_coordinates(52.37, 4.90, "EPSG:4326")
points = convert_many([(52.37, 4.90), (40.71, -74.0)], resolve_crs("WGS84/GPS"))
```

## Development

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -U pip
python -m pip install -e ".[dev]"
pytest
```
