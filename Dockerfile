FROM python:3.7.2-slim

ENV DEBIAN_FRONTEND noninteractive

# Install the requirements
RUN pip install pandas scikit-learn Flask requests gunicorn

# Setup file in container
RUN mkdir /app
WORKDIR /app
COPY api.py /app
COPY model.p /app

CMD ["/usr/local/bin/gunicorn", "-b", "0.0.0.0:5000", "--pythonpath", "/app", "api:app"]