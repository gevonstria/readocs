# GET BASE IMAGE
FROM python:3.8

# UPDATE PIP
RUN pip install --upgrade pip

# INSTALL APP requirements.txt (python modules)
COPY ./readocs /readocs
WORKDIR /readocs
RUN pip install -r requirements.txt

# Prepare gunicorn log file
RUN touch /var/log/gunicorn.access.log
RUN chmod a+rwx /var/log/gunicorn.access.log
RUN touch /var/log/gunicorn.error.log
RUN chmod a+rwx /var/log/gunicorn.error.log

# RUN DJANGO APP
CMD ["gunicorn", "--config", "gunicorn.conf.py", "readocs.wsgi"]
EXPOSE 8080