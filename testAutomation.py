import requests

# Define the test cases
testcases = [
    {"url": "http://localhost:8000/add/2/2", "expected": 4, "description": "Test addition of 2 and 2"},
    {"url": "http://localhost:8000/subtract/2/2", "expected": 0, "description": "Test subtraction of 2 from 2"},
    {"url": "http://localhost:8000/multiply/2/2", "expected": 4, "description": "Test multiplication of 2 and 2"}
]

# Function to run the tests
def test():
    for case in testcases:
        response = requests.get(case["url"])
        result = response.json()["result"]
        
        # Assertion for validation
        assert result == case["expected"], f"Test failed: {case['description']}. Expected {case['expected']}, got {result}"
        
        print(f"✅ Test passed: {case['description']}")

    print("\n🎯 All tests passed!")

# Run the tests
test()
