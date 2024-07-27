pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'master', credentialsId: 'your-github-credentials-id', url: ''
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t my-calculator-app ./'
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                    docker run my-calculator-app pytest --cov=calculator --cov-report html
                '''
            }
        }
        stage('Static Code Analysis') {
            steps {
                sh '''
                    docker run my-calculator-app flake8 .
                    docker run my-calculator-app pycodestyle .
                '''
            }
        }
        stage('Coverage Report') {
            steps {
                archiveArtifacts artifacts: '**/*.html', fingerprint: true, followSymlinks: false
            }
        }
        stage('Deploy (Optional)') {
            // Implement deployment logic to your desired environment (e.g., AWS Lambda, EC2 instance)
        }
    }

    post {
        always {
            cleanWs()
        }
        success {
            emailext body: 'CI/CD Pipeline Successful!', subject: 'Calculator App Build Successful', to: 'awahedmutayyib@gmail.com'
        }
        failure {
            emailext body: 'CI/CD Pipeline Failed!', subject: 'Calculator App Build Failed', to: 'awahedmutayyib@gmail.com'
        }
    }
