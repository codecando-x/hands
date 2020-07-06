import types

class HierarchyAndStructure:

    __generated_object = None
    __quick_access_data = {}
    __py_code_access_keys = []
    __separator = None

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

    __templates = {
        dict:"{}['{}']",
        list:"{}[{}]",
        tuple:"{}[{}]",
        set:"{}[{}]"
    }

    __xtemplates = {
        dict:"{}X{}",
        list:"{}X{}",
        tuple:"{}X{}",
        set:"{}X{}"
    }

    def __init__(self, data, separator = '.'):
        self.__separator = separator

        """
        while we recursively traverse the the data object once, we do the following things:
            - build a generated object hierarchy which one could access like(one.two.three.val), to get rid of the bracket access pattern
            - build a list of all key:val pairs which will enable direct lookup without recursing again
            - build a list of all access code snippets, mostly used for discovery to find out available keys deep in the object hierarchy, also for looking up value deep down

        """
        self.__generated_object = self.__build(data, types.SimpleNamespace(), 'X')

        print("======================================\n")
        print(self.__quick_access_data)
        print("======================================\n")
        print(self.__py_code_access_keys)

    #def query(self, sql

    def get(self, key: str):
        if key in self.__quick_access_data:
            return self.__quick_access_data[key]
        else:
            raise KeyError("key: {} not found".format(key))

    """
        will print all access keys/values to reach all values across object structure
    """

    def __quick_access_key_py_access_key(self, quick_access_key: str):
        quick_access_key = quick_access_key.replace("['", self.__separator)
        quick_access_key = quick_access_key.replace("']", self.__separator)
        quick_access_key = quick_access_key.replace("[", self.__separator)
        quick_access_key = quick_access_key.replace("]", self.__separator)

        return quick_access_key

    def __build(self, current, sobj, hier: str = ''):

        current_type = type(current)

        if current_type in self.__empties.keys():
            empty = self.__empties[current_type]
            if len(current) == 0:
                print(hier + ' : ' + empty)

                #add key:val pair to quick_access_data for easy flat retrieval latter

                self.__quick_access_data[self.__quick_access_key_py_access_key(hier)] = empty

                #add key to py_code_access_keys list so we can find out key paths for development
                self.__py_code_access_keys.append(hier)

                nkey = hier
                if type(nkey) is int:
                    nkey = 'i' + str(nkey)

                setattr(sobj, nkey, self.__inits[current_type])
                return sobj

            #this holds the keys which we will store in quick_access_data
            xtemplate = self.__xtemplates[current_type].replace('X', self.__separator)

            #this holds the keys which we will store in py_code_access_keys
            template = self.__templates[current_type]
        else:
            empty = str(None)

        if current_type is dict:
            items = list(current.items())
        elif current_type in [list, tuple, set]:
            items = list(enumerate(current))

        for key, val in items:

            nkey = key
            if type(nkey) is int or nkey.isdigit() is True:
                nkey = 'i' + str(nkey)
            #print('NKEY: ' + str(type(nkey)))
            #print('NKEY VAL: ' + str(nkey))

            val_type = type(val)
            h = template.format(hier,str(key))
            if val_type in [dict, list, tuple, set]:
                new_obj_val = self.__build(val, types.SimpleNamespace(), h)
                setattr(sobj, nkey, new_obj_val)
            else:
                v = str(val)
                if val_type is str and len(v) == 0:
                    v = '""'

                print("{} : {}".format(h, v))
                #add key:val pair to quick_access_data for easy flat retrieval latter
                self.__quick_access_data[self.__quick_access_key_py_access_key(h)] = v

                self.__py_code_access_keys.append(h)

                new_obj_val = v
                #print('NKEY: ' + str(type(nkey)))
                setattr(sobj, nkey, new_obj_val)

        return sobj

    '''
    def query
    '''
