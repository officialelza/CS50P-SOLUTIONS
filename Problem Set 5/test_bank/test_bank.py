from bank import value

def test_hello():
    A = ["Hello","Hello!","Hello sir","Hello, ma'am"]
    for i in A:
        assert value(i) == 0

def test_h():
    A = ["Hey there","Hey",'How is it going?','How are you?','Howdy']
    for i in A:
        assert value(i) == 20

def test_other():
    A = ["What's up?","What are you upto?"]
    for i in A:
        assert value(i) == 100
