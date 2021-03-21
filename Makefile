.ONESHELL:
SHELL := /bin/bash
SRC = $(wildcard nbs/*.ipynb)

all: cute_ranking docs

cute_ranking: $(SRC)
	nbdev_build_lib
	touch cute_ranking

sync:
	nbdev_update_lib

docs_serve: docs
	cd docs && bundle exec jekyll serve

docs: $(SRC)
	nbdev_build_docs
	touch docs

test:
	nbdev_test_nbs

release: pypi
	nbdev_bump_version

pypi: dist
	twine upload dist/*

dist: clean
	python setup.py sdist bdist_wheel

clean:
	rm -rf dist