pipeline {
    agent any
    stages {
        stage('Checkout git') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/vr-vinayak/DummyTest.git']]])
            }
        }
        stage('Build and Test(pytest)') {
            steps {
                echo 'building and testing stage'
                git branch: 'main', url: 'https://github.com/vr-vinayak/DummyTest.git'
                sh 'python3 --version'
                sh 'pip3 --version'
                sh 'python3 -m pytest --version'
                sh 'python3 -m pytest test_2.py'
            }
        }
        stage('QA(pylint)') {
            steps {
                echo 'Code Quality Check'
                sh "python3 -m pylint test_1.py"
            }
        }
        stage('Dev Approval'){
            steps {
                echo 'Getting Approval of Admin'
                timeout(time: 3, unit: 'DAYS') {
                     // some block
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
