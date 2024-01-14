#!/usr/bin/python3
"""This class serve as the entry point of our project"""

import json
import cmd
from shlex import split
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """main class for the command interpreter to handle the console"""

    prompt = "(hbnb) "

    cmd_classes = ["BaseModel", "Place", "Review",
                   "City", "User", "Amenity", "State"]

    cmd_actions = ["all", "count", "create", "show", "update", "destroy"]

    def precmd(self, command):
        """precmd method parses user input"""
        if all(char in command for char in [".", "(", ")"]):
            class_and_method = command.split(".")
            method_and_args = class_and_method[1].split("(")
            arguments = method_and_args[1].split(")")

            if (
                method_and_args[0] in HBNBCommand.cmd_actions
                and class_and_method[0] in HBNBCommand.cmd_classes
            ):
                command = (
                    method_and_args[0] + " " +
                    class_and_method[0] + " " +
                    arguments[0]
                )

        return command

    def emptyline(self):
        """handle empty line from the user"""
        pass

    def do_count(self, name):
        """count the number of instances of a specific class"""
        count = 0
        for key in storage.all():
            if key.split(".")[0] == name:
                count += 1
        print(count)

    def do_create(self, name):
        """Creates a new instance of BaseModel, saves it and prints the id"""

        if not name:
            print("** class name missing **")
        elif name not in HBNBCommand.cmd_classes:
            print("** class doesn't exist **")
        else:
            dct = {
                "BaseModel": BaseModel,
                "User": User,
                "Place": Place,
                "City": City,
                "Amenity": Amenity,
                "State": State,
                "Review": Review,
            }
            my_model = dct[name]()
            print(my_model.id)
            my_model.save()

    def do_show(self, arg):
        """Displays the string representation of the provided instance."""

        if not arg:
            print("** class name missing **")
            return

        arguments = HBNBCommand.parse_cmd(arg)

        if arguments[0] not in HBNBCommand.cmd_classes:
            print("** class doesn't exist **")
        elif len(arguments) == 1:
            print("** instance id missing **")
        else:
            for key, value in storage.all().items():
                name = value.__class__.__name__
                if name == arguments[0] and value.id == arguments[
                    1
                ].strip('"'):
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance passed"""

        if not arg:
            print("** class name missing **")
            return

        args = HBNBCommand.parse_cmd(arg)

        if args[0] not in HBNBCommand.cmd_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            for key, value in storage.all().items():
                if (
                    value.id == args[1].strip('"')
                    and value.__class__.__name__ == args[0]
                ):
                    del value
                    del storage.__objects[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """Prints string represention of all instances of a given class"""

        if not arg:
            print("** class name missing **")
            return

        args = HBNBCommand.parse_cmd(arg)

        if args[0] not in HBNBCommand.cmd_classes:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            list_instances = []
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                if ob_name == args[0]:
                    list_instances += [value.__str__()]
            print(list_instances)

    def do_update(self, arg):
        """Updates an instance (based on the class name and id)"""

        if not arg:
            print("** class name missing **")
            return

        args = HBNBCommand.parse_cmd(arg)
        args_len = len(args)

        if args[0] not in HBNBCommand.cmd_classes:
            print("** class doesn't exist **")
        elif args_len == 1:
            print("** instance id missing **")
        else:
            for key, obj in storage.all().items():
                name = obj.__class__.__name__
                if obj.id == args[1].strip('"') and name == args[0]:
                    if args_len == 2:
                        print("** attribute name missing **")
                    elif args_len == 3 and args[2].startswith("{"):
                        try:
                            json_data = json.loads(args[2].replace("'", '"'))
                            for key, value in json_data.items():
                                setattr(obj, key, value)
                            storage.save()
                        except json.JSONDecodeError:
                            print("error: invalid json")
                    else:
                        setattr(obj, args[2], args[3])
                        storage.save()
                    return
            print("** no instance found **")

    def do_quit(self, line):
        """use the Quit command to exit the script"""
        return True

    def do_EOF(self, line):
        """use the EOF command to exit the script"""
        return True

    def parse_cmd(arg):
        """Parse the user input into a list of arguments"""
        start1 = arg.find("{")
        end1 = arg.find("}")
        start2 = arg.find("[")
        end2 = arg.find("]")

        if start1 == -1:
            if start2 == -1:
                return [i.strip(",") for i in split(arg)]
            else:
                data1 = split(arg[:start2])
                res1 = [i.strip(",") for i in data1]
                res1.append(arg[start2: end2 + 1])
                return res1
        else:
            data1 = split(arg[:start1])
            res1 = [i.strip(",") for i in data1]
            res1.append(arg[start1: end1 + 1])
            return res1


if __name__ == "__main__":
    HBNBCommand().cmdloop()
