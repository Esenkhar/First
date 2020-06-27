class Person:
    def __init__(self, name):
        self._name = name

    class Name:
        """name descriptor docs"""

        def __get__(self, instance, owner):
            print('fetch...')
            return instance._name

        def __set__(self, instance, value):
            print('change...')
            instance._name = value

        def __delete__(self, instance):
            print('remove...')
            raise AttributeError('cannot delete')

    name = Name()


    #
    # @property
    # def name(self):
    #     """name property docs"""
    #     print('fetch...')
    #     return self._name
    #
    # @name.setter
    # def name(self, name):
    #     print('change...')
    #     self._name = name
    #
    # @name.deleter
    # def name(self):
    #     print('remove...')
    #     del self._name


if __name__ == '__main__':
    bob = Person('Bob Smith')
    print(bob.name)
    bob.name = 'Robert Smith'
    print(bob.name)
    try:
        del bob.name
    except AttributeError as error:
        print(error)
    print('-' * 20)
    sue = Person('Sue Jones')
    print(sue.name)
    print(sue.name)
    sue.name = 'Sue Jones'
    print(sue.name)
    print('-' * 20)
    print(Person.Name.__doc__)

