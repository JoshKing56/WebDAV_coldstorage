import configuration.nextcloud as nc

def test_nextcloud_connection():
    assert nc.EXISTS == True
    assert nc.NEXTCLOUD_USER == "josh" 
