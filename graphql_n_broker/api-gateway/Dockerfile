FROM node:14

COPY ./nodejs /usr/src/app

WORKDIR /usr/src/app

RUN rm -rf node_modules && npm install

EXPOSE 80

CMD [ "node", "index.js" ]
