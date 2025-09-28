import unittest
import subprocess
import sys
import os

project_location= os.path.join("python-beginner-projects\\projects\\Password Projects\\Password Hashing","main.py")

#calling the script using the information of the readme
def fileCaller(password,hashtype):
    if not hashtype:
        return subprocess.run(
        [sys.executable, project_location, password],
        capture_output=True,
        text=True
    )
    return subprocess.run(
        [sys.executable, project_location, password,"-t",hashtype],
        capture_output=True,
        text=True 
    )

class TestHashingResults(unittest.TestCase):
    #Testing for Github using sha256
    def test_sha256_output(self):
        inputPassword="Github"
        inputHashtype="sha256"
        outputExpectedResult="1720d8eaff790da6af4406905ba663d0cc6a6cea2b3e54e7384ac334a037f59d"
        result = fileCaller(inputPassword,inputHashtype)
        #Verify that the call to the main file is correct. 
        self.assertEqual(result.returncode, 0)
        #Verify result
        self.assertIn(
            outputExpectedResult,
            result.stdout
        )

    def test_nohashtype(self):
        inputPassword="Github"
        inputHashtype=""
        outputExpectedResult="1720d8eaff790da6af4406905ba663d0cc6a6cea2b3e54e7384ac334a037f59d"
        result = fileCaller(inputPassword,inputHashtype)
        #Verify that the call to the main file is correct. 
        self.assertEqual(result.returncode, 0)
        #Verify result
        self.assertIn(
            outputExpectedResult,
            result.stdout
        )





if __name__ == "__main__":
    unittest.main()