FROM python:3.9.15
FROM python:3.9.15-alpine as base
FROM base as builder
COPY requirements.txt /requirements.txt
RUN pip install --user -r /requirements.txt

FROM base
# copy only the dependencies installation from the 1st stage image
RUN mkdir /app && mkdir -p /app/json && mkdir -p /app/templates && mkdir -p /app/util
COPY --from=builder /root/.local /root/.local
COPY fserver.py /app
COPY json/ /app/json
COPY templates/ /app/templates
COPY util/ /app/util
WORKDIR /app
ENV PATH=/home/app/.local/bin:$PATH
CMD ["python","fserver.py"]