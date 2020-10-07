FROM node:12-slim
COPY . /ui/
WORKDIR /ui
# RUN npm install
#ENTRYPOINT ["npm", "start"]
RUN npm install && npm run build --prod
RUN npm install -g serve

EXPOSE 3000
ENTRYPOINT ["serve", "-s", "build", "-l", "3000"]
