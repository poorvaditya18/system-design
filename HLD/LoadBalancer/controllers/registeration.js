//signup
const signup = async (req, res) => {
  try {
    console.log("Registering User in Database....");
    const response = {
      email: req.body.email,
      password: req.body.password,
      name: req.body.name,
    };
    console.log("Successfully registered in Database.");
    return res.status(200).json({
      message: "Successfully signed up user",
      data: response,
      success: true,
      err: {},
    });
  } catch (error) {
    return res.status(500).json({
      message: "Something Went Wrong. Not able to register user.",
      data: {},
      success: false,
      err: error,
    });
  }
};

module.exports = {
  signup,
};
