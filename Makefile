# Jenkins CI Pipeline Targets
.PHONY: pypi-release

pypi-release:
	tox -e publish
