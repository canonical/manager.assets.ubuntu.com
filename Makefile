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
	scripts/setup.sh

##
# Start the development server
##
develop:
	scripts/runserver.sh ${PORT}


setenv:
	export NODE_ENV=hello

# Non-file make targets (https://www.gnu.org/software/make/manual/html_node/Phony-Targets.html)
.PHONY: help setup develop
