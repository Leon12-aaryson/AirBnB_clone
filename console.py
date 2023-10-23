#!/usr/bin/python3
"""module is the entry point of the command interpreter"""

import cmd
from models import storage


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program using EOF (Ctrl+D)"""
        print()
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        """Creates new instance
        """
        if not arg:
            print("** class name missing **")
        elif arg not in storage.get_classes().keys():
            print("** class doesn't exist **")
        else:
            new_instance = storage.get_classes().get(arg)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in storage.get_classes().keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = args[0] + '.' + args[1]
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in storage.get_classes().keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = args[0] + '.' + args[1]
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Print all instances or all instances of a specific class"""
        objects = storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
        elif args[0] not in storage.get_classes().keys():
            print("** class doesn't exist **")
        else:
            print([str(obj) for key, obj in objects.items() if
                   key.split('.')[0] == arg])

    def do_update(self, arg):
        """Update an instance's attribute."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in storage.get_classes().keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = args[0] + '.' + args[1]
        if key not in objects:
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            instance = objects[key]
            attr_name = args[2]
            attr_value = args[3]
            try:
                attr_value = eval(attr_value)
            except (ValueError, NameError):
                print("** value must be a valid Python expression **")
                return

            if hasattr(instance, attr_name):
                setattr(instance, attr_name, attr_value)
                instance.save()
            else:
                print("** attribute doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
