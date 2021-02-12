#!/usr/bin/python3
'''Module console '''

import cmd
from models.base_model import BaseModel
from models.__init__ import storage
import models


class HBNBCommand(cmd.Cmd):
    """ command console for managing and interacting with the AirBnB clone """

    prompt = "(hbnb) "  # <--- Defines the look of the prompt

    # Definition override for handling ENTER with an empty line.--------------|
    def emptyline(self):
        pass

    # Implementations 0.1-----------------------------------------------------|
    #                                                                         |
    # do_create - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
    def do_create(self, line):
        """Create a new BaseModel instance.\n"""
        if line:
            if line == 'BaseModel':
                x = BaseModel()
                models.storage.new(x)
                models.storage.save()
                print(x.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    # do_create - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
    def do_show(self, line):
        """ Shows the BaseModel instance given its id. """
        if line:
            args = line.split(" ")
            if args[0] == 'BaseModel':
                if len(args) > 1:
                    string = "BaseModel." + "{}".format(args[1])
                    models.storage.reload()
                    dicto = models.storage.all()
                    switch = False
                    for obj_id, obj in dicto.items():
                        if string == obj_id:
                            print(obj)
                            switch = True
                    if switch is False:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    # do_destroy - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -|
    def do_destroy(self, line):
        """ Deletes an instance of BaseModel given its id. """
        if line:
            args = line.split(" ")
            if args[0] == 'BaseModel':
                if args[1]:
                    if models.storage.delete(args[1]) is False:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    # do_destroy - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -|
    def do_all(self, line):
        if line == "BaseModel" or line == "":
            dicto = models.storage.all()
            list_of_strings = []
            for obj_id, obj in dicto.items():
                list_of_strings.append(obj.__str__())
            print(list_of_strings)
        else:
            print("** class doesn't exist **")

    # do_update - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
    def do_update(self, line):
        pass

    # Implementations 0.0.1---------------------------------------------------|
    #                                                                         |
    # do_quit - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
    def do_quit(self, line):
        """Exits the program.\n"""
        return True

    # do_EOF - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -|
    def do_EOF(self, line):
        """Exits the program.\n"""
        return True

if __name__ == '__main__':

    green = "\033[92m"
    reset = "\033[0m"

    hlp = green + "help" + reset
    qut = green + "quit" + reset
    title_string = green + "Welcome to the hbnb C.L.I" + reset

    intro_string = "._______________________________.\n" \
                   "|                               |\n" \
                   "|   " + title_string + "   |\n" \
                   "|                               |\n" \
                   "|     for help, type '" + hlp + "'     |\n" \
                   "|      to quit, type '" + qut + "'     |\n" \
                   "|                               |\n" \
                   "'- - - - - - - - - - - - - - - -'"

    HBNBCommand().cmdloop(intro_string)
