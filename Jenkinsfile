pipeline {
    agent any
    environment {
        IMAGE_NAME = "afr273/fastapi-app"
        IMAGE_TAG = "v2${BUILD_NUMBER}"
    }
    stages {
        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
            }
        }
        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    sh "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
                }
            }
        }
        // Optional deploy stage below:
        // stage('Deploy') {
        //     steps {
        //         sh 'kubectl apply -f deployment.yaml'
        //     }
        // }
    }

    post {
        always {
            sh "docker rmi ${IMAGE_NAME}:${IMAGE_TAG} || true"
        }
    }
}
