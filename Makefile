MOCK_CONFIG=stable-7-x86_64
ROOT=/
PREFIX=/usr
ANSIBLE_BRANCH=master

install:
	# Cleanup temporary files
	rm -f INSTALLED_FILES

	# Use Python setuptools
	python setup.py build ; python ./setup.py install -O1 --prefix="${PREFIX}" --root="${ROOT}" --record=INSTALLED_FILES
	cat INSTALLED_FILES | sed 's/^/\//g' >> INSTALLED_FILES

test:
	py.test -svvvv --junitprefix=mets --junitxml=junit.xml tests

coverage:
	py.test tests --cov=mets --cov-report=html
	coverage report -m
	coverage html
	coverage xml

clean: clean-rpm
	find . -iname '*.pyc' -type f -delete
	find . -iname '__pycache__' -exec rm -rf '{}' \; | true

clean-rpm:
	rm -rf rpmbuild

rpm: clean-rpm
	create-archive.sh
	preprocess-spec-m4-macros.sh include/rhel7
	build-rpm.sh ${MOCK_CONFIG}

e2e-localhost-cleanup: .e2e/ansible-fetch
	cd .e2e/ansible ; ansible-playbook -i inventory/localhost e2e-pre-test-cleanup.yml

.e2e/ansible:
	git clone https://gitlab.csc.fi/dpres/ansible-preservation-system.git .e2e/ansible

.e2e/ansible-fetch: .e2e/ansible
	cd .e2e/ansible ; \
		git fetch ; \
		git checkout $(ANSIBLE_BRANCH) ; \
		git reset --hard origin/$(ANSIBLE_BRANCH) ; \
		git clean -fdx ; \
		git status

