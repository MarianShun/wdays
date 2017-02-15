import requests
import json
from random import randint


def test_create_candidate_valid():

    # The test data:
    candidates_url = "http://candidates.com"  # Replace this with the real URL
    candidate_name = "Test Name " + str(randint(0, 100000000))
    candidate_position = "Technical Support"

    # Making the POST request with the test data put to the body:
    resp = requests.post(
        candidates_url,
        json={"name": candidate_name,
              "position": candidate_position}
    )

    # Checking response status code
    assert 201 == resp.status_code

    # Pulling all candidates info with GET request
    get_candidate = requests.get(candidates_url)

    # Parse out all candidates list
    candidates_list = json.loads(get_candidate.content)["candidates"]

    # Collecting all positions of the candidates having the same name as ours
    result = [el["position"] for el in candidates_list if el["name"] == candidate_name]

    #print(json.dumps(candidates_list, indent=4, sort_keys=True))

    assert result  # The list is not empty, so there were some results
    assert len(result) == 1  # The result is only one
    assert result[0] == candidate_position  # The stored position of the candidate is the same as in the


if __name__ == "__main__":
    test_create_candidate_valid()
