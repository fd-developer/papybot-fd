import pappyapp.google_utils as script

def test_geocode():
	myplace = script.ApiGoogle("25320 TORPES")
	myplace.geocode()
	assert myplace.found == True
	assert myplace.city == "25320 Torpes, France"
	assert myplace.lat == 47.169692
	assert myplace.lng == 5.891695899999999
