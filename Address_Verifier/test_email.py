from address_regex import validate

def test_valid():
    assert validate('rosela31@unet.com') == 'Valid!'
    assert validate('r@gmail.com') == 'Valid!'
    assert validate('rosic23@univie.ac.at') == 'Valid!'
    assert validate('rosela31@unet.AC.AT') == 'Valid!'
    assert validate('fire_@yahoo.giz.gov') == 'Valid!'

def test_invalid():
    assert validate('fire_@yahoo.giz.something') == 'Invalid!'
    assert validate('@unet.com') == 'Invalid!'
    assert validate('@') == 'Invalid!'
    assert validate('r31@@unet.com') == 'Invalid!'
    assert validate('rosela31@unet.univie.al.ac.com') == 'Invalid!'
    assert validate('rc@.giz') == 'Invalid!'
