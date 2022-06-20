# ----------------------------------
#          INSTALL & TEST
# ----------------------------------
install_requirements:
	@pip install -r requirements.txt

check_code:
	@flake8 scripts/* FaVoriTe/*.py

black:
	@black scripts/* FaVoriTe/*.py

test:
	@coverage run -m pytest tests/*.py
	@coverage report -m --omit="${VIRTUAL_ENV}/lib/python*"

ftest:
	@Write me

clean:
	@rm -f */version.txt
	@rm -f .coverage
	@rm -fr */__pycache__ */*.pyc __pycache__
	@rm -fr build dist
	@rm -fr FaVoriTe-*.dist-info
	@rm -fr FaVoriTe.egg-info

install:
	@pip install . -U

all: clean install test black check_code

count_lines:
	@find ./ -name '*.py' -exec  wc -l {} \; | sort -n| awk \
        '{printf "%4s %s\n", $$1, $$2}{s+=$$0}END{print s}'
	@echo ''
	@find ./scripts -name '*-*' -exec  wc -l {} \; | sort -n| awk \
		        '{printf "%4s %s\n", $$1, $$2}{s+=$$0}END{print s}'
	@echo ''
	@find ./tests -name '*.py' -exec  wc -l {} \; | sort -n| awk \
        '{printf "%4s %s\n", $$1, $$2}{s+=$$0}END{print s}'
	@echo ''

# ----------------------------------
#      UPLOAD PACKAGE TO PYPI
# ----------------------------------
PYPI_USERNAME=<AUTHOR>
build:
	@python setup.py sdist bdist_wheel

pypi_test:
	@twine upload -r testpypi dist/* -u $(PYPI_USERNAME)

pypi:
	@twine upload dist/* -u $(PYPI_USERNAME)

# ----------------------------------
#      PYGETTEXT
# ----------------------------------
extract:
	@/mnt/c/Users/Lubomir/anaconda3/pkgs/python-3.9.7-h6244533_1/Tools/i18n/pygettext.py -d base -o locales/base.pot FaVoriTe/app.py
base_po:
	@cp locales/base.pot locales/de/LC_MESSAGES/base.po
	@cp locales/base.pot locales/svk/LC_MESSAGES/base.po
base_mo:
	@msgfmt -o locales/de/LC_MESSAGES/base.mo locales/de/LC_MESSAGES/base
	@msgfmt -o locales/svk/LC_MESSAGES/base.mo locales/svk/LC_MESSAGES/base
