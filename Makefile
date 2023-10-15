VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip3

setup: $(VENV)/bin/activate
	python3 -m pip install --upgrade pip
	pre-commit install

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt
clean:
	# Remove the virtual environment and any other generated files
	rm -rf venv
	rm -rf _pycache__
	rm -rf backend/__pycache__
