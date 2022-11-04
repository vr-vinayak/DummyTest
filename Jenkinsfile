pipeline {
    agent any
    stages {
        stage('git repo & clean') {
            steps {
               //bat "rmdir  /s /q DummyTest"
                bat "git clone https://github.com/vr-vinayak/DummyTest.git"
                bat "mvn clean -f DummyTest"
            }
        }
        stage('install') {
            steps {
                bat "mvn install -f DummyTest"
            }
        }
        stage('test') {
            steps {
                bat "mvn test -f DummyTest"
            }
        }
        stage('package') {
            steps {
                bat "mvn package -f DummyTest"
            }
        }
    }
}
