import copy


def delete_data_field(data, key):
    d = copy.copy(data)
    d.pop(key)
    return d
