sandbox {
  pipeline {
    agent any

    environment {
      RESET_STAGE = '' // Initially empty
    }

    stages {
      stage('Reset Check') {
        steps {
          script {
            if (env.RESET_STAGE) {
              echo "Stages reset. Skipping remaining stages."
              return
            }
          }
        }
      }
      stage('Checkout Code') {
        steps {
          git branch: 'master',
            url: 'https://github.com/abdulwahedmutayyib/awm.git' // Replace with your repository URL
        }
      }
      stage('Install Dependencies') {
        steps {
          script {
            sh 'pip install -r requirements.txt' 
          }
        }
      }
      stage('Build Docker Image') {
        steps {
          script {
            docker.withRegistry('https://hub.docker.com/', credentialsId: 'docker-credential') { 
              def imageName = 'python:latest' 
              sh "docker build -t ${imageName} ." 
            }
          }
        }
      }
      stage('Static Code Analysis') {
        steps {
          script {
            sh 'pip install flake8' 
            sh 'flake8 .'     
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
            sh 'pytest' 
          }
        }
      }
      stage('Code Coverage Analysis') {
        steps {
          script {
            sh 'coverage run -m pytest && coverage report' 
          }
          publisher coberturaReport( 
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

    post {
      always {
        script {
          env.RESET_STAGE = '' // Reset RESET_STAGE to an empty string after all stages (or on success)
        }
      }
      failure {
        script {
          env.RESET_STAGE = 'true' // Set RESET_STAGE to a flag value on failure
        }
      }
    }
  }
}
