FROM python:3.9-slim AS venv_image
COPY requirements.txt .
RUN pip install --user -r /requirements.txt

FROM python:3.9-slim AS code_image
COPY --from=venv_image /root/.local /root/.local
RUN mkdir /app && mkdir -p /app/json && mkdir -p /app/templates && mkdir -p /app/util
COPY flaskserver.py /app
COPY json/ /app/json
COPY templates/ /app/templates
COPY util/ /app/util
WORKDIR /app
ENV PATH=/root/.local/bin:$PATH
CMD ["python","flaskserver.py"]
