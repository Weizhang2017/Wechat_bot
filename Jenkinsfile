pipeline {
    agent { docker { image 'python:3.13.3-alpine3.21' } }
    stages {
        stage('install dependency') {
            steps {
                sh 'pip install pytest'
            }

        }
        stage('build') {
            steps {
                sh 'pytest test_app.py'
            }
        }
    }
}
