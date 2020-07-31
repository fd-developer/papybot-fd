import pappyapp.clean_query as script


def test_strip_accents():
    """ use pytest to test the method strip_accent() of the CleanQuery
    class """
    mystring = script.CleanQuery("Donnée")
    assert mystring.strip_accents("Donnée") == "Donnee"


def test_clean():
    """ use pytest to test the method clean() of the CleanQuery class """
    mystring = script.CleanQuery("Donnée vers Paris")
    assert mystring.clean() == "donnee paris"
