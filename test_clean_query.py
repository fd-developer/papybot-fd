import pappyapp.clean_query as script

def test_strip_accents():
	mystring = script.CleanQuery("Donnée")
	assert mystring.strip_accents("Donnée") == "Donnee"

def test_clean():
	mystring = script.CleanQuery("Donnée vers Paris")
	assert mystring.clean() == "donnee paris"