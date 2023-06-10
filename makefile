clean:
	rm -rf dist/
	rm -rf build/
build:
	pip install wheel
	python setup.py bdist_wheel
upload:
	pip install twine
	python -m twine upload dist/*.whl
deploy:
	make clean
	make build
	make upload
