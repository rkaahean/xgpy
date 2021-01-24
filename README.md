<p align="center">
  <h1 align="center">
    xgpy: a powerful python wrapper for football data
  </h1>
</p>
<p align="center">
   <a href="https://travis-ci.com/rkaahean/xgpy"><img src="https://travis-ci.com/rkaahean/xgpy.svg?branch=main"></a>
   <a href="https://xgpy.readthedocs.io/en/latest/"><img src="https://readthedocs.org/projects/xgpy/badge/?version=latest"></a>
   <a href="https://www.codacy.com/gh/rkaahean/xgpy/dashboard"><img src="https://app.codacy.com/project/badge/Grade/8474374650fb4fe88b24bc51245187d8"></a>
   <a href="https://badge.fury.io/py/xgpy"><img src="https://badge.fury.io/py/xgpy.svg" alt="PyPI version" height="18"></a>
</p>

## What is it?

**xgpy** is a Python package that aims to aggregate multiple football data sources into a single python module.
Using a single function, one can retrieve data from multiple sources, compare and perform a more complete analysis.

| Source | Status |
| -------|--------|
| understat.com | Beta |
| fbref.com | Tesing |
| whoscored.com | In Progress |
| fantasy.premierleague.com | Planned |
| transfermarkt.us | Planned |

## Installation

The source code is currently [here.](https://github.com/rkaahean/xgpy)

The simplest way to install the package is by pip.
```bash
pip install xgpy
```

If you want to clone the repository instead:
```bash
git clone https://github.com/rkaahean/xgpy.git
```

To generate the requirements, use the following:
```bash
pipreqs xgpy/
```
I will probably start using `pipenv` in the near future.

## Usage

**xgpy** has multiple modules, each for every source. For example, in order to get stats from understat:

```python
import xgpy
from xgpy.understat import UnderstatPlayer

player = UnderstatPlayer(1228)
match_data = player.get_player_match_data()
```

And that's it! Look through the documentation and call upon a number of functions.

## Documentation

All the documentation for the functions can be found at [here.](https://xgpy.readthedocs.io/en/latest/)
