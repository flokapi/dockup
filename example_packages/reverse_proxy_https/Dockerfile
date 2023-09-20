

FROM nginx:latest

COPY ./default.conf /etc/nginx/conf.d/default.conf

COPY ./fullchain.pem /etc/ca-certificates/fullchain.pem
COPY ./privkey.pem /etc/ca-certificates/privkey.pem
COPY ./options-ssl-nginx.conf /etc/ca-certificates/options-ssl-nginx.conf
COPY ./ssl-dhparams.pem /etc/ca-certificates/ssl-dhparams.pem

RUN mkdir /home/nginxcfg
