#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
import models
list_of_classes = ["BaseModel", "User"]


class HBNBCommand(cmd.Cmd):
    """ command console for managing and interacting with the AirBnB clone """

    prompt = "(hbnb) "  # <--- Defines the look of the prompt

    # Definition override for handling ENTER an empty line.-------------------|
    def emptyline(self):
        pass

    # Implementations 0.1-----------------------------------------------------|
    #                                                                         |
    # do_create - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
    def do_create(self, line):
        """Create a new BaseModel instance.\n"""
        if line:
            switch = False
            for name in list_of_classes:
                if line == name:
                    x = eval(name)()  # <--Create instance.
                    storage.new(x)
                    storage.save()
                    print(x.id)
                    switch = True
                    break

            if switch is False:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    # do_show - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
    def do_show(self, line):
        """ Shows a class instance given its name class and id. """
        if line:
            args = line.split(" ")
            # Compare switch
            switch = False

            # Compare given class name against list of classes.
            for name in list_of_classes:
                if args[0] == name:
                    switch = True
                    break

            # If found the correct class name
            if switch is True:
                # If given an id
                if len(args) > 1:
                    string = args[0] + "." + args[1]  # <-- ClassName.id string
                    storage.reload()  # <-- Reload all objects from file.
                    dicto = storage.all()  # <-- Retrieve dictionary of objects
                    switch = False  # <-- Set switch for looking in dictionary

                    for obj_id, obj in dicto.items():
                        # If correct ClassName.id found
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
            # Compare switch
            switch = False

            # Compare given class name against list of classes.
            for name in list_of_classes:
                if args[0] == name:
                    switch = True
                    break

            if switch is True:
                if len(args) > 1:
                    if storage.delete(args[0], args[1]) is False:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    # do_all - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -|
    def do_all(self, line):
        """ Prints all the objects, currently present. """
        storage.reload()
        dicto = storage.all()
        list_of_strings = []

        # If only all command was given
        if line == "":

            # For all objects in the dict append their str representation.
            for obj_id, obj in dicto.items():
                list_of_strings.append(obj.__str__())

            # If list_of_strings is not empty
            if bool(list_of_strings):
                print(list_of_strings)

        else:

            # Compare switch
            switch = False
            # Compare given class name against list of classes.
            for name in list_of_classes:
                if line == name:
                    switch = True
                    break

            # If found the correct class name
            if switch is True:

                # Append only the given classes.
                for obj_id, obj in dicto.items():
                    class_name = obj_id.split(".")
                    if line == class_name[0]:
                        list_of_strings.append(obj.__str__())

                # If list_of_strings is not empty
                if bool(list_of_strings):
                    print(list_of_strings)
            else:
                print("** class doesn't exist **")

    # do_update - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
    def do_update(self, line):
        '''Updates or adds an attribute for an instance of a class given its
 name, id, the attribute to add and the value for it, only one
 attribute can be set up at a time.

usage:

    update <class name> <id> <attribute name> "<attribute value>"
        '''
        if line:
            # Change single ' to double " for cmds running non-tty
            line = line.replace("'", '"')
            # Split once delimited by "
            val = line.split('"')
            # Split normally a second time the first arguments
            arg = val[0].split(" ")
            # Compare switch
            switch = False

            # Compare given class name against list of classes.
            for name in list_of_classes:
                if arg[0] == name:
                    switch = True
                    break

            # If correct class name given.
            if switch is True:
                # If given an id.
                if len(arg) > 1:
                    obj_id = arg[0] + "." + arg[1]  # <--- ClassName.id string
                    # If name of attribute given.
                    if len(arg) > 2:
                        # If value for the attribute was given.
                        if len(val) > 1:
                            # If no instance exists by the given
                            if storage.update(obj_id, arg[2], val[1]) is False:
                                print("** no instance found **")
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    # Implementations 0.0.1---------------------------------------------------|
    #                                                                         |
    # do_quit - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
    def do_quit(self, line):
        """Exits the program.\n"""
        print("")
        return True

    # do_EOF - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -|
    def do_EOF(self, line):
        """Exits the program.\n"""
        print("")
        return True

# If being executed not imported - - - - - - - - - - - - - - - - - - - - - - -|
if __name__ == '__main__':

    import sys
    if len(sys.argv) > 2:
        HBNBCommand().onecmd(' '.join(sys.argv[1:]))
    else:
        green = "\033[92m"  # <-- Green color format
        reset = "\033[0m"  # <-- Default color format

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
