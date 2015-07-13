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


### ``GET /events``
| Parameter | Description                           |
|-----------|---------------------------------------|
| start     | The number of the first row to return |
| num_rows  | The number of rows to return          |

Return event data, start from row ``start`` and containing ``num_rows`` rows, in the format:

```
{
  "events": [
    {
      "data": "34.9, 2016.0, 0, 2103.0", 
      "device": "53ff6d066667574824460967", 
      "id": 3
    }, 
    {
      "data": "29.2, 3331.0, 0, 2091.0", 
      "device": "53ff6d066667574831402467", 
      "id": 4
    }, 
    {
      "data": "35.7, 2020.0, 0, 2102.0", 
      "device": "53ff6d066667574824460967", 
      "id": 5
    }
  ]
}
```
