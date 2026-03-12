pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Venv') {
            steps {
                // Create a virtual environment and install dependencies
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Selenium Tests') {
            steps {
                // Activate venv and run tests
                sh '''
                    . venv/bin/activate
                    mkdir -p reports
                    pytest tests/ -v --junitxml=reports/results.xml
                '''
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'reports/results.xml'
        }
        success {
            echo '✅ All tests passed!'
        }
        failure {
            echo '❌ Some tests failed. Check the report above.'
        }
        cleanup {
            // Clean up the virtual environment
            sh 'rm -rf venv'
        }
    }
}
