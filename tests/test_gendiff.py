from gendiff.generator_diff import generate_diff


def test_generate_json():
    diff_json_json = generate_diff("tests/fixtures/file1.json", "tests/fixtures/file2.json", 'json')
    diff_yaml_json = generate_diff("tests/fixtures/file1.yaml", "tests/fixtures/file2.yaml", 'json')
    diff_yml_json = generate_diff("tests/fixtures/file1.yml", "tests/fixtures/file2.yml", 'json')
    result_true_json = open("tests/fixtures/result_true_json.json").read()

    assert diff_json_json == result_true_json
    assert diff_yaml_json == result_true_json
    assert diff_yml_json == result_true_json


def test_generate_plain():
    #diff_json_plain = generate_diff("tests/fixtures/file1.json", "tests/fixtures/file2.json", 'plain')
    diff_yaml_plain = generate_diff("tests/fixtures/file1.yaml", "tests/fixtures/file2.yaml", 'plain')
    diff_yml_plain = generate_diff("tests/fixtures/file1.yml", "tests/fixtures/file2.yml", 'plain')
    result_true_plain = open("tests/fixtures/result_true_plain.txt").read()

    #assert diff_json_plain == result_true_plain
    assert diff_yaml_plain == result_true_plain
    assert diff_yml_plain == result_true_plain
