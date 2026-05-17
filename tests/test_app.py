import ai_buddy_test_app


def test_main_prints_expected_message(capsys):
    ai_buddy_test_app.main()

    captured = capsys.readouterr()

    assert captured.out == "AI Buddy test project is running\n"
