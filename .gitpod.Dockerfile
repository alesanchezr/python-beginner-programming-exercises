FROM gitpod/workspace-full:latest

USER gitpod

RUN pip3 install pytest==4.4.2 mock pytest-testdox && npm i learnpack@0.0.4 learnpack-python -g
