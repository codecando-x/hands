import types
import json

class HierarchyAndStructure:

    __data = None
    __generated_object = None
    __quick_access_data = {}
    __py_code_access_keys = {}
    __separator = '.'
    __index_identifier = 'i'

    __empties = {
        dict:'{}',
        list:'[]',
        tuple:'()',
        set:'{}'
    }

    __inits = {
        dict:{},
        list:[],
        tuple:(),
        set:{}
    }

    __direct_access_templates = {
        dict:"{}['{}']",
        list:"{}[{}]",
        tuple:"{}[{}]",
        set:"{}[{}]"
    }

    __obj_chain_templates = {
        dict:"{}X{}",
        list:"{}X{}",
        tuple:"{}X{}",
        set:"{}X{}"
    }

    def __init__(self, data = {}, file_path: str = '', separator: str = '.', index_identifier: str = 'i'):
        self.__data = data
        self.__file_path = file_path
        self.__separator = separator
        self.__index_identifier = index_identifier

        """
        while we recursively traverse the the data object once, we do the following things:
            - build a generated object hierarchy which one could access like(one.two.three.val),
                to get rid of the bracket access pattern
            - build a list of all key:val pairs which will enable direct lookup without recursing again
            - build a list of all access code snippets, mostly used for discovery to find out
                available keys deep in the object hierarchy, also for looking up value deep down

        """
        self.__generated_object = self.__build(self.__data, types.SimpleNamespace(), 'X', 'X')

        print("======================================\n")
        self.print_obj_access_keys()
        print("======================================\n")
        self.print_direct_access_keys()

    #def query(self, sql

    def print_direct_access_keys(self):
        print(json.dumps(self.__py_code_access_keys, indent=4))

    def print_obj_access_keys(self):
        print(json.dumps(self.__quick_access_data, indent=4))

    def get(self, key: str):
        if key in self.__quick_access_data:
            return self.__quick_access_data[key]
        else:
            raise KeyError("key: {} not found".format(key))

    """
        will print all access keys/values to reach all values across object structure
    """

    def __build(self, current_obj, obj_hierarchy, direct_access_key_hierarchy: str = '', obj_chain_key_hierarchy: str = ''):

        current_object_type = type(current_obj)

        if current_object_type in self.__empties.keys():
            empty = self.__empties[current_object_type]
            if len(current_obj) == 0:
                #add key:val pair to quick_access_data for easy flat retrieval latter
                self.__quick_access_data[obj_chain_key_hierarchy] = empty

                #add key to py_code_access_keys list so we can find out key paths for development
                self.__py_code_access_keys[direct_access_key_hierarchy] = empty

                index_key = direct_access_key_hierarchy
                #if type(index_key) is int:
                if type(index_key) is int or index_key.isdigit() is True:
                    index_key = 'i' + str(index_key)

                setattr(obj_hierarchy, index_key, self.__inits[current_object_type])
                return obj_hierarchy

            #this holds the keys which we will store in quick_access_data
            obj_chain_template = self.__obj_chain_templates[current_object_type].replace('X', self.__separator)

            #this holds the keys which we will store in py_code_access_keys
            direct_access_template = self.__direct_access_templates[current_object_type]
        else:
            empty = str(None)

        if current_object_type is dict:
            items = list(current_obj.items())
        elif current_object_type in [list, tuple, set]:
            items = list(enumerate(current_obj))

        for key, val in items:

            index_key = key
            if type(index_key) is int or index_key.isdigit() is True:
                index_key = 'i' + str(index_key)

            val_type = type(val)
            new_direct_access_key_hierarchy = direct_access_template.format(direct_access_key_hierarchy,str(key))
            obj_chain_key_hierarchy = obj_chain_template.format(obj_chain_key_hierarchy,str(key))
            if val_type in [dict, list, tuple, set]:
                new_obj_val = self.__build(val, types.SimpleNamespace(), new_direct_access_key_hierarchy, obj_chain_key_hierarchy)
                setattr(obj_hierarchy, index_key, new_obj_val)
            else:
                new_val = str(val)
                if val_type is str and len(new_val) == 0:
                    new_val = '""'

                #print("{} : {}".format(new_direct_access_key_hierarchy, new_val))

                #add key:val pair to quick_access_data for easy flat retrieval latter
                self.__quick_access_data[obj_chain_key_hierarchy] = new_val

                self.__py_code_access_keys[new_direct_access_key_hierarchy] = new_val

                setattr(obj_hierarchy, index_key, new_val)

        return obj_hierarchy

    '''
    def query
    '''
