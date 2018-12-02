# Smart-Aeroponic-Project

---
The rest of the scripts are to be uploaded
---
This is a project to build a solar-powered smart hydroponic system that collect data including temperature, humidity, PH value, conductivity, lighting, in order to adjust the lighting, water pumping frequency, and nutrients. 

The project contains 3 parts: solar power system, gardening part, and a control center. We use off-grid solar panels to power for the whole system, a water pump that is connected to the control center and supply water according to the signals that the control center sends. I only focus on the control center here.

We used a single board controller, Raspberry Pi to be specific in this project. The Pi is connected to a relay board which connects to a waterpump that controls how frequent water is pumped to the gardening part, a nutrient solution pump that pumps nutrient according to the PH value/ TDS value, and lights that turn on when it's too dark. There are sesnsors connected to the Pi that record these data: air temperature, water temperature, humidity, PH value, TDS value Depending on the data that the sensors send back, the Pi decides on the frequency. 

There are 3 programming needs:
1. Control of the water pump, nutrient pump, and lights: this is to read the sensor data and control the relay. We used a Python script. 
2. Data storage: all the data the sensors recorded are being sent to a data warehouse for later analysis. In this project we used Amazon DynamoDB.
3. Dashobard: we build an online dashboard to present the live data collected by sensors and provide the possibility to remotely control the waterpump if we want. The script is coded in JavaScript. In this project we used an online Node.js application on IBM cloud.

Further Improvements to make:
A. add more sensors to collect more data such as a camera to monitor how the growth of the plants.
B. with more data, we hope to optimise the #1 script and find the optimised PH value, lighting, and so forth.
