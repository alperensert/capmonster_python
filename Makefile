build:
	python -m pip install --upgrade pip
	pip install build

install: install_test install_pkg

install_test:
	pip install .[test]

install_pkg:
	python -m pip install --upgrade pip wheel
	pip install .

test:
	python -m unittest -v tests/test_tasks.py

setup_dependencies:
	pip install setuptools_scm wheel
