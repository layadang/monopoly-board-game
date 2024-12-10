# Define virtual environment
VENV = venv

# Install dependencies
install:
	python3 -m venv $(VENV)
	./$(VENV)/bin/pip install -r requirements.txt

# Run the demo script
test:
	./$(VENV)/bin/python run_demo.py

# Clean up virtual environment
clean:
	rm -rf $(VENV)

# Reinstall all dependencies
reinstall: clean install