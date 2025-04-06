pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                    git branch: 'main', url: 'https://github.com/DevOpsLearrnn/AI-Driven-DevOps-CI-CD-Pipeline-with-Kubernetes-AWS.git'

            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t fastapi-app .'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    sh 'docker run -d -p 8000:8000 --name fastapi-app fastapi-app'
                }
            }
        }
    }
}
