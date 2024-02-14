#!/bin/sh
R -e 'renv::use_python(type = \"virtualenv\", python = \"/usr/local/python/3.11.4/bin/python\"); renv::restore()'
ln .devcontainer/pre-commit .git/hooks/
chmod +x .git/hooks/pre-commit