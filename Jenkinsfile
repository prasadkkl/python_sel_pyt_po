pipeline {
    agent {
        docker {
            image 'python:3.8'
            args '-u root' // Optional: runs as root inside container for full access
        }
    }

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Cloning GitHub repository...'
                git branch: 'main', url: 'https://github.com/prasadkkl/python_sel_pyt_po.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo 'Setting up virtual environment and installing dependencies...'

                // Create virtual environment
                sh 'python3 -m venv ${VENV_DIR}'

                
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests via run_tests.sh...'

                sh '''
                    source ${VENV_DIR}/bin/activate
                    ./run_tests.sh
                '''
            }
        }

        stage('Archive Reports') {
            steps {
                echo 'Archiving test reports...'
                archiveArtifacts artifacts: 'reports/**', fingerprint: true
            }
        }
    }

    post {
        always {
            echo 'Cleaning up virtual environment...'
            sh 'rm -rf ${VENV_DIR}'
        }

        success {
            echo 'Pipeline completed successfully.'
        }

        failure {
            echo 'Pipeline failed.'
        }
    }
}
