pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'python -m venv env'
                bat 'env\\Scripts\\pip install -r requirements.txt'
                bat 'env\\Scripts\\playwright install'
            }
        }

        stage('Start Django Server') {
            steps {
                bat '''
                start /B env\\Scripts\\python manage.py migrate
                start /B env\\Scripts\\python manage.py runserver 127.0.0.1:8000
                timeout /t 10
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat 'env\\Scripts\\pytest'
            }
        }
    }

    post {
        always {
            bat 'taskkill /F /IM python.exe'
        }
    }
}