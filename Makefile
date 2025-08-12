ifeq ($(origin MONKEYTYPE), undefined)
  PYTHON = python3
else
  PYTHON = MONKEYTYPE_TRACE_MODULES=dbus_signature_pyparsing monkeytype run
endif

MONKEYTYPE_MODULES_IGNORE = dbus_signature_pyparsing._parsing

.PHONY: lint
lint:
	pylint setup.py
	pylint src/dbus_signature_pyparsing
	pylint tests

.PHONY: test
test:
	${PYTHON} -m unittest discover --verbose tests

.PHONY: coverage
coverage:
	coverage --version	
	coverage run --timid --branch -m unittest discover tests
	coverage report -m --fail-under=100 --show-missing --include="./src/*"

.PHONY: fmt
fmt:
	isort setup.py src tests
	black .

.PHONY: fmt-travis
fmt-travis:
	isort --diff --check-only setup.py src tests
	black . --check

.PHONY: yamllint
yamllint:
	yamllint --strict .github/workflows/main.yml

.PHONY: package
package:
	(umask 0022; python -m build; python -m twine check --strict ./dist/*)

.PHONY: apply
apply:
	@echo "Modules traced:"
	@monkeytype list-modules
	@echo
	@echo "Annotating:"
	@for module in ${MONKEYTYPE_MODULES_IGNORE}; do \
	  monkeytype apply  --sample-count --ignore-existing-annotations $${module} > /dev/null; \
	done
