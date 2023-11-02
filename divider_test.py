import divider


def test_1(monkeypatch, capsys):
    inputs = iter([8565, 135])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    divider.main()
    captured = capsys.readouterr()
    assert captured.out == ('15\n')


def test_3(monkeypatch, capsys):
    inputs = iter([11, 58762])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    divider.main()
    captured = capsys.readouterr()
    assert captured.out == ('11\n')