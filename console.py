#!/usr/bin/python3
"""
Command interpreter to control models
"""
import cmd
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    """
    HBNB class
    """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """
        Quit the cmd
        """
        return True

    def do_EOF(self, line):
        """
        End of File
        """
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered
        """
        pass

    def do_create(self, obj):
        """
        Create a BaseModel Object
        """
        if obj:
            if (obj == "BaseModel"):
                model = BaseModel()
                model.save()
                print(model.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """
        Show Data about a specific instance based on the Id
        """
        if len(arg) > 0:
            args = arg.split()
            name = args[0]
            if (name == "BaseModel"):
                if len(args) > 1:
                    id = args[1]
                    all_values = models.storage.all()
                    search_string = f"{name}.{id}"
                    if search_string in all_values:
                        print(all_values[search_string])
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """
        Delete a specific entry
        """
        if len(arg) > 0:
            args = arg.split()
            name = args[0]
            if (name == "BaseModel"):
                if len(args) > 1:
                    id = args[1]
                    all_values = models.storage.all()
                    search_string = f"{name}.{id}"
                    if search_string in all_values:
                        del all_values[search_string]
                        models.storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, arg):
        """
        Show all instences
        """
        all_values = models.storage.all()
        if len(arg) > 0:
            if (arg == "BaseModel"):
                final_dic = {}
                for key, value in all_values.items():
                    if key.startswith("BaseModel."):
                        final_dic[key] = value
                print(final_dic)
            else:
                print("** class doesn't exist **")
        else:
            print(all_values)

    def do_update(self, arg):
        """
        Update a specific instence
        """
        if len(arg) > 0:
            args = arg.split()
            name = args[0]
            if (name == "BaseModel"):
                if len(args) > 1:
                    id = args[1]
                    all_values = models.storage.all()
                    search_string = f"{name}.{id}"
                    if search_string in all_values:
                        if len(arg) > 2:
                            if len(arg) > 3:
                                if (args_array[3] not in
                                        ["created_at", "updated_at", "id"]):
                                    setattr(all_values[search_string], str(
                                        args[2]), str(arggs[3]))
                            else:
                                print("** value missing **")
                        else:
                            print("** attribute name missing **")
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()