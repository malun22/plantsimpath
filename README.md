<h1 align="center">
plantsimpath
</h1>

<h4 align="center">A Python helper class to make <a href="https://www.dex.siemens.com/plm/tecnomatix/plant-simulation" target="_blank">Siemens Tecnomatix Plant Simulation</a> Path usage accessible.</h4>

<p align="center">
  <a href="#setup">Setup</a> •
  <a href="#examples">Examples</a> •
  <a href="https://malun22.github.io/plantsimpath/" target="_blank">Further documentation</a> •
  <a href="#notice">Notice</a> •
  <a href="#license">License</a>
</p>

## Setup

Install via pip:

```
pip install plantsimpath
```

Find this package on [Pypi](https://pypi.org/project/plantsimpath/).

## Examples

```python
from plantsimpath import PlantsimPath

station = PlantsimPath(".Models.Model.Station")
station_wo_dot = PlantsimPath("Models.Model.Station")

print(
    f'Do Plantsim path always begin with a "."? {"Yes" if station == station_wo_dot else "No"}'
)

attribute_div = station / "ProcTime"
attribute_add = station + "ProcTime"
attribute_init = PlantsimPath(station, "ProcTime")

print(
    f"Are all paths the same? {'Yes' if attribute_div == attribute_add == attribute_init else 'No'}"
)

model = station.parent()
is_child = station.is_child_of(model)
print(f"Is {station} a child of {model}? {'Yes' if is_child else 'No'}")

system_path = station.to_path()
print(f"{station} is located at {system_path}")

table_path = PlantsimPath('.Models.Model.Table["ColumnIndex",10]')
object_in_table = table_path / "ProcTime"

print(
    f"Is {object_in_table} a child of {table_path}? {'Yes' if object_in_table.is_child_of(table_path) else 'No'}"
)
```

There are further examples in the [example folder](https://github.com/malun22/plantsimpath/tree/main/examples).

## Further documentation

Here is the [documentation for plantsimpath](https://malun22.github.io/plantsimpath/)

## Notice

This package is not developed, endorsed, or maintained by Siemens AG.
The names "SimTalk" and "Plant Simulation" are trademarks of Siemens AG.

## License

This package is distributed under the MIT License.
