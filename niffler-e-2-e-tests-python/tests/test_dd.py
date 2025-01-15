from deepdiff import DeepDiff

dict1 = {
'a': 1,
'b': [
      {'c': [{'d': 32.069},{'e': 32.420}]}
     ]
}
dict2 = {
'a': 1,
'b': [ {'c': [{'d': 32.069},{'e': 32.420}]}
     ]
}

def test():
    diff = DeepDiff(dict1, dict2)
    print(diff)
    assert diff == {}