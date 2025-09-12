pipeline {
    agent any   // Runs on any available Jenkins agent

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
                sh 'python3.8 -m venv ${VENV_DIR}'

                // Activate virtualenv and install requirements
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Executing tests using run_tests.sh...'
                
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
            echo 'Cleaning up...'
            sh 'rm -rf ${VENV_DIR}'
        }

        success {
            echo 'Tests passed successfully.'
        }

        failure {
            echo 'Tests failed.'
        }
    }
}
