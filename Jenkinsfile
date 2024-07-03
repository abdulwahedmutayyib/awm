pipeline {
  agent {
    node {
      label 'docker'
      customWorkspace '/home/jenkins/workspace'
    }
  }

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
          sh 'pip install -r requirements.txt' // Replace with your command if using virtualenv
        }
      }
    }
    // New Stage: Build Docker Image
    stage('Build Docker Image') {
      steps {
        script {
          docker.withRegistry('https://your-docker-registry.com', credentialsId: 'docker_hub_credentials') { // Replace details
            def imageName = 'your_image_name:latest' // Replace with your image name
            sh "docker build -t $imageName ."
          }
        }
      }
    }
    stage('Static Code Analysis') {
      steps {
        script {
          sh 'pip install flake8' // Install Flake8
          sh 'flake8.'     // Execute Flake8 on your Python code
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
          sh 'pytest' // Execute Pytest (assuming you use Pytest)
        }
      }
    }
    stage('Code Coverage Analysis') {
      steps {
        script {
          sh 'coverage run -m pytest && coverage report' // Example with coverage.py
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
    }
    stage('Deploy to Server') {
      steps {
        script {
          sh 'cp -r dist/* user@server.com:/path/to/deployment/directory' // Replace with your details (assuming build output in dist/)
        }
      }
    }
  }

  // Set post-conditions (optional):
  post {
    always {
      // Reset RESET_STAGE to an empty string after all stages (or on success)
      environment {
        RESET_STAGE = ''
      }
    }
    failure {
      // Set RESET_STAGE to a flag value on failure
      environment {
        RESET_STAGE = 'true'
      }
    }
  }
}

