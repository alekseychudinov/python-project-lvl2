from gendiff.generator_diff import generate_diff


def test_generate_diff():
    diff_json = generate_diff("tests/fixtures/file1.json", "tests/fixtures/file2.json", 'json')
    diff_yaml = generate_diff("tests/fixtures/file1.yaml", "tests/fixtures/file2.yaml", 'json')
    diff_yml = generate_diff("tests/fixtures/file1.yml", "tests/fixtures/file2.yml", 'json')
    result_true_json = open("tests/fixtures/result_true_json.json").read()

    result_true_plain = open("tests/fixtures/result_true_plain.txt").read()
    diff_plain = generate_diff("tests/fixtures/file61.yml", "tests/fixtures/file62.yml", 'plain')

    assert diff_plain == result_true_plain
    assert diff_json == result_true_json
    assert diff_yaml == result_true_json
    assert diff_yml == result_true_json