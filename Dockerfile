FROM python:3.11

ENV PYTHONUNBUFFERED=1

ARG WORKDIR=/wd
ARG USER=user

WORKDIR ${WORKDIR}

RUN useradd --system ${USER} && \
    chown --recursive ${USER} ${WORKDIR}

RUN apt update && apt upgrade -y

COPY --chown=${USER} requirements.txt requirements.txt

RUN pip install --upgrade pip && \
    pip install --requirement requirements.txt

COPY --chown=${USER} ./main.py main.py
COPY --chown=${USER} ./task_is task_is
COPY --chown=${USER} ./tasks tasks

USER ${USER}

#docker run -i --entrypoint /bin/bash -t dz_5-app
ENTRYPOINT ["python", "main.py"]