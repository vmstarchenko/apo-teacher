clean:
	find . -name \*.pyc -delete
	find . -name __pycache__ -delete
	find . -name ".mypy_cache" -exec rm -rf {} \;
	find . -name "flycheck_*" -exec rm -rf {} \;

tree: clean
	tree -I "venv|tmp|*.egg-info" .

start:
	jupyter notebook

# venv
new_venv: remove_venv
	python3.6 -m venv venv


remove_venv:
	rm -rf venv


install:
	pip install -r requirements.txt


freeze:
	pip freeze > requirements.txt



