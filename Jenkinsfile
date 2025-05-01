pipeline {
    agent { docker { image 'python:3.13.3-alpine3.21' } }
    stages {
        stage('build') {
            steps {
                sh 'pip install pytest'
            }
            steps {
                sh 'pytest test_app.py'
            }
        }
    }
}
