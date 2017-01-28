init:
	pip install -e .

test: init
	python tests/test_*
	rm -rf float_range.egg-info

update-pypitest:
	python setup.py register -r pypitest
	python setup.py sdist upload -r pypitest

update-pypi:
	python setup.py register -r pypi
	python setup.py sdist upload -r pypi
