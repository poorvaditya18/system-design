// Server 1 config
const express = require("express");
const bodyParser = require("body-parser");
const ApiRoutes = require("./routes/index.js");
const axios = require("axios");
const router = express.Router();

let PORT = 3000;
let isRegister = false;
let isAlive = true; // based on usecase we can change this parameter

const server_setup = async () => {
  const app = express();

  // initations body parser
  app.use(bodyParser.json());
  app.use(bodyParser.urlencoded({ extended: true }));

  app.use("/", ApiRoutes);

  // start server1
  app.listen(PORT, async () => {
    console.log("Server 1 started on PORT", PORT);

    // to register server : send initial register request to  loadbalancer  at "localhost:5000/register"
    try {
      const payload = {
        server_id: "1",
        server_ip: "127.0.0.1",
        server_port: 3000,
        data: {
          isRegister: isRegister,
          isAlive: isAlive,
        },
      };
      // send to load balancer at ip : localhost:5000
      const response = await axios.post("http://127.0.0.1:5001", payload);
      console.log(
        "Server registred with loadbalancer successfully :",
        response.data
      );
      isRegister = response.data.isRegister;
    } catch (err) {
      console.log("Failed to register server . Error: " + err);
    }
  });
};

server_setup();
