#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """Console command interpreter class."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the console."""
        return True

    def do_EOF(self, arg):
        """Exit the console."""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
