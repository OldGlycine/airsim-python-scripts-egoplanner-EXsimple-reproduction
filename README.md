# airsim-python-scripts-egoplanner-EXsimple-reproduction
python version = 3.7.12

requirements: numpy airsim scipy (newest version)

settings.json

{
    "SeeDocsAt": "https://microsoft.github.io/AirSim/settings/",
    "SettingsVersion": 1.2,
 
    "SimMode": "Multirotor",
 
     "Vehicles": {
        "Drone1": {
            "VehicleType": "simpleflight",
            "MoveControlMinDistance": 0.1, 
            "AutoCreate": true,
            "Sensors": {
                "LidarSensor1": {
                    "SensorType": 6,
                    "Enabled" : true,
                    "NumberOfChannels": 32,
                    "RotationsPerSecond": 10,
                    "PointsPerSecond": 100000,
                    "X": 0, "Y": 0, "Z": -1.0,
                    "Roll": 0, "Pitch": 0, "Yaw" : 0,
                    "VerticalFOVUpper": 20,
                    "VerticalFOVLower": -20,
                    "HorizontalFOVStart": -20,
                    "HorizontalFOVEnd": 20,
                    "DrawDebugPoints": true,
                    "DataFrame": "SensorLocalFrame"
                },
                "LidarSensor2": {
                   "SensorType": 6,
                    "Enabled" : true,
                    "NumberOfChannels": 4,
                    "RotationsPerSecond": 10,
                    "PointsPerSecond": 10000,
                    "X": 0, "Y": 0, "Z": 0,
                    "Roll": 0, "Pitch": 0, "Yaw" : 0,
                    "VerticalFOVUpper": -15,
                    "VerticalFOVLower": -25,
                    "DrawDebugPoints": false,
                    "DataFrame": "SensorLocalFrame"
                }
            }
        }
    }
}
