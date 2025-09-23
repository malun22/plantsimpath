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
import pyplantsim

with Plantsim(license=PlantsimLicense.STUDENT, version=PlantsimVersion.V_MJ_22_MI_1,
                    visible=True, trusted=True, suppress_3d=False, show_msg_box=False) as plantsim:

        plantsim.new_model()

        plantsim.save_model(
            folder_path=r"C:\users\documents\plantsimmodels", file_name="MyNewModel")
```

There are further examples in the [example folder](https://github.com/malun22/pyplantsim/tree/main/examples).

## Further documentation

Here is the [documentation for plantsimpath](https://malun22.github.io/plantsimpath/)

## Notice

This package is not developed, endorsed, or maintained by Siemens AG.
The names "SimTalk" and "Plant Simulation" are trademarks of Siemens AG.

## License

This package is distributed under the MIT License.
