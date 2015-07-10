# Particle logging API
A simple, Python-powered web API for accessing stored Particle.io data from our VPS.

## Current endpoints

### ``GET /``
Display welcome message and database version.

### ``GET /devices``
Return all devices that the database knows of, in the format:
```
{
  "devices": [
    {
      "id": "53ff6d066667574831402467", 
      "name": "Sensor Unit"
    }, 
    {
      "id": "53ff6d066667574824460967", 
      "name": "Dummy Sensor Device"
    }
  ]
}
```
