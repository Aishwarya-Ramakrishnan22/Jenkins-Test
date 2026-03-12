pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Pull code from the Git repository
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install Python packages from requirements.txt
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                // Run pytest and generate a JUnit XML report
                bat 'pytest tests/ -v --junitxml=reports/results.xml'
            }
        }
    }

    post {
        always {
            // Publish test results so Jenkins shows them in the UI
            junit allowEmptyResults: true, testResults: 'reports/results.xml'
        }
        success {
            echo '✅ All tests passed!'
        }
        failure {
            echo '❌ Some tests failed. Check the report above.'
        }
    }
}
