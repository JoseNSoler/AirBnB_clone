#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    """ command console for managing and interacting with the AirBnB clone """

    prompt="(hbnb) "  #<--- Defines the look of the prompt

    # Definition override for handling ENTER with an empty line.--------------|
    def emptyline(self):
        pass


    # Implementations 0.1-----------------------------------------------------|
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


    # Implementations 0.0.1---------------------------------------------------|
    def do_quit(self, line):
        """Exits the program.\n"""
        return True

    def do_EOF(self, line):
        """Exits the program.\n"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
