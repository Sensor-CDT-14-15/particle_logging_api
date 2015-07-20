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
| Parameter | Description                            |
|-----------|----------------------------------------|
| start     | The number of the first row to return  |
| num_rows  | The number of rows to return           |
| [device]  | The device id for which to return rows |

Return event data, start from ``start_date`` and ending on ``end_date`` (for device ``device``, if specified), in the format below.

or

| Parameter  | Description                            |
|------------|----------------------------------------|
| start_date | The date of the first row to return    |
| end_date   | The date of the last row to return     |
| device     | The device id for which to return rows |

Return event data, start from row ``start`` and containing ``num_rows`` rows for device ``device``, in the format below.

```
{
  "events": [
    {
      "data": "28.6, 3331.0, 0, 2107.0", 
      "device": "53ff6d066667574831402467", 
      "id": 4, 
      "timestamp": "2015-06-24 16:42:42"
    }, 
    {
      "data": "35.5, 2016.0, 0, 2102.0", 
      "device": "53ff6d066667574824460967", 
      "id": 5, 
      "timestamp": "2015-06-24 16:42:50"
    }, 
    {
      "data": "28.6, 3331.0, 0, 2093.0", 
      "device": "53ff6d066667574831402467", 
      "id": 6, 
      "timestamp": "2015-06-24 16:42:50"
    }
  ]
}
```
