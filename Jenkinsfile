pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'python3 app.py'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m pytest test_app.py -v'
            }
        }

        stage('Package') {
            steps {
                sh 'tar -czf order-app.tar.gz application.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Order Processing Application...'
            }
        }
    }
}
