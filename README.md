<h1 align="center">
   <img src="https://i.ibb.co/VCvKg3g/Selection-041.png" alt="AirBnb Console Image" title="AirBnB Console  By JoseNSoler and Diego Lopez" />
</h1>
<p align="center">  
<a href="https://github.com/DiegoCol93/AirBnB_clone"><img src="https://api.codacy.com/project/badge/Coverage/8a941e0f57c047c8a481f4854666b42d"></a>
<a href="https://github.com/DiegoCol93/AirBnB_clone"><img src="https://travis-ci.org/teles/array-mixer.svg?branch=master"></a>
<a href="https://www.npmjs.com/package/array-mixer"><img src="https://img.shields.io/badge/python-3.4.3-blue.svg"></a>
 <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/license-MIT-blue.svg"></a>
 <a href="https://discord.gg/CeMkZpdZ"><img src="https://img.shields.io/discord/308323056592486420?logo=discord"
            alt="chat on Discord"></a>
</p>

<p align="center">
  This repository contains the <strong>AirBnB</strong> clone source code.
  AirBnB clone <strong>V1.0</strong> is a functional console prepared to store, analyze and modify a JSON database.
 
Powerful and easy to use.
</p>


Folder hierarchy
----------------------------------

```Python
AirBnB
├── models
│   ├── engine
│   │   └── file_storage.py
│   │
│   ├── amenity.py
│   ├── base_model.py
│   ├── city.py
│   ├── place.py
│   ├── review.py
│   ├── state.py
│   └── user.py
│
├── tests
│   ├── test_models
│   │   ├── test_engine 
│   │   │   └── test_file_storage.py
│   │   │
│   │   └── test_base_model.py
│   │
│   └── test_console.py
│
└── console.py
```

## Storage
All data will be analyzed, stored and modified in the filename <file.json>


## Console
**[V1.0]:**
The console AirBnB Clone is a line interpreter that allows the user, interact directly from a database <file.json>, editing, creating and removing objects, attributtes and values from the own object

**Usage**
This console can be run both interactively and non-interactively. For a better image of how to do this, here is a example of both methods

**Interactive mode**
```Python
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) 
(hbnb) 
(hbnb) quit
$
```


**Non-interactive mode**
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
(hbnb) 
$
```

## Console Commands



## Base and objectsd properties 

|             	| Public Instance Attributes 	| Public Instance Methods                 	| Public Class Attributes                                                                                                	| Private Class Attributes 	|
|-------------	|----------------------------	|-----------------------------------------	|------------------------------------------------------------------------------------------------------------------------	|--------------------------	|
| BaseModel   	|```id created_at updated_at ```  	|``` save to_dict```                            	|                                                                                                                        	|                          	|
| FileStorage 	|                            	|```all new save reload (n)delete (n)update ```	|                                                                                                                        	|```__file_path __objects ```   	|
| User        	|```Inherits from BaseModel ```   	|                                         	|```email password first_name last_name ```                                                                                   	|                          	|
| State       	|```Inherits from BaseModel ```   	|                                         	|```name                                                                                                                 ```  	|                          	|
| City        	|```Inherits from BaseModel```    	|                                         	|```state_id name```                                                                                                          	|                          	|
| Amenity     	|```Inherits from BaseModel```    	|                                         	|```name ```                                                                                                                  	|                          	|
| Place       	|```Inherits from BaseModel```    	|                                         	|```city_id user_id name description number_rooms number_bathrooms max_guest price_by_night latitude longitude amenity_ids``` 	|                          	|
| Review      	|```Inherits from BaseModel```    	|                                         	|```place_id user_id text ```                                                                                                 	|     ""                       	|



## Maintainers

[@JoseNsoler](https://github.com/JoseNSoler).
[@DiegoCol93](https://github.com/DiegoCol93).


### Contributors

This project exists thanks to all the people who contribute. 
<a href="https://github.com/DiegoCol93/AirBnB_clone/graphs/contributors"><img src="https://i.ibb.co/Km8RXWP/Selection-042.png" /></a>


## License

[MIT](LICENSE)
