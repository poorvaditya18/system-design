// routes configuration
const express = require("express");
const RegisterationController = require("../controllers/registeration.js");
const router = express.Router();

// sigup route
router.post("/signup", RegisterationController.signup);

module.exports = router;
