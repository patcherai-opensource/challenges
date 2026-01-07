FROM python
RUN pip3 --no-cache-dir install flask gunicorn
WORKDIR /srv
COPY jar.py pickle.jpg ./
ENV FLAG="PLACEHOLDER_FLAG"
EXPOSE 5000
USER nobody
CMD python jar.py
