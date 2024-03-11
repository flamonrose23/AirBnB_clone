#!/usr/bin/python3
"""
Writing program containing entry point
of command interpreter
"""

import cmd
import json
import models
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Defining command line
    """

    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "State", "City",
               "Amenity", "Place", "Review"]
    attributes = ["updated_at", "created_at", "id"]
    specs = ["\'", "\""]


    def emptyline(self):
        """
        Defining command to pass empty line
        """
        pass

    def do_quit(self, argum):
        """
        Defining command to exit on quit
        """
        return True

    def do_EOF(self, line):
        """
        Defining command to exit on EOF
        """
        print()
        return True

    def do_create(self, argum):
        """
        Creating instance of new BaseModel
        """
        argums = argum.split()
        if not validate_classname(argums):
            return

        objt = class_list[argums[0]]()
        objt.save()

        print(objt.id)

    def do_show(self, arg):
        """
        Printing string represenatation of  instance
        based on name and id
        """
        argums = argum.split()
        if not validate_classname(argums, True):
            return

        objt_dict = models.storage.all()
        key = "{}.{}".format(argums[0], argums[1])
        if key not in objt_dict.keys():
            print("** no instance found **")
        else:
            valour = objt_dict[key]
            print(value)

    def do_destroy(self, argum):
        """
        Deleting instance based on name
        and id then saving changes to JSON file
        """
        argums = argum.split()
        if not validate_classname(argums, True):
            return

        objt_dict = models.storage.all()
        key = "{}.{}".format(argums[0], argums[1])
        if key not in objt_dict.keys():
            print("** no instance found **")
        else:
            del objt_dict[key]
            models.storage.save()

    def do_all(self, argum):
        """
        Printing all string represenatation of all instances and attributes
        """
        argums = argum.split()

        objt_dict = models.storage.all()

        if len(argums) == 0:
            print(["{}".format(str(valour)) for valour in objt_dict.valours()])
        else:
            if argums[0] not in class_list.keys():
                print("** class doesn't exist **")
            else:
                print(["{}".format(str(valour)) 
                    for valour in objt_dict.valours()
                       if type(valour).__name__ == argums[0]])

    def do_update(self, argum):
        """
        Updating instances
        """
        argums = argum.split(maxsplit=3)
        if not validate_classname(argums, check_id=True):
            return
        if not validate_attributes(argums):
            return

        objt_dict = models.storage.all()
        key = "{}.{}".format(argums[0], argums[1])
        if key not in objt_dict.keys():
            print("** no instance found **")
        else:
            objt_instance = objt_dict[key]
            valour = parse_str(argums[3])
            setattr(objt_instance, argums[2], valour)
            models.storage.save()

    def obj_count(self, class_name):
        """
        Counting number of instances of specific class
        """
        num_instances = 0
        all_objects = models.storage.all()
        for key in all_objects.keys():
            argums = key.split(".")
            if argums[0] == class_name:
                num_instances += 1
        print(num_instances)

    def default(self, line):
        """
        Overrriding default behavior for unrecognized commands.
        Executing undocumented commands
        """
        commands = {
            "all": self.do_all,
            "count": self.obj_count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update
        }

        pattern = r"^(\w+)\.(\w+)\((.*)\)"
        argum_t = ()
        argums = re.match(pattern, line)
        if argums:
            argums_t = argums.groups()
        if len(argums_t) < 2 or argums_t[0] not in class_list.keys()\
           or argums_t[1] not in commands.keys():
            super().default(line)
            return

        if argums_t[1] in ["all", "count"]:
            commands[argums_t[1]](argums_t[0])

        if argums_t[1] in ["show", "destroy"]:
            commands[argums_t[1]](argums_t[0] + " " + argums_t[2])



    def validate_classname(argums, check_id=False):
        if len(argums) == 0:
            print("** class name missing **")
            return False
        if argums[0] not in class_list.keys():
            print("** class doesn't exist **")
            return False
        if len(argums) < 2 and check_id:
            print("** instance id missing **")
            return False
        return True


def validate_attributes(argums):
    """
    Validating attributes parsed as command argument
    """
    if len(args) < 3:
        print("** attribute name missing **")
        return False
    if len(argums) < 4:
        print("** value missing **")
        return False
    return True


def is_float(valour):
    """
    Checking if 'valour' is float.
    """
    try:
        v = float(valour)
    except (TypeError, ValueError):
        return False
    else:
        return True


def is_int(valour):
    """
    Checking if valour is int.
    """
    try:
        a = float(valour)
        b = int(valour)
    except (TypeError, ValueError):
        return False
    else:
        return a == b


def parse_str(arg):
    """
    Parsing `arg` to an `int`, `float` or `string`.
    """
    str = re.sub(r"\"", "", argum)
    str = re.sub("'", "", str)

    if is_int(str):
        return int(str)
    elif is_float(str):
        return float(str)
    else:
        return str


if __name__ == "__main__":
    HBNBCommand().cmdloop()
