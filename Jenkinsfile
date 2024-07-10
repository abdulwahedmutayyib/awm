pipeline {
    agent any

    environment {
        RESET_STAGE = false // Initialize to false
        PYENV_VERSION = '3.8.12' // Specify the Python version to use
    }

    stages {
        stage('Reset Check') {
            steps {
                script {
                    if (env.RESET_STAGE == 'true') {
                        echo "Stages reset. Skipping remaining stages."
                        return
                    }
                }
            }
        }
        stage('Checkout Code') {
            steps {
                git branch: 'master',
                    url: 'https://github.com/abdulwahedmutayyib/awm.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    pyenvPython(PYENV_VERSION) {
                        sh 'pip install -r requirements.txt'
                    }
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    pyenvPython(PYENV_VERSION) {
                        docker.withRegistry('https://hub.docker.com/', credentialsId: 'docker-credential') {
                            def imageName = 'python:latest'
                            sh "docker build -t ${imageName} ."
                        }
                    }
                }
            }
        }
        stage('Static Code Analysis') {
            steps {
                script {
                    pyenvPython(PYENV_VERSION) {
                        sh 'pip install flake8'
                        sh 'flake8 .'
                    }
                }
            }
            post {
                always {
                    warningsNG(regions: '**/*.py',
                                failedTotal: 'high',
                                unstableTotal: 'low')
                }
            }
        }
        stage('Test Code') {
            steps {
                script {
                    pyenvPython(PYENV_VERSION) {
                        sh 'pytest'
                    }
                }
            }
        }
        stage('Code Coverage Analysis') {
            steps {
                script {
                    pyenvPython(PYENV_VERSION) {
                        // Run pytest with coverage
                        sh 'pytest --cov=calculator --cov-report=xml'
                    }
                }
                post {
                    always {
                        publish {
                            coberturaReport(
                                coberturaReportFile: '**/coverage.xml', // Adjust this based on your coverage report file path
                                onlyStableBuilds: true,
                                failNoReports: true,
                                failUnhealthy: true,
                                autoUpdateHealth: false,
                                autoUpdateStability: false,
                                zoomCoverageChart: true
                            )
                        }
                    }
                }
            }
        }
    }

    post {
        always {
            script {
                env.RESET_STAGE = false // Reset RESET_STAGE to false after all stages (or on success)
            }
        }
        failure {
            script {
                env.RESET_STAGE = 'true' // Set RESET_STAGE to 'true' on failure
            }
        }
    }
}
