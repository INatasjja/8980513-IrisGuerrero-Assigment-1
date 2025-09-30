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

    def test_md5_output(self):
        inputPassword="Github"
        inputHashtype="md5"
        outputExpectedResult="e1adbcbb92c622d0b3e619f9d0730abf"
        result = fileCaller(inputPassword,inputHashtype)
        #Verify that the call to the main file is correct. 
        self.assertEqual(result.returncode, 0)
        #Verify result
        self.assertIn(
            outputExpectedResult,
            result.stdout
        )
    
    def test_sha1_output(self):
        inputPassword="Github"
        inputHashtype="sha1"
        outputExpectedResult="c53ced31f785a1888b348de05057011fedd3be48"
        result = fileCaller(inputPassword,inputHashtype)
        #Verify that the call to the main file is correct. 
        self.assertEqual(result.returncode, 0)
        #Verify result
        self.assertIn(
            outputExpectedResult,
            result.stdout
        )

    def test_sha512_output(self):
        inputPassword="Github"
        inputHashtype="sha512"
        outputExpectedResult="567efaa953d9c7f53865ab6efca82ddd1031d772503352c5ac992f0ca7eef88ddf523ba7e1d049b0d3559941679697be2b874bfb68e5fc0dc8eb37aa204fcca9"
        result = fileCaller(inputPassword,inputHashtype)
        #Verify that the call to the main file is correct. 
        self.assertEqual(result.returncode, 0)
        #Verify result
        self.assertIn(
            outputExpectedResult,
            result.stdout
        )

        ##Black Box Test
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

    def test_noInputPassword(self):
        inputPassword=""
        inputHashtype=""
        outputExpectedResult=""
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