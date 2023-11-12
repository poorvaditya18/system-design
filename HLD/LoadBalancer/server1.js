// Server 1 config
const express = require("express");
const bodyParser = require("body-parser");
const ApiRoutes = require("./routes/index.js");

const axios = require("axios");
const router = express.Router();

const PORT = 3000;
let isRegister = 0;
let isAlive = 1; // based on usecase we can change this parameter

const server_setup = async () => {
  const app = express();

  // initations body parser
  app.use(bodyParser.json());
  app.use(bodyParser.urlencoded({ extended: true }));

  app.use("/", ApiRoutes);

  // start server1
  app.listen(PORT, async () => {
    console.log("Server 1 started on PORT", PORT);
    app.post("/heartbeat", heartbeat);
    app.post("/registration-response", register_response);
    console.log("Registering server with load balancer....");
    try {
      const payload = {
        server_ip: "127.0.0.1",
        server_port: 3000,
        request_type: "Register",
        isAlive: isAlive,
      };
      await axios.post("http://127.0.0.1:5001", payload);
    } catch (err) {
      console.log("Failed to register server . Error: " + err);
    }
  });
};

server_setup();

// heart beat
const heartbeat = async (req, res) => {
  try {
    console.log("checking heartbeat status of server .....");
    // TODO : actual logic to check heartbeat of server
    console.log("Health Status", isAlive);
    const response = {
      server_ip: "127.0.0.1",
      server_port: 3000,
      isAlive: isAlive,
    };
    return res.status(200).json({
      message: `server1 is healthy.`,
      data: response,
      success: true,
      err: {},
    });
  } catch (error) {
    return res.status(500).json({
      message: "Something went wrong checking server health.",
      data: {},
      success: false,
      err: error,
    });
  }
};

const register_response = async (req, res) => {
  try {
    const response = req.body;
    if (response.data.isRegistered === 1) {
      isRegister = response.data.isRegistered;
      console.log("server1 successfully registered with load balancer.");
    }
    return res.status(200).json({
      message: `server1 registeration completed`,
    });
  } catch (err) {
    console.log("Failed to register server . Error: " + err);
  }
};
