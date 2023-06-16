from example_lab.example_script import encrypt, decrypt, crack

def test_encrypt():
    assert encrypt("abc", 1) == "bcd"
    assert encrypt("abc", 10) == "klm"
    assert encrypt("zzz", 1) == "aaa"

def test_decrypt():
    assert decrypt("bcd", 1) == "abc"
    assert decrypt("klm", 10) == "abc"
    assert decrypt("aaa", 1) == "zzz"

def test_crack(capsys):
    crack("bcd")
    captured = capsys.readouterr()
    assert "Shift: 1\tDecrypted text: abc" in captured.out

    crack("klm")
    captured = capsys.readouterr()
    assert "Shift: 10\tDecrypted text: abc" in captured.out

    crack("aaa")
    captured = capsys.readouterr()
    assert "Shift: 1\tDecrypted text: zzz" in captured.out

if __name__ == '__main__':
    pytest.main()
