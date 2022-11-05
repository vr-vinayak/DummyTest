pipeline {
    agent any
    stages {
        stage('checkout git') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/vr-vinayak/DummyTest.git']]])
            }
        }
        stage('Build & test') {
            steps {
                echo 'building and testing stage'
                git branch: 'main', url: 'https://github.com/vr-vinayak/DummyTest.git'
                bat "python --version"
                bat "python -m pip install pip"
                bat "pip --version"
                bat "pip install pytest"
                bat "pytest FizzBuzz.py"
                bat "pytest test_2.py"
            }
        }
        stage('QA') {
            steps {
                echo 'Test Succeeded'
            }
        }
        stage('Dev Approval'){
            steps {
                echo 'Getting Approval of Admin'
                timeout(time: 3, unit: 'DAYS') {
                    input message: 'Code has been build and tested, Would you like to proceed ahead?', submitter: 'Admin'
                }
            }
        }
        stage('Deploy') {
            steps{
                echo 'Deploying'
            }
        }
    }
}
