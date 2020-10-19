FROM python:3.8.5

COPY . /opt/toms_calculator
WORKDIR /opt/toms_calculator
RUN pip install --upgrade pip  && pip install  -r /opt/toms_calculator/requirements.txt
EXPOSE 8000
