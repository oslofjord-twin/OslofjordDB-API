# Dockerfile for api-web-server/apollo-server

FROM node:18.16.0-alpine3.17
RUN mkdir -p /opt/app
WORKDIR /opt/app
COPY api/package.json .
COPY api/package-lock.json .
RUN npm install
COPY api/src/ .
EXPOSE 3000:3000
RUN npm run build
ENTRYPOINT ["npm", "start"]