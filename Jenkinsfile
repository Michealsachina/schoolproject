pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                bat 'python -m venv env'
                bat 'env\\Scripts\\activate && pip install -r requirements.txt'
                bat 'env\\Scripts\\activate && python -m playwright install'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'env\\Scripts\\activate && pytest -v'
            }
        }
    }
}