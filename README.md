![vettom.pages.dev banner](https://vettom-images.s3.eu-west-1.amazonaws.com/logo/vettom-banner.jpg)

# Task in hand

## Build and deploy python flask app to container

# CI Tasks
- Up on pull
  - pylint
  - test app
  - build container
  - upload to repo


# Generate requirement.txt
```bash
python -m venv venv
source venv/bin/activate
pip install flask
pip freeze > requirements.txt
deactivate
```

# What I am trying
 - Build image with git hub action and publish to GHCR private
 - Build Helm chart to deploy this app
 - Package Helm chart and push auto with GH Action
 - Automate Image tag
 - Automate Helm chart image tag


`gh auth token | helm registry login ghcr.io -u propyless --password-stdin`
