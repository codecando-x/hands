# hands

A command line utility to inspect the hierarchy of keys and values of a json structure.

Usage:
```
user@base:~/dev/hands$ python3 hands.py -h
usage: hands.py [-h] [--get GET] [--source SOURCE] [--separator SEPARATOR] [--values] [--obj_keys] [--py_keys] [--query QUERY] [--stats STATS] [--no-wrap NO_WRAP]

optional arguments:
  -h, --help            show this help message and exit
  --get GET             get a flattened key's value
  --source SOURCE       path to json file
  --separator SEPARATOR
                        separator to use for obj_keys (default : . )
  --values              show values
  --obj_keys            show flatened access keys
  --py_keys             show python statements as access keys
  --query QUERY         for later
  --stats STATS         for later
  --no-wrap NO_WRAP     for later
```

With file:
```
user@base:~/dev/hands$ python3 hands.py --source test.json --get "X.rows.0.elements.5.status"
OK
```

Getting a specific value using the flattened key:
```
user@base:~/dev/hands$ cat test.json | python3 hands.py --get "X.rows.0.elements.5.status"
OK
```

Printing the flattened keys and values:
```
user@base:~/dev/hands$ cat test.json | python3 hands.py --obj_keys --values
{
    "X.destination_addresses.0": "Washington, DC, USA",
    "X.destination_addresses.1": "Philadelphia, PA, USA",
    "X.destination_addresses.2": "Santa Barbara, CA, USA",
    "X.destination_addresses.3": "Miami, FL, USA",
    "X.destination_addresses.4": "Austin, TX, USA",
    "X.destination_addresses.5": "Napa County, CA, USA",
    "X.origin_addresses.0": "New York, NY, USA",
    "X.rows.0.elements.0.distance.text": "227 mi",
    "X.rows.0.elements.0.distance.value": "365468",
    "X.rows.0.elements.0.duration.text": "3 hours 54 mins",
    "X.rows.0.elements.0.duration.value": "14064",
    "X.rows.0.elements.0.status": "OK",
    "X.rows.0.elements.1.distance.text": "94.6 mi",
    "X.rows.0.elements.1.distance.value": "152193",
    "X.rows.0.elements.1.duration.text": "1 hour 44 mins",
    "X.rows.0.elements.1.duration.value": "6227",
    "X.rows.0.elements.1.status": "OK",
    "X.rows.0.elements.2.distance.text": "2,878 mi",
    "X.rows.0.elements.2.distance.value": "4632197",
    "X.rows.0.elements.2.duration.text": "1 day 18 hours",
    "X.rows.0.elements.2.duration.value": "151772",
    "X.rows.0.elements.2.status": "OK",
    "X.rows.0.elements.3.distance.text": "1,286 mi",
    "X.rows.0.elements.3.distance.value": "2069031",
    "X.rows.0.elements.3.duration.text": "18 hours 43 mins",
    "X.rows.0.elements.3.duration.value": "67405",
    "X.rows.0.elements.3.status": "OK",
    "X.rows.0.elements.4.distance.text": "1,742 mi",
    "X.rows.0.elements.4.distance.value": "2802972",
    "X.rows.0.elements.4.duration.text": "1 day 2 hours",
    "X.rows.0.elements.4.duration.value": "93070",
    "X.rows.0.elements.4.status": "OK",
    "X.rows.0.elements.5.distance.text": "2,871 mi",
    "X.rows.0.elements.5.distance.value": "4620514",
    "X.rows.0.elements.5.duration.text": "1 day 18 hours",
    "X.rows.0.elements.5.duration.value": "152913",
    "X.rows.0.elements.5.status": "OK",
    "X.status": "OK"
}
```

Grabbing only the python code access statements:
```
user@base:~/dev/hands$ cat test.json | python3 hands.py --py_keys
[
    "X['destination_addresses'][0]",
    "X['destination_addresses'][1]",
    "X['destination_addresses'][2]",
    "X['destination_addresses'][3]",
    "X['destination_addresses'][4]",
    "X['destination_addresses'][5]",
    "X['origin_addresses'][0]",
    "X['rows'][0]['elements'][0]['distance']['text']",
    "X['rows'][0]['elements'][0]['distance']['value']",
    "X['rows'][0]['elements'][0]['duration']['text']",
    "X['rows'][0]['elements'][0]['duration']['value']",
    "X['rows'][0]['elements'][0]['status']",
    "X['rows'][0]['elements'][1]['distance']['text']",
    "X['rows'][0]['elements'][1]['distance']['value']",
    "X['rows'][0]['elements'][1]['duration']['text']",
    "X['rows'][0]['elements'][1]['duration']['value']",
    "X['rows'][0]['elements'][1]['status']",
    "X['rows'][0]['elements'][2]['distance']['text']",
    "X['rows'][0]['elements'][2]['distance']['value']",
    "X['rows'][0]['elements'][2]['duration']['text']",
    "X['rows'][0]['elements'][2]['duration']['value']",
    "X['rows'][0]['elements'][2]['status']",
    "X['rows'][0]['elements'][3]['distance']['text']",
    "X['rows'][0]['elements'][3]['distance']['value']",
    "X['rows'][0]['elements'][3]['duration']['text']",
    "X['rows'][0]['elements'][3]['duration']['value']",
    "X['rows'][0]['elements'][3]['status']",
    "X['rows'][0]['elements'][4]['distance']['text']",
    "X['rows'][0]['elements'][4]['distance']['value']",
    "X['rows'][0]['elements'][4]['duration']['text']",
    "X['rows'][0]['elements'][4]['duration']['value']",
    "X['rows'][0]['elements'][4]['status']",
    "X['rows'][0]['elements'][5]['distance']['text']",
    "X['rows'][0]['elements'][5]['distance']['value']",
    "X['rows'][0]['elements'][5]['duration']['text']",
    "X['rows'][0]['elements'][5]['duration']['value']",
    "X['rows'][0]['elements'][5]['status']",
    "X['status']"
]
```
