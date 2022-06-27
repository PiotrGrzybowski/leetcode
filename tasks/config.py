from pathlib import Path

from generator.basics import Config, Writer
from generator.golang import GO_MAPPING
from generator.python import PYTHON_MAPPING

templates_path = Path('../generator/templates')
go_path = Path('../go')
python_path = Path('../python/algos')

paths = Config(templates_path, python_path, go_path, PYTHON_MAPPING, GO_MAPPING)
writer = Writer(paths)