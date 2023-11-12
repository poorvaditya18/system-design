// setup initial communication with Load balancer
const axios = require('axios');
/* 
Register Request -->
    {
        server_id : 1, 
        destination_id: 2 , (Assuming Destination of load balancer as 2 )
        data:
        {
            isRegister : False 
        }
    } 
*/
const register_server = async () => {
  try {
    const payload = {
      server_id: "1",
      server_ip:"127.0.0.1",
      server_port:3000,
      data: {
        isRegister: "False",
      },
    };
    // send to load balancer at ip : localhost:5000
    const response = await axios.post("http://localhost:5001",payload);
    console.log("Server registration successful:", response.data);
  } catch (err) {
    console.log("Failed to register server . Error: " + err)
  }
};

