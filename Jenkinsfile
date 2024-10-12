pipeline {
    agent any
    environment {
         DOCKERHUB_CREDENTIALS= credentials('dockerhub')

    }
    stages {
        stage('Checkout') {
            steps {
                " "
                git branch: 'main', credentialsId: 'github', url: 'https://github.com/Sanjeevvisuu/deploy-test.git'
            }
        }
        

       
        stage('docker build') {
            steps {
                script {
                    echo 'Building and running the Django application as a image ...'
                    sh '''
                    docker-compose build 
                    '''
                }
            }
        }
        stage('docker-image -push') {
                script {
                    echo 'Pushing application to Docker Hub...'
                    withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh '''
                        echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
                        # i created a repo in dockerhub called docker push sanjeevvisu/django:tagname
                        docker tag latest $DOCKER_USERNAME/django
                        docker push $DOCKER_USERNAME/django:latest
                        '''
                    }
                    echo 'Pushed application to Docker Hub.'
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
