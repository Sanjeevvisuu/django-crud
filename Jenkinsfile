pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
    }
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out the code...'
               git branch: 'main', credentialsId: 'github', url: 'https://github.com/Sanjeevvisuu/django-crud.git'
            }
        }

        stage('Docker Build') {
            steps {
                script {
                    echo 'Building the Django application as a Docker image...'
                    sh '''
                    docker-compose build
                    '''
                }
            }
        }

        stage('Docker Image Push') {
            steps {
                script {
                    echo 'Pushing application to Docker Hub...'
                    withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh '''
                        echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
                        # Tag and push the image
                        docker tag django:latest $DOCKER_USERNAME/django:latest
                        docker push $DOCKER_USERNAME/django:latest
                        '''
                    }
                    echo 'Pushed application to Docker Hub.'
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up workspace...'
            cleanWs()
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
