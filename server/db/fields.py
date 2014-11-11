from query import Queryable

class Field(object):

    def __init__(self, null=True, default=None, **options):
        pass

    def __get__(self, obj, type=None):
        pass

    def __set__(self, obj, value):
        pass


class RelatedField(Field):

    def __init__(self, othermodel, related_name=None, **options):
        super(Field, self).__init__(**options)


class OneToOneField(RelatedField):

    def __get__(self, obj, type=None):
        pass

    def __set__(self, obj, value):
        pass


class ForeignKey(RelatedField):

    def __get__(self, obj, type=None):
        pass

    def __set__(self, obj, value):
        pass



class ManyToManyField(RelatedField, Queryable):

    def __get__(self, obj, type=None):
        pass

    def __set__(self, obj, value):
        pass