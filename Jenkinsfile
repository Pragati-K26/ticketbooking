pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/Pragati-K26/ticketbooking.git'
            }
        }
        stage('Build') {
            steps {
                sh 'docker-compose build'
            }
        }
        stage('Test') {
            steps {
                sh 'docker-compose run web python manage.py test'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }
}
