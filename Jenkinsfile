pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/Michealsachina/schoolproject.git'
            }
        }

        stage('Setup Python') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\activate && python -m pip install --upgrade pip'
            }
        }

        stage('Install Requirements') {
            steps {
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
                bat 'venv\\Scripts\\activate && pip install pytest playwright pytest-playwright'
                bat 'venv\\Scripts\\activate && playwright install'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\activate && pytest -v'
            }
        }
    }
}