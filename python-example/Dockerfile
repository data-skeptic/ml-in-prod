FROM lbosqmsft/mssql-python-pyodbc
LABEL maintainer="Kyle Polich"
RUN apt-get update
RUN apt-get install bash-completion

# See https://jpetazzo.github.io/2013/12/01/docker-python-pip-requirements/ for an explanation of the duplication below with requirements.txt
RUN pip install xgboost
RUN pip install azure-storage-blob
RUN pip install fastparquet
RUN pip install Flask
RUN pip install Flask-RESTful
RUN pip install jupyter
RUN pip install matplotlib
RUN pip install numpy
RUN pip install pandas
RUN pip install pandocfilters
RUN pip install pyarrow
RUN pip install python-dateutil
RUN pip install requests
RUN pip install scikit-learn
RUN pip install scipy
RUN pip install sklearn
RUN pip install snappy
RUN pip install xmltodict
RUN pip install idna
RUN pip install ijson
RUN pip install ipython
RUN pip install ipywidgets
RUN pip install jupyterlab
RUN pip install notebook
RUN pip install python_dateutil
RUN pip install schedule
RUN pip install widgetsnbextension
RUN pip install json_tricks
RUN pip install boto3

ENV SHELL=/bin/bash
RUN mkdir /util/
WORKDIR /files
COPY startup.sh /util/startup.sh

# If you find this build to be slow at the next step, update the install statements above so that they get cached by docker
COPY requirements.txt /files
RUN pip install -r /files/requirements.txt

COPY *.py /app/
COPY api/*.py /app/api/
COPY api/*.htm /app/api/
EXPOSE 8888 9988
ENTRYPOINT ["sh", "/util/startup.sh"]