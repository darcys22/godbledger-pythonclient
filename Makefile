venv: venv/touchfile

venv/touchfile: requirements.txt
	test -d venv || virtualenv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/touchfile

run: venv
	. venv/bin/activate; python ./sendtransaction.py

clean:
	rm -rf venv
	find -iname "*.pyc" -delete
