pipeline {
    agent { docker { image 'python:latest' } }
    stages {
        stage('git') {
            steps {
                echo 'Getting Git project'
                git url: 'https://github.com/mathieusr/jenkins-python-test'
            }
        }
        stage('test') {
            steps {
                echo 'Launch python unit test'
                sh 'python -m unittest'
            }
        }
    }
    post {
        always {
            emailext body: 'Your build has been completed',
                recipientProviders: [
                    [$class: 'CulpritsRecipientProvider'],
                    [$class: 'DevelopersRecipientProvider'],
                    [$class: 'RequesterRecipientProvider']
                ],
                subject: 'Build completed'
        }
    }
}