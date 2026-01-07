FROM nginx:alpine

COPY index.html /usr/share/nginx/html/index.html.template
COPY start.sh /start.sh
RUN chmod +x /start.sh

CMD ["/start.sh"]
