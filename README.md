# Smart-Hydroponic-Project

---
Code to be uploaded
---
This is a project to build a smart hydroponic system that is powered by solar panels. 

The project contains 3 parts: solar power system, farming part, and a control center. We use off-grid solar panels to provide electricity for the whole system, a water pump that is connected to the control center and supply water according to the signals that the control center sends. I only focus on the control center here.

We used a single board controller, Raspberry Pi to be specific in this project. The Pi is connected to a relay board which connects to the waterpump and controls how frequent it should pump water to the farming part. There are sesnsors connected to the Pi that record these data: air temperature, water temperature, humidity. Depending on the data that the sensors send back, the Pi decides on the frequency. 

There are 3 programming needs:
1. Smart control of the water pump: this is to read the sensor data and control the relay. We used a Python script. 
2. Data storage: all the data the sensors recorded are being sent to a data warehouse for later analysis. In this project we used Amazon DynamoDB.
3. Dashobard: we build an online dashboard to present the live data collected by sensors and provide the possibility to remotely control the waterpump if we want. The script is coded in JavaScript. In this project we used an online Node.js application on IBM cloud.

Improvements:
A. add more sensors to collect more ambient data such as lightness.
B. with more data, we hope to optimise the #1 script and make it smarter.
C. we're hoping to add illuminator to the farming part and have it also controlled by the Pi
