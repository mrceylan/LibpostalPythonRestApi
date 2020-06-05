# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 4444

RUN apt-get update && apt-get install -y \
    curl autoconf automake libtool python-dev pkg-config build-essential git libsnappy-dev

RUN  git clone https://github.com/openvenues/libpostal 
COPY ./*.sh /libpostal/
WORKDIR /libpostal

RUN ./build_libpostal.sh

# Install pip requirements
ADD requirements.txt .
RUN python -m pip install -r requirements.txt


WORKDIR /app
ADD . /app

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN useradd appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn",  "api:app"]
