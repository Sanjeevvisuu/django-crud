pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                " "
                git branch: 'main', credentialsId: 'github', url: 'https://github.com/Sanjeevvisuu/deploy-test.git'
            }
        }

        stage('Set Up Python Environment') {
            steps {
                script {
                    echo 'Setting up Python environment...'
                    sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    python --version
                    pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    echo 'Building and running the Django application...'
                    sh '''
                    . venv/bin/activate
                    python manage.py runserver 
                    '''
                }
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
