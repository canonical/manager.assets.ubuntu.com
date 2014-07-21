rebuild-dependencies-cache:
	rm -rf pip-cache
	bzr branch lp:~webteam-backend/assets-manager/dependencies pip-cache
	pip install --exists-action=w --download pip-cache/ -r requirements.txt
	bzr commit pip-cache/ --unchanged -m 'automatically updated partners requirements'
	bzr push --directory pip-cache lp:~webteam-backend/assets-manager/dependencies
	rm -rf pip-cache src
