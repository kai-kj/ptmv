default: clean
	python setup.py sdist bdist_wheel
	twine upload dist/*

clean:
	@$(RM) -rf bin/ build/ dist/ ptmv.egg-info