pipeline {
	agent any
     
	stages {
		
		
			
		stage('Stage 1 : Pre-check Python is installed or not') {
			steps {
				bat 'echo "Check Python Version"'
				bat 'python --version'
				bat 'echo "Python latest version is installed, up and running"'
                           
            }
        }
		
		stage("Code Quality") {
			steps {
				bat 'echo "Run Code Quality check with SonarQube"'
				bat 'C:\\Users\\Dell\\Documents\\Office\\Devops\\sonar-scanner-cli-4.3.0.2102-windows\\sonar-scanner-4.3.0.2102-windows\\bin\\sonar-scanner.bat
			}
		}
		stage('Stage 2 : Unit Test') {
			parallel {
				
				stage('Testcase 1 : Verify Calculator with Addition') {
					steps {
						bat 'echo "Lets run the testcase for additing 2 numbers using calculator."'
						bat 'python calculator.py 1 10 25'
						bat 'echo "Testcase pass for addition."'
					}
				}
				
				stage('Testcase 2 : Verify Calculator with Subtraction') {
					steps {
						bat 'echo "Lets run the testcase for subtracting 2 numbers using calculator."'
						bat 'python calculator.py 2 25 10'
						bat 'echo "Testcase pass for subtraction."'
					}
				}
				
				stage('Testcase 3 : Verify Calculator with Multiplication') {
					steps {
						bat 'echo "Lets run the testcase for multiplication of 2 numbers using calculator."'
						bat 'python calculator.py 3 3 5'
						bat 'echo "Testcase pass for multiplication."'
					}
				}
				
				stage('Testcase 4 : Verify Calculator with Division') {
					steps {
						bat 'echo "Lets run the testcase for division of 2 numbers using calculator."'
						bat 'python calculator.py 4 10 2'
						bat 'echo "Testcase pass for division."'
					}
				}
			}
		}
	}
	
	post {
		always {
			bat 'echo "Clean the files from WS"'
			bat 'del calculator.py'
			bat 'del .gitignore'
			bat 'del README.md'
		}
		success {
			bat 'echo "Build Passed"'
		
		}
		
		failure {
			bat 'echo "Build Failed"'
			bat 'echo "Please fix!"'
		}
				
	}

	
}
