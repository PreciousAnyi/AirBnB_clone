#!/usr/bin/python3
"""console module"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for HBNB project.
    """
    prompt = "(hbnb) "

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it, and prints the id.
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            cls = eval(arg)
        except NameError:
            print("** class doesn't exist **")
            return
        new_instance = cls()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on class name and id.
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name, instance_id = args[0], args[1]

        try:
            cls = eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return

        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on class name and id.
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name, instance_id = args[0], args[1]

        try:
            cls = eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return

        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """
        Prints all string representations of instances based on class name.
        """
        if not arg:
            print([str(obj) for obj in storage.all().values()])
            return

        try:
            cls = eval(arg)
        except NameError:
            print("** class doesn't exist **")
            return

        print([str(obj) for key, obj in storage.all().items()
              if key.startswith(arg)])

    def do_update(self, arg):
        """
        Updates an instance based on class name and id by
        adding or updating attribute.
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if len(args) < 3:
            print("** instance id missing **")
            return

        class_name, instance_id = args[0], args[1]
        attr_name, attr_value = args[2], args[3]

        try:
            cls = eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return

        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return

        instance = storage.all()[key]
        setattr(instance, attr_name, attr_value)
        storage.save()

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program using EOF
        """
        print()
        return True

    def emptyline(self):
        """
        Override default behavior when the user enters an empty line.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
