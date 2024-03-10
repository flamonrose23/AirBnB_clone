#!/usr/bin/python3
"""
Writing program containing entry point
of command interpreter
"""

import cmd
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Defining class definition
    """

    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "State", "City",
               "Amenity", "Place", "Review"]
    attributes = ["updated_at", "created_at", "id"]
    specs = ["\'", "\""]

    def do_EOF(self, line):
        """
        Defining command to exit on EOF
        """
        print()
        return True

    def do_quit(self, line):
        """
        Defining command to exit on quit
        """
        return True

    def emptyline(self):
        """
        Defining command to pass empty line
        """
        pass

    def do_create(self, param):
        """
        Creating instance of new BaseModel
        """
        if not param:
            print("** class with missing name **")
        elif param not in self.classes:
            print("** class doesn't exist **")
        else:
            new_it = eval(param)()
            print(new_it.id)
            new_it.save()

    def do_show(self, param):
        """
        Printing string representation
        """
        com = param.split()
        if not param:
            print("** class name missing **")
            return
        elif com[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(com) == 1:
            print("** instance id missing **")
            return
        new_it = "{}.{}".format(com[0], com[1])
        if new_it not in storage.all().keys():
            print("** no instance found **")
            return
        else:
            print("[{}] ({}) {}".format(com[0],
                                        com[1], storage.all()[new_it]))

    def do_destroy(self, param):
        """
        Deleting instance based on class
        """
        com = param.split()
        if not param:
            print("** class name missing **")
            return
        elif com[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(com) == 1:
            print("** instance id missing **")
            return
        else:
            new_it = "{}.{}".format(com[0], com[1])
            if new_it not in storage.all():
                print("** no instance found **")
            else:
                storage.all().pop(new_it)
                storage.save()

    def do_all(self, param):
        """
        Printing all strings
        """
        list_obj = []
        new_it = storage.all()
        if param and param not in self.classes:
            print("** class doesn't exist **")
            return
        elif param in self.classes:
            for key, value in new_it.items():
                split_key = key.split(".")
                new_key = "[" + split_key[0] + "] (" + split_key[1] + ")"
                list_obj.append(new_key + " " + str(valour))
        else:
            for key, valour in new_it.items():
                list_obj.append(str(key) + " " + str(valour))
        print(list_obj)

    def do_update(self, param):
        """
        Updating instances
        """
        com = param.split()
        if not param:
            print("** class name missing **")
        elif com[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(com) == 1:
            print("** instance id missing **")
            return
        elif com[0] + "." + com[1] not in storage.all().keys():
            print("** no instance found **")
            return
        elif len(com) == 2:
            print("** attribute name missing **")
            return
        elif len(com) == 3:
            print("** valour missing **")
            return
        else:
            object = storage.all()
            key = com[0] + "." + com[1]
            if key in object:
                if com[2] not in self.attributes:
                    if com[3][0] in self.specs and comm[3][-1] in self.specs:
                        setattr(object[key], com[2], str(com[3][1: -1]))
                    else:
                        setattr(object[key], com[2], str(com[3]))
                    storage.save()
            else:
                print("** no instance found **")
                return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
