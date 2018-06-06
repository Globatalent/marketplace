FROM node:9.11.1-alpine
WORKDIR /app
COPY ./frontend /app
ADD ./frontend/package.json /app/package.json
ADD ./frontend/package.json /tmp/package.json
RUN cd /tmp && npm install
RUN cp -a /tmp/node_modules /app/

COPY ./compose/local/frontend/start.sh /start.sh
RUN sed -i 's/\r//' /start.sh
RUN chmod +x /start.sh
