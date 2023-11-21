VENV = venv
PYTHON = $(VENV)/Scripts/python
PIP = $(VENV)/Scripts/pip

setup: $(VENV)/Scripts/activate
	$(PYTHON) -m pip install --upgrade pip

$(VENV)/Scripts/activate: requirements.txt
	python -m venv $(VENV)
	$(PIP) install -r requirements.txt

clean:
	# Remove the virtual environment and any other generated files
	rmdir /s /q $(VENV)
	del /q /s _pycache__
	del /q /s backend\__pycache__
