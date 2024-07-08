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
          git branch: 'aster',
            url: 'https://github.com/abdulwahedmutayyib/awm.git' // Replace with your repository URL
        }
      }
      stage('Install Dependencies') {
        steps {
          script {
            // Use approved steps instead of sh
            bat 'pip install -r requirements.txt' 
          }
        }
      }
      // New Stage: Build Docker Image
      stage('Build Docker Image') {
        steps {
          script {
            docker.withRegistry('https://hub.docker.com/', credentialsId: 'ecb850b0-9a99-42c2-8786-5dc858d67221') { // Replace details
              def imageName = 'python:latest' // Replace with your image name
              // Use approved steps instead of sh
              bat "docker build -t $imageName."
            }
          }
        }
      }
      stage('Static Code Analysis') {
        steps {
          script {
            // Use approved steps instead of sh
            bat 'pip install flake8' // Install Flake8
            bat 'flake8.'     // Execute Flake8 on your Python code
          }
        }
        post {
          always {
            warningsNG(regions: '**/*.py', // Analyze Python files
                        failedTotal: 'high',
                        unstableTotal: 'low')
          }
        }
      }
      stage('Test Code') {
        steps {
          script {
            // Use approved steps instead of sh
            bat 'pytest' // Execute Pytest (assuming you use Pytest)
          }
        }
      }
      stage('Code Coverage Analysis') {
        steps {
          script {
            // Use approved steps instead of sh
            bat 'coverage run -m pytest && coverage report' // Example with coverage.py
          }
          publisher coberturaReport( // Publish coverage report
                    onlyStableBuilds: true,
                    failNoReports: true,
                    failUnhealthy: true,
                    autoUpdateHealth: false,
                    autoUpdateStability: false,
                    zoomCoverageChart: true
          )
        }
