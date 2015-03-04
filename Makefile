SHELL := /bin/bash # Use bash syntax

define HELP_TEXT
Assets manager project
===

Usage:

> make setup        # Prepare dependencies
> make develop      # Run the dev server

endef

ENVPATH=${VIRTUAL_ENV}

ifeq ($(ENVPATH),)
	ENVPATH=env
endif

VEX=vex --path ${ENVPATH}

ifeq ($(PORT),)
	PORT=8011
endif

##
# Print help
##
help:
	$(info ${HELP_TEXT})

##
# Prepare the project
##
setup:
	# Install missing dependencies
	if ! dpkg -s python-pip &> /dev/null; then \
		sudo apt update && sudo apt install -y python-pip; \
	fi

	# Install vex globally (also installs virtualenv)
	type vex &> /dev/null || sudo pip install vex

	# Create virtual env folder, if not already in one
	if [ -z ${VIRTUAL_ENV} ]; then virtualenv ${ENVPATH}; fi

	# Install requirements into virtual env
	${VEX} pip install -r requirements/dev.txt

##
# Start the development server
##
develop:
	${VEX} python manage.py runserver_plus 0.0.0.0:${PORT}

# Non-file make targets (https://www.gnu.org/software/make/manual/html_node/Phony-Targets.html)
.PHONY: help setup develop
