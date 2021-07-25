FROM node:14.17.3-alpine as builder

# Install dependencies
COPY react/test/package*.json /tmp/test/
COPY react/subtest/package*.json /tmp/subtest/
COPY react/baebug/package*.json /tmp/baebug/

# Install test dependencies & build
WORKDIR /tmp/test/
RUN npm ci
COPY react/test/ /tmp/test/
RUN npm run build

# Install subtest dependencies & build
WORKDIR /tmp/subtest/
RUN npm ci
COPY react/subtest/ /tmp/subtest/
RUN npm run build

# Install baebug dependencies & build
WORKDIR /tmp/baebug/
RUN npm ci
COPY react/baebug/ /tmp/baebug/
RUN npm run build

# Build source code
# COPY react/test/ /tmp/test/
# COPY react/subtest/ /tmp/subtest/
# COPY react/baebug/ /tmp/baebug/

# RUN npm run build

FROM nginx:stable-alpine

COPY ./nginx.conf /etc/nginx/
COPY ./sites-available/ /etc/nginx/sites-available/

COPY --from=builder /tmp/test/build/ /usr/share/nginx/html/test/
COPY --from=builder /tmp/subtest/build/ /usr/share/nginx/html/subtest/
COPY --from=builder /tmp/baebug/build/ /usr/share/nginx/html/baebug/

CMD ["nginx", "-g", "daemon off;"]

EXPOSE 80
