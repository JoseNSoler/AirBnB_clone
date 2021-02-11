#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """ command console for managing and interacting with the AirBnB clone """

    prompt="(hbnb) "  #<--- Defines the look of the prompt

    # Definition override for handling ENTER with an empty line.--------------|
    def emptyline(self):
        pass

    # Implementations.--------------------------------------------------------|
    def do_quit(self, line):
        """Exits the program.\n"""
        return True

    def do_EOF(self, line):
        """Exits the program.\n"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
