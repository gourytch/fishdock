# assume python3.7 is somewhere in the PATH
PYTHON3 = python3.7

PYTEST_ARGS = -xvv

.PHONY: check-pep8
check-pep8::
	$(PYTHON3) -m pep8 -- --first .

.PHONY: test
test::
	$(PYTHON3) -m pytest tests/
