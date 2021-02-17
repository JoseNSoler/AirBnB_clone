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


## Console Commands

Following the table, this could be a posible time-line execution demonstrating the use of the console

The principle execution file has already all permission needed, with a simple execution in linux environment "./<filename>", the console will start
```
hbnb@ubuntu:~/AirBnB$ ./console.py
```

If is the first time you run the console, you will probably don't see any content in <file.json>, or even the existing of this file

**all**: Prints all string representation of all instances based or not on the class name. ie: "$ all BaseModel" or "$ all"
```
(hbnb) all MyModel
** class doesn't exist **
```

**show**: Prints the string representation of an instance based on the class name and id "$ show BaseModel 1234-1234-1234"
```
(hbnb) show BaseModel
** class doesn't exist **
```

**create**:
Creates a new base *BaseModel*, or any kind of his instances: *City*, *Amenity*, *Place*, *Review*, *State*, *User* And prints on screen his unique id (uuid4) for a future reffer ; and at the same time, creates a file <file.json> where we could store, manage and save all instances created in the process. ie: "$ create BaseModel"

```
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c5590
______________________________________
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
______________________________________
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
```

**update**: Updates an instance based on the class name and id by adding or updating attribute (save the change into the <file.json>). ie: "$ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"

```
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
______________________________________
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
```

**destroy**: destroys an object by his unique id, stored in <file.json>. ie: "$ destroy BaseModel 1234-1234-1234"

```
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
______________________________________
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
```


## Maintainers

[@JoseNsoler](https://github.com/JoseNSoler).
[@DiegoCol93](https://github.com/DiegoCol93).


### Contributors

This project exists thanks to all the people who contribute. 
<a href="https://github.com/DiegoCol93/AirBnB_clone/graphs/contributors"><img src="https://i.ibb.co/Km8RXWP/Selection-042.png" /></a>

alt=""



<h1 align="center">
   <img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210216%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210216T203255Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6039724420d1de1da1b5d6a9f0b8a01a4f94b47946cdc750dc608c5454213028" alt="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210216%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210216T203255Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6039724420d1de1da1b5d6a9f0b8a01a4f94b47946cdc750dc608c5454213028" title="AirBnB Console Holberton By JoseNSoler and Diego Lopez" />
</h1>


## License

[MIT](LICENSE)
