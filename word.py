import os

methods = ("Create", "Destroy", "Update", "Retrieve", "List")

files = lambda model_import_from, model_name, method, fields: {

"__init__.py": "from .views import *\n\n",

"serializers.py": f"""from rest_framework.serializers import ModelSerializer
from {model_import_from} import {model_name}


class {model_name}{method}Serializer(ModelSerializer):
    class Meta:
        model = {model_name}
        fields = {fields}
""",
"tests.py":"""""",
"views.py":f"""from rest_framework.generics import {method}APIView
from .serializers import {model_name}{method}Serializer
from {model_import_from} import {model_name}


class {model_name}{method}ApiView({method}APIView):
    queryset = {model_name}.objects.all()
    serializer_class = {model_name}{method}Serializer

__all__ = ("{model_name}{method}ApiView", )
"""
}

_init_file = lambda model_name: f"""from .{model_name}{methods[0]} import *
from .{model_name}{methods[1]} import *
from .{model_name}{methods[2]} import *
from .{model_name}{methods[3]} import *
from .{model_name}{methods[4]} import *


__all__ = (
    "{model_name}{methods[0]}ApiView",
    "{model_name}{methods[1]}ApiView",
    "{model_name}{methods[2]}ApiView",
    "{model_name}{methods[3]}ApiView",
    "{model_name}{methods[4]}ApiView",
)
"""

def mkdirs_app_apis():
    model_import_from_input = input("Model from [example: dir.model] => ")
    app_api_dir = input("From api append [example: dir/dir/] => ")
    model_fields = input("Model fields [example: field, field, field ...] => ").split(",")

    model_import_from = ".".join(model_import_from_input.split(".")[:-1])
    model_name = model_import_from_input.split(".")[-1]

    if os.path.exists(app_api_dir):

        for method in methods:
            data_fiels = dict(files(model_import_from, model_name, method, model_fields))

            for filename, code in data_fiels.items():

                method_dir_path = os.path.join(app_api_dir, model_name + method)

                if not os.path.exists(method_dir_path):
                    os.makedirs(method_dir_path)
              
                method_dir_path_file = os.path.join(method_dir_path, filename)

                with open(method_dir_path_file, "w") as file:
                    file.write(code)
            
        with open(os.path.join(app_api_dir, "__init__.py"), "w") as init_file:
            init_file.write(_init_file(model_name))

        return f"Successfully appended on path --> {app_api_dir}"

    return f"{app_api_dir} Does not exist!"


def main():
    print(mkdirs_app_apis())

if __name__=="__main__":
    main()

