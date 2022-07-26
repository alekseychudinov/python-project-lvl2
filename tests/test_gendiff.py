from gendiff.generator_diff import generate_diff


def test_generate_diff():
    diff_json = generate_diff("tests/fixtures/file1.json", "tests/fixtures/file2.json", 'json')
    diff_yaml = generate_diff("tests/fixtures/file1.yaml", "tests/fixtures/file2.yaml", 'json')
    diff_yml = generate_diff("tests/fixtures/file1.yml", "tests/fixtures/file2.yml", 'json')
    result_true_json = open("tests/fixtures/result_true_json.json").read()

    diff_json6 = generate_diff("tests/fixtures/file61.json", "tests/fixtures/file62.json", 'json')
    diff_yaml6 = generate_diff("tests/fixtures/file61.yaml", "tests/fixtures/file62.yaml", 'json')
    diff_yml6 = generate_diff("tests/fixtures/file61.yml", "tests/fixtures/file62.yml", 'json')
    result_true6 = open("tests/fixtures/result_true6.txt").read()

    result_true_plain = open("tests/fixtures/result_true_plain.txt").read()
    diff_plain = generate_diff("tests/fixtures/file61.yml", "tests/fixtures/file62.yml", 'plain')

    assert diff_plain == result_true_plain
    assert diff_json == result_true_json
    assert diff_yaml == result_true_json
    assert diff_yml == result_true_json
    assert diff_json6 == result_true6
    assert diff_yaml6 == result_true6
    assert diff_yml6 == result_true6


def test_generate_diff8():
    result_true_json8 = open("tests/fixtures/result_true_json8.json").read()
    diff_json8 = generate_diff("tests/fixtures/file81.json", "tests/fixtures/file82.json", 'json')
    assert diff_json8 == result_true_json8
