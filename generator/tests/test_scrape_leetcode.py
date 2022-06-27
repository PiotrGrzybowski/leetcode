import requests


def test_collect_site():
    response = requests.get("https://leetcode.com/problems/two-sum/")
    print(response.text)
    assert 1 == 1
