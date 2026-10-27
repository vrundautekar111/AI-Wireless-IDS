AI-Based Wireless Network Intrusion Detection System




PROJECT OVERVIEW
   
The AI-Based Wireless Network Intrusion Detection System (WIDS) is a machine-learning-based cybersecurity application designed to identify potentially suspicious activity in wireless network traffic.

The system analyzes wireless traffic characteristics such as packet rate, deauthentication rate, failed authentication attempts, unique source count, signal strength, connection duration, and retry rate. A Random Forest classification algorithm is used to classify traffic as either Normal Traffic or Potential Intrusion. 

The project includes a Flask-based web dashboard where users can enter network traffic parameters and receive an AI-generated security classification along with normal and intrusion probabilities.

OBJECTIVES 
Detect potentially suspicious wireless network traffic using machine learning. 
Build an AI-based classification model for wireless intrusion detection. 

Analyze important network traffic characteristics.
Provide intrusion and normal-traffic probability scores.
Develop a simple web-based security monitoring interface. 
Demonstrate the use of machine learning in cybersecurity.
 
MACHINE LEARNING

The project uses the Random Forest Classifier because it can handle multiple numerical features and provides reliable classification performance.

The model uses the following features:

Packet Rate
Deauthentication Rate
Failed Authentication Attempts
Unique Source Count
Average Signal Strength
Connection Duration
Retry Rate

The target classes are:

0 → Normal Traffic
1 → Potential Intrusion

TECHNOLOGIES USES
Python
NumPy
Pandas
Scikit-learn
Random Forest
Joblib
Flask
HTML5
CSS3
JavaScript
Future Enhancements

Future versions can include:

Real-time authorized wireless network telemetry
Real-time intrusion monitoring
Attack-type classification
Database logging
Security alert notifications
Interactive traffic graphs
Network-device monitoring
Model retraining
Advanced deep-learning models
Authentication and administrator dashboard
Deployment using Docker and cloud infrastructure
