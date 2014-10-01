SHELL := /bin/bash # Use bash syntax

define HELP_TEXT
Ubuntu.com website project
===

Usage:

> make auth-token   # Generate an API key for pairing with the assets-server

> make setup        # Prepare dependencies
> make develop      # Run the dev server

endef

ENVPATH=${VIRTUAL_ENV}
VEX=vex --path ${ENVPATH}
ifeq ($(ENVPATH),)
	ENVPATH=env
endif

##
# Prepare the project
##
setup:
	# Create virtual env folder, if not already in one
	-[ -z ${VIRTUAL_ENV} ] && virtualenv ${ENVPATH}

	# Install requirements into virtual env
	${VEX} pip install -r requirements/dev.txt

develop:
	${VEX} python manage.py runserver_plus 8011

rebuild-dependencies-cache:
	rm -rf pip-cache
	bzr branch lp:~webteam-backend/assets-manager/dependencies pip-cache
	pip install --exists-action=w --download pip-cache/ -r requirements.txt
	bzr commit pip-cache/ --unchanged -m 'automatically updated partners requirements'
	bzr push --directory pip-cache lp:~webteam-backend/assets-manager/dependencies
	rm -rf pip-cache src

auth-token:
	@$(eval TOKEN := $(shell uuidgen -r | sed 's/-//g'))
	@sed -i "s/<TOKEN_PLACEHOLDER>/${TOKEN}/" assets_manager/settings.py; \
	echo "Authorization token (in assets_manager/settings.py):"
	@grep -o -P "(?<=AUTH_TOKEN\\s=\\s')[^']+(?=')" assets_manager/settings.py


pip-cache:
	(cd pip-cache && bzr pull && bzr up) || bzr branch lp:~webteam-backend/assets-manager/dependencies pip-cache
