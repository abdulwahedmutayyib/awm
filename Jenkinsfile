sandbox {
  pipeline {
    agent any

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
            bat 'pip install -r requirements.txt' 
          }
        }
      }
      // ... rest of the script ...
    }

    // Set post-conditions (optional):
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
