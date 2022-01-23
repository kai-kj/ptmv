default: clean
	python3 setup.py sdist bdist_wheel
	twine upload dist/*

clean:
	@$(RM) -rf bin/ build/ dist/ ptmv.egg-info