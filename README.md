# fake-rpigpio

`fake-rpigpio` is a package intended to provide a lightweight (dependency-free) fake
interface for Raspberry Pi GPIO. The GPIO functions match those in the [`RPi.GPIO`](https://pypi.org/project/RPi.GPIO/)
library, however the functions do nothing. This makes it easier to test GPIO-related code
and to get the code to run on non-pi machines.

## Installation

This package can be installed via pip:

```
pip install fake-rpigpio
``` 

## Usage

A basic example of using this package to run with `RPi.GPIO` on a Pi and `fake-rpigpio` on
a non-Pi:

```python
try:
    import RPi.GPIO
except (RuntimeError, ModuleNotFoundError):
    import fake_rpigpio.utils
    fake_rpigpio.utils.install()
```

This will install `fake-rpigpio.RPi` as `RPi` and `fake-rpigpio.RPi.GPIO` as `RPi.GPIO`,
so you should not need to change imports for the `RPi.GPIO` library.

## Acknowledgements

The following projects inspired this one. While all are similar, the usage and dependency
weight varies between projects.

* [`fake_rpi`](https://github.com/MomsFriendlyRobotCompany/fake_rpi)
* [`fakeRPiGPIO`](https://github.com/luxedo/fakeRPiGPIO)
