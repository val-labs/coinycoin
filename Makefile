all: .ve2 .ve3
	@echo '# To set up your environment,'
	@echo '# Paste this into a prompt:'
	@echo 'eval "$$(make env)"'
go:
	$(MAKE) lc1
env:
	@echo . .ve2/bin/activate
	@echo export PYTHONPATH=`pwd`
	@echo '# eval "$$(make env)"'
.ve2:
	virtualenv -p python2 .ve2
	.ve2/bin/pip install -r requirements.txt
.ve3:
	virtualenv -p python3 .ve3
	.ve3/bin/pip install -r requirements.txt
c1:
	mkdir -p c1/g c1/t c1/n
	cp profile/* c1
	tree c1
lc1: c1
	. c1/env.sh start 1234
sc1:
	. c1/env.sh stop
clean:
	rm -fr c1 he* pid
	find . -name \*.pyc | xargs rm
	tree .
realclean: clean
	rm -fr .ve?
