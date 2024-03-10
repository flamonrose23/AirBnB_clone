#!/usr/bin/python3
"""Console"""

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
    bla bla bla bla
    """
    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "State", "City",
               "Amenity", "Place", "Review"]
    attributes = ["updated_at", "created_at", "id"]
    specs = ["\'", "\""]

    def do_EOF(self, line):
        """Exits on EOF"""
        print()
        return True

    def do_quit(self, line):
        """exits when typing quit"""
        return True

    def emptyline(self):
        """passing emptyline do nothing"""
        pass

    def do_create(self, line):
        """
        Creates a new instance of BaseModel
        """
        if not line:
            print("** class name missing **")
        elif line not in self.classes:
            print("** class doesn't exist **")
        else:
            new_item = eval(line)()
            print(new_item.id)
            new_item.save()

    def do_show(self, line):
        """ Prints the instance """
        comm = line.split()
        if not line:
            print("** class name missing **")
            return
        elif comm[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(comm) == 1:
            print("** instance id missing **")
            return
        new_item = "{}.{}".format(comm[0], comm[1])
        if new_item not in storage.all().keys():
            print("** no instance found **")
            return
        else:
            print("[{}] ({}) {}".format(comm[0],
                                        comm[1], storage.all()[new_item]))

    def do_destroy(self, line):
        """delete an instance"""
        comm = line.split()
        if not line:
            print("** class name missing **")
            return
        elif comm[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(comm) == 1:
            print("** instance id missing **")
            return
        else:
            new_item = "{}.{}".format(comm[0], comm[1])
            if new_item not in storage.all():
                print("** no instance found **")
            else:
                storage.all().pop(new_item)
                storage.save()

    def do_all(self, line):
        """Prints all instance"""
        list_object = []
        new_item = storage.all()
        if line and line not in self.classes:
            print("** class doesn't exist **")
            return
        elif line in self.classes:
            for key, value in new_item.items():
                split_key = key.split(".")
                new_key = "[" + split_key[0] + "] (" + split_key[1] + ")"
                list_object.append(new_key + " " + str(value))
        else:
            for key, value in new_item.items():
                list_object.append(str(key) + " " + str(value))
        print(list_object)

    def do_update(self, line):
        """Updates an instance"""
        comm = line.split()
        if not line:
            print("** class name missing **")
        elif comm[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(comm) == 1:
            print("** instance id missing **")
            return
        elif comm[0] + "." + comm[1] not in storage.all().keys():
            print("** no instance found **")
            return
        elif len(comm) == 2:
            print("** attribute name missing **")
            return
        elif len(comm) == 3:
            print("** value missing **")
            return
        else:
            object = storage.all()
            key = comm[0] + "." + comm[1]
            if key in object:
                if comm[2] not in self.attributes:
                    if comm[3][0] in self.specs and comm[3][-1] in self.specs:
                        setattr(object[key], comm[2], str(comm[3][1: -1]))
                    else:
                        setattr(object[key], comm[2], str(comm[3]))
                    storage.save()
            else:
                print("** no instance found **")
                return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
