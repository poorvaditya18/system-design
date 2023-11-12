// Server 1 config
const express = require("express");
const bodyParser = require("body-parser");
const ApiRoutes = require("./routes/index.js");

const router = express.Router();

const PORT = 3001;

const server_setup = async () => {
  const app = express();

  // initations body parser
  app.use(bodyParser.json());
  app.use(bodyParser.urlencoded({ extended: true }));

  app.use("/", ApiRoutes);

  // start server1
  app.listen(PORT, async () => {
    console.log("Server 2 started on PORT", PORT);
  });
};

server_setup();
