# get info
OS = $(shell uname)
SFLAG = $(shell id -u)

# set commands
RM = rm -f
MV = mv
MKDIR = mkdir -p
INSTALLER = pyinstaller --onefile --name ptmv

# default
default: build

# build
build: clean
	@$(INSTALLER) ptmv/__main__.py
	@$(MKDIR) bin
	@$(MV) dist/ptmv bin/
	@$(RM) -r dist/ build/ ptmv.spec

# install
install: uninstall
	@$(MV) bin/ptmv /usr/local/bin

# uninstall
uninstall:
	@$(RM) /usr/local/bin/ptmv

# clean
clean:
	@$(RM) -r bin/ build/ dist/ ptmv.egg-info

# update pip
pip: clean
	python setup.py sdist bdist_wheel
	twine upload dist/*