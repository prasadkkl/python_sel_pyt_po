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

                // Install python3 and python3-venv if missing
                sh '''
                    if ! command -v python3 > /dev/null 2>&1; then
                        echo "🔧 Installing python3..."
                        sudo apt update && sudo apt install -y python3
                    else
                        echo "python3 already installed."
                    fi

                    if ! python3 -m ensurepip --version > /dev/null 2>&1; then
                        echo "🔧 Installing python3-venv..."
                        sudo apt install -y python3-venv
                    else
                        echo "python3-venv already available."
                    fi
                '''

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
