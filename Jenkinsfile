pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git credentialsId: 'github-creds', branch: 'main', url: 'https://github.com/DevOpsLearrnn/AI-Driven-DevOps-CI-CD-Pipeline.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building the application...'
                // Add your Docker build command here if needed
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                // Add your test script or logic here
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
                // Add your deployment logic here (e.g., kubectl apply)
            }
        }
    }
}
